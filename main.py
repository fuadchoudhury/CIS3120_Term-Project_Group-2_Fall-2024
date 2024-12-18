from processing import clean_nba_salaries, get_active_players, merge_data
from visualization import visualize_top_10_for_position


# class to handle the NBA salary data analysis and visualization.
class NBA_Analysis:


    def __init__(self):
        print("Initializing NBA Analysis...")
        self.salaries_df = None
        self.active_players_df = None
        self.merged_df = None
        self.top_players_filter = None

# Clean, fetch, and merge NBA data.
    def load_data(self):

        
        self.salaries_df = clean_nba_salaries()
        self.active_players_df = get_active_players()
        self.merged_df = merge_data(self.salaries_df, self.active_players_df)
        self.top_players_filter = NBATopPlayersByPosition(self.merged_df)
        
# # Filter top players by position and display results
    def filter_and_display(self, position):
        
        top_10_players = self.top_players_filter.get_top_10_by_position(position)
        print(f"\nTop 10 Players for Position: {position}")
        print(top_10_players[['player', 'pos', '2024/2025']])

        # Visualize the result
        visualize_top_10_for_position(self.merged_df, position)
# Run the NBA analysis program
    def run(self):
        self.load_data()
        valid_positions = self.merged_df['pos'].unique()
        
        while True:
            position = input("Enter the position (e.g., PG, SG, SF, PF, C or type 'exit' to quit): ").strip().upper()
            
            # Ignore empty inputs or unexpected strings
            if not position:
                print("Please enter a valid position.")
                continue

            if position == "EXIT":
                print("Exiting program. Goodbye.")
                break

            if position in valid_positions:
                self.filter_and_display(position)
            else:
                print(f"Error: '{position}' is not a valid position. Valid positions are: {valid_positions}")


class NBATopPlayersByPosition:
    """
    Class to filter the top 10 players by salary for a specific position.
    """
    def __init__(self, merged_df):
        self.merged_df = merged_df

    def get_top_10_by_position(self, position):
        """Get the top 10 players for a given position."""
        position_df = self.merged_df[self.merged_df['pos'] == position]
        top_10 = position_df.sort_values(by='2024/2025', ascending=False).head(10)
        return top_10


if __name__ == "__main__":
    analysis = NBA_Analysis()
    analysis.run()
# sss
