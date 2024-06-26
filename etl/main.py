import os

from etl.extraction_load import Extract, Load
from etl.transformation import Transform
import pandas as pd
from src.parameters import BCRA, BYMA

extract = Extract()
load = Load()
transform = Transform()
bcra = BCRA()
byma = BYMA()
root_directory = os.environ.get('BASEPATH')

url_base, endpoints = bcra.api_bcra(2004, 2025)
for i in range(len(endpoints)):
    path = f"datalake/bronze/api_bcra/{endpoints[i][0]}/{endpoints[i][0]}_{endpoints[i][1][3:7]}.csv"
    data = extract.get_data(url_base, endpoints[i][1])
    load.save_to_csv(data, path)

transform.history_creator(root_directory)

url_base, endpoints = byma.api_byma()
for i in range(len(endpoints)):
    path = f"datalake/bronze/api_byma/{endpoints[i][0]}/{endpoints[i][1]}.csv"
    data = extract.get_data_byma(url_base, endpoints[i][1])
    load.save_to_csv(data, path)





