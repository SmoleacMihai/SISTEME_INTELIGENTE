from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def task1():
    x = [1, 2, 6, 7, 8, 10] 
    y = [3, 8, 1, 1, 1, 9]

    plt.plot(x, y, ".-")
    plt.grid(color="cyan", linestyle=":", linewidth=1)
    plt.title("Dynamic of sales")
    plt.xlabel("Week number")
    plt.ylabel("Amount of sales")
    plt.show()


def task2():
    df = pd.read_csv('task2.csv')
    duration = df["Duration"].tolist()
    pulse = df["Pulse"].tolist()
    x = range(1, 25)
    plt.plot(x, duration, marker="s", markersize=12, label="Duration values")
    plt.plot(x, pulse, marker="v", markersize=12, label="Pulse values")
    plt.xlabel("Index", fontdict={"color": "#8B0000", "size": 15, "family": "fantasy"})
    plt.ylabel("Values for pulse and duration", fontdict={"color": "#8B0000", "size": 15, "family": "fantasy"})
    plt.legend()
    plt.grid(color="#483D8B", axis="y")
    plt.title("Comparasion between pulse and duration", fontdict={'family': 'cursive', 'size': 25, 'color': 'Crimson'},
              loc="left")
    plt.show()


def task3():
    df = pd.read_csv("task2.csv")
    xx = ["Set 1", "Set 2", "Set 3", "Set 4", "Set 5"]
    font = {
        "family": "monospace",
        "color": "indigo",
        "size": 16
    }
    X = df["Duration"][0:5]
    Y = df["Pulse"][0:5]
    Z = df["Calories"][0:5]

    X_axis = np.arange(len(xx))

    plt.bar(X_axis + 0.2, X, 0.2, label="Duration", lw=0.2)
    plt.bar(X_axis + 0.4, Y, 0.2, label="Pulse", lw=0.2)
    plt.bar(X_axis + 0.6, Z, 0.2, label="Calories", lw=0.2)

    plt.grid(axis="y", color="#808080")
    plt.xticks(X_axis, xx)
    plt.title("Comparison Table", loc="right", fontdict=font)
    plt.legend(loc="upper center", title="Efficincy of training")
    plt.show()


def task4():
    df = pd.read_csv("task2.csv")

    font = {
        "family": "monospace",
        "color": "DodgerBlue",
        "size": 14
    }
    titleFont = {
        "color": "Chocolate",
        "size": 14,
        "family": "cursive"
    }

    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(12, 8))

    plt.suptitle("Basic diagrams", fontdict=titleFont)
    axs[0, 0].plot(df['Maxpulse'], df['Calories'])
    axs[0, 0].set_title('Pyplot diagram', loc="right", fontdict=font)

    axs[1, 1].hist(df['Calories'], color='purple')

    sales = [23, 17, 35, 29, 12, 41]
    models = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
    axs[2, 1].pie(sales, labels=models, startangle=90)

    axs[0, 1].scatter(df['Maxpulse'], df['Calories'], alpha=0.5, label='Maxpulse - Calories')
    axs[0, 1].scatter(df['Pulse'], df['Calories'], alpha=0.7, label='Pulse - Calories')
    axs[0, 1].set_title('Scatter diagram', fontdict=font, loc="left")
    axs[0, 1].legend(loc='upper right')

    axs[2, 0].barh(df['Maxpulse'], df['Calories'], color='DarkOrchid')
    axs[2, 0].set_xlabel('Calories')
    axs[2, 0].set_ylabel('Maxpulse')
    axs[2, 0].grid(axis='x', color='DarkSlateBlue', linewidth=2)
    axs[2, 0].set_yticks(range(100, max(df['Maxpulse']) + 1, 20))

    axs[1, 0].bar(df['Maxpulse'], df['Calories'], color='BurlyWood', linewidth=0.3)
    axs[1, 0].grid(axis='y', color='LightCoral', linewidth=3)

    sc = axs[0, 1].scatter(df['Maxpulse'], df['Calories'], c=df['Pulse'], cmap='viridis', alpha=0.5, vmin=0, vmax=1.0)
    fig.colorbar(sc, ax=axs[0, 1])

    fig.tight_layout()  
    plt.show()


if __name__ == "__main__":
    task1()
    # task2()
    # task3()
    # task4()