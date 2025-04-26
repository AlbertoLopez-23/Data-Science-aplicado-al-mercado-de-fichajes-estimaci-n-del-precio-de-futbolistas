import os
import sys
import pandas as pd
import soccerdata as sd

def create_output_dir():
    """Crear la carpeta output/ESPN si no existe"""
    # Crear directorio principal de output
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Crear directorio principal de output
    base_output_dir = os.path.join(current_dir, "output")
    if not os.path.exists(base_output_dir):
        os.makedirs(base_output_dir)
    
    # Crear directorio específico para ESPN
    espn_output_dir = os.path.join(base_output_dir, "ESPN")
    if not os.path.exists(espn_output_dir):
        os.makedirs(espn_output_dir)
    
    return espn_output_dir

def setup_soccerdata_dir():
    """Configurar el directorio de caché de soccerdata en el directorio local"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cache_dir = os.path.join(current_dir, "soccerdata")
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    
    # Establecer la variable de entorno para soccerdata
    os.environ['SOCCERDATA_DIR'] = cache_dir
    return cache_dir

def save_dataframe_to_csv(df, filename, output_dir):
    """Guardar DataFrame en CSV con punto y coma como separador y punto para decimales"""
    output_path = os.path.join(output_dir, filename)
    df.to_csv(output_path, sep=";", decimal=".", index=False)
    print(f"Archivo creado exitosamente: {output_path}")

def get_schedule(espn, league, season, output_dir):
    """Obtener y guardar la programación de partidos"""
    try:
        schedule = espn.read_schedule()
        
        # Crear versión plana con equipos como columnas regulares
        if 'home_team' in schedule.columns and 'away_team' in schedule.columns:
            home_df = schedule.copy()
            home_df['team'] = home_df['home_team']
            home_df['is_home'] = True
            
            away_df = schedule.copy()
            away_df['team'] = away_df['away_team']
            away_df['is_home'] = False
            
            combined_schedule = pd.concat([home_df, away_df], ignore_index=True)
            save_dataframe_to_csv(combined_schedule, f"ESPN_schedule_{season}_1.csv", output_dir)
        else:
            # Si ya tiene una estructura diferente, simplemente guardar
            save_dataframe_to_csv(schedule, f"ESPN_schedule_{season}_1.csv", output_dir)
        
        return schedule  # Devolver schedule para su posible uso posterior
    except Exception as e:
        print(f"Error al obtener programación: {str(e)}")
        return None

def get_matchsheet(espn, match_id, season, output_dir):
    """Obtener y guardar la hoja de partido"""
    try:
        matchsheet = espn.read_matchsheet(match_id=match_id)
        
        # Asegurar que 'team' sea una columna normal
        if hasattr(matchsheet, 'index') and hasattr(matchsheet.index, 'names') and 'team' in matchsheet.index.names:
            matchsheet = matchsheet.reset_index()
        
        save_dataframe_to_csv(matchsheet, f"ESPN_matchsheet_{season}_2.csv", output_dir)
    except Exception as e:
        print(f"Error al obtener hoja de partido: {str(e)}")

def get_lineup(espn, match_id, season, output_dir):
    """Obtener y guardar las alineaciones"""
    try:
        lineups = espn.read_lineup(match_id=match_id)
        
        # Asegurar que 'team' y 'player' sean columnas normales
        if hasattr(lineups, 'index') and hasattr(lineups.index, 'names'):
            if 'team' in lineups.index.names or 'player' in lineups.index.names:
                lineups = lineups.reset_index()
        
        save_dataframe_to_csv(lineups, f"ESPN_lineup_{season}_3.csv", output_dir)
    except Exception as e:
        print(f"Error al obtener alineaciones: {str(e)}")

def print_usage():
    """Imprimir instrucciones de uso del script"""
    print("\nUso: python3 ESPN.py [opción] [liga] [temporada] [match_id (opcional)]")
    print("\nOpciones:")
    print("1: Obtener programación de partidos (schedule)")
    print("2: Obtener hoja de partido (matchsheet) - requiere match_id")
    print("3: Obtener alineaciones (lineup) - requiere match_id")
    print("0: Obtener todos los datos disponibles")
    print("\nEjemplos:")
    print('python3 ESPN.py 1 "ENG-Premier League" 2021')
    print('python3 ESPN.py 2 "ENG-Premier League" 2021 541844')
    print('python3 ESPN.py 0 "ENG-Premier League" 2021 541844')

def main():
    # Verificar argumentos de línea de comandos
    if len(sys.argv) < 4:
        print("Error: Debes proporcionar opción, liga y temporada.")
        print_usage()
        return
    
    try:
        option = int(sys.argv[1])
        league = sys.argv[2]
        season = int(sys.argv[3])
        
        # Verificar si se proporcionó match_id para opciones 2 y 3
        match_id = None
        if len(sys.argv) >= 5:
            match_id = sys.argv[4]
        elif option in [2, 3]:
            print(f"Error: Para la opción {option}, debes proporcionar un match_id.")
            print_usage()
            return
        
        # Crear directorio de salida
        output_dir = create_output_dir()
        
        # Configurar el directorio de caché de soccerdata
        setup_soccerdata_dir()
        
        # Inicializar ESPN
        espn = sd.ESPN(leagues=league, seasons=season)
        
        # Procesar según la opción seleccionada
        if option == 0 or option == 1:
            schedule = get_schedule(espn, league, season, output_dir)
            
            # Si es opción 0 y no se proporcionó match_id, usar el primero disponible
            if option == 0 and match_id is None and schedule is not None and not schedule.empty:
                match_id = str(schedule.iloc[0]['game_id'])
                print(f"Usando match_id automático: {match_id}")
        
        if option == 0 or option == 2:
            if match_id:
                get_matchsheet(espn, match_id, season, output_dir)
            else:
                print("No se pudo obtener hoja de partido: match_id no disponible.")
        
        if option == 0 or option == 3:
            if match_id:
                get_lineup(espn, match_id, season, output_dir)
            else:
                print("No se pudo obtener alineaciones: match_id no disponible.")
    
    except ValueError:
        print(f"Error: '{sys.argv[1]}' no es una opción válida. Debe ser un número.")
        print_usage()
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        print_usage()

if __name__ == "__main__":
    main()