from bs4 import BeautifulSoup
import requests
while True:
	most_relevent = []
	less_relevent = []
	least_relevent = []
	synonym_list = []
	list_size = 5

	item = input('')

	page = requests.get('https://www.thesaurus.com/browse/{}'.format(item))
	soup = BeautifulSoup(page.content,'html.parser')

	most = soup.find_all('a', class_='css-r5sw71-ItemAnchor etbu2a31',href=True)
	less = soup.find_all('a', class_='css-1k3kgmb-ItemAnchor etbu2a31',href=True)
	least = soup.find_all('a', class_='css-8umlxa-ItemAnchor etbu2a31',href=True)

	for i in range(len(most)):
		synonym = list(most[i])
		most_relevent.append(synonym[0])
		
	for i in range(len(less)):
		synonym = list(less[i])
		less_relevent.append(synonym[0])
		
	for i in range(len(least)):
		synonym = list(least[i])
		least_relevent.append(synonym[0])

	if len(most_relevent) <= list_size:
		for i in range(len(most_relevent)):
			synonym_list.append(most_relevent[i])
			
		if len(less_relevent) <= list_size-int(len(most_relevent)):
			for i in range(list_size-int(len(most_relevent))):
				synonym_list.append(most_relevent[i])
				
			for i in range(list_size-int(len(most_relevent))-int(len(less_relevent))):
				synonym_list.append(least_relevent[i])
		else:
			for i in range(list_size-int(len(most_relevent))):
				synonym_list.append(less_relevent[i])
	else:
		for i in range(list_size):
			synonym_list.append(most_relevent[i])

	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	for i in range(len(synonym_list)):
		print('\n{}\n'.format(synonym_list[i]))
