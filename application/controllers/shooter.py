import datetime

__author__ = "Robert"

__version__ = 0.1

# Use the same index file for all our responses.
response.view = "shooter/index.html"

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.title = "Shooter management"
    content = []
    data = {"content": "".join(content)}
    return data

#@auth.requires_login()
def record_score():
    response.title = "Shooter: Record Score"
    response.view = "shooter/record_score.html"
    """
     represent=lambda id, row: "%s %s %s" % (row.qualification.qualification_name,
                                                                        row.rating.rating_name,
                                                                        row.s_posision.position_name),
    """
    courses = [OPTION("%s %s %s" % (s.qualification.qualification_name, s.rating.rating_name,
                                     s.s_position.position_name), _value=s.id)
                for s in db(db.course_of_fire).select()]
    select = TR(LABEL("Course Of Fire:"),
                SELECT(*courses, _name="course", requires=IS_IN_DB(db, 'course_of_fire.id')))
    form = SQLFORM(db.shot_score)
    form[0].insert(1,select)
    data = {"message": T("Input shooter scores"), "form": form}
    return data

#@auth.requires_login()
def manage():
    response.title = "Shooter: Add shooter"
    response.view = "shooter/input.html"
    form = SQLFORM.grid(db.shooter, user_signature=False)
    data = {"message": T("Add/Edit new shooter"), "form": form}
    return data

def checkin():
    content = []
    flash = []
    checkins = []
    dupes = []
    record = db.shooter(request.args(0))
    response.title = "Shooter Check in"
    response.view = "shooter/checkin.html"
    # response.debug = True
    now = datetime.datetime.now()
    shooters = [OPTION("%s, %s" % (s.lname, s.fname), _value=s.id)
                for s in db(db.shooter).select(orderby=db.shooter.lname|db.shooter.fname)]
    select = SELECT(*shooters, _name="shooter", _multiple="multiple",
                    requires=IS_IN_DB(db, 'shooter.id', multiple=True))
    form = FORM(select, INPUT(_type="submit", _value="Check-in"))
    if form.accepts(request, session):
        for arg in form.vars.shooter:
            record = db.shooter(arg)
            checkin_records = db(db.attendance.shooter==arg).select(orderby=db.attendance.checkin)
            if len(checkin_records) > 0:
                last_checkin = (checkin_records.records[-1]).attendance.checkin
                if ((last_checkin.year, last_checkin.month, last_checkin.day) == (now.year, now.month, now.day)):
                    dupes.append("%s %s" % (record.fname, record.lname))
                    continue
            db.attendance.insert(shooter=record.id, checkin=now)
            checkins.append("%s %s" % (record.fname, record.lname))
    elif form.errors:
        flash.append("Form has errors")
    if len(checkins) > 0:
        flash.append("Checked in: %s" % (", ".join(checkins)))
    if len(dupes) > 0:
        if len(flash) > 0:
            flash.append(BR())
        flash.append("Already checked in: %s" % (", ".join(dupes)))
    if len(flash) > 0:
        response.flash = BEAUTIFY(flash)
        content += flash
    content += [HR(), "CHECKINS", BEAUTIFY(checkins), HR(), "DUPES", BEAUTIFY(dupes)]
    return {"content": BEAUTIFY(content), "form": form}

def add_score():
    response.title = "Course of fire: Add new rating"
    response.view = None
    data = {"message": T("Create new rating")}
    return data