import random
import requests

api_key = ''

def get_random_item():
    headers = {'X-API-Key': api_key}

    endpoint = 'https://www.bungie.net/Platform/Destiny2/Manifest/'

    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        manifest_url = data['Response']['jsonWorldContentPaths']['en']

        manifest_response = requests.get(f'https://www.bungie.net{manifest_url}')
        if manifest_response.status_code == 200:
            manifest_data = manifest_response.json()
            item_hashes = list(manifest_data['DestinyInventoryItemDefinition'].keys())
            rand_num = random.randint(0, 22957)
            item1 = manifest_data['DestinyInventoryItemDefinition'][item_hashes[rand_num]]['displayProperties']['name']
            message = f'{item1}'
            return message
        else:
            return 'Error getting item'

    else:
        return 'Error getting manifest'