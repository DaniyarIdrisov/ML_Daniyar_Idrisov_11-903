import matplotlib.pyplot as plt
import pandas as pd


def start():
    labels = []
    result_pass = []
    data = pd.read_csv("titanic.csv")
    classes = data.Pclass
    all_classes = data['Pclass'].unique()
    results = [(i, classes[classes == i].count()) for i in all_classes]
    for result in results:
        labels.append(result[0])
        result_pass.append(result[1])
    fig, ax = plt.subplots()
    ax.pie(result_pass, labels=labels, autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    start()
