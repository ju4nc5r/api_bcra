import requests
import pandas as pd
import os

class Extract:

    def get_data(self, base_url, endpoint, params=None, headers=None):
        """
        Parametros:
        base_url(str): URL base de la API
        endpoint(str): endpoint al que se realizará la solicitud
        params(dict): parametros de consulta que se enviaran en la solicitud
        headers(dict): encabezados que se enviaran en la solicitud

        Retorna:
        dict: JSON de respuesta de la API
        """

        try:
            endpoint_url = f'{base_url}/{endpoint}'
            response = requests.get(endpoint_url, params=params, headers=headers, verify=False)
            response.raise_for_status()

            try:
                json_data = response.json()
                df = pd.json_normalize(json_data, record_path='results')
            except:
                print("Formato de response inesperado")
                return None
            return df

        except requests.exceptions.RequestException as err:
            print(f"La peticion ha fallado. Codigo de error: {err}")
            return None

    def save_to_csv(self, df, output_path, partition_cols=None):
        """
        Parametros:
        df (pd.DataFrame). Dataframe a guardar.
        output_path (str). Ruta donde se guardará el archivo. Si no existe, se creará.
        """

        # Crear el directorio si no existe
        directory = os.path.dirname(output_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        df.to_csv(output_path)

