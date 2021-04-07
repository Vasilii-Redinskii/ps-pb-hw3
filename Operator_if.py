# Make list & dictionaries
cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]
# Input city
user_city = input('Введите город: ')
# Make var city with capital letter
city = user_city.capitalize()
# Compare city with list
if city in cities:
    # If city in list display info about tourist
    i = 0
    for i in range(len(tourists)):
        tourist = tourists[i]
        if city == tourist['city']:
            print('Турист {} возраст {}. Посетил город {}.'.format(tourist['user']['name'],tourist['user']['age'],user_city))
# if city out of the list print about it.
else:
    print("Туристы не посещали этот город.")
