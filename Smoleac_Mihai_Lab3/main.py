from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.linear_model import Lasso
from matplotlib import pyplot as plt


if __name__ == '__main__':
    train_df = pd.read_excel('price_lab3.xlsx')
    test_df = pd.read_excel('predict_lab3.xlsx')
    diagram_df = pd.read_excel('predict_lab3.xlsx')

    train_df.drop_duplicates(inplace=True)

    train_df.dropna(subset=['price'], inplace=True)

    train_df.dropna(subset=['area', 'rooms', 'floor'], inplace=True)
    test_df.dropna(subset=['area', 'rooms', 'floor'], inplace=True)
    diagram_df.dropna(subset=['area'], inplace=True)
    train_df = train_df[(train_df['floor'] <= 15) & (train_df['price'] > 0)]

    median_price = train_df['price'].median()
    train_df['price'].fillna(median_price, inplace=True)
    test_df['price'].fillna(median_price, inplace=True)

    X_train = train_df[['area', 'rooms', 'floor']]
    y_train = train_df['price']

    X_test = test_df[['area', 'rooms', 'floor']]
    xdiagram_test = test_df['area']

    linear_reg = LinearRegression()
    lasso_reg = Lasso(alpha=0.1)

    linear_reg.fit(X_train, y_train)
    lasso_reg.fit(X_train, y_train)

    test_df['linear_reg_price'] = linear_reg.predict(X_test)
    test_df['lasso_reg_price'] = lasso_reg.predict(X_test)

    diagram_df['linear_reg_price'] = linear_reg.predict(X_test)
    diagram_df['lasso_reg_price'] = lasso_reg.predict(X_test)

    test_df[['area', 'rooms', 'floor', 'linear_reg_price']].to_excel('predicted_values_ap1.xlsx', index=False)
    test_df[['area', 'rooms', 'floor', 'lasso_reg_price']].to_excel('predicted_values_ap2.xlsx', index=False)

    print("Linear Regression coefficients: ", linear_reg.coef_)

    plt.scatter(train_df['area'], train_df['price'], color='blue')
    plt.plot(X_test['area'], diagram_df['linear_reg_price'], color='red')
    plt.xlabel('Area')
    plt.ylabel('Price')
    plt.show()