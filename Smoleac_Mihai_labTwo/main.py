import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.interpolate import make_interp_spline
import numpy as np
import datetime as DT
from matplotlib.dates import date2num


def task1():
    x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

    plt.plot(x, y, "D")
    plt.grid(color="m", linestyle=":", linewidth=2)
    plt.title("Quality of sales")
    plt.xlabel("Week number")
    plt.ylabel("Amount of sales")
    plt.show()


def task2():
    df = pd.read_csv('task2.csv')
    duration = df["Duration"].tolist()
    pulse = df["Pulse"].tolist()
    fig, ax = plt.subplots()
    x = range(1, 25)
    plt.plot(x, duration, marker="s", markersize=12, label="Duration values")
    plt.plot(x, pulse, marker="v", markersize=12, label="Pulse values")

    plt.legend()
    plt.grid(color="#483D8B", axis="y")
    plt.title("Comparasion between pulse and duration", fontdict={'family': 'cursive', 'size': 25, 'color': 'Crimson'}, loc="left")
    plt.show()


def task3():
    # ne rabotaet
    df = pd.read_csv('task2.csv')
    print()
    duration = df["Duration"].tolist()
    pulse = df["Pulse"].tolist()
    calories = df["Calories"].tolist()

    plt.bar([0.2*n for n in range(1,3)], duration, color="tab:blue", width=0.2, label='Duration',
            align='edge')
    plt.bar([0.2*n for n in range(1,3)], pulse, color="orange", width=0.2, label='Pulse',
            align='edge')
    plt.bar([0.2*n for n in range(1,3)], calories, color="green", width=0.2, label='Calories',
            align='edge')

    plt.legend(loc='upper left')
    plt.title('Sales data')
    plt.xticks(["Set 1", "Set 2", "Set 3"])

    plt.grid(True, linewidth=1, linestyle="--")
    plt.title('Facewash and facecream sales data')
    plt.show()


def task4():
    return


if __name__ == '__main__':
    # task1()
    # task2()
    task3()
    # task4()