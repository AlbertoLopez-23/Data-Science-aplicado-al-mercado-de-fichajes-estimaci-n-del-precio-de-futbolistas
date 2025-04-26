import os
import sys
import pandas as pd
import soccerdata as sd
import warnings
from pathlib import Path
import json
import traceback

# Role parameter (1: games, 2: forecasts, 3: clinches)
rol = 1

# Create directories if they don't exist
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
cache_dir = os.path.join(output_dir, "cache")
five38_dir = os.path.join(output_dir, "FiveThirtyEight")

for directory in [output_dir, cache_dir, five38_dir]:
    os.makedirs(directory, exist_ok=True)

# Function to process and save data based on role
def process_and_save_data(role):
    try:
        print(f"Initializing FiveThirtyEight data source...")
        # Initialize with more seasons to increase chances of finding data
        five38 = sd.FiveThirtyEight(
            leagues="ENG-Premier League", 
            seasons=[2020, 2021, 2022],  # Try multiple seasons
            data_dir=Path(cache_dir),
            no_cache=False
        )
        
        filename = f"FiveThirtyEight_{role}.csv"
        filepath = os.path.join(five38_dir, filename)
        
        print(f"Fetching data for role {role}...")
        try:
            if role == 1:
                # Game schedule and predicted results
                data = five38.read_games()
                data_type = "games"
            elif role == 2:
                # Forecasted league table
                data = five38.read_forecasts()
                data_type = "forecasts"
            elif role == 3:
                # Clinches data
                data = five38.read_clinches()
                data_type = "clinches"
            else:
                print(f"Error: Role {role} not supported")
                return
            
            # Check if 'team' is in the index and reset if needed
            if 'team' in data.index.names:
                data = data.reset_index()
            
            # Print data shape and first few rows for debugging
            print(f"Data shape: {data.shape}")
            print("First few rows:")
            print(data.head())
            
            # Save to CSV with semicolon separator and point as decimal separator
            data.to_csv(filepath, sep=';', decimal='.', index=True)
            print(f"Successfully saved {data_type} data to {filepath}")
            
        except json.JSONDecodeError as je:
            print(f"JSON decoding error: {str(je)}")
            print("This could be due to network issues or changes in the data format.")
            print("Try running the script again or checking your internet connection.")
        
        except Exception as e:
            print(f"Error processing role {role}: {str(e)}")
            print("Traceback:")
            traceback.print_exc()
    
    except Exception as e:
        print(f"Error initializing data source: {str(e)}")
        print("Traceback:")
        traceback.print_exc()

# Execute based on the role parameter
if __name__ == "__main__":
    # If role is provided as command line argument, use it
    if len(sys.argv) > 1:
        try:
            rol = int(sys.argv[1])
        except ValueError:
            print("Error: Role argument must be an integer")
    
    # Process and save data
    process_and_save_data(rol)