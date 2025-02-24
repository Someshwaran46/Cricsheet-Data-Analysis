import os
import json
import pandas as pd
import pymysql

# Define the JSON directory
json_dir = r"C:\Users\Hp\OneDrive\Documents\Guvi\Cricsheet\cricsheet_json_downloads\odis_json"

# Get list of JSON files
json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

# Initialize list to store all match deliveries
all_deliveries = []

# Process each JSON file
for json_file in json_files:
    file_path = os.path.join(json_dir, json_file)
    
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Extract match metadata
    city = data['info'].get('city', 'Unknown')
    date = data['info']['dates'][0]  # Assuming first date is the match date
    match_no = data['info'].get('event', {}).get('match_number', '0')  # Default to '0' if missing

    event_name = data['info'].get('event', {}).get('name', 'Unknown')
    gender = data['info'].get('gender', 'Unknown')
    match_type = data['info']['match_type']
    venue = data['info']['venue']

    # Get match result details
    outcome = data['info'].get('outcome', {})
    result = outcome.get('result', outcome.get('winner', 'Unknown'))
    by_runs = outcome.get('by', {}).get('runs', None)  # Use None if missing
    player_of_match = data['info'].get('player_of_match', ['Unknown'])[0]
    season = data['info']['season']
    team_type = data['info'].get("team_type", "")  # Fixed: Removed extra comma
    teams = ", ".join(data['info'].get("teams", []))  # Convert list to a string

    toss_decision = data['info'].get('toss', {}).get('decision', 'Unknown')
    toss_winner = data['info'].get('toss', {}).get('winner', 'Unknown')

    # Extract delivery details
    if 'innings' in data:
        for inning in data['innings']:
            team_name = inning['team']
            for over_data in inning.get('overs', []):
                over_number = over_data['over']
                for delivery in over_data.get('deliveries', []):
                    all_deliveries.append((
                        city, date, match_no, event_name, gender, match_type, venue, result, by_runs, player_of_match,
                        season, team_type, teams, toss_decision, toss_winner, team_name, over_number, 
                        delivery['batter'], delivery['bowler'], delivery['non_striker'], 
                        delivery['runs']['batter'], delivery['runs']['extras'], delivery['runs']['total']
                    ))

# Convert to DataFrame
df = pd.DataFrame(all_deliveries, columns=[
    'city', 'date', 'match_no', 'event_name', 'gender', 'match_type', 'venue', 'result', 'by_runs',
    'player_of_match', 'season', 'team_type', 'teams', 'toss_decision', 'toss_winner', 'team_name', 
    'over_number', 'batter', 'bowler', 'non_striker', 'runs_batter', 'runs_extras', 'runs_total'
])
print(df)  # Display first few rows

# Connect to MySQL database
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="cricket",
    autocommit=True
)
mycursor = mydb.cursor()

# Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS odis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255),
    date DATE,
    match_no INT,
    event_name VARCHAR(255),
    gender VARCHAR(255),
    match_type VARCHAR(255),
    venue VARCHAR(255),
    `result` VARCHAR(255),
    by_runs INT,
    player_of_match VARCHAR(255),
    season VARCHAR(100),
    team_type VARCHAR(100),
    teams VARCHAR(255),
    toss_decision VARCHAR(100),
    toss_winner VARCHAR(100),
    team_name VARCHAR(255),
    over_number INT,
    batter VARCHAR(255),
    bowler VARCHAR(255),
    non_striker VARCHAR(255),
    runs_batter INT,
    runs_extras INT,
    runs_total INT
)
"""
mycursor.execute(create_table_query)

# Prepare batch insert query
insert_query = """
INSERT INTO odis (
    city, date, match_no, event_name, gender, match_type, venue, result, by_runs, player_of_match, season, 
    team_type, teams, toss_decision, toss_winner, team_name, over_number, batter, bowler, non_striker, 
    runs_batter, runs_extras, runs_total
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Bulk insert using executemany()
mycursor.executemany(insert_query, all_deliveries)
print(f"Successfully inserted {len(all_deliveries)} records into MySQL database under table 'ODIS'.")

# Close the connection
mycursor.close()

