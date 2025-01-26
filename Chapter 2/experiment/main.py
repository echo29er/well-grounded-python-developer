'''
Software purpose: 
* Online community of users interested in similar things. 
* The software emails users about upcoming events.
* The email includes noncommunity members who've registered for event emails. 
* The community wants to change how personalised email is rendered by creating concepts: 
* Formal, informal and casual. 
* Nonmembers receive formal. 
* Members would have an email based on the user's account settings. 
'''

from utilities import names
from utilities import informal
from utilities import casual
from utilities import account 

# generate a community list of three of the same people 
community = [{
    "title": "Mr.",
    "fname": "John",
    "lname": "Smith"
    } for x in range(3)
]

# iterate through the community sending emails
for person in community: 
    tone = account.get_tone(person)
    if tone == "formal":
        get_name = names.get_name
    elif tone == "informal":
        get_name = informal.get_name
    elif tone == "casual":
        get_name = casual.get_name

    print(get_name(person))

