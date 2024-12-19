# CIS3120_Term-Project_Group-Project_Fall-2024
\
This is the repository for the "Term Project".\
Group Project, CIS3120 Course.\
Professor: Sonyl Nagle, Fall 2024 Semester.\
Group Members: Fuad Choudhury, Yammy So, Jimmy Zhang.\
\
The project is focused on NBA player salaries analytics.

## Features

1. Cleans and processes NBA salary data from a CSV file (`nba_salaries.csv`).
2. Merges salary data with active player data from the `nba_api` library.
3. Allows users to:
   - Filter and display the top 10 players for a specific position.
   - Visualize the results using a bar chart.
---
## How to Use

### 1. **Program Start**
- Run the program by executing `main.py`.
- The program will initialize, clean, and merge salary data with active player data.
- You will be asked to enter a position to analyze.

### 2. **User Input**
- Enter a valid NBA position:
  - `PG` (Point Guard)
  - `SG` (Shooting Guard)
  - `SF` (Small Forward)
  - `PF` (Power Forward)
  - `C` (Center)
- If you want to exit the program, type `exit`.

### 3. **Output**
- The program will display a table of the top 10 players for the specified position based on their salaries.
- A bar chart will also be generated, showing player salaries for the chosen position.
