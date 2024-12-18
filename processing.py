import pandas as pd
from nba_api.stats.static import players

def clean_nba_salaries():
    salaries_df = pd.read_csv('nba_salaries.csv')
    cleaned_salaries = []
    for value in salaries_df['2024/2025']:
        clean_value = value.replace('$', '').replace(',', '')
        cleaned_salaries.append(int(clean_value))
    salaries_df['2024/2025'] = cleaned_salaries
    return salaries_df

def get_active_players():
    active_players = players.get_active_players()
    return pd.DataFrame(active_players)

def merge_data(salaries_df, active_players_df):
    merged_df = pd.merge(
        salaries_df,
        active_players_df,
        left_on="player",
        right_on="full_name",
        how="inner"
    )
    return merged_df
