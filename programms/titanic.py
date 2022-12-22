import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


def read_csv(filename):
    data = pd.read_csv(filename)
    return data


if __name__ == '__main__':
    dataset = read_csv("titanic.csv")
    print(dataset)
    dataset.head()
    g = sns.FacetGrid(dataset, height=6)
    g.map(plt.hist, 'Age', bins=20)
    plt.figure(figsize=(9, 6))
    colors = sns.color_palette('pastel')
    plt.pie(dataset.Pclass.value_counts(), labels=['Pclass: 3', 'Pclass: 1', 'Pclass: 2'], colors=colors,
            autopct='%.2f%%')
    plt.title('Распределение по классам')
    plt.show()
    sns.catplot(x='Pclass', y='Survived', hue='Sex', data=dataset, kind='bar')
