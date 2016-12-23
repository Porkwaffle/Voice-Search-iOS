import ui, json, requests, dialogs, console

def search(sender):
	view = sender.superview['textview']
	view.text = ''
	view.text += 'Searching for Voice Artists in the top 200...\n\n'
	
	#console.show_activity('Searching itunes top 200...')
	
	# Download the JSON data from itunes
	url = 'https://itunes.apple.com/us/rss/topsongs/limit=200/explicit=true/json'
	response = requests.get(url)
	response.raise_for_status()
	
	# Load JSON data into a Python variable.
	data = json.loads(response.text)
	songs = data['feed']['entry']

	# Perform search
	i = 0
	for song in songs:
		if "The Voice Performance" in songs[i]['title']['label']:
			view.text += str(i + 1) + ') ' + song['im:artist']['label'] + '\n'
			view.text += '\t(' + songs[i]['im:name']['label'].replace('(The Voice Performance)', '') + ')\n'
			view.text += '---------------------\n'
		i += 1
	
	if view.text == 'Searching for Voice Artists in the top 200...\n\n':
		view.text += 'No results found'

v = ui.load_view()

v['imageview'].image = ui.Image.named('IMG_1130.PNG')

v.present('sheet')
