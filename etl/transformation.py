import pandas as pd
import os

class Transform:

    def history_creator(self, root_directory):
        paths = os.listdir(root_directory)
        for path in paths:
            new_path = root_directory + f'/{path}'
            filenames = os.listdir(new_path)
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

