import requests
apikey= 'API_KEY'
keyString = '&key='+apikey
baseUrl = 'https://maps.googleapis.com/maps/api/geocode/json?address='

with open('address_locations.csv', 'a') as out_file:
    with open("address_list.csv", "r") as ins:
        for line in ins:
            addressString = line.rstrip()
            response = requests.get(baseUrl + addressString + keyString)
            resp_json_payload = response.json()
            location = resp_json_payload['results'][0]['geometry']['location']
            out_file.write(addressString +','+ str(location['lat']) +','+ str(location['lng']) +'\n')
