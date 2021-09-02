import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.offline import init_notebook_mode
from sklearn import preprocessing
import jupyterlab as jp

init_notebook_mode()   # для отображения интерактивных графиков на хабре/кеггле/етк


def correlation_map(data, column_names):
    """ Построение тепловой карты корреляции с отображением чисел с одним знаком после запятой """
    # premap =  data[column_names].corr()
    f,ax = plt.subplots(figsize=(15, 15))  # размер ячейки
    sns.heatmap(data[column_names].corr(), annot=True, linewidths=.8, fmt= '.3f') # отобр-ть числа, ширина 8, 3 знака после запятой
    return plt


def all_in_one_lineplot(data, column_names):
    """ Линейный график со всеми датчиками """
    fig = px.line(data_frame=data,
                y=column_names, # список всех датчиков
                title='Channels',
                width=900
                  )
    return fig


def scatter_plots(column_x, column_y, data):
    """ Точечный график для двух значений """
    figure = px.scatter(data_frame=data, # название DataFrame
                 y=column_x, # название колонки, значения которой будут расположены по оси Ох
                 color=column_y,# имя столбца, который будет использоваться для присвоения цвета меткам на точечной диаграмме
                 title=column_x, # Название графика
                 template = 'ggplot2', # ggplot2 встроенная настройка темы графика
                 width=900

                )
    return figure

def scatter_matrix(data, names_pair=None):
    """ График зависимости двух величин друг от друга, разные классы выделяются разными цветами"""
    fig = px.scatter_matrix(data,   # данные
                            dimensions=names_pair,   # пара величин для которых строится график
                            color="class")           # по значениям какой колонки наносятся разные цвета
    return fig


def all_scatter_matrixes(data):
    """ Вызов отрисовки scatter_matrix для каждой параллельной пары датчиков (соответствие левый-правый) """
    scatter_matrix(data, ['AF3','AF4']).show()
    scatter_matrix(data, ['F3', 'F4']).show()
    scatter_matrix(data, ['F7', 'F8']).show()
    scatter_matrix(data, ['FC5', 'FC6']).show()
    scatter_matrix(data, ['T7', 'T8']).show()
    scatter_matrix(data, ['P7', 'P8']).show()
    scatter_matrix(data, ['O1', 'O2']).show()
    return