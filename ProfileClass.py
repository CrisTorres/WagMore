import math

# The profile for the user. We will store each profile in the SQLLite database upon each new instance of a Profile class.
class Profile:
    def __init__(self, userName, dogName, location, adven=0, bubbl=0, confi=0,
                 conse=0, creat=0, fiery=0, goofy=0,
                 intel=0, openn=0, spont=0):
        self.uname = userName
        self.dname = dogName
        self.locat = location
        self.interests = []
        self.questions = []
        # 10 personality traits to help with the Matching Algorithm:
        self.adven = adven #adventurous
        self.bubbl = bubbl #bubbly
        self.confi = confi #confident
        self.conse = conse #conservative
        self.creat = creat #creative
        self.fiery = fiery #fiery
        self.goofy = goofy #goofy
        self.intel = intel #intellectuality
        self.openn = openn #openness
        self.spont = spont #spontaneity
        self.personalities = [adven, bubbl, confi, conse, creat, fiery, goofy, intel, openn, spont]
        self.ranks = []

    def add_interestCollage(self, interest):
        self.interests.append(interest)

    def add_questionsBank(self, question):
        self.questions.append(question)

def aver(Profile1, trait1, Profile2, trait2):
    return math.ceil((min(Profile1.adven, Profile2.adven)/max(Profile1.adven, Profile2.adven)) * 100)

# averAll returns the overall match percentage based on personalities
def averAll(Profile1, trait1, Profile2, trait2):
    for i in Profile1.personalities and Profile2.personalities:
        return math.ceil((min(Profile1.personalities[i], Profile2.personalities[i]) / max(Profile1.personalities[i], Profile2.personalities[i]))
                         * 100)

# averages the matches for specific key (0 = adven, 1 = bubbl, ... 9 = spont)
def averAny(Profile1, Profile2, traitKey):
    thisAver = math.ceil((min(Profile1.personalities[traitKey], Profile2.personalities[traitKey]) / max(Profile1.personalities[traitKey],
                                                                                             Profile2.personalities[traitKey]))
                         * 100)
    return thisAver

def averInterests(Profile1, interests1, Profile2, interests2):
    interestsCount = 0
    interests1.sort()
    interests2.sort()
    for i in interests1:
        for j in interests2:
            if i == j:
                interestsCount += 1
    interestsPercentage = math.ceil((interestsCount/(max(len(interests1), len(interests2)))) * 100)
    return interestsPercentage

"""
# here I test the classes + algorithms:
Jimbob = Profile("JimBob", "Steve", "Santa Cruz", 2, 3, 10)
Marylou = Profile("MaryLou", "Juju", "Santa Cruz", 2, 2, 8)

Jimbob.add_interestCollage("food")
Marylou.add_interestCollage("food")
Jimbob.add_interestCollage("cats")
Marylou.add_interestCollage("hockey")
Marylou.add_interestCollage("cats")

print(Jimbob.uname)
print(Jimbob.dname)
print(Jimbob.adven)
print(Jimbob.bubbl)
print(Jimbob.confi)
Jimbob.confi += 2
print(Jimbob.confi)
print(Jimbob.adven)
print(aver(Jimbob, Jimbob.adven, Marylou, Marylou.adven)) #should print 100
print(averInterests(Jimbob, Jimbob.interests, Marylou, Marylou.interests)) #should print 67
print(averAny(Jimbob, Marylou, 0)) #should also print 100
print(averAny(Jimbob, Marylou, 1)) #should print 67
Jimbob.add_interestCollage("tennis")
Jimbob.add_interestCollage("hiking")
Jimbob.add_interestCollage("mario")
print(averInterests(Jimbob, Jimbob.interests, Marylou, Marylou.interests)) #should print 40
print(averAll(Jimbob, Jimbob.adven, Marylou, Marylou.adven)) #should print 80 -> Jimbob & Marylou have 80% overall match
"""
