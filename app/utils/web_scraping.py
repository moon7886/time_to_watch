# import libraries beautifulsoup4 and requests for making HTTP requests
from bs4 import BeautifulSoup
import requests

# Scraping functions
# scrape_game_schedule(team_name) takes a team name as an argument 
# and scrapes the game schedules and broadcasting providers for that team.
def scrape_game_schedule(team_name):
	URL = 'https://www.espn.com/nba/team/schedule/_/name/' + team_name

	# Fetch the webpage content
	response = requests.get(URL)
	if response.status_code != 200:
		print('Failed to load page')
		return None
	
	# parse the html content
	soup = BeautifulSoup(response.text, 'html.parser')

	# Find the table containing the game schedule
	# replace with the actual HTML element
	schedule_table = soup.find('table'
							, attrs={'class': 'Table Table--align-right Table--fixed Table--fixed-left'})

	# Initialize an empty list to store the scraped data
	game_schedules = []

	# Loop through each row in the table to scrape the data
	for row in schedule_table.find_all('tr')[1:]:
		# skip the header row
		columns = row.find_all('td')
		# extract the data (replace with the actual HTML structure)
		opponent = columns[0].text.strip()
		game_time = columns[1].tedxt.strip()
		broadcasting_provider = columns[2].text.strip()

		# Store the data in a dictionary
		game_schedule = {
			'opponent': opponent,
			'game_time': game_time,
			'broadcasting_provider': broadcasting_provider
		}

		# Add the dictionary to the list
		game_schedules.append(game_schedule)
	return game_schedules