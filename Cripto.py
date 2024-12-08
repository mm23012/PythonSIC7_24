import pandas as pd
import os
import matplotlib.pyplot as plt

# Cargar los archivos CSV en un diccionario de DataFrames
data_folder = 'C:/Users/cwald/Documents/PROYECTO SAMSUMG/data'
crypto_files = os.listdir(data_folder)

# Cargar todos los CSV en un diccionario
crypto_data = {}
for file in crypto_files:
    if file.endswith('.csv'):
        coin_name = file.split('.')[0].lower()  # Obtener el nombre de la criptomoneda
        try:
            df = pd.read_csv(os.path.join(data_folder, file))
            # Renombrar la columna 'Date' si hay variantes
            date_columns = ['Date', 'date', 'Timestamp', 'fecha']
            for col in date_columns:
                if col in df.columns:
                    df.rename(columns={col: 'Date'}, inplace=True)
                    break
            # Verificar si la columna 'Date' está presente
            if 'Date' in df.columns:
                # Convertir la columna 'Date' a formato datetime
                df['Date'] = pd.to_datetime(df['Date'])
                crypto_data[coin_name] = df
            else:
                print(f"Advertencia: La columna 'Date' no se encuentra en {file}.")
        except Exception as e:
            print(f"Error al procesar {file}: {e}")

# 1. Exploración inicial de los datos
for coin, df in crypto_data.items():
    print(f"Primeras filas de {coin}:")
    print(df.head(), "\n")

# Estadísticas descriptivas para las primeras criptomonedas
for coin, df in crypto_data.items():
    print(f"Estadísticas descriptivas de {coin}:")
    print(df.describe(), "\n")

# Verificar los valores nulos
for coin, df in crypto_data.items():
    print(f"Valores nulos en {coin}:")
    print(df.isnull().sum(), "\n")

# 2. Preprocesamiento de datos
# Convertir las columnas de fecha y precio a los tipos de datos correctos
for coin, df in crypto_data.items():
    df['Price'] = df['Price'].astype(float)  # Asegurarse que el precio sea float
    df['Volume'] = df['Volume'].astype(float)  # Asegurarse que el volumen sea float

# Rellenar valores nulos con la media de la columna correspondiente
for coin, df in crypto_data.items():
    df.fillna(df.mean(), inplace=True)

# 3. Agrupar los datos por fecha
for coin, df in crypto_data.items():
    grouped = df.groupby('Date').agg({'Price': 'mean', 'Volume': 'sum'})
    print(f"Datos agrupados de {coin}:")
    print(grouped.head(), "\n")

# 4. Análisis y visualización

# Graficar la evolución de los precios de las criptomonedas
cryptos_to_plot = ['bitcoin', 'ethereum', 'dogecoin', 'litecoin']

plt.figure(figsize=(10, 6))

for coin in cryptos_to_plot:
    if coin in crypto_data:
        df = crypto_data[coin]
        df_2015 = df[df['Date'].dt.year == 2015]  # Filtrar datos de 2015
        plt.plot(df_2015['Date'], df_2015['Price'], label=coin.capitalize())

plt.title('Evolución de precios de las criptomonedas más interesantes en 2015')
plt.xlabel('Fecha')
plt.ylabel('Precio (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Calcular la media y desviación estándar
for coin, df in crypto_data.items():
    df_2015 = df[df['Date'].dt.year == 2015]
    mean_price = df_2015['Price'].mean()
    std_price = df_2015['Price'].std()
    print(f"{coin.capitalize()} - Media 2015: {mean_price:.2f}, Desviación estándar: {std_price:.2f}")

# Determinar la criptomoneda más volátil
volatility = {}
for coin, df in crypto_data.items():
    df_2015 = df[df['Date'].dt.year == 2015]
    std_price = df_2015['Price'].std()
    volatility[coin] = std_price

# Ordenar por volatilidad
sorted_volatility = sorted(volatility.items(), key=lambda x: x[1], reverse=True)
print("Criptomonedas más volátiles en 2015:")
for coin, vol in sorted_volatility:
    print(f"{coin.capitalize()} - Volatilidad: {vol:.2f}")
