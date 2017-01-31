# The profile for the user. We will store each profile in the SQLLite database upon each new instance of a Profile class.
class Profile:
    def __init__(self, userName, dogName, location,
                 personalityAdventurous=0, personalityBubbly=0, personalityConfident=0,
                 personalityConservative=0, personalityCreative=0, personalityFiery=0, personalityGoofy=0,
                 personalityIntellectual=0, personalityOpenness=0, personalitySpontaneous=0):
        self.uname = userName
        self.dname = dogName
        self.locat = location
        self.interests = []
        self.questions = []
        # 10 personality traits to help with the Matching Algorithm:
        self.adven = personalityAdventurous
        self.bubbl = personalityBubbly
        self.confi = personalityConfident
        self.conse = personalityConservative
        self.creat = personalityCreative
        self.fiery = personalityFiery
        self.goofy = personalityGoofy
        self.intel = personalityIntellectual
        self.openn = personalityOpenness
        self.spont = personalitySpontaneous

    def add_interestCollage(self, interest):
        self.interests.append(interest)

    def add_questionsBank(self, question):
        self.questions.append(question)

# Here I test the class.
#Jimbob = Profile("JimBob", "Steve", "Santa Cruz", 2, 2, 10)
#
#print(Jimbob.uname)
#print(Jimbob.dname)
#print(Jimbob.adven)
#print(Jimbob.bubbl)
#print(Jimbob.confi)
#Jimbob.confi += 2
#print(Jimbob.confi)
