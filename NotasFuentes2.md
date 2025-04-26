# Opinion sobre las bases de datos:


Recordar poner no_store=True para que no lo almacene en local home/user/sofascore

---
**ESPN:**
Creo que esta no vale la pena porque FBREF es simplemnente mejor

1. Habría que hacer un bucle donde primero ejecutamos espn.read_schedule()
2. Los ids obtenidos del paso 1 los iterariamso en espn.read_matchsheet(match_id={}) **Es mejor el de FBref**
3. Iteramos los ids por espn.read_lineup(match_id={}) y obtenemos la información detallada de cada juagdor.

Obtendriamos las estadistcias base del partido (2), y las estadísticas básicas de cada jugador (3).


**FBref:**
Tiene dos funciones:

1. read_team_season_stats(stat_type="passing"): que nos da informacion muy detallada de un equipo sobre un atributo ()
2. Con Team match stat conseguimos lo mismo que en FBref, pero ademas informacion adicional como la alineación y el xG
3. read_player_season_stats(stat_type="standard") Nos da el resumen de la temporada de cada jugador, con estadisticas avanzadas (xG npxG...)
4. read_player_match_stats nos da lo mismo que (3) peor por partido, yo pienso que simplifica mucho más coger (3) qu e(4) aunque coger (4) nos permitiria correlacionarlo con las alineaciones (creo que no vale la pena).
5. read_lineup(match_id='db261cb0'),.read_events(match_id='db261cb0'),read_shot_events(match_id='db261cb0'). Opino que no interesan, las alineaciones, los eventos no aportan informacion no presente entre el 1 y 4.

**FiveThirtyEight**

Opino que es una web con pronósticos, si usamos pronosticos ne nuetsro análisis dependemos de como de bueno sean nuetsro análisis, al ser un proyecto universitario creo que no convieneincluirlos.

**FotMob**

1. .read_team_match_stats, tien menos información que FBref pero incluye Big Chances, que son atributos que noincluiye Bref, creo que interesaría si no es demasiado complicado utilizarla.
   
**MatchHistory**

1. La estadistica más cmpleta suele ser la de Fbref, esta tiene n read_games(), las cuotas de epauetsas de los partidos, aunque es muy interesnate,c reo que a la hora de evaluar los juagdores no es un dato que nos interese.

**Understat**
1. Tiene .read_team_match_stats() atributos que no estan presentes en FBref, podria servir de complementaria.
2. .read_player_season_stats() Tiene estadisticas complejas de los ugadores, las justas y necesarias, creo que vale la pena.
3. Como en FBref .read_player_match_stats(), las de partido aunque son útiles creo que con las de temporada vamos perfe.

**Whoscore**
1. .read_missing_players(match_id=1485184) Esto es lo que ocnsidero rescatable de esta web, podríamos crear un atributo como la influencia del jugador, a ver que pasa cuando no está.