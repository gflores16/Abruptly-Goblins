#create a gamer's list
gamers = []

#function1 to verify that the person has a name and availability
def add_gamer(gamer, gamers_list):
    if gamer.get('name') and gamer.get('availability'):
        gamers_list.append(gamer)
    else:
        print('missing gamer information, please try again.')

#adding our first person, calling function1 and verifying its added to the gamers list 
kimberly ={'name': 'Kimberly', 'availability': ['Monday', 'Tuesday', 'Friday']}
add_gamer(kimberly, gamers)
#print(gamers)

#adding more people to the list and verifying once again that everyone was added successfully 
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
#print(gamers)

#function2 to add the total number of days in our gamers list
def build_daily_frequency_table():
    return {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0 , 'Sunday':0}

#calling the function to make sure it works as intended
count_availability = build_daily_frequency_table()
#print(count_availability)

#function3 to iterate through each person and day to count and add to our function2 
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
                available_frequency[day] += 1

print(calculate_availability(gamers, count_availability))
print(count_availability)

#function4 to pick the day from function3 with the most available people to attend
def find_best_night(availability_table):
    best_night = max(availability_table, key=availability_table.get)
    return best_night

game_night = find_best_night(count_availability)
print(game_night)

#function5 making a list of all of the people who are available that night
def available_on_night(gamers_list, day):
    people_available = []
    for people in gamers_list:
        if day in people['availability']:
            people_available.append(people['name'])
    return people_available

attending_game_night= (available_on_night(gamers, game_night))
print(attending_game_night)

#Generating an email for the participants
form_email = """Dear {name},

The following email is to inform you that on {day_of_week}s
we will be playing {game} We look forward 
to seeing you there. 

Best, 
Antonio

"""
#function6 to automate the email using function5 and function4
def send_email(gamers_who_can_attend, day, game):
    for people in gamers_who_can_attend:
        print(form_email.format(name = people, day_of_week = day, game = game))

send_email(attending_game_night, game_night, 'Abruptly Goblins!')

#function7 to make a list for those that wont be able to attend
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]
second_night_availability = build_daily_frequency_table()
print(calculate_availability(unable_to_attend_best_night, second_night_availability))
second_night = find_best_night(second_night_availability)
print(second_night)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, game = 'Abruptly Goblins!')