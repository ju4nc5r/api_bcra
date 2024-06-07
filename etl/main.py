from etl.data_load import Extract
import pandas as pd
from src.parameters import BCRA

extract = Extract()

bcra = BCRA()
url_base, endpoints = bcra.api_bcra()


for var in endpoints:
    path = f"datalake/bronze/{var[0]}/{var[0]}.csv"
    data = extract.get_data(url_base, var[1])
    extract.save_to_csv(data, path)







