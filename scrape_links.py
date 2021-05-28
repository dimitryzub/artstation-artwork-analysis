import requests, json
# opening a .txt file
with open('artstation_links.txt', 'w') as f:
    for page_num in range(1,1001):
        response = requests.get(f'https://www.artstation.com/api/v2/community/explore/projects/trending.json?page={page_num}&dimension=all&per_page=100').text
        # open json response
        data = json.loads(response)
        
        # collecting links to the list()
        links = []
        # loopinh through json response
        for result in data['data']:
            # still looping and grabbing url's
            url = result['url']
            links.append(url)
            # writing each link on the new line (\n)
            f.write(f'{url}\n')
