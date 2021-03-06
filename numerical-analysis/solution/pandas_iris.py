from datetime import datetime, timezone
import pandas as pd
import numpy as np


FILENAME = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'

iris = pd.read_csv(FILENAME, encoding='utf-8')
iris.columns = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species',
]

iris.where(iris['Petal length'] > 2.0, inplace=True)
iris.dropna(how='all', inplace=True)

iris['datetime'] = datetime.now(tz=timezone.utc)
iris['big_enough'] = np.where(iris['Petal width'] > 1.0, True, False)

iris = iris[['Sepal length', 'Sepal width', 'Species']]
iris.describe()
