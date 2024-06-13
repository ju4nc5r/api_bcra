# Pasos

# 1. Unificar todos los csv's en uno.
# 2. Defino un data frame por endpoint
# 3. Realizar las consultas con inline_sql

#import pandas as pd
#import os
'''
# Directorio raíz donde se encuentran los archivos CSV y subcarpetas
root_directory = '/home/juancr/Proyectos/APIBCRA/APIBCRA/etl/datalake/bronze'

# Verificar que el directorio raíz exista
if not os.path.exists(root_directory):
    print(f"El directorio {root_directory} no existe.")
else:
    # Lista para almacenar cada DataFrame
    data_frames = []

    # Recorrer todos los directorios y subdirectorios
    for dirpath, dirnames, filenames in os.walk(root_directory):
        print(f"Explorando el directorio: {dirpath}")  # Depuración
        for file in filenames:
            print(f"Encontrado archivo: {file}")  # Depuración
            if file.endswith('.csv'):
                file_path = os.path.join(dirpath, file)
                print(f"Leyendo archivo CSV: {file_path}")  # Depuración
                # Leer cada archivo CSV y agregarlo a la lista
                df = pd.read_csv(file_path)
                data_frames.append(df)

            # Verificar si se encontraron archivos CSV
            if data_frames:
                # Concatenar todos los DataFrames en uno solo
                combined_df = pd.concat(data_frames, ignore_index=True)
                # Guardar el DataFrame combinado en un nuevo archivo CSV
                combined_csv_path = f'{dirpath}/history.csv'
                combined_df.to_csv(combined_csv_path, index=False)
                print(f"Archivos CSV unificados y guardados en {combined_csv_path}")
            else:
                print("No se encontraron archivos CSV.")
'''

import pandas as pd
import os


root_directory = '/home/juancr/Proyectos/APIBCRA/APIBCRA/etl/datalake/bronze'
paths = os.listdir(root_directory)

for path in paths:
    new_path = f'/home/juancr/Proyectos/APIBCRA/APIBCRA/etl/datalake/bronze/{path}'
    filenames = (os.listdir(new_path))

    data_frames = []

    for file in filenames:
        if file.endswith('.csv'):
            file_path = os.path.join(new_path, file)
            print(file_path)
            df = pd.read_csv(file_path)
            data_frames.append(df)

    if data_frames:
        combined_df = pd.concat(data_frames, ignore_index=True) # Concatenar todos los DataFrames en uno solo
        combined_csv_path = f'{new_path}/history.csv' # Guardar el DataFrame combinado en un nuevo archivo CSV
        combined_df.to_csv(combined_csv_path, index=False)
        print(f"Archivos CSV unificados y guardados en {combined_csv_path}")
    else:
        print("No se encontraron archivos CSV.")



