__author__ = 'Robert'

__version__ = 0.1

# Use the same index file for all our responses.
response.view = 'default/index.html'

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.title = 'Award management'
    data = {"message": "Put the award links here."}
    return data

def add_award():
    response.title = 'award of fire: Add new award'
    data = {"message": T("Create new award")}
    return data