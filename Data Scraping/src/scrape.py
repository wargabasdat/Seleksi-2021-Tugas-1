import requests
from bs4 import BeautifulSoup
import json
from pymongo import MongoClient
import config

def getListings(listings):
    sourceFirst = 'https://www.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes%2Fsection%2FNEARBY_LISTINGS%3A2400&room_types%5B%5D=Entire%20home%2Fapt&property_type_id%5B%5D=5&property_type_id%5B%5D=6&property_type_id%5B%5D=8&property_type_id%5B%5D=10&property_type_id%5B%5D=12&property_type_id%5B%5D=15&property_type_id%5B%5D=16&property_type_id%5B%5D=17&property_type_id%5B%5D=18&property_type_id%5B%5D=19&property_type_id%5B%5D=23&property_type_id%5B%5D=24&property_type_id%5B%5D=25&property_type_id%5B%5D=28&property_type_id%5B%5D=32&property_type_id%5B%5D=34&property_type_id%5B%5D=44&property_type_id%5B%5D=50&property_type_id%5B%5D=54&property_type_id%5B%5D=57&property_type_id%5B%5D=58&property_type_id%5B%5D=61&property_type_id%5B%5D=63&property_type_id%5B%5D=64&property_type_id%5B%5D=66&property_type_id%5B%5D=67&property_type_id%5B%5D=68&property_type_id%5B%5D=69&property_type_id%5B%5D=62&property_type_id%5B%5D=51&title_type=CURATED_PROPERTY_TYPE'
    sourceSecondPlus = 'https://www.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes%2Fsection%2FNEARBY_LISTINGS%3A2400&room_types%5B%5D=Entire%20home%2Fapt&property_type_id%5B%5D=5&property_type_id%5B%5D=6&property_type_id%5B%5D=8&property_type_id%5B%5D=10&property_type_id%5B%5D=12&property_type_id%5B%5D=15&property_type_id%5B%5D=16&property_type_id%5B%5D=17&property_type_id%5B%5D=18&property_type_id%5B%5D=19&property_type_id%5B%5D=23&property_type_id%5B%5D=24&property_type_id%5B%5D=25&property_type_id%5B%5D=28&property_type_id%5B%5D=32&property_type_id%5B%5D=34&property_type_id%5B%5D=44&property_type_id%5B%5D=50&property_type_id%5B%5D=51&property_type_id%5B%5D=54&property_type_id%5B%5D=57&property_type_id%5B%5D=58&property_type_id%5B%5D=61&property_type_id%5B%5D=62&property_type_id%5B%5D=63&property_type_id%5B%5D=64&property_type_id%5B%5D=66&property_type_id%5B%5D=67&property_type_id%5B%5D=68&property_type_id%5B%5D=69&title_type=CURATED_PROPERTY_TYPE&tab_id=home_tab&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=july&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&search_type=unknown&federated_search_session_id=b8951c34-204e-4642-bea2-011410730288&pagination_search=true&items_offset='
    sourceTail = '&section_offset=1'

    # Find data from 1st to 5th page of Airbnb's Unique Stays collection
    for i in range (0,100,20):
        if (i == 0):
            source = requests.get(sourceFirst).text
        else:
            source = requests.get(sourceSecondPlus + str(i) + sourceTail).text

        soupPage = BeautifulSoup(source, 'lxml')

        # Retrieve all listings in one page
        for soup in soupPage.find_all('div', class_='_8ssblpx'):
            try:
                listing = {
                    '_id': 0,
                    'type': '',
                    'area': '',
                    'name': '',
                    'guest': 0,
                    'bedroom': 0.0,
                    'bed': 0.0,
                    'bath': 0.0,
                    'price': 0.0,
                    'rating': 0.0,
                    'link': ''
                }

                # Retrieve listing's link
                try:
                    link = soup.find('div', class_='_8s3ctt')
                    listing['link'] = 'https://www.airbnb.com' + link.a['href']
                except:
                    raise Exception('Link not found')

                # Retrieve listing's id based on link
                listing['_id'] = int(listing['link'].partition('?')[0].rsplit('/',1)[1])

                # Only add listing if it hasn't been retrieved
                if not any(l['_id'] == listing['_id'] for l in listings):

                    # Retrieve listing's type
                    listing['type'] = soup.find('div', class_='_1olmjjs6').text.partition(' in ')[0]

                    # Retrieve listing's area
                    listing['area'] = soup.find('div', class_='_1olmjjs6').text.partition(' in ')[2]
                    
                    # Retrieve listing's name
                    listing['name'] = soup.find('span', class_='_1whrsux9').text.replace('\n',' ').replace('\u2013','-')

                    specs = soup.find('div', class_='_3c0zz1')
                    for spec in specs.find_all('span', class_='_3hmsj'):
                        spec = str(spec)
                        
                        # Retrieve listing's number of guests if provided
                        if ('guest' in spec):
                            listing['guest'] = int(spec.replace('<span class="_3hmsj">','').replace('</span>','').replace(' guest','').replace('s',''))
                        
                        # Retrieve listing's number of bedrooms if provided
                        elif ('bedroom' in spec):
                            listing['bedroom'] = spec.replace('<span class="_3hmsj">','').replace('</span>','').replace(' bedroom','').replace('s','')
                            listing['bedroom'] = 0.0 if listing['bedroom'] == 'Studio' else float(listing['bedroom'])
                        
                        # Retrieve listing's number of beds if provided
                        elif ('bed' in spec):
                            listing['bed'] = float(spec.replace('<span class="_3hmsj">','').replace('</span>','').replace(' bed','').replace('s',''))
                        
                        # Retrieve listing's number of baths if provided
                        elif ('bath' in spec):
                            listing['bath'] = spec.replace('<span class="_3hmsj">','').replace('</span>','').replace(' bath','').replace('s','')
                            listing['bath'] = 0.5 if listing['bath'] == 'Half-bath' else float(listing['bath'])

                    # Retrieve listing's price per night
                    listing['price'] = float(soup.find('span', class_='_155sga30').text.replace('$',''))

                    # Retrieve listing's rating if provided
                    try:
                        listing['rating'] = float(soup.find('span', class_='_10fy1f8').text)
                    except:
                        listing['rating'] = 0.0

                    listings.append(listing)
                
            except Exception as e:
                # Data has unknown/unusual format
                print('Unknown format')
                print(e)

listings = []

getListings(listings)
print('Number of Listings: ' + str(len(listings)))

# Save json file
directory = '../data/' + 'listings.json'
with open(directory, 'w') as f:
    json.dump(listings, f, indent=4)

# Upload data to MongoDB Atlas cloud database
uri = 'mongodb+srv://13519054:' + config.db_pass + '@tugas-1.uw3kw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
cluster = MongoClient(uri)
db = cluster['airbnb-listings']
col = db['unique-stays']
col.delete_many({})
col.insert_many(listings)