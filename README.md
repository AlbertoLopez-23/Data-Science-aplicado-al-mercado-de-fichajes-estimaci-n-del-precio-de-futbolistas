# SoccerData

## Cómo usar el código




---

## Fuentes de datos

A continuación se describen las fuentes de datos disponibles en SoccerData. Cada apartado incluye la URL del sitio, una breve descripción de la información y los atributos que obtendremos de cada una de ellas

### ClubElo

- **URL**: [URL de Club Elo](http://clubelo.com/)
  
- **Datos principales**  
  - `read_by_date()` → Elo rating de todos los clubes en la fecha más reciente o especificada:  
    - `rank`, `team`, `country`, `level`, `elo`, rango de validez (`from`–`to`), `league`  
  - `read_team_history(team)` → Historial completo de Elo de un club:  
    - Fecha de inicio y fin de cada valor de Elo, `elo`, `level`, `country`  
- **Único en**  
  - Ofrece **clasificaciones Elo** históricas y actuales sin depende de partidos individuales.

---

### ESPN

- **URL**: [URL de ESPN](https://espndeportes.espn.com/futbol/)
  
- **Datos principales**  
  - `read_schedule()` → Fixtures con fecha/hora, local/visitante, `game_id`, `league_id`  
  - `read_matchsheet(match_id)` → Hoja de partido:  
    - Local/visitante, estadio, asistencia/capacidad, lista de `roster`, faltas, tarjetas, offsides, córners, paradas, posesión, disparos totales y a puerta  
  - `read_lineup(match_id)` → Alineaciones y cambios:  
    - Para cada jugador: posición, tiempo en cancha, sustituciones, estadísticas de faltas, goles, asistencias, disparos, offsides, tarjetas  
- **Único en**  
  - Datos extraídos del **JSON oficial de ESPN**, idénticos a los que usa la web.

---

### FBref

- **URL**: [URL de FBref](https://fbref.com/es/)
  
- **Datos principales**  
  - `read_team_season_stats(stat_type)` → Estadísticas de temporada por equipo:  
    - Pases (Cmp/Att/%), distancias (Total, Short, Medium, Long), progresiones (PPA, CrsPA, PrgP), xA/xAG, key passes, KP, 1/3 entries, URL del equipo  
  - `read_team_match_stats(stat_type, team)` → Stats por partido:  
    - Fecha, jornada, local/visitante, resultado, GF/GA, xG/xGA, posesión, capitán, formación, árbitro, enlace al report  
  - `read_player_season_stats(stat_type)` → Stats de temporada por jugador:  
    - Minutos, goles, asistencias, xG/npxG, xA, pases progresivos, métricas per-90  
  - `read_player_match_stats(stat_type, match_id)` → Stats de partido por jugador (ej. passing, defensive)  
  - `read_schedule()` → Calendario con xG, marcador, árbitro, asistencia, `game_id`  
  - `read_lineup(match_id)` → Alineaciones con minutos y posiciones  
  - `read_events(match_id)` → Eventos (goles, tarjetas, sustituciones…) con minuto y jugadores  
  - `read_shot_events(match_id)` → Disparos con xG, PSxG, outcome, distancia, parte del cuerpo, SCA  
- **Único en**  
  - Métricas de **progresión de pase** (PPA, PrgP, CrsPA) y enlaces directos a páginas de FBref.

---

### FotMob

- **URL**: [URL de FotMob](https://www.fotmob.com/es)
  
- **Datos principales**  
  - `read_league_table()` → Tabla de posiciones: MP, W, D, L, GF, GA, GD, Pts  
  - `read_schedule()` → Calendario y resultados: ronda, fecha/hora, marcador, estado, `game_id`, URL directa a FotMob  
  - `read_team_match_stats(team)` → Stats por partido para un equipo:  
    - Pases precisos y %, posesión, “big chances” y falladas, córners, xG, tiros totales y a puerta, faltas  
- **Único en**  
  - **Enlaces directos** a cada partido en FotMob y métricas de “big chances” exclusivas.

---

### FiveThirtyEight

- **URL**: [URL de FiveThirtyEight](https://data.fivethirtyeight.com/)

- **Datos principales**  
  - `read_games()` → Fixtures con probabilidades (home/away/tie), goles reales vs. ajustados, “chances” y “moves” del modelo, resultado agregado  
  - `read_forecasts()` → Proyección de tabla: puntos, xG, probabilidades de título/Champions/Europa/descenso, distribución por posición  
  - `read_clinches()` → Fechas en que cada equipo asegura o queda eliminado de objetivos (título, descenso…)  
- **Único en**  
  - Proporciona **predicciones de modelo** con probabilidades y expected goals detallados, además de fechas de “clinches”.

---

### Match History

- **URL**: [URL de football-data](https://www.football-data.co.uk/data.php)

- **Datos principales**  
  - `read_games()` → Resultados históricos: FTHG, FTAG, FTR, HTHG, HTAG, HTR, árbitro  
  - Estadísticas de partido: HS/AS, HST/AST, HF/AF, HC/AC, HY/AY, HR/AR  
  - **Cuotas de apuestas**: Bet365, BW, IW, PS, WH, VC – mercados 1X2, O/U 2.5, hándicap asiático, córners… (máximos, mínimos y promedios)  
- **Único en**  
  - Cobertura exhaustiva de **mercados de apuestas** y cuotas de múltiples casas por partido.

---

### SoFIFA

- **URL**: [URL de SoFIFA](https://sofifa.com/) 

- **Datos principales**  
  - `read_players()` → Ficha de jugadores:  
    - `player_id`, `name`, `age`, `overall`, `potential`, `value`, `wage`, posiciones, país  
    - Atributos de EA Sports FC: pace, shoot, pass, dribble, defend, physical, skills  
  - `read_team_players(team)` → Mismos datos para un club concreto  
- **Único en**  
  - Atributos detallados de videojuego (**EA FC**) para cada futbolista, ideal para scouting y análisis gamificado.

---

### Understat

- **URL**: [URL de Understat](https://understat.com/) 
  
- **Datos principales**  
  - `available_leagues()` / `read_seasons()` → Listado de ligas y temporadas  
  - `read_schedule()` → Fixtures (incluso sin datos de xG)  
  - `read_team_match_stats()` → xG, non-penalty xG (npxG), xGA por equipo y partido  
  - `read_player_season_stats()` → Stats de temporada de jugadores: goles, asistencias, xG, xA, npxG…  
  - `read_player_match_stats(match_id)` → Mismo por partido  
  - `read_shot_events(match_id)` → Eventos de tiro: coordenadas, xG, outcome, tipo de tiro  
- **Único en**  
  - **Shot-level data** con xG y non-penalty xG en cada intento de disparo.

---

### WhoScored

- **URL**: [URL de WhoScored](https://es.whoscored.com/)

- **Datos principales**  
  - `read_schedule()` → Calendario: tarjetas, flags de incidentes, alineación confirmada, marcador, `game_id`  
  - `read_missing_players(match_id)` → Lesionados/suspendidos por partido (motivo, estado)  
  - `read_events(match_id, output_fmt)` →  
    - `events`: DataFrame con eventos Opta detallados  
    - `raw`: JSON original  
    - `spadl` / `atomic-spadl`: SPADL / Atomic SPADL  
    - `loader`: `OptaLoader` para luego llamar a `.games()`, `.teams()`, `.players()`, `.events()`  
- **Único en**  
  - Flujo de eventos **al nivel Opta**, exportable a SPADL y Atomic-SPADL para análisis táctico profundo.
