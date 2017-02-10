from datetime import datetime

def index():
    profiles = db().select(db.profile.ALL)
    images = db().select(db.images.ALL)
    return dict(profiles=profiles, images=images)

def first():
    return dict()

def second():
    return dict()

def loginpage():
    return dict()

def signuppage():
    return dict()

def signuppage2():
    return dict()

def createProfile():
    return dict()

def createProfile2():
    db.images.userID.default=auth.user.id
    form = SQLFORM(db.images)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

@auth.requires_login()
def createProfile_interests():
    if (db(db.interestFood.id==auth.user.id).count()!=1):
        db.interestFood.insert(id=auth.user.id)
    interest1=db(db.interestFood.id==auth.user.id).select()
    print(interest1)
    return dict(interest1=interest1)

def createProfile_interest_2():
    if (db(db.interestActivities.id == auth.user.id).count() != 1):
        db.interestActivities.insert(id=auth.user.id)
    interest2 = db(db.interestActivities.id == auth.user.id).select()
    print(interest2)
    return dict(interest2=interest2)

def createProfile_interest_3():
    if (db(db.interestHobbies.id == auth.user.id).count() != 1):
        db.interestHobbies.insert(id=auth.user.id)
    interest3 = db(db.interestHobbies.id == auth.user.id).select()
    print(interest3)
    return dict(interest3=interest3)

def createProfile_interest_4():
    if (db(db.interestPlaces.id == auth.user.id).count() != 1):
        db.interestPlaces.insert(id=auth.user.id)
    interest4 = db(db.interestPlaces.id == auth.user.id).select()
    print(interest4)
    return dict(interest4=interest4)

def createProfile_interest_5():
    if (db(db.interestSports.id == auth.user.id).count() != 1):
        db.interestSports.insert(id=auth.user.id)
    interest5 = db(db.interestSports.id == auth.user.id).select()
    print(interest5)
    return dict(interest5=interest5)

def createProfile_aboutYourself():
    if (db(db.interestFood.id==auth.user.id).count()!=1):
        db.interestFood.insert(id=auth.user.id)
    interest1=db(db.interestFood.id==auth.user.id).select()
    print(interest1)
    return dict(interest1=interest1)

def createProfile_confirmation():
    return dict()

def show():
    profile = db.profile(request.args(0, cast=int)) or redirect(URL('index'))
    return dict(profile=profile)

@auth.requires_login()
def mainPage():
    from gluon.tools import geocode
    latitude = longtitude = ''
    if (db(db.profile.id==auth.user.id).count()==1):
        redirect(URL("index"))
    #record = db.profile(request.args(0,cast=int)) or redirect(URL('index'))
    #db.profile.id.default=auth.user.id
    #form = SQLFORM(db.profile,record)
    #form = SQLFORM(db.profile, buttons = [TAG.image(_type="submit", _href=URL("user"), _src= "http://127.0.0.1:8000/WagMore/static/_2.14.6/images/nextButton.png"),TAG.button('Submit',_type="submit")]) ##Wanna make the first image to work as a button
    
    db.profile.id.default=auth.user.id
    db.profile.name.default=auth.user.first_name+' '+auth.user.last_name
    form = SQLFORM(db.profile)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

#Page for managing item posts as well as the comments inside of them
@auth.requires_membership('manager')
def manage_users():
    grid = SQLFORM.smartgrid(db.auth_user)
    return dict(grid=grid)

#Page for managing item posts as well as the comments inside of them
@auth.requires_membership('manager')
def manage_profiles():
    grid = SQLFORM.smartgrid(db.profile)
    return dict(grid=grid)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
