__author__ = 'Robert'

__version__ = 0.1

# Use the same index file for all our responses.
response.view = "report/index.html"

def index():
    response.title = "Reports"
    return {}

def shooter():
    response.title = "Shooter Record"
    script = SCRIPT("""
                    $('document').ready(function(){
                        $('#mycombo').change(function(){
                            $('#myform').submit();
                        });
                    });
                    """)
    form = SQLFORM.factory(
        Field("shooter",label="Shooter",
              requires=IS_IN_DB(db, 'shooter.id', '%(lname)s, %(fname)s',
                                error_message="Please pick a shooter")),
        buttons=[])
    form.attributes['_id'] = 'myform'
    form.element('select').attributes['_id'] = 'mycombo'
    data = dict(script=script,form=form)
    if form.accepts(request.vars, keepvalues=True):
        content = 'Shooter report for %s' % (db.shooter._format % db.shooter[form.vars.shooter])
        for
        data.update(dict(content=content))
    return data

