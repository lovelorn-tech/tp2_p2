import matplotlib.pyplot as mp
from pandas_utils import abrir_archivo
from pandas_utils import nuevo_dataframe
from pandas_utils import crear_top5_dataframe
from pandas_utils import filtrar_dataframe
import constantes


def main():
    dataframe = get_dataframe()
    top5 = crear_top5_dataframe(dataframe, constantes.ULTIMO_ANIO_DISPONIBLE)
    top5.plot(kind='bar', x=constantes.ARCHIVO_ENERGIAS_RENOVABLES_CODIGO_PAIS, y=constantes.ULTIMO_ANIO_DISPONIBLE)
    mp.show()


def get_dataframe():
    country_code = get_country_code_list()
    dataframe = nuevo_dataframe(abrir_archivo(constantes.ARCHIVO_ENERGIAS_RENOVABLES))
    return filtrar_dataframe(dataframe, country_code, constantes.ARCHIVO_EMISIONES_CO2_COLUMNA_CODIGOS_PAISES)


def get_country_code_list():
    country_code = nuevo_dataframe(abrir_archivo(constantes.ARCHIVO_CODIGOS_PAISES))
    return country_code[constantes.ARCHIVO_CODIGOS_PAISES_COLUMNA_CODIGOS].to_list()


if __name__ == '__main__':
    main()

