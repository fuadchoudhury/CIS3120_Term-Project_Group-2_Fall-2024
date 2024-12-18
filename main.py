from processing import clean_nba_salaries, get_active_players, merge_data

class NBATopPlayersByPosition:
    """
    Class to filter the top 10 players by salary for a specific position.
    """
    def __init__(self, merged_df):
  
        self.merged_df = merged_df

    def get_top_10_by_position(self, position):
      
        # Filter for the specific position
        position_df = self.merged_df[self.merged_df['pos'] == position]
        
        # Sort by salary descending and get top 10
        top_10 = position_df.sort_values(by='2024/2025', ascending=False).head(10)
        
        return top_10


if __name__ == "__main__":
    # Step 1: Clean salaries data
    print("Cleaning salaries data...")
    salaries_df = clean_nba_salaries()

    # Step 2: Fetch active NBA players
    print("Fetching active players...")
    active_players_df = get_active_players()

    # Step 3: Merge salaries and active player data
    print("Merging data...")
    merged_df = merge_data(salaries_df, active_players_df)

    # Step 4: Initialize the filtering class
    top_players_filter = NBATopPlayersByPosition(merged_df)

    # Step 5: Prompt user to input position
    position = input("Enter the position (e.g., PG, SG, SF, PF, C): ").upper()

    # Validate input
    valid_positions = merged_df['pos'].unique()
    if position not in valid_positions:
        print(f"Error: '{position}' is not a valid position. Valid positions are: {valid_positions}")
    else:
        # Step 6: Filter the top 10 players for the input position
        print(f"\nFiltering top 10 players for position: {position}...")
        top_10_players = top_players_filter.get_top_10_by_position(position)

        # Step 7: Display and save the result
        print(f"\nTop 10 Players for Position: {position}")
        print(top_10_players[['player', 'pos', '2024/2025']])

# Step 5: Prompt user to input position
position = input("Enter the position (e.g., PG, SG, SF, PF, C): ").upper()

try:
    # Step 6: Filter the top 10 players for the input position
    print(f"\nFiltering top 10 players for position: {position}...")
    top_10_players = top_players_filter.get_top_10_by_position(position)

    # Check if the result is empty
    if top_10_players.empty:
        raise ValueError(f"No players found for position '{position}'.")

    # Step 7: Display the result
    print(f"\nTop 10 Players for Position: {position}")
    print(top_10_players[['player', 'pos', '2024/2025']])
except ValueError as e:
    print(f"Error: {e}")
# sss
