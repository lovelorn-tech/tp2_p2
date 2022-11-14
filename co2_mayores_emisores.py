import matplotlib.pyplot as mp

from pandas_utils import nuevo_dataframe
from pandas_utils import crear_top5_dataframe
from pandas_utils import filtrar_dataframe
from pandas_utils import abrir_archivo

import constantes

def main():
    emisiones_co2_dataframe = obtener_dataframe_emisiones_co2()

    top_5_emisores_df = crear_top5_dataframe(emisiones_co2_dataframe, constantes.ULTIMO_ANIO_DISPONIBLE)
    top_5_emisores_df.plot(kind = 'bar', x = constantes.ARCHIVO_EMISIONES_CO2_COLUMNA_NOMBRES_PAISES, y =constantes.ULTIMO_ANIO_DISPONIBLE)

    mp.show()


def obtener_lista_codigos_paises():
    codigos_paises = nuevo_dataframe(abrir_archivo(constantes.ARCHIVO_CODIGOS_PAISES))
    return codigos_paises[constantes.ARCHIVO_CODIGOS_PAISES_COLUMNA_CODIGOS].to_list()

def obtener_dataframe_emisiones_co2():
    codigos_paises = obtener_lista_codigos_paises()
    emisiones_dataframe = nuevo_dataframe(abrir_archivo(constantes.ARCHIVO_EMISIONES_CO2))
    return filtrar_dataframe(emisiones_dataframe, codigos_paises, constantes.ARCHIVO_EMISIONES_CO2_COLUMNA_CODIGOS_PAISES)

if __name__ == "__main__":
    main()