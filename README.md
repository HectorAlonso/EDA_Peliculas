**RESUMEN Y CONCLUSIÓN DEL ANÁLISIS**

**EXPLORACION GENERAL** <br>

- **¿Cuál es la calificación promedio general de las películas?** <br>
  La calificación promedio es de 3.27 <br>
  
- **¿Qué porcentaje tiene más de 100,000 ratings?** <br>
  El porcentaje con más de 100,000 de ratings es del 20.05% <br>
  
- **¿Cuáles son los directores más frecuentes?** <br>
  Chuck Jones, Cirio H. Santiago, Antonio Margheriti, Robert Stevenson, Steven Spielberg <br>
  
- **¿Qué películas tienen calificación promedio más alta y más baja?** <br>
  La película con promedio mas alto es: Radiohead: In Rainbows - From the Basement - 4.71 <br>
  La película con promedio mas bajo es: 365 Days                                   - 1.08 <br>


**VISUALIZACIONES CON INTERPRETACIÓN** <br>

- **¿Hay un rango típico de duración? ¿Hay muchas películas muy cortas o muy largas?** <br>
  Si hay un rango típico: están en 70 y 120 min aproximadamente la mayoría de las películas, <br>
  No hay muchas películas muy cortas o largas, sin embargo, si existe un número considerable de películas muy cortas. <br> <br>
  ![Histograma de duración ](https://github.com/user-attachments/assets/42149b86-0e3b-4254-affc-e712ce0293c1) <br> <br>

- **¿Hay idiomas que suelen tener películas mejor calificadas?** <br>
  si, países como indonesian, Thai, Greek(modern) tienen mejores calificaciones <br> <br>
![Boxplot de calificación promedio por idioma original](https://github.com/user-attachments/assets/92eecc1a-b4c7-406e-b3d5-512467ffdc5f) <br> <br>
  
  
- **Cuenta cuántas veces aparece cada género.** <br> <br>
  ![Gráfico de barras de géneros más comunes](https://github.com/user-attachments/assets/5a032008-d0f5-4485-9ff5-34bfe3059ec4) <br> <br>

- **¿Las películas más largas reciben mejores calificaciones?** <br>
  No precisamente, la gran mayoría de las películas se encuentra en un rango de 0-200 minutos con una variabilidad considerable en sus calificaciones promedio.<br>
  Hay muy pocas películas con gran duración mayor a 200 o 300, pero sus calificaciones no parecer ser más altas que el resto de las películas,
  así que no, no hay una tendencia clara que a mayor duración mejor calificación promedio tendrá. <br> <br>
  ![Scatterplot de duración vs calificación promedio ](https://github.com/user-attachments/assets/6f7f9ec1-187e-43f2-ae4b-a01e9af151d1) <br> <br>


**ANÁLISIS POR POPULARIDAD** <br>

- **¿Cuáles son las películas con más ratings? ¿Coinciden con las mejor calificadas?** <br>
  Películas con mas rating: Barbie, Parasite, Interstellar, Fight Club, Joker. <br>
  Películas con mejor calificación: Radiohead: In Rainbows, Harakiri, Stop Making Sense, Planet Earth II, Come and See. <br>
  No hay una coincidencia entre películas con más rating y películas con mejor calificación, ya que depende mucho de las opiniones y gustos de los usuarios. <br>
  
- **Calcula el porcentaje de usuarios que dieron 5 estrellas vs 1 estrella para detectar películas polarizantes.** <br>
  No se encontró ninguna polarizante. <br>
  
- **¿Qué géneros aparecen más entre las películas con muchos votos?** <br>
  Drama, Comedia, Crimen, Aventura, Thriller, Ciencia ficción entre los más votados<br>

**ANÁLISIS POR PAÍS O REGIÓN** <br>

- **¿Qué países tienen más películas en el dataset?** <br>
  USA (7099) <br> UK (1330) <br> Francia (847) <br> Italia (614) <br> Alemania (518) <br>
  
- **Calcula el promedio de calificaciones por país.** <br>
  Paises como Algeria, Bosnia, Uganda dominan el promedio de calificación  <br>
  ![Promedio Por Pais](https://github.com/user-attachments/assets/313d6bb2-fcd9-4dc2-bf6a-b9f8a1cde909) <br> <br>

- **¿Hay países que destacan por tener películas consistentemente bien valoradas?** <br>
  En base a la desviación estándar y al promedio podemos deducir que países como Iran, Japan, Denmark, France, mantienen películas consistentes ya que tienen buen promedio de              calificación, buena cantidad de películas y su variación en base al promedio es baja, así que no hay mucha diferencia entre las calificaciones de las películas de esos países, lo que    quiere decir que sus calificaciones son buenas y que son consistentes. <br>

**ANÁLISIS POR DÉCADA** <br>

- **Número de películas por década.** <br>
  1950s: 1257 <br> 1960s: 1286 <br> 1970s: 1295 <br> 1980s: 1290 <br> 1990s: 1329 <br> 2000s: 1267 <br> 2010s: 1335 <br> 2020s: 773 <br>
  
- **Promedio de calificación por década.** <br>
  1950s: 3.294926 <br> 1960s: 3.244363 <br> 1970s: 3.264374 <br> 1980s: 3.252622 <br> 1990s: 3.268501 <br> 2000s: 3.260200 <br> 2010s: 3.267962 <br> 2020s: 3.296531 <br>
  
- **¿Hubo décadas “doradas”?** <br>
  Si hubo décadas doradas, las décadas los 70s y 2000s <br>

- **¿Algún descenso de calidad reciente?** <br>
  no, de hecho, incremento un poco, aunque nada realmente considerable. <br>
  
**CONCLUSIÓN** <br>

1. ¿Qué tipo de películas suelen gustar más según los datos? <br>
Las películas con genero de drama, Comedia y Crimen. <br> <br>

2. ¿Qué géneros o países tienen la mejor recepción crítica? <br>
  Los países Algeria, Bosnia, Uganda junto con los géneros Drama, Crimen y comedia mantienen la mejor recepción critica. <br>

3. ¿Hay relación entre duración y calificación? <br>
  no, no hay una tendencia clara que a mayor duración mejor calificación promedio tendrán las películas. <br>
   
4. ¿Cuáles son las películas más polarizantes del dataset? <br>
  No, hay películas polarizantes, puede que algunas películas tendrán un promedio de calificación de 30 o más en 5 estrellas pero no mantienen un promedio alto en 1 estrella, lo que        indica que no hay películas polarizantes. <br>

5. ¿Qué aprendiste sobre el gusto del público? <br>
  El publico prefiere películas de duración entre 70 y 140 min alrededor, con los géneros de Drama, Comedia y Acción, la mayoría del público fue más fan de las películas en la década de    los 2010s. <br> <br>

Países menos convencionales como Argelia, Bosnia o Uganda obtuvieron calificaciones muy altas, esto indica que, aunque producen menos películas logran mejor audiencia internacional y suelen tener mejor calidad o propuestas muy valoradas por el público. <br> <br>
Géneros normalmente populares como acción, aventura o ciencia ficción no se posicionan entre los de mayor calificación promedio, esto no es necesariamente falta de aceptación, sino más bien se debe a que su percepción es porque tiende a ser más variable o moderada. <br> <br>
Un dato interesante del análisis por país es que algunas naciones con menor presencia a nivel global como Argelia, Bosnia, Uganda y Latvia obtuvieron promedios de calificaciones altos, esto podría deberse a que las pocas películas de estos países que logran alcanzar un reconocimiento internacional suelen destacarse por su calidad cinematográfica, su valor cultural o lo original de su producción. <br> <br>
Por otro lado, países con grandes industrias cinematográficas como Estados unidos, Reino Unido o Francia no aparecen en los primeros lugares de promedio de calificación, esto podría deberse a que tienen un mayor volumen de producción y diversidad en la temática de las películas, lo que podría generar que su media de calificación sea tan amplia y menos concentrada en calificación con un nivel alto. <br> <br>
En conclusión, el conjunto de datos revela que el público tienden a valorar con mayor entusiasmó las películas con una experiencia significativa, además evidencia que la calidad y valor cultural de una obra puede sobresalir incluso en industrias cinematográficas pequeñas.


