from etl.data_load import Extract
import pandas as pd

# URL's
url_varPrincipales = "https://api.bcra.gob.ar/estadisticas/v2.0/PrincipalesVariables"
url_base = "https://api.bcra.gob.ar/estadisticas/v2.0/DatosVariable"
endpoints = {"CER": '30/2016-05-31/2024-05-31',
             "UVA": '31/2016-05-31/2024-05-31'}

extract = Extract()
for k in endpoints.keys():
    path = f"datalake/bronze/{k}/data.csv"
    data = extract.get_data(url_base, endpoints[k])
    extract.save_to_csv(data, path)







