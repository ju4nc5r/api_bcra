def create_list(**kwargs):
    return [(key, value) for key, value in kwargs.items()]


def dates(year_s: int, year_e: int):

    starts: list[str] = []
    ends: list[str] = []

    for year in range(year_s, year_e):
        date: str = f'{year}-01-01'
        end: str = f'{year}-12-31'
        starts.append(date)
        ends.append(end)

    return starts, ends

# Tenemos una funcion que devuelve una lista con fechas iniciales y una lista
# con fechas finales.
#
# El objetivo es que las variables asignadas a cada endpoint esten definidas
# con una fecha 'desde' de la lista 'starts' y una fecha 'end' de la lista 'ends'.


class BCRA:

    def api_bcra(self, year_s: int, year_e: int):
        #url_varPrincipales = "https://api.bcra.gob.ar/estadisticas/v2.0/PrincipalesVariables",

        url_base = "https://api.bcra.gob.ar/estadisticas/v2.0/DatosVariable"

        starts, ends = dates(year_s, year_e)
        res: list = []
        years: list = []

        for i in range(len(starts)):
            year_end = int(ends[i][:4])
            year_st = int(starts[i][:4])
            if year_end > 2016 and year_st > 2016:
                endpoints = create_list(
                    reservas_BCRA=f'1/{starts[i]}/{ends[i]}',
                    depositos_bcos_bcra=f'19/{starts[i]}/{ends[i]}',
                    inflacion_mensual=f'27/{starts[i]}/{ends[i]}',
                    inflacion_esperada=f'29/{starts[i]}/{ends[i]}',
                    inflacion_interanual=f'28/{starts[i]}/{ends[i]}',
                    CER=f'30/{starts[i]}/{ends[i]}',
                    UVA=f'31/{starts[i]}/{ends[i]}',
                    UVI=f'32/{starts[i]}/{ends[i]}'
                )
            else:
                endpoints = create_list(
                    reservas_BCRA=f'1/{starts[i]}/{ends[i]}',
                    depositos_bcos_bcra=f'19/{starts[i]}/{ends[i]}',
                    inflacion_mensual=f'27/{starts[i]}/{ends[i]}',
                    inflacion_esperada=f'29/{starts[i]}/{ends[i]}',
                    inflacion_interanual=f'28/{starts[i]}/{ends[i]}',
                )

            res.extend(endpoints)

        return url_base, res

class BYMA:

    def api_byma(self):
        url_base = f'https://open.bymadata.com.ar/vanoms-be-core/rest/api/bymadata/free'
        endpoints = create_list(
                     cedear='cedears',
                     etf='etf',
                     acciones_locales='leading-equity',
                     acciones_globales='general-equity',
                     indices_byma='index-price',
                     titulos_publicos='public-bonds')

        return url_base, endpoints

