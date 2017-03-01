from datetime import datetime
import masking3
import maskingpersonality
import matchTest


@auth.requires_login()
def testingMatch():
    print("Calculating your matches! Please wait...")
    db.profile.id.default = auth.user.id
    profile1 = db(db.profile.id == auth.user.id)
    profiles = db(db.profile.id != auth.user.id)
    ##db(db.matchTable.idFromMatch==auth.user.id).delete()
    for profile in profiles.select():
        profile2 = db(db.profile.id == profile.id)
        matchTest.calcDistance(profile1, profile2)
        # if matchLocat > 25.0:
        #    print("Too far away! Person won't show up in matches!")
        if matchTest.lookingforConstraint(profile1, profile2) == True:
            print("Match with same interest")
        else:
            print("Not a match --interest violation--")
        matchPercen = matchTest.testAdven(profile1, profile2)
        if (matchPercen > 56 and db((db.matchTable.idFromMatch == auth.user.id and db.matchTable.idToMatch ==
            profile2.select()[0].id)).count() == 0):
            db.matchTable.insert(idToMatch=profile2.select()[0].id, percentage=matchPercen, idFromMatch=auth.user.id,
                                 images_id=profile2.select()[0].id)
    redirect(URL("signuppage"))
    return dict()


@auth.requires_login()
def profilesMatched():
    profiles = db().select(db.profile.ALL)
    matches = db(db.matchTable.idFromMatch == auth.user.id).select()
    images = db().select(db.images.ALL)
    return dict(profiles=profiles, matches=matches, images=images)


def profiles():
    profiles = db().select(db.profile.ALL)
    images = db().select(db.images.ALL)
    return dict(profiles=profiles, images=images)


def index():
    return dict()


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
    db.images.id.default = auth.user.id
    form = SQLFORM(db.images)
    if form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL("createProfile_interests"))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


@auth.requires_login()
def createProfile_interests():
    db.interestFood.id.default = auth.user.id
    form = SQLFORM(db.interestFood)
    if form.process().accepted:
        response.flash = 'form accepted'
        # Modifiying the profile mask
        profileMask = db(db.profile.id == auth.user.id)
        profileMask.update(interestMask='')
        # function in maskModule.py (in the module folder of the application)
        masking3.bitMask(form.vars.values(), profileMask)
        redirect(URL("createProfile_interest_2"))
    return dict(form=form)


def video():
    db.video.videoId.default = auth.user.id
    form = SQLFORM(db.video)
    if form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL("show"))

    return dict(form=form)


def morepictures():
    db.extraPictures.extraPictureId.default = auth.user.id
    form = SQLFORM(db.extraPictures)
    if form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL("show"))

    elif form.errors:
        response.flash = 'form has errors'
    return dict(form=form)


def createProfile_interest_2():
    db.interestActivities.id.default = auth.user.id
    form = SQLFORM(db.interestActivities)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        masking3.bitMask(form.vars.values(), profileMask)
        redirect(URL("createProfile_interest_3"))
    return dict(form=form)


def createProfile_interest_3():
    db.interestSports.id.default = auth.user.id
    form = SQLFORM(db.interestSports)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        masking3.bitMask(form.vars.values(), profileMask)
        redirect(URL("createProfile_interest_4"))
    return dict(form=form)


def createProfile_interest_4():
    db.interestHobbies.id.default = auth.user.id
    form = SQLFORM(db.interestHobbies)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        masking3.bitMask(form.vars.values(), profileMask)
        redirect(URL("createProfile_interest_5"))
    return dict(form=form)


def createProfile_interest_5():
    db.interestPlaces.id.default = auth.user.id
    form = SQLFORM(db.interestPlaces)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        masking3.bitMask(form.vars.values(), profileMask)
        redirect(URL("questions1"))
    return dict(form=form)


def createProfile_aboutYourself():
    return dict()


def createProfile_confirmation():
    return dict()


def show():
    profile = db.profile(request.args(0, cast=int)) or redirect(URL('index'))
    return dict(profile=profile)


@auth.requires_login()
def mainPage():
    from gluon.tools import geocode
    latitude = longtitude = ''
    if (db(db.profile.id == auth.user.id).count() == 1):
        redirect(URL("index"))
    # record = db.profile(request.args(0,cast=int)) or redirect(URL('index'))
    # db.profile.id.default=auth.user.id
    # form = SQLFORM(db.profile,record)
    # form = SQLFORM(db.profile, buttons = [TAG.image(_type="submit", _href=URL("user"), _src= "http://127.0.0.1:8000/WagMore/static/_2.14.6/images/nextButton.png"),TAG.button('Submit',_type="submit")]) ##Wanna make the first image to work as a button

    db.profile.id.default = auth.user.id
    db.profile.name.default = auth.user.first_name + ' ' + auth.user.last_name
    form = SQLFORM(db.profile)
    if form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL("createProfile2"))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


# Page for managing item posts as well as the comments inside of them
@auth.requires_membership('manager')
def manage_users():
    grid = SQLFORM.smartgrid(db.auth_user)
    return dict(grid=grid)


# Page for managing item posts as well as the comments inside of them
@auth.requires_membership('manager')
def manage_profiles():
    grid = SQLFORM.smartgrid(db.profile)
    return dict(grid=grid)


@auth.requires_login()
def questions1():
    db.question1.id.default = auth.user.id
    form = SQLFORM(db.question1)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        maskingpersonality.q1Mask(form.vars.values(), profileMask)
        redirect(URL("questions2"))
    return dict(form=form)


def questions2():
    db.question2.id.default = auth.user.id
    form = SQLFORM(db.question2)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        maskingpersonality.q2Mask(form.vars.values(), profileMask)
        redirect(URL("questions3"))
    return dict(form=form)


def questions3():
    db.question3.id.default = auth.user.id
    form = SQLFORM(db.question3)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        maskingpersonality.q3Mask(form.vars.values(), profileMask)
        redirect(URL("questions4"))
    return dict(form=form)


def questions4():
    db.question4.id.default = auth.user.id
    form = SQLFORM(db.question4)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        maskingpersonality.q4Mask(form.vars.values(), profileMask)
        redirect(URL("createProfile_confirmation"))
    return dict(form=form)


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
    auth.settings.register_next = URL("mainPage")
    auth.settings.login_next = URL("profiles")

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
