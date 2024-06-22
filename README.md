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


## Temas por ver 

1. Frontera eficiente
2. Capital Asset Pricing Model CAPM
3. Portafolio de Markowitz
4. RSI `indice de fuerza relativa`: Indica si hay precio de sobrecompra
5. Pruebas de normalidad


### Pruebas de Normalidad
Los contrastes o análisis de normalidad son pruebas estadísticas para determinar si una muestra de datos proviene de una población
que sigue una distribución normal.

    Test de Kolmogorov-Smirnov.

    Compara la distribución acumulativa de los datos de la muestra con la distribución acumulativa esperada de una distribución normal.
    Mide la máxima diferencia absoluta entre las dos distribuciones.

    Test de Shapiro-Wilk.

    Evalúa si una muestra proviene de una población normalmente distribuida.
    Es especialmente eficaz para tamaños de muestra pequeños.

    Test de Anderson-Darling.

    Una versión mejorada de la prueba de Kolmogorov-Smirnov que da más peso a los extremos de la distribución.

    Test de Jarque-Bera.

    Se basa en la asimetría y la curtosis de los datos para determinar la normalidad.
    Evalúa si la distribución de los datos difiere de una distribución normal en términos de asimetría y curtosis.

#### ¿Cómo analizar los resultados?

#### Uso del Valor p en Pruebas de Hipótesis
Se establacen las hipótesis nula y alternativa:

Hipótesis nula. Los datos siguen una distribución normal.

Hipótesis alternativa. Los datos no siguen una distribución normal.

 - Si el valor p de la prueba es mayor que el nivel de significancia (por ejemplo, 0.05), no se rechaza la hipótesis nula de normalidad. Esto significa que no hay evidencia suficiente para decir que los datos no provienen de una distribución normal.


 - Si el valor p es menor que el nivel de significancia, se rechaza la hipótesis nula de normalidad, lo que sugiere que los datos no provienen de una distribución normal.


