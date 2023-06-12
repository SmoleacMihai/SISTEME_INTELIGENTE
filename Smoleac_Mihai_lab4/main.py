import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

def prepare_data(df):
  # Identify rows with missing values
  missing_rows = df.isnull().sum(axis=1) > 0
  print("Missing values found in the following rows:")
  print(df[missing_rows])

  # If the number of rows with missing values is <= 10, drop them
  if missing_rows.sum() <= 10:
    df = df.dropna()
  else:
    # Otherwise, fill missing values with the column median
    for column in df.columns:
      if df[column].isnull().sum() > 0:
        print(f"Empty parameter in {column} | Rows: {df[df[column].isnull()].index.tolist()}")
        df[column].fillna(df[column].median(), inplace=True)

  # Identify and print duplicate rows
  duplicate_rows = df.duplicated()
  if duplicate_rows.sum() > 0:
    print("Duplicate rows found at the following indices:")
    print(df[duplicate_rows].index.tolist())
    # Drop duplicates
    df = df.drop_duplicates()

  return df

# Load the data
df = pd.read_csv('Iris.csv')
df = prepare_data(df)

# Encode the labels
le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])

# Load data to predict
df_predict = pd.read_csv('iris_predict.csv')
df_predict_for_excel = df_predict

# Split the data into features and target
X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = df['Species']

# Create and train the model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, y)

# Load the data for prediction
df_predict = pd.read_csv('iris_predict.csv')

# Split the prediction data into features
X_predict = df_predict[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]

# Make predictions
predictions = model.predict(X_predict)

# Convert the encoded labels back to original form
predictions = le.inverse_transform(predictions)

# Inputing data to excel
df_predict_for_excel['Species'] = predictions

df_predict_for_excel.to_excel('predicted_values.xlsx', index=False)

species_mapping = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
df['Species'] = df['Species'].map(species_mapping)

# Define marker shapes for each species
marker_shapes = {'Iris-setosa': '*', 'Iris-versicolor': 'p', 'Iris-virginica': '^'}

# Create a figure with six subplots
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Iterate over the species and plot the diagrams
for i, species in enumerate(df['Species'].unique()):
  # Filter the data for the current species
  species_data = df[df['Species'] == species]
  
  # Calculate the row and column indices for the current species
  row = i // 3
  col = i % 3
  
  # Plot the petal width and length diagram
  ax = axes[row, col]
  ax.scatter(species_data['PetalWidthCm'], species_data['PetalLengthCm'], marker=marker_shapes[species])
  ax.set_ylabel('Petal Width')
  ax.set_xlabel('Petal Length')
  
  # Set the title as the species name for the current column
  if row == 0:
    ax.set_title(species)
    ax.set_title(species, fontname='monospace', fontsize=14, color='DodgerBlue')
  
  print(species)
  # Plot the sepal width and length diagram
  ax = axes[row+1, col]
  ax.scatter(species_data['SepalWidthCm'], species_data['SepalLengthCm'], marker=marker_shapes[species])
  ax.set_ylabel('Sepal Width')
  ax.set_xlabel('Sepal Length')

# Add a centered title for the entire diagram
fig.suptitle('Iris Classification', fontname='monospace', fontsize=14, color='DodgerBlue', y=0.95)

# Adjust the spacing between subplots and add margin at the bottom
plt.subplots_adjust(bottom=0.1, hspace=0.5)


# Adjust the spacing between subplots
plt.tight_layout()

# Display the diagram
plt.show()