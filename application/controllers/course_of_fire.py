__author__ = 'Robert'

__version__ = 0.1

# Use the same index file for all our responses.
response.view = 'course_of_fire/index.html'

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.title = 'Course of fire management'
    data = {}
    return data

#@auth.requires_login()
def course():
    response.title = "Manage Courses of Fire"
    response.view = "course_of_fire/modify.html"
    data = {"message": T("Manage Courses of Fire"), "type": "course",
            "grid": SQLFORM.smartgrid(db.course_of_fire,
                                      linked_tables=[db.qualification, db.rating, db.shot_position],
                                      user_signature=False)}
    return data

#@auth.requires_login()
def position():
    response.title = "Manage Positions"
    response.view = "course_of_fire/modify.html"
    data = {"message": T("Manage Positions"), "type": "position",
            "grid": SQLFORM.grid(db.shot_position, user_signature=False)}
    return data


#@auth.requires_login()
def qualification():
    response.title = "Manage Qualifications"
    response.view = "course_of_fire/modify.html"
    data = {"message": T("Manage Qualifications"), "type": "qualification",
            "grid": SQLFORM.grid(db.qualification, user_signature=False)}
    return data


#@auth.requires_login()
def rating():
    response.title = "Manage Ratings"
    response.view = "course_of_fire/modify.html"
    data = {"message": T("Manage Ratings"), "type": "rating",
            "grid": SQLFORM.grid(db.rating, user_signature=False)}
    return data
