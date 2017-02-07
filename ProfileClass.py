import math

# The profile for the user. We will store each profile in the SQLLite database upon each new instance of a Profile class.
class Profile:
    def __init__(self, userName, dogName, location, foodsBreakfast=0, foodsBurger=0, foodsFruits=0, foodsPizza=0, foodsSushi=0, foodsTaco=0,
            activHiking=0, activReading=0, activSkydiving=0, activTravel=0, activWorkout=0, activWine=0,
            hobbyArt=0, hobbyCooking=0, hobbyGames=0, hobbyGuitar=0, hobbyPhotography=0, hobbyScience=0,
            placeBeach=0, placeConcert=0, placeHome=0, placeLibrary=0, placeWoods=0, placeWorld=0,
            sportBasketball=0, sportChess=0, sportFootball=0, sportRunning=0, sportSoccer=0, sportTennis=0,
                 adven=0, bubbl=0, confi=0,
                 conse=0, creat=0, fiery=0, goofy=0,
                 intel=0, intro=0, openn=0, spont=0,
                 ):
        self.uname = userName
        self.dname = dogName
        self.locat = location
        self.interests = [
            foodsBreakfast, foodsBurger, foodsFruits, foodsPizza, foodsSushi, foodsTaco,
            activHiking, activReading, activSkydiving, activTravel, activWorkout, activWine,
            hobbyArt, hobbyCooking, hobbyGames, hobbyGuitar, hobbyPhotography, hobbyScience,
            placeBeach, placeConcert, placeHome, placeLibrary, placeWoods, placeWorld,
            sportBasketball, sportChess, sportFootball, sportRunning, sportSoccer, sportTennis
        ]
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
        self.intro = intro #introverted
        self.openn = openn #openness
        self.spont = spont #spontaneity
        # update personality traits with the index of the .personlities array:
        self.personalities = [adven, bubbl, confi, conse, creat, fiery, goofy, intel, intro, openn, spont]

    # when the user selects an image, append it to the Interest Collage

    # when the user unselects an image, take it away from the Interest Collage
    def delete_interestCollage(self, key):
        self.interests[key]=0

    # when the user answers a queston, append it to their questions answered
    def add_questionsBank(self, question):
        self.questions.append(question)

# averAll returns the overall match percentage based on personalities
def add_interestCollage(Profile, key):
    Profile.interests[key]=1

def averAll(Profile1, Profile2):
    total = 0
    for i in Profile1.personalities and Profile2.personalities:
        total += averAny(Profile1, Profile2, i)
    total /= len(Profile1.personalities)
    total = math.ceil(total)
    return total

# averages the matches for specific key (0 = adven, 1 = bubbl, ... 9 = spont)
def averAny(Profile1, Profile2, traitKey):
    numerator = min(Profile1.personalities[traitKey], Profile2.personalities[traitKey])
    # need divByZeroFix because if max(trait1, trait2) = 0, when we divide, program will crash
    divByZeroFix = max(Profile1.personalities[traitKey], Profile2.personalities[traitKey])
    if divByZeroFix == 0:
        return 0
        # we return 100 because if both people haven't answered any questions, their match% = 0
    else:
        return math.ceil((numerator/divByZeroFix) * 100)

def averInterests(Profile1, Profile2):
    interestsCount = 0
    for i in range(len(Profile1.interests)):
        if Profile1.interests[i]==Profile2.interests[i]==1:
            interestsCount += 1
    return math.ceil((interestsCount/10)*150)
    # interests match higher than questions, so we multiply by 150%. If the total match
    # goes above 100%, it will just be 100%

# updateTraits takes in a user, and four traits, adds 2 points to one trait, 2 points to another, 1 point to another,
#    and subtracts 1 point from another trait. Profile.personalities[trait] corresponds to the list of traits defined
#    in the class (1 = adventurous, 2 = bubbly, etc.)
def updateTraits(Profile, trait1, trait2, trait3, trait4):
    Profile.personalities[trait1] += 2
    Profile.personalities[trait2] += 2
    Profile.personalities[trait3] += 1
    if (Profile.personalities[trait4] == 0):
        Profile.personalities[trait4] = 0
    else:
        Profile.personalities[trait4] -= 1

# SAMPLE QUESTION: #
def question1(Profile):
    loop = True
    print("On a Friday night, I prefer to...")
    print("1. Go out dancing")
    print("2. Stay in and read a book")
    print("3. Prepare for a weekend of travel")
    print("4. Something creative (writing, drawing, painting, etc.")
    print("5. Skip question")
    while (loop):
        answer = input("Enter 1-5: ")
        if (answer == '1'):
            updateTraits(Profile, 1, 10, 9, 8)
            loop = False
        elif (answer == '2'):
            updateTraits(Profile, 8, 7, 3, 10)
            loop = False
        elif (answer == '3'):
            updateTraits(Profile, 0, 10, 2, 8)
            loop = False
        elif (answer == '4'):
            updateTraits(Profile, 7, 4, 1, 5)
            loop = False
        elif (answer == '5'):
            print("Question skipped!")
            loop = False
        else:
            print("Invalid input. Please enter a valid input.")

"""
#here I test the classes + algorithms:
Jimbob = Profile("JimBob", "Steve", "Santa Cruz")
Marylou = Profile("MaryLou", "Juju", "Santa Cruz")
basketball = 24

add_interestCollage(Jimbob, 0) #Jimbob likes Breakfast Foods
add_interestCollage(Jimbob, 1) #Jimbob likes Burgers
add_interestCollage(Marylou, 0) #Marylou also likes Breakfast Foods
add_interestCollage(Marylou, 1) #Marylou also likes Burgers
add_interestCollage(Jimbob, basketball) #Jimbob likes Basketball
add_interestCollage(Marylou, basketball) #Marylou also likes Breakfast Foods
print(Jimbob.interests[0])
print(Marylou.interests[0])
print(averInterests(Jimbob, Marylou))

print(Jimbob.intel)
print(Jimbob.personalities[7], Jimbob.personalities[4], Jimbob.personalities[1], Jimbob.personalities[5])
question1(Jimbob)
question1(Jimbob)
question1(Jimbob)
print(Jimbob.personalities[7], Jimbob.personalities[4], Jimbob.personalities[1], Jimbob.personalities[5])
print(Jimbob.intel)
question1(Marylou)
question1(Marylou)
question1(Marylou)
print(Marylou.personalities[7], Marylou.personalities[4], Marylou.personalities[1], Marylou.personalities[5])


print("Name of Profile1: ", Jimbob.uname) #print Jimbob's name
print("Name of Profile1's Dog: ", Jimbob.dname)

print("Adventurous Match%: ", averAny(Jimbob, Marylou, 0))
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 1))
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 2))
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 3))
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 4))
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 5))
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 6))
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 7))
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 8))
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 9))
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 10))

print("Match% for INTERESTS: ", averInterests(Jimbob, Marylou)) #should print 45
print("Adventurous Match%: ", averAny(Jimbob, Marylou, 0)) #averages the adventurous trait
print("Bubbly Match%: ", averAny(Jimbob, Marylou, 1)) #averages the bubbly trait
print("Average Personality Match%: ", averAll(Jimbob, Marylou)) #prints the average of all the interests
totalMatch = ((averInterests(Jimbob, Marylou)+averAll(Jimbob, Marylou))/2)
print("Total match%:", totalMatch)
"""
