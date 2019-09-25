from eventer import Eventer


# Your calendar id here (probably just your gmail adress)
calendar_id = "mateusz.baczek1998@gmail.com"


#
# REMEMBER TO GET YOUR ACCOUNT CREDENTIALS FROM 
# https://console.developers.google.com/apis/credentials
# AND PUT THEM IN THE REPO'S ROOT UNDER THE NAME `credentials.json`
#
# You might need to create a GoogleAPI project
# (which is free and perfectly safe)
#


'''
The color setup below is as similiar
to the one in JSOS as it was possible.


All avialable colors (for google calendar):
Eventer.Color.
              Default
              Tomato
              Tangerine
              Banana
              Basil
              Sage
              Peacock
              Blueberry
              Lavender
              Grape
              Flamingo
              Graphite
'''

LECTURE_COLOR = Eventer.Color.Basil
PRACTICALS_COLOR = Eventer.Color.Banana
PROJECT_COLOR = Eventer.Color.Peacock
LAB_COLOR = Eventer.Color.Lavender
SEMINARS_COLOR = Eventer.Color.Sage
