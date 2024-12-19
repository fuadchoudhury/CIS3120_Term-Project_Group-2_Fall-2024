import matplotlib.pyplot as plt
import seaborn as sns
class SalaryVisualizer:
    def __init__(self, players):
        
        # Initializes the SalaryVisualizer with a list of players
        self.players = players
        
    def visualize_salaries(self):

        # Grabs player names and salaries from the Player objects
        player_names = [player.name for player in self.players]
        player_salaries = [player.salary for player in self.players]

        # Creates a bar chart of the NBA players' salaries
        plt.figure(figsize=(12, 6))
        sns.barplot(x=player_names, y=player_salaries)
        # Rotate the x-axis labels
        plt.xticks(rotation=90)
        plt.title("NBA Player Salaries")
        plt.xlabel("Player Name")
        plt.ylabel("Salary (USD)")
        # Adjust the layout to prevent overlap of labels
        plt.tight_layout()
        plt.show()
        
    def visualize_salary_distribution(self):
        # Creates a histogram of the NBA player salaries.
        salaries = [player.salary for player in self.players]
        plt.figure(figsize=(10, 6))
        sns.histplot(salaries, kde=True, bins=20)
        plt.title("Salary Distribution of NBA Players")
        plt.xlabel("Salary (USD)")
        plt.ylabel("Frequency")
        plt.show()
