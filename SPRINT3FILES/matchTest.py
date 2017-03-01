import math  # for min, max, ceil, and other operations
import haversine  # for calculating the radial distance difference


def calcDistance(profile1, profile2):
    if profile1.select()[0].locationLat is None:
        profile1.update(locationLat='0')
    if profile1.select()[0].locationLong is None:
        profile1.update(locationLong='0')
    if profile2.select()[0].locationLat is None:
        profile2.update(locationLat='0')
    if profile2.select()[0].locationLong is None:
        profile2.update(locationLong='0')
    distance1Lat = float(profile1.select()[0].locationLat)
    distance1Lon = float(profile1.select()[0].locationLong)
    distance2Lat = float(profile2.select()[0].locationLat)
    distance2Lon = float(profile2.select()[0].locationLong)
    totalDistance1 = (distance1Lat, distance1Lon)
    totalDistance2 = (distance2Lat, distance2Lon)
    print(distance1Lat)
    print(distance1Lon)
    print(distance2Lat)
    print(distance2Lon)
    totDist = haversine.haversine(totalDistance1, totalDistance2, miles=True)
    if totDist > 25.0:
        print("Person is too far away! ", totDist, " miles away, to be exact! Won't show up in matches!")
    elif totDist < 2.0:
        print("Person is really close to you! Only ", totDist,
              " miles away! Hopefully you have a high match percentage!")
    else:
        print("Miles away: ", totDist)


def lookingforConstraint(profile1, profile2):
    authuserLookingfor = profile1.select()[0].interest
    allmatchLookingfor = profile2.select()[0].interest
    authuserGender = profile1.select()[0].gender
    allmatchGender = profile2.select()[0].gender

    # Woman looking for a man:
    if authuserLookingfor == 'Woman' and authuserGender == 'Male' and allmatchLookingfor == 'Man' and allmatchGender == 'Female':
        return True
    # Man looking for a woman:
    elif authuserLookingfor == 'Man' and authuserGender == 'Female' and allmatchLookingfor == 'Woman' and allmatchGender == 'Male':
        return True
    # Man looking for a man:
    elif authuserLookingfor == 'Man' and authuserGender == 'Male' and allmatchLookingfor == 'Man' and allmatchGender == 'Male':
        return True
    # Woman looking for a woman:
    elif authuserLookingfor == 'Woman' and authuserGender == 'Female' and allmatchLookingfor == 'Woman' and allmatchGender == 'Female':
        return True
    # Friendship looking for friendship:
    elif authuserLookingfor == 'Friendship' and allmatchLookingfor == 'Friendship':
        return True
    # If nothing pairs up, there won't be a match:
    else:
        return False


def interestCollageMask(profile1, profile2):
    usersInterestCollage = bytearray(profile1.select()[0].interestMask)
    matchInterestCollage = bytearray(profile2.select()[0].interestMask)
    andMask = bytearray(len(usersInterestCollage))
    oneCounter = 0
    for i in range(len(usersInterestCollage)):
        andMask[i] = usersInterestCollage[i] & matchInterestCollage[i]
    andMask = str(andMask)
    for i in range(len(andMask)):
        if andMask[i] == '1':
            oneCounter += 1
    # all the PRINT statements are for DEBUGGING purposes only
    print("Number of images that match is: ", oneCounter)
    return oneCounter


