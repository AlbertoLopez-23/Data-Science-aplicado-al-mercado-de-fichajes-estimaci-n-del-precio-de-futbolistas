import os
import sys
import pandas as pd
import soccerdata as sd

def create_output_dir(source_name="FBref"):
    """Crear la carpeta output y una subcarpeta para la fuente de datos"""
    # Obtener la ruta del directorio actual donde se ejecuta el script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Crear la carpeta output si no existe
    output_dir = os.path.join(current_dir, "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Crear una subcarpeta para la fuente de datos
    source_dir = os.path.join(output_dir, source_name)
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
    
    return source_dir

def setup_soccerdata_dir():
    """Configurar el directorio de caché de soccerdata en el directorio local"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cache_dir = os.path.join(current_dir, "soccerdata")
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    
    # Establecer la variable de entorno para soccerdata
    os.environ['SOCCERDATA_DIR'] = cache_dir
    return cache_dir

def get_team_season_stats(output_dir, leagues="ENG-Premier League", seasons=2021, stat_type="passing"):
    """Obtiene estadísticas de temporada por equipo"""
    fbref = sd.FBref(leagues=leagues, seasons=seasons, no_store=True)
    team_stats = fbref.read_team_season_stats(stat_type=stat_type)
    
    # Convertir el índice a columnas
    team_stats_modified = team_stats.reset_index()
    
    # Definir la ruta de salida
    output_path = os.path.join(output_dir, f"fbref_1.csv")
    
    # Guardar los datos en un archivo CSV con punto y coma como separador
    # y punto para los decimales
    team_stats_modified.to_csv(output_path, sep=";", decimal=".", index=False)
    
    print(f"Archivo creado exitosamente: {output_path}")
    return team_stats

def get_team_match_stats(output_dir, team="Manchester City", leagues="ENG-Premier League", seasons=2021, stat_type="schedule"):
    """Obtiene estadísticas de partidos por equipo"""
    fbref = sd.FBref(leagues=leagues, seasons=seasons, no_store=True)
    match_stats = fbref.read_team_match_stats(stat_type=stat_type, team=team)
    
    # Convertir el índice a columnas
    match_stats_modified = match_stats.reset_index()
    
    # Definir la ruta de salida
    output_path = os.path.join(output_dir, f"fbref_2.csv")
    
    # Guardar los datos en un archivo CSV con punto y coma como separador
    # y punto para los decimales
    match_stats_modified.to_csv(output_path, sep=";", decimal=".", index=False)
    
    print(f"Archivo creado exitosamente: {output_path}")
    return match_stats

def get_player_season_stats(output_dir, leagues="ENG-Premier League", seasons=2021, stat_type="standard"):
    """Obtiene estadísticas de temporada por jugador"""
    fbref = sd.FBref(leagues=leagues, seasons=seasons, no_store=True)
    player_stats = fbref.read_player_season_stats(stat_type=stat_type)
    
    # Convertir el índice a columnas
    player_stats_modified = player_stats.reset_index()
    
    # Definir la ruta de salida
    output_path = os.path.join(output_dir, f"fbref_3.csv")
    
    # Guardar los datos en un archivo CSV con punto y coma como separador
    # y punto para los decimales
    player_stats_modified.to_csv(output_path, sep=";", decimal=".", index=False)
    
    print(f"Archivo creado exitosamente: {output_path}")
    return player_stats

def get_player_match_stats(output_dir, match_id, leagues="ENG-Premier League", seasons=2021, stat_type="passing"):
    """Obtiene estadísticas de partidos por jugador para un partido específico"""
    fbref = sd.FBref(leagues=leagues, seasons=seasons, no_store=True)
    player_match_stats = fbref.read_player_match_stats(stat_type=stat_type, match_id=match_id)
    
    # Convertir el índice a columnas
    player_match_stats_modified = player_match_stats.reset_index()
    
    # Definir la ruta de salida
    output_path = os.path.join(output_dir, f"fbref_4_{match_id}.csv")
    
    # Guardar los datos en un archivo CSV con punto y coma como separador
    # y punto para los decimales
    player_match_stats_modified.to_csv(output_path, sep=";", decimal=".", index=False)
    
    print(f"Archivo creado exitosamente: {output_path}")
    return player_match_stats

def get_schedule(output_dir, leagues="ENG-Premier League", seasons=2021):
    """Obtiene el calendario de partidos"""
    fbref = sd.FBref(leagues=leagues, seasons=seasons, no_store=True)
    schedule = fbref.read_schedule()
    
    # Convertir el índice a columnas
    schedule_modified = schedule.reset_index()
    
    # Definir la ruta de salida
    output_path = os.path.join(output_dir, f"fbref_5.csv")
    
    # Guardar los datos en un archivo CSV con punto y coma como separador
    # y punto para los decimales
    schedule_modified.to_csv(output_path, sep=";", decimal=".", index=False)
    
    print(f"Archivo creado exitosamente: {output_path}")
    return schedule

def get_lineup(output_dir, match_id, leagues="ENG-Premier League", seasons=2021):
    """Obtiene las alineaciones de un partido específico"""
    fbref = sd.FBref(leagues=leagues, seasons=seasons, no_store=True)
    lineup = fbref.read_lineup(match_id=match_id)
    
    # Convertir el índice a columnas
    lineup_modified = lineup.reset_index()
    
    # Definir la ruta de salida
    output_path = os.path.join(output_dir, f"fbref_6_{match_id}.csv")
    
    # Guardar los datos en un archivo CSV con punto y coma como separador
    # y punto para los decimales
    lineup_modified.to_csv(output_path, sep=";", decimal=".", index=False)
    
    print(f"Archivo creado exitosamente: {output_path}")
    return lineup

def get_events(output_dir, match_id, leagues="ENG-Premier League", seasons=2021):
    """Obtiene los eventos de un partido específico"""
    fbref = sd.FBref(leagues=leagues, seasons=seasons, no_store=True)
    events = fbref.read_events(match_id=match_id)
    
    # Convertir el índice a columnas
    events_modified = events.reset_index()
    
    # Definir la ruta de salida
    output_path = os.path.join(output_dir, f"fbref_7_{match_id}.csv")
    
    # Guardar los datos en un archivo CSV con punto y coma como separador
    # y punto para los decimales
    events_modified.to_csv(output_path, sep=";", decimal=".", index=False)
    
    print(f"Archivo creado exitosamente: {output_path}")
    return events

def get_shot_events(output_dir, match_id, leagues="ENG-Premier League", seasons=2021):
    """Obtiene los eventos de tiros de un partido específico"""
    fbref = sd.FBref(leagues=leagues, seasons=seasons, no_store=True)
    shots = fbref.read_shot_events(match_id=match_id)
    
    # Convertir el índice a columnas
    shots_modified = shots.reset_index()
    
    # Definir la ruta de salida
    output_path = os.path.join(output_dir, f"fbref_8_{match_id}.csv")
    
    # Guardar los datos en un archivo CSV con punto y coma como separador
    # y punto para los decimales
    shots_modified.to_csv(output_path, sep=";", decimal=".", index=False)
    
    print(f"Archivo creado exitosamente: {output_path}")
    return shots

def print_usage():
    """Imprime instrucciones de uso del script"""
    print("\nUso: python3 FBref.py [opción] [parámetros adicionales]")
    print("\nOpciones:")
    print("1: Obtener estadísticas de temporada por equipo (stat_type opcional)")
    print("2 [equipo]: Obtener estadísticas de partidos por equipo (stat_type opcional)")
    print("3: Obtener estadísticas de temporada por jugador (stat_type opcional)")
    print("4 [match_id]: Obtener estadísticas de partidos por jugador para partido específico (stat_type opcional)")
    print("5: Obtener calendario de partidos")
    print("6 [match_id]: Obtener alineaciones de un partido específico")
    print("7 [match_id]: Obtener eventos de un partido específico")
    print("8 [match_id]: Obtener eventos de tiros de un partido específico")
    print("\nEjemplos:")
    print("python3 FBref.py 1 passing")
    print("python3 FBref.py 2 \"Manchester City\" schedule")
    print("python3 FBref.py 3 standard")
    print("python3 FBref.py 4 db261cb0 passing")
    print("python3 FBref.py 5")
    print("python3 FBref.py 6 db261cb0")
    print("python3 FBref.py 7 db261cb0")
    print("python3 FBref.py 8 db261cb0")

def main():
    # Configurar el directorio de caché de soccerdata
    setup_soccerdata_dir()
    
    # Crear la carpeta output con una subcarpeta para FBref
    output_dir = create_output_dir("FBref")
    
    # Verificar los argumentos de la línea de comandos
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar al menos una opción.")
        print_usage()
        return
    
    try:
        option = int(sys.argv[1])
        
        # Parámetros predeterminados
        league = "ENG-Premier League"
        season = 2021
        
        if option == 1:
            # Opción 1: Obtener estadísticas de temporada por equipo
            stat_type = "passing"  # valor predeterminado
            if len(sys.argv) >= 3:
                stat_type = sys.argv[2]
            get_team_season_stats(output_dir, leagues=league, seasons=season, stat_type=stat_type)
            
        elif option == 2:
            # Opción 2: Obtener estadísticas de partidos por equipo
            if len(sys.argv) >= 3:
                team = sys.argv[2]
                stat_type = "schedule"  # valor predeterminado
                if len(sys.argv) >= 4:
                    stat_type = sys.argv[3]
                get_team_match_stats(output_dir, team=team, leagues=league, seasons=season, stat_type=stat_type)
            else:
                print("Error: Para la opción 2, debes proporcionar un nombre de equipo.")
                print_usage()
                
        elif option == 3:
            # Opción 3: Obtener estadísticas de temporada por jugador
            stat_type = "standard"  # valor predeterminado
            if len(sys.argv) >= 3:
                stat_type = sys.argv[2]
            get_player_season_stats(output_dir, leagues=league, seasons=season, stat_type=stat_type)
            
        elif option == 4:
            # Opción 4: Obtener estadísticas de partidos por jugador para un partido específico
            if len(sys.argv) >= 3:
                match_id = sys.argv[2]
                stat_type = "passing"  # valor predeterminado
                if len(sys.argv) >= 4:
                    stat_type = sys.argv[3]
                get_player_match_stats(output_dir, match_id=match_id, leagues=league, seasons=season, stat_type=stat_type)
            else:
                print("Error: Para la opción 4, debes proporcionar un ID de partido.")
                print_usage()
                
        elif option == 5:
            # Opción 5: Obtener calendario de partidos
            get_schedule(output_dir, leagues=league, seasons=season)
            
        elif option == 6:
            # Opción 6: Obtener alineaciones de un partido específico
            if len(sys.argv) >= 3:
                match_id = sys.argv[2]
                get_lineup(output_dir, match_id=match_id, leagues=league, seasons=season)
            else:
                print("Error: Para la opción 6, debes proporcionar un ID de partido.")
                print_usage()
                
        elif option == 7:
            # Opción 7: Obtener eventos de un partido específico
            if len(sys.argv) >= 3:
                match_id = sys.argv[2]
                get_events(output_dir, match_id=match_id, leagues=league, seasons=season)
            else:
                print("Error: Para la opción 7, debes proporcionar un ID de partido.")
                print_usage()
                
        elif option == 8:
            # Opción 8: Obtener eventos de tiros de un partido específico
            if len(sys.argv) >= 3:
                match_id = sys.argv[2]
                get_shot_events(output_dir, match_id=match_id, leagues=league, seasons=season)
            else:
                print("Error: Para la opción 8, debes proporcionar un ID de partido.")
                print_usage()
                
        else:
            print(f"Error: Opción '{option}' no reconocida.")
            print_usage()
            
    except ValueError:
        print(f"Error: '{sys.argv[1]}' no es una opción válida. Debe ser un número.")
        print_usage()

if __name__ == "__main__":
    main()