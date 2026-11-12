import sys
import pandas as pd
import matplotlib.pyplot as plt
def analisis_basico(nombre_fichero):
    filas = 0
    columnas = 0
    validos = 0

    with open(nombre_fichero, "r") as fichero:
        for linea in fichero:
            linea = linea.strip()

            if linea == "":
                continue

            valores = linea.split(",")
            filas += 1

            if filas == 1:
                columnas = len(valores)

            for valor in valores:
                if valor != "?":
                    validos += 1

    return filas, columnas, validos

def cargar_datos(nombre_fichero):
    return pd.read_csv(
        nombre_fichero,
        header=None,
        na_values="?"
    )


def es_numerica(columna):
    valores = columna.dropna()

    if len(valores) == 0:
        return False

    convertidos = pd.to_numeric(valores, errors="coerce")

    return convertidos.notna().all()

def determinar_tipos(datos):
    tipos = []

    for columna in datos.columns:
        if es_numerica(datos[columna]):
            tipos.append("numerica")
        else:
            tipos.append("categorica")

    return tipos

def formatear_numero(numero):
    return f"{numero:.2f}"

def opcion_p(datos, tipos):
    resultado = []

    for columna in datos.columns:
        serie = datos[columna].dropna()

        if len(serie) == 0:
            resultado.append("?")

        elif tipos[columna] == "numerica":
            numeros = pd.to_numeric(serie)
            resultado.append(formatear_numero(numeros.mean()))

        else:
            moda = serie.mode()
            resultado.append(str(moda.iloc[0]))

    print(",".join(resultado))

def opcion_s(datos, tipos):
    resultado = []

    for columna in datos.columns:
        serie = datos[columna].dropna()

        if len(serie) == 0:
            resultado.append("?")

        elif tipos[columna] == "numerica":
            numeros = pd.to_numeric(serie)
            resultado.append(formatear_numero(numeros.std()))

        else:
            resultado.append(str(serie.nunique()))

    print(",".join(resultado))

def opcion_n(datos):
    resultado = []

    for columna in datos.columns:
        cantidad = datos[columna].count()
        resultado.append(str(cantidad))

    print(",".join(resultado))


def opcion_m(datos, tipos):
    resultado = []

    for columna in datos.columns:
        serie = datos[columna].dropna()

        if len(serie) == 0:
            resultado.append("?")

        elif tipos[columna] == "numerica":

            numeros = pd.to_numeric(serie)
            resultado.append(formatear_numero(numeros.min()))

        else:
            frecuencias = serie.value_counts()
            minimo = frecuencias.min()
            categorias = frecuencias[frecuencias == minimo].index
            resultado.append(str(categorias[0]))

    print(",".join(resultado))

def opcion_M(datos, tipos):
    resultado = []

    for columna in datos.columns:
        serie = datos[columna].dropna()

        if len(serie) == 0:
            resultado.append("?")

        elif tipos[columna] == "numerica":
            numeros = pd.to_numeric(serie)
            resultado.append(formatear_numero(numeros.max()))

        else:
            frecuencias = serie.value_counts()
            maximo = frecuencias.max()
            categorias = frecuencias[frecuencias == maximo].index
            resultado.append(str(categorias[0]))

    print(",".join(resultado))

def opcion_P(datos, tipos):
    for columna in datos.columns:
        serie = datos[columna].dropna()

        if len(serie) == 0:
            continue

        plt.figure()

        if tipos[columna] == "numerica":
            numeros = pd.to_numeric(serie)
            barras = max(5, len(numeros) // 20)

            plt.hist(numeros, bins=barras)
            plt.title("Atributo " + str(columna))

        else:
            frecuencias = serie.value_counts()

            plt.pie(
                frecuencias.values,
                labels=frecuencias.index,
                autopct="%1.1f%%"
            )

            plt.title("Atributo " + str(columna))

        plt.show()

def main():
    if len(sys.argv) != 3:
        print("Uso: python estads.py nombre_fichero.csv opciones")
        return

    nombre_fichero = sys.argv[1]
    opciones = sys.argv[2]

    filas, columnas, validos = analisis_basico(nombre_fichero)

    print(f"{filas}x{columnas}: {validos}")

    datos = cargar_datos(nombre_fichero)
    tipos = determinar_tipos(datos)

    for opcion in opciones:
        if opcion == "p":
            opcion_p(datos, tipos)

        elif opcion == "s":
            opcion_s(datos, tipos)

        elif opcion == "n":
            opcion_n(datos)

        elif opcion == "m":
            opcion_m(datos, tipos)

        elif opcion == "M":
            opcion_M(datos, tipos)

        elif opcion == "P":
            opcion_P(datos, tipos)


if __name__ == "__main__":
    main()


