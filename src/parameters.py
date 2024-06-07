def create_list(**kwargs):
    return [(key, value) for key, value in kwargs.items()]

def dates(year_s: int, year_e: int):

    starts: list = []
    ends: list = []

    for year in range(year_s, year_e):
        date = f'{year}-01-01'
        ends = f'{year}-12-31'
        starts.append(date)
        ends.append(ends)

    return starts, ends


class BCRA:

    def api_bcra(self):
        #url_varPrincipales = "https://api.bcra.gob.ar/estadisticas/v2.0/PrincipalesVariables",

        url_base = "https://api.bcra.gob.ar/estadisticas/v2.0/DatosVariable"
        endpoints = create_list(
                                reservas_BCRA='1/2024-05-01/2024-05-02',
                                depositos_bcos_bcra='19/2024-05-01/2024-05-02',
                                inflacion_mensual='27/2023-05-01/2024-05-01',
                                inflacion_esperada='29/2023-05-01/2024-05-01',
                                inflacion_interanual='28/2023-05-01/2024-05-01',
                                CER='30/2024-05-30/2024-05-31',
                                UVA='31/2024-05-30/2024-05-31',
                                UVI='32/2023-05-31/2024-05-31'
                                )

        return url_base, endpoints

