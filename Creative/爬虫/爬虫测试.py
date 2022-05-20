from bs4 import BeautifulSoup
import requests

item = input('Search: ')

item = item.split()
item = '%20'.join(item)

with open('output.txt','w') as f:
	pass

page = requests.get('https://www.walmart.com/search/?query={}'.format(item))
soup = BeautifulSoup(page.content,'html.parser')


a = soup.find_all('a', class_='search-result-productimage gridview display-block',href=True)

for j in range(len(a)):
	page = requests.get('https://www.walmart.com{}'.format(a[j]['href']))
	soup = BeautifulSoup(page.content,'html5lib')


	span = soup.find_all('span', class_='display-block-xs font-bold')
	if len(span) == 1:
		if span[0].text == 'Out of stock':
			stock = False
	else:
		stock = True
	
	with open('output.txt','a') as f:
		if stock:
			stock = 'In'
		else:
			stock = 'Out of'
		f.write('({} stock) https://www.walmart.com{}\n'.format(str(stock),a[j]['href']))
f.close()
