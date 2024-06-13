from etl.data_load import Extract
import pandas as pd
from src.parameters import BCRA

extract = Extract()

bcra = BCRA()
url_base, endpoints = bcra.api_bcra(2004, 2025)


for i in range(len(endpoints)):
    path = f"datalake/bronze/{endpoints[i][0]}/{endpoints[i][0]}_{endpoints[i][1][3:7]}.csv"
    data = extract.get_data(url_base, endpoints[i][1])
    extract.save_to_csv(data, path)