def testAdven(profile1, profile2):
    adve1, bubb1, conf1, cons1, crea1, fier1, goof1, inte1, intr1, open1, spon1 = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # this is tedius but we have to
    adve2, bubb2, conf2, cons2, crea2, fier2, goof2, inte2, intr2, open2, spon2 = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # initialize otherwise it fails
    adve1 = profile1.select()[0].adventurous
    bubb1 = profile1.select()[0].bubbly
    conf1 = profile1.select()[0].confident
    cons1 = profile1.select()[0].conservative
    crea1 = profile1.select()[0].creative
    fier1 = profile1.select()[0].fiery
    goof1 = profile1.select()[0].goofy
    inte1 = profile1.select()[0].intellectual
    intr1 = profile1.select()[0].introverted
    open1 = profile1.select()[0].openness
    spon1 = profile1.select()[0].spontaneity

    adve2 = profile2.select()[0].adventurous
    bubb2 = profile2.select()[0].bubbly
    conf2 = profile2.select()[0].confident
    cons2 = profile2.select()[0].conservative
    crea2 = profile2.select()[0].creative
    fier2 = profile2.select()[0].fiery
    goof2 = profile2.select()[0].goofy
    inte2 = profile2.select()[0].intellectual
    intr2 = profile2.select()[0].introverted
    open2 = profile2.select()[0].openness
    spon2 = profile2.select()[0].spontaneity

    profile1List = [adve1, bubb1, conf1, cons1, crea1, fier1, goof1, inte1, intr1, open1, spon1]
    profile2List = [adve2, bubb2, conf2, cons2, crea2, fier2, goof2, inte2, intr2, open2, spon2]

    # THE PERSONALITIES #
    numerator = min(profile1List[0], profile2List[0])  # adventurous
    numerator2 = min(profile1List[1], profile2List[1])  # bubbly
    numerator3 = min(profile1List[2], profile2List[2])  # confident
    numerator4 = min(profile1List[3], profile2List[3])  # conservative
    numerator5 = min(profile1List[4], profile2List[4])  # creative
    numerator6 = min(profile1List[5], profile2List[5])  # fiery
    numerator7 = min(profile1List[6], profile2List[6])  # goofy
    numerator8 = min(profile1List[7], profile2List[7])  # intellectual
    numerator9 = min(profile1List[8], profile2List[8])  # introverted
    numerator10 = min(profile1List[9], profile2List[9])  # openness
    numerator11 = min(profile1List[10], profile2List[10])  # spontaneous
    # need divByZeroFix because if max(profileList[i], profileList[i]) = 0, when we divide, program will crash
    divByZeroFix = max(profile1List[0], profile2List[0])  # adventurous
    divByZeroFix2 = max(profile1List[1], profile2List[1])  # bubbly
    divByZeroFix3 = max(profile1List[2], profile2List[2])  # confident
    divByZeroFix4 = max(profile1List[3], profile2List[3])  # conservative
    divByZeroFix5 = max(profile1List[4], profile2List[4])  # creative
    divByZeroFix6 = max(profile1List[5], profile2List[5])  # fiery
    divByZeroFix7 = max(profile1List[6], profile2List[6])  # goofy
    divByZeroFix8 = max(profile1List[7], profile2List[7])  # intellectual
    divByZeroFix9 = max(profile1List[8], profile2List[8])  # introverted
    divByZeroFix10 = max(profile1List[9], profile2List[9])  # openness
    divByZeroFix11 = max(profile1List[10], profile2List[10])  # spontaneous

    try:
        total = float(numerator) / divByZeroFix * 100
    except ZeroDivisionError:
        total = 0.0  # we return 0 because if both people haven't answered any questions, their match % = 0

    try:
        total2 = float(numerator2) / divByZeroFix2 * 100
    except ZeroDivisionError:
        total2 = 0.0

    try:
        total3 = float(numerator3) / divByZeroFix3 * 100
    except ZeroDivisionError:
        total3 = 0.0

    try:
        total4 = float(numerator4) / divByZeroFix4 * 100
    except ZeroDivisionError:
        total4 = 0.0

    try:
        total5 = float(numerator5) / divByZeroFix5 * 100
    except ZeroDivisionError:
        total5 = 0.0

    try:
        total6 = float(numerator6) / divByZeroFix6 * 100
    except ZeroDivisionError:
        total6 = 0.0

    try:
        total7 = float(numerator7) / divByZeroFix7 * 100
    except ZeroDivisionError:
        total7 = 0.0

    try:
        total8 = float(numerator8) / divByZeroFix8 * 100
    except ZeroDivisionError:
        total8 = 0.0

    try:
        total9 = float(numerator9) / divByZeroFix9 * 100
    except ZeroDivisionError:
        total9 = 0.0

    try:
        total10 = float(numerator10) / divByZeroFix10 * 100
    except ZeroDivisionError:
        total10 = 0.0

    try:
        total11 = float(numerator11) / divByZeroFix11 * 100
    except ZeroDivisionError:
        total11 = 0.0

    grandtotal = (
                 total + total2 + total3 + total4 + total5 + total6 + total7 + total8 + total9 + total10 + total11) / 11
    grandtotal = int(
        math.ceil((grandtotal + (interestCollageMask(profile1, profile2) * 15)) / 2))  # messy, but works lol
    if grandtotal > 100:
        grandtotal = 100  # if the total match % is greater than 100, just return 100%

    print("Percentage of match: ", grandtotal)

    return grandtotal