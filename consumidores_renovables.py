import matplotlib.pyplot as mp

from pandas_utils import abrir_archivo
from pandas_utils import nuevo_dataframe
from pandas_utils import crear_top5_dataframe
from pandas_utils import filtrar_dataframe
import constantes


def main():
    dataframe_energy = get_dataframe(constantes.ARCHIVO_ENERGIAS_RENOVABLES)
    dataframe_energy = filter_dataframe(dataframe_energy, constantes.COLUMNA_CODIGOS_PAISES, get_country_code_list())
    top5 = crear_top5_dataframe(dataframe_energy, constantes.ULTIMO_ANIO_DISPONIBLE)
    top5.plot(kind='bar', x=constantes.COLUMNA_NOMBRES_PAISES, y=constantes.ULTIMO_ANIO_DISPONIBLE)

    dataframe_co2_per_year = get_dataframe(constantes.ARCHIVO_EMISIONES_CO2)
    country_energy_names = top5[constantes.COLUMNA_NOMBRES_PAISES].tolist()
    dataframe_co2_per_year = filter_dataframe(dataframe_co2_per_year,
                                              constantes.COLUMNA_NOMBRES_PAISES,
                                              country_energy_names)
    top5_co2 = crear_top5_dataframe(dataframe_co2_per_year, constantes.ULTIMO_ANIO_DISPONIBLE)
    top5_co2.plot(kind='bar', x=constantes.COLUMNA_NOMBRES_PAISES, y=constantes.LAST_FIVE_YEARS)

    mp.show()


def get_dataframe(file):
    return nuevo_dataframe(abrir_archivo(file))


def filter_dataframe(dataframe, filter_column, filter_values):
    return filtrar_dataframe(dataframe, filter_values, filter_column)


def get_country_code_list():
    country_code = nuevo_dataframe(abrir_archivo(constantes.ARCHIVO_CODIGOS_PAISES))
    return country_code[constantes.ARCHIVO_CODIGOS_PAISES_COLUMNA_CODIGOS].to_list()


if __name__ == '__main__':
    main()
