import pandas


def abrir_archivo(nombre):
    return pandas.read_csv(nombre)


def nuevo_dataframe(other): 
    return pandas.DataFrame(other)


'''
Devuelve un nuevo DataFrame que contiene solamente el top 5 de registros 
del DataFrame de origen, a partir de los valores de una columna data
'''
def crear_top5_dataframe(dataframe, columna):
    return pandas.DataFrame(dataframe.sort_values(by = columna, ascending = False).head(5))


'''
Filtra los registros de un dataframe, dejando sólo aquellos cuyos valores de la columna
indicada se encuentren dentro de la lista

Parametros
----------
dataframe: el dataframe que contiene el origen de datos que se desea filtrar
lista: la lista que contiene los valores que se deasean preservar
columna: el nombre de la columna del dataframe que se usará para filtrar
'''
def filtrar_dataframe(dataframe, lista, columna):
    return dataframe[dataframe[columna].isin(lista)]