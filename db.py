# coding: utf-8

import dataset

db = dataset.connect('sqlite:///noticias.db')
noticias_table = db['noticias']