destinations = ['Cape Town', 'Marrakesh', 'Cairo', 'Lagos', 'Johannesburg', 'San Juan', 'Kingston', 'Gros Islet']

cape_town_restaurants = ['La Colombe', 'Grub & Vine', 'The Cousins Trattoria', 'Chefs Warehouse Winebar & Pinchos', 'The Pot Luck Club', 'Mozambik V & A Waterfront', 'Pigalle', 'SeaBreeze Fish & Shell']
marrakesh_restaurants = ['Pepe Nero', 'Al Fassia', 'Dar Moha', 'Comptoir Darna', 'Nomad', 'Dameh', 'Kabana Rooftop Food & Cocktails', 'La Famille']
cairo_restaurants = ['The Grill', 'JW Steakhouse', 'Zooba', 'Pane Vino', 'Saigon', 'Osmanly', 'Pier 88 Nile River', 'Crimson Bar & Grill']
lagos_restaurants = ['RSVP', 'Cactus', 'Shiro Lagos', 'Lagoon', 'Bungalow', 'Z Kitchen', "Gurunar's Viceroy", 'Yellow Chilli']
johannesburg_restaurants = ['Marble', 'Level Four', 'The Grillhouse Rosebank', 'La Boqueria Parktown North', 'Signature', 'Mezepoli', 'Bellagio', 'Che Argentine Grill']
san_juan_restaurants = ['Marmalade', 'Princesa', 'Barrachina', 'Fogo de Chao Brazillian Steakhouse', 'La Casita Blanca', 'Casita Marimar', 'Serafina', "Sofia's Old San Juan"]
kingston_restaurants = ['Tamarind', 'Broken Plate', 'Nirvanna Restaurant Lady Musgrave', "Usain Bolt's Tracks & Records", 'South Avenue Grill', 'Uncorked!', 'Saffron', 'Reggae Mill']
gros_islet_restaurants = ['Golden Taste', "Vino's Bar and Bistro", 'Frydays', "Angel's Delight", 'Rituals Sushi', 'Merlyn', 'Pork Eat Up', "Boaty's Seafood Grill"]

transportation = ['by boat', 'by train', 'by plane', 'by rental car', 'on bicycle', 'on foot']

cape_town_entertainment = ['go shark cage diving', 'go on a wine tram tour', 'see the penguins', 'go on a safari', 'go on a champagne cruise', 'go on a helicopter tour', 'visit Robben Island', 'go seal snorkeling']
marrakesh_entertainment = ['go on a hot air balloon ride', 'go on a camel ride tour', 'ride a quad bike through the desert', 'visit Ouzoud Falls', 'visit Essaouira', 'take a Moroccan cooking class', 'go shopping in the souks of Marrakesh', 'tour the "hidden sites" of Marrakesh']
cairo_entertainment = ['tour the pyramids', 'tour Alexandria', 'sail the Nile', 'visit the Red Sea', 'go on a hot air balloon ride', 'ride an ATV through Giza', 'visit the Siwa oasis', 'tour the mosques of Cairo']
lagos_entertainment = ['boat to Ponta da Piedad', 'go on a "seafari"', 'cruise the Golden Coast', 'go on a wine tasting tour', 'visit Algarve', 'go swimming in Benagil', 'go dolphin and whale watching', 'tour old and new Lagos']
johannesburg_entertainment = ['visit the Apartheid Museum', 'visit the Gold Reef City theme park', "visit Mandele's house", 'visit the Cradle of Humankind', 'visit the Johannesburg Zoo', 'go on a safari', 'tour Soweto', 'go on a hot air balloon ride']
san_juan_entertainment = ['go snorkeling with sea turtles', 'ride ATVs at Campo Rico Ranch', 'tour the El Yunque Rainforest', 'tour the Culebra Islands', 'tour the Ron del Barrilito Distillarty', 'tour San Juan', 'tour the bay and hot springs by boat', 'go zip lining through the rainforest']
kingston_entertainment = ['visit the Bob Marley Museum', 'visit the National Gallery of Jamaica', 'visit Emancipation Park', 'visit Lime Cay', 'visit Fort Charles', 'bobsled River Falls', 'tour Konoko Falls and Garden', 'raft on Rio Grande']
gros_islet_entertainment = ['snorkel in Catamaran', 'to zip lining in the rainforest', 'tour St Lucia on an ATV', 'go horseback riding on the beach', 'go dolphin and whale watching', 'go on a boat tour', 'tour the rainforest by aerial tram', 'take a mud bath in the sulphur springs']

print('Welcome to your personalized day trip generator!')

def find_destination():
    import random
    final_destination = random.shuffle(destinations)

    for final_destination in destinations:
        destination_input = input(f'You have chosen {final_destination}! Is this correct? y/n: ')
        if destination_input == 'y':
            return final_destination


def find_transportation():
    import random
    ran_transportation = random.shuffle(transportation)

    for ran_transportation in transportation:
        trans_input = input(f'You have chosen to arrive by {ran_transportation}! Is this correct? y/n: ')
        if trans_input == 'y':
            return ran_transportation

def find_cape_town_restaurant():
    import random
    ran_restaurant = random.shuffle(cape_town_restaurants)

    for ran_restaurant in cape_town_restaurants:
        rest_input = input(f'You have chosen to eat at {ran_restaurant}! Is this correct? y/n: ')
        if rest_input == 'y':
            return ran_restaurant

def find_marrakesh_restaurant():
    import random
    ran_restaurant = random.shuffle(marrakesh_restaurants)

    for ran_restaurant in marrakesh_restaurants:
        rest_input = input(f'You have chosen to eat at {ran_restaurant}! Is this correct? y/n: ')
        if rest_input == 'y':
            return ran_restaurant

def find_cairo_restaurant():
    import random
    ran_restaurant = random.shuffle(cairo_restaurants)

    for ran_restaurant in cairo_restaurants:
        rest_input = input(f'You have chosen to eat at {ran_restaurant}! Is this correct? y/n: ')
        if rest_input == 'y':
            return ran_restaurant

def find_lagos_restaurant():
    import random
    ran_restaurant = random.shuffle(lagos_restaurants)

    for ran_restaurant in lagos_restaurants:
        rest_input = input(f'You have chosen to eat at {ran_restaurant}! Is this correct? y/n: ')
        if rest_input == 'y':
            return ran_restaurant

def find_johannesburg_restaurant():
    import random
    ran_restaurant = random.shuffle(johannesburg_restaurants)

    for ran_restaurant in johannesburg_restaurants:
        rest_input = input(f'You have chosen to eat at {ran_restaurant}! Is this correct? y/n: ')
        if rest_input == 'y':
            return ran_restaurant

def find_san_juan_restaurant():
    import random
    ran_restaurant = random.shuffle(san_juan_restaurants)

    for ran_restaurant in san_juan_restaurants:
        rest_input = input(f'You have chosen to eat at {ran_restaurant}! Is this correct? y/n: ')
        if rest_input == 'y':
            return ran_restaurant

def find_kingston_restaurant():
    import random
    ran_restaurant = random.shuffle(kingston_restaurants)

    for ran_restaurant in kingston_restaurants:
        rest_input = input(f'You have chosen to eat at {ran_restaurant}! Is this correct? y/n: ')
        if rest_input == 'y':
            return ran_restaurant

def find_gros_islet_restaurant():
    import random
    ran_restaurant = random.shuffle(gros_islet_restaurants)

    for ran_restaurant in gros_islet_restaurants:
        rest_input = input(f'You have chosen to eat at {ran_restaurant}! Is this correct? y/n: ')
        if rest_input == 'y':
            return ran_restaurant

