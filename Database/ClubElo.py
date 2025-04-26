import os
import sys
import pandas as pd
from soccerdata import ClubElo

def create_output_dir(source_name="ClubElo"):
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
    
    # Establecer para que no almacene datos
    os.environ['SOCCERDATA_NOSTORE'] = "True"
    
    return cache_dir

def get_current_elo(output_dir):
    """Obtiene los datos de ELO actuales para todos los equipos"""
    # Configurar la ubicación de la caché de datos
    setup_soccerdata_dir()
    
    elo = ClubElo()
    current_elo = elo.read_by_date()
    
    # Convertir el índice (nombres de equipos) a una columna antes de guardar
    current_elo_modified = current_elo.reset_index()
    
    # Definir la ruta de salida
    output_path = os.path.join(output_dir, "clubelo_1.csv")
    
    # Guardar los datos en un archivo CSV con punto y coma como separador
    # y punto para los decimales
    current_elo_modified.to_csv(output_path, sep=";", decimal=".", index=False)
    
    print(f"Archivo creado exitosamente: {output_path}")
    return current_elo

def get_team_elo_history(output_dir, team_name="Barcelona"):
    """Obtiene el historial de ELO para un equipo específico"""
    # Configurar la ubicación de la caché de datos
    setup_soccerdata_dir()
    
    elo = ClubElo()
    team_history = elo.read_team_history(team_name)
    
    # Convertir el índice a una columna antes de guardar
    team_history_modified = team_history.reset_index()
    
    # Definir la ruta de salida
    output_path = os.path.join(output_dir, f"clubelo_2_{team_name}.csv")
    
    # Guardar los datos en un archivo CSV con punto y coma como separador
    # y punto para los decimales
    team_history_modified.to_csv(output_path, sep=";", decimal=".", index=False)
    
    print(f"Archivo creado exitosamente: {output_path}")
    return team_history

def print_usage():
    """Imprime instrucciones de uso del script"""
    print("\nUso: python3 ClubElo.py [opción] [parámetros adicionales]")
    print("\nOpciones:")
    print("1: Obtener ELO actual de todos los equipos")
    print("2 [nombre_equipo]: Obtener historial completo de ELO para un equipo específico")
    print("\nEjemplos:")
    print("python3 ClubElo.py 1")
    print("python3 ClubElo.py 2 \"Real Madrid\"")

def main():
    # Crear la carpeta output con una subcarpeta para ClubElo
    output_dir = create_output_dir("ClubElo")
    
    # Verificar los argumentos de la línea de comandos
    if len(sys.argv) < 2:
        print("Error: Debes proporcionar al menos una opción.")
        print_usage()
        return
    
    try:
        option = int(sys.argv[1])
        
        if option == 1:
            # Opción 1: Obtener ELO actual de todos los equipos
            get_current_elo(output_dir)
            
        elif option == 2:
            # Opción 2: Obtener historial completo de ELO para un equipo específico
            if len(sys.argv) >= 3:
                team_name = sys.argv[2]
                get_team_elo_history(output_dir, team_name)
            else:
                print("Error: Para la opción 2, debes proporcionar un nombre de equipo.")
                print_usage()
                
        else:
            print(f"Error: Opción '{option}' no reconocida.")
            print_usage()
            
    except ValueError:
        print(f"Error: '{sys.argv[1]}' no es una opción válida. Debe ser un número.")
        print_usage()

if __name__ == "__main__":
    main()