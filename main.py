import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')  # O 'Qt5Agg', 'GTK3Agg', etc.
import matplotlib.pyplot as plt
import qgrid

url_varPrincipales = "https://api.bcra.gob.ar/estadisticas/v2.0/PrincipalesVariables"
url_base = "https://api.bcra.gob.ar/estadisticas/v2.0/DatosVariable"

# URL de la API

url_CER = f'{url_base}/30/2023-05-01/2023-06-01'
url_UVA = f'{url_base}/31/2023-05-31/2024-05-31'


class create_graphic:

    def proccess(self, url):
        data = self.request2df(url)
        self.graphic(data)

    def request2df(self, url):
        response = requests.get(url, verify=False)

        # Verificar que la solicitud fue exitosa
        if response.status_code == 200:
            data = response.json()
            data_normalize = pd.json_normalize(data, record_path='results')
            print(data_normalize)

            return data_normalize

        else:
            print(f"Error en la solicitud: {response.status_code}")

    def graphic(self, data):
        #   Ejemplo de gráfico de línea
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x='fecha', y='valor')
        plt.title('UVA 31-05-2023 a 31-05-2024')
        plt.xlabel('Fecha')
        plt.xticks(rotation=45)
        plt.ylabel('Valor')
        plt.show()

        # Ejemplo de gráfico de barras
        plt.figure(figsize=(10, 6))
        sns.barplot(data=data, x='fecha', y='valor')
        plt.title('UVA 31-05-2023 a 31-05-2024')
        plt.xlabel('Fecha')
        plt.xticks(rotation=45)
        plt.ylabel('Valor')
        plt.show()


req = create_graphic()
req.proccess(url_varPrincipales)


