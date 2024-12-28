# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pandas",
#     "rich",
# ]
# ///

"""
Parses Netflix viewership data (.csv)

You can download it from the Account page on Netflix.com.
"""

from rich.console import Console
from rich.table import Table
import pandas as pd
import re

# Load CSV with proper header handling
file_path = "netflix.csv"  # CSV filename
data = pd.read_csv(file_path, header=None, names=["Title", "Date"])

# Parse the date with a specified format
data['Date'] = pd.to_datetime(data['Date'], format="%m/%d/%y", errors="coerce")

# Drop rows with invalid dates (e.g., header row if mistakenly included)
data = data.dropna(subset=['Date'])

# Filter for 2024 and create a new copy to avoid SettingWithCopyWarning
filtered_data = data[data['Date'].dt.year == 2024].copy()

# List of exceptions that are always classified as TV shows
tv_show_exceptions = ["Bodkin", "La Palma", "Gudetama"]

# Function to determine show name and type
def classify_title(title):
    if any(keyword in title for keyword in ["Season", "Episode", "Series"]) or any(exception in title for exception in tv_show_exceptions):
        # Determine the show name
        for exception in tv_show_exceptions:
            if exception in title:
                return exception, "TV Show"
        show_name = re.split(r": Season|: Episode|: Series", title)[0].strip()
        return show_name, "TV Show"
    return title, "Movie"  # Default to movie

# Apply classification
filtered_data[['Show Name', 'Type']] = filtered_data['Title'].apply(lambda x: pd.Series(classify_title(x)))

# Group by show name and count episodes/movies
grouped_data = (
    filtered_data.groupby(['Show Name', 'Type'])
    .size()
    .reset_index(name='Count')
)

# Separate TV shows and movies
tv_shows = grouped_data[grouped_data['Type'] == "TV Show"].sort_values(by="Count", ascending=False)
movies = grouped_data[grouped_data['Type'] == "Movie"]

# Initialize Console
console = Console()

# Create TV Shows Table
tv_table = Table(title="Netflix Viewing History (TV Shows, 2024)")
tv_table.add_column("TV Show", style="cyan", no_wrap=True)
tv_table.add_column("Episode Count", style="magenta")

total_tv_episodes = tv_shows['Count'].sum()
for _, row in tv_shows.iterrows():
    tv_table.add_row(row['Show Name'], str(row['Count']))
tv_table.add_row("[bold]Total[/bold]", f"[bold]{total_tv_episodes}[/bold]")

# Create Movies Table
movie_table = Table(title="Netflix Viewing History (Movies, 2024)")
movie_table.add_column("Movie", style="cyan", no_wrap=True)
movie_table.add_column("Count", style="magenta")

total_movies = movies['Count'].sum()
for _, row in movies.iterrows():
    movie_table.add_row(row['Show Name'], str(row['Count']))
movie_table.add_row("[bold]Total[/bold]", f"[bold]{total_movies}[/bold]")

# Print the tables
console.print(tv_table)
console.print(movie_table)

