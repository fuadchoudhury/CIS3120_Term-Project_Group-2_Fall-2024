import pandas as pd
from nba_api.stats.static import players

# Cleans the salary data from a CSV file
def clean_nba_salaries():
    salaries_df = pd.read_csv('nba_salaries.csv')
    # Create empty list to store cleaned salary values
    cleaned_salaries = []
    for value in salaries_df['2024/2025']:
        # Remove dollar signs and commas from the values
        clean_value = value.replace('$', '').replace(',', '')
        # Convert the cleaned salary value to an integer and add to the list
        cleaned_salaries.append(int(clean_value))
    # Replace the original '2024/2025' column with the cleaned salary values
    salaries_df['2024/2025'] = cleaned_salaries

    # Return the DataFrame
    return salaries_df

def get_active_players():
    
    # Get a list of active players from nba_api
    active_players = players.get_active_players()
    # Convert the list of players into a DataFrame
    return pd.DataFrame(active_players)

def merge_data(salaries_df, active_players_df):
    # inner merge on the 'player' column from salaries_df and the 'full_name' column from active_players_df
    merged_df = pd.merge(
        salaries_df,
        active_players_df,
        left_on="player",
        right_on="full_name",
        how="inner"
    )
    # Return the merged DataFrame
    return merged_df

