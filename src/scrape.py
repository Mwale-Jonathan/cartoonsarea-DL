import requests, json
from bs4 import BeautifulSoup

SEASON_URL = 'https://cartoonsarea.xyz/Japanese-Dubbed-Videos/H-Subbed-Series/Haikyuu-Subbed-Videos/Haikyuu-Season-2-Subbed-Videos/'

def get_episodes(url):
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')

	container = soup.find('div', class_='none')
	folders = container.find_all('a')

	links = []

	for folder in folders:
		folder_link = folder['href']
		links.append(f'http:{folder_link}')

	return links

def get_episode_details(url):
	episodes = get_episodes(url)
	
	links = []

	for episode in episodes:
		url = episode
		req = requests.get(url)
		soup = BeautifulSoup(req.content, 'html.parser')

		container = soup.find('td')
		link = container.find('a')
		url = link['href']

		links.append(f'http:{url}')

	return links


def get_download_links(url):
	episodes = get_episode_details(url)

	links = []

	for episode in episodes:
		url = episode
		req = requests.get(url)
		soup = BeautifulSoup(req.content, 'html.parser')

		link = soup.find('a', class_='download-btn')['href']
		url = f'https://cartoonsarea.xyz/{link}'
		title = soup.find('td', class_='desc_value').text

		links.append({ 'title': title, 'url': url })

	return links
