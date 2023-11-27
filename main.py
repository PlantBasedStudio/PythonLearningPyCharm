import datetime
from datetime import date

bot_name = "David"
current_date = datetime.datetime.now()
year_date = current_date.year


def first_encounter():
    '''Le bot va se présenter et donner sa date de naissance'''
    print(f"Hello! My name is {bot_name} .")
    print(f"I was created in {year_date} .")
    print('test de year : {} suivi de name {}'.format(year_date, bot_name))


first_encounter()
print(first_encounter.__doc__)
#Revoir les sets