# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    #db = DAL(myconf.get('db.uri'),
	db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

db.define_table('profile',
                Field('name'),
                Field('gender', requires=IS_IN_SET(['Male', 'Female', 'Other'])),
                Field('birthDate','date', requires = IS_DATE(format='%Y-%m-%d',
                     error_message='must be YYYY-MM-DD!')),
                Field('city', requires=IS_NOT_EMPTY()),
                Field('interest', requires=IS_IN_SET(['Man', 'Woman', 'Friendship'])),
                Field('dogName', requires=IS_NOT_EMPTY()),
                Field('dogGender', requires=IS_IN_SET(['Male', 'Female', 'Other'])),
                Field('dogAge','integer',  requires = IS_INT_IN_RANGE(0, 20,
                     error_message='Dog\'s age not possible!')),
                Field('locationLong'),
                Field('locationLat'))
db.profile.id.writable = db.profile.id.readable = False
db.profile.name.writable = False
db.profile.locationLong.readable = False

db.define_table('images',
                Field('userID'),
                Field('profilePic', 'upload'),
                Field('profilePicDog', 'upload'))
db.images.userID.writable = db.images.userID.readable = False

## this table is used for when the user selects images to be added to his/her image collage.
## the user can select a MAX of 2 images (MAX of 2 items from each field: ex, Tacos and Salad from food)
db.define_table(
    'interestCollage',
    Field('food', 'string', requires=IS_IN_SET(['Tacos', 'Salad', 'Cheeseburger', 'Pizza', 'Sushi', 'Breakfast'])),
    Field('pepe', 'boolean', default=False),
    Field('activities', 'string', requires=IS_IN_SET(['Hiking', 'Partying', 'Working Out', 'Travel', 'Reading', 'Skydiving'])),
    Field('hobbies', 'string', requires=IS_IN_SET(['Games', 'Sciences', 'Art', 'Movies', 'Cooking', 'Guitar'])),
    Field('places', 'string', requires=IS_IN_SET(['Beach', 'Woods', 'Library', 'Concert', 'WorldMap', 'HomeWithDog'])),
    Field('sports', 'string', requires=IS_IN_SET(['Tennis', 'RunningJogging', 'Football', 'Soccer', 'Basketball', 'Chess']))
)
db.interestCollage.id.writable = db.interestCollage.id.readable = False

##Defines food Interests
db.define_table(
    'interestFood',
    Field('Tacos', 'boolean', default=False),
    Field('Salad', 'boolean', default=False),
    Field('Cheeseburger', 'boolean', default=False),
    Field('Pizza', 'boolean', default=False),
    Field('Sushi', 'boolean', default=False),
    Field('Breakfast', 'boolean', default=False))
db.interestFood.id.writable = db.interestFood.id.readable = False

##Defines Activites Interests
db.define_table(
    'interestActivities',
    Field('Hicking', 'boolean', default=False),
    Field('Partying', 'boolean', default=False),
    Field('Working_Out', 'boolean', default=False),
    Field('Travel', 'boolean', default=False),
    Field('Reading', 'boolean', default=False),
    Field('Skydiving', 'boolean', default=False))
db.interestActivities.id.writable = db.interestActivities.id.readable = False


##Defines Hobbies Interests
db.define_table(
    'interestHobbies',
    Field('Games', 'boolean', default=False),
    Field('Sciences', 'boolean', default=False),
    Field('Art', 'boolean', default=False),
    Field('Movies', 'boolean', default=False),
    Field('Cooking', 'boolean', default=False),
    Field('Guitar', 'boolean', default=False))
db.interestHobbies.id.writable = db.interestHobbies.id.readable = False


##Defines Place Interests
db.define_table(
    'interestPlaces',
    Field('Beach', 'boolean', default=False),
    Field('Woods', 'boolean', default=False),
    Field('Library', 'boolean', default=False),
    Field('Concert', 'boolean', default=False),
    Field('WorldMap', 'boolean', default=False),
    Field('HomeWithDog', 'boolean', default=False))
db.interestPlaces.id.writable = db.interestPlaces.id.readable = False

##Defines Sports Interests
db.define_table(
    'interestSports',
    Field('Tennis', 'boolean', default=False),
    Field('RunningJogging', 'boolean', default=False),
    Field('Football', 'boolean', default=False),
    Field('Soccer', 'boolean', default=False),
    Field('Basketball', 'boolean', default=False),
    Field('Chess', 'boolean', default=False))
db.interestSports.id.writable = db.interestSports.id.readable = False

db.define_table(
	'personalities',
	Field('id'),
	Field('adventurous', 'integer'),
	Field('bubbly', 'integer'),
	Field('confident', 'integer'),
	Field('conservative', 'integer'),
	Field('creative', 'integer'),
	Field('fiery', 'integer'),
	Field('goofy', 'integer'),
	Field('intellectual', 'integer'),
	Field('introverted', 'integer'),
	Field('openness', 'integer'),
	Field('spontaneity', 'integer')
)
# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
