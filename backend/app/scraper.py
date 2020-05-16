import requests
from bs4 import BeautifulSoup

def scrape(username):
  if username is None:
    return 'Usage: python3 scraper.py <dev.to username>'

  URL = 'https://dev.to/' + username
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  banner = soup.find(id='page-content-inner')

  if banner is None:
    return("User " + username + " not found")

  follow_button = banner.find('span', class_='user-profile-follow-button-wrapper')
  styles = follow_button.find('button', class_='cta')['style']

  # background-color
  bg_color_index = styles.find('background-color:') 
  bg_color_offset = len('background-color:')
  bg_color_start = bg_color_index + bg_color_offset
  bg_color_end = bg_color_start + 7 # length of '#eeeeee'
  bg_color = styles[bg_color_start:bg_color_end]

  # color
  text_color_index = styles.find('color:')
  text_color_offset = len('color:')
  text_color_start = text_color_index + text_color_offset
  text_color_end = text_color_start + 7 # length of '#eeeeee'
  text_color = styles[text_color_start:text_color_end]

  return {'bg': bg_color, 'color': text_color}
