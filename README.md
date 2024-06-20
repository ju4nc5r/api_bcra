# api_bcra

## Puntos a considerar: 

- Comportamiento del precio del UVA a lo largo de los diferentes gobiernos.
- Comportamiento del precio del metro cuadrado a lo largo del tiempo
- Relacion entre el valor del CER, el UVA y la inflación. 

## Por agregar

1. Agregar los siguientes endpoints:
    1. M2: https://api.bcra.gob.ar/estadisticas/v2.0/DatosVariable/25/2024-05-01/2024-05-02
    2. DolarMay: https://api.bcra.gob.ar/estadisticas/v2.0/DatosVariable/5/2024-05-01/2024-05-02
    3. DolarMin: https://api.bcra.gob.ar/estadisticas/v2.0/DatosVariable/4/2024-05-01/2024-05-02

2. Integrar YF a la estructura de este proyecto o poder utilizar la información obtenida
   de este proyecto desde el otro.


## Necesidades

- Enteder como fue la relación entre el CER, UVA, Dolar e Inflación
- Analizar el comportamiento de la inflación en las diferentes presidencias
- Crear método que permita conocer el patrimonio actual y el porcentaje destinado a cada inversion.
- Simular ganancias futuras a partir de la tenencia/precio de cada accion a largo plazo.
- Simular ganancias futuras a partir de las distintas monedas (USD,BTC,ETH)
- Crear método para definir cuando comprar/vender una accion.


## Preguntas
1. ¿Cómo verifico que existe una relación entre cada variable?
2. ¿A qué se deben los cambios en la base monetaria?
3.


## Propuestas

1. Calcular el impacto que tiene la variación diaria del CER sobre el precio del UVA.
2. Calcular el impacto que tiene la variación de la inflación sobre el precio del CER y UVA.
3. Calcular el valor de la devaluación diaria o semanal.
4. Monitorear el valor del metro cuadrado y el metro de construcción.
5. Monitorear el valor del riesgo pais




Ideas:
(Verificar si se puede implementar a partir de la API de FMP)
    Dentro de una organización el exceso de liquidez global no es un buen indicio del estado
    de la misma. Esto se puede calcular a partir de RL = AC/PC

    Se calcula dividiendo el activo corriente (AC) o a corto plazo, aquel que se puede
    convertir en dinero en efectivo en menos de un año, entre el pasivo corriente (PC) o
    a corto plazo, con las deudas con vencimiento inferior al año.


Primeros pasos:

1. 