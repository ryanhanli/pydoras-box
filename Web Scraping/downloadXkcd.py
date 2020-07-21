#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'		# Starting URL
os.makedirs('xkcd', exist_ok=True)	# Store comics in ./xkcd

while not url.endswith('#'):
	# Download the page.
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)
	
	# Find the URL of the comic image.
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		comicUrl = comicElem[0].get('src').strip("http://")
		comicUrl="http://"+comicUrl
		#comicURL looks like 'http://imgs.xkcd.com/comics/heartbleed_explanation.png'
		# Download the image.
		print('Downloading image %s...' % (comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()
	
		# Save the image to ./xkcd.
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		#os.path.basename() with comicURL will return just last part which is heartbleed_explanation.png
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		
	# Get the Prev button's url.
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')
	
print('Done.')