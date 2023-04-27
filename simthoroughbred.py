import time
import random
import sys
import pickle
import tkinter as tk

horse1 = ""
horse1speed = 0
horse1stam = 0
horse1surface = 0
horse1age = 0
horse1sex = ""
horse1wins = 0
horse1seconds = 0
horse1thirds = 0
horse1races = 0
horse1record = "Unraced"
horse1earnings = 0
horseinjury = 0
raceform1 = 0
raceform2 = 0
raceform3 = 0
raceform4 = 0
raceform5 = 0
raceform6 = 0
raceform7 = 0
raceform8 = 0
raceform9 = 0
raceform10 = 0
raceform11 = 0
raceform12 = 0
raceform13 = 0
raceform14 = 0
raceform15 = 0
raceform16 = 0
raceform17 = 0
raceform18 = 0
raceform19 = 0
raceform20 = 0
raceform21 = 0
raceform22 = 0
raceform23 = 0
raceform24 = 0
raceform25 = 0
raceform26 = 0
raceform27 = 0
raceform28 = 0
raceform29 = 0
raceform30 = 0
monthlypayment = 0
numskipbreak = 0
breakrest = 0
mare1 = 0
mare1speed = 0
mare1stam = 0
foalspeed = 0
foalstam = 0
foalsex = 0
timeoff = 0

def resethorse():
    global horse1
    global horse1speed
    global horse1stam
    global horse1surface
    global horse1age
    global horse1sex
    global horse1wins
    global horse1seconds
    global horse1thirds
    global horse1races
    global horse1record
    global horse1earnings
    global horseinjury
    global raceform1
    global raceform2
    global raceform3
    global raceform4
    global raceform5
    global raceform6
    global raceform7
    global raceform8
    global raceform9
    global raceform10
    global raceform11
    global raceform12
    global raceform13
    global raceform14
    global raceform15
    global raceform16
    global raceform17
    global raceform18
    global raceform19
    global raceform20
    global raceform21
    global raceform22
    global raceform23
    global raceform24
    global raceform25
    global raceform26
    global raceform27
    global raceform28
    global raceform29
    global raceform30
    horse1 = ""
    horse1speed = 0
    horse1stam = 0
    horse1surface = 0
    horse1age = 0
    horse1sex = ""
    horse1wins = 0
    horse1seconds = 0
    horse1thirds = 0
    horse1races = 0
    horse1record = "Unraced"
    horse1earnings = 0
    horseinjury = 0
    raceform1 = 0
    raceform2 = 0
    raceform3 = 0
    raceform4 = 0
    raceform5 = 0
    raceform6 = 0
    raceform7 = 0
    raceform8 = 0
    raceform9 = 0
    raceform10 = 0
    raceform11 = 0
    raceform12 = 0
    raceform13 = 0
    raceform14 = 0
    raceform15 = 0
    raceform16 = 0
    raceform17 = 0
    raceform18 = 0
    raceform19 = 0
    raceform20 = 0
    raceform21 = 0
    raceform22 = 0
    raceform23 = 0
    raceform24 = 0
    raceform25 = 0
    raceform26 = 0
    raceform27 = 0
    raceform28 = 0
    raceform29 = 0
    raceform30 = 0
    numskipbreak = 0
    breakrest = 0

resethorse()
loan = 0
day = 1
month = 1
year = 2023
foalage = -1000
breedingfarm = 0
b = 100000
bal = float(b)

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Sim Thoroughbred")
time.sleep(1)
print("")
print("This is a text-based game. When faced with options you should select the number associated with your choice and then click the enter key. The game may not recognize other entries.")
time.sleep(2)
print("If this is your first time playing, please read the rules.")
time.sleep(1)
print("")
print("[1]... Start new game")
print("[2]... Load game")
print("[3]... Options")
pick = input()
if pick == "2":
    with open('save.pkl', 'rb') as f:
        b,bal,horse1,horse1speed,horse1stam,horse1surface,horse1age,horse1sex,horse1wins,horse1seconds,horse1thirds,horse1races,horse1record,horse1earnings,horseinjury,raceform1,raceform2,raceform3,raceform4,raceform5,raceform6,raceform7,raceform8,raceform9,raceform10,raceform11,raceform12,raceform13,raceform14,raceform15,raceform16,raceform17,raceform18,raceform19,raceform20,raceform21,raceform22,raceform23,raceform24,raceform25,raceform26,raceform27,raceform28,raceform29,raceform30,loan,day,month,year,breedingfarm,circuitnum,circuit,numskipbreak,breakrest,mare1,mare1speed,mare1stam,foalspeed,foalstam,foalage,foalsex,monthlypayment,timeoff = pickle.load(f)
elif pick == "3":
    print("This area is under construction")

if pick == "1":
    loopone = 0
    while loopone == 0:
        print("")
        print("")
        print("Before you begin, please select which circuit you would like to base your stable in. There will be a fee when you run your horse in a circuit that is not your home circuit.")
        print("[1]... Southern California (Santa Anita, Los Alamitos, & Del Mar)")
        print("[2]... Northern California (Golden Gate, Pleasanton, Ferndale, & Sacramento)")
        print("[3]... Arizona & Nevada (Turf Paradise, Arizona Downs, & Las Vegas Race Course)")
        print("[4]... Oklahoma & Arkansas (Oaklawn Park & Remington Park)")
        circuitnum = input()
        if circuitnum == "1":
            circuit = "Southern California"
            monthlyfee = 3500
        elif circuitnum == "2":
            circuit = "Northern California"
            monthlyfee = 2500
        elif circuitnum == "3":
            circuit = "AriNev"
            monthlyfee = 2000
        elif circuitnum == "4":
            circuit = "OklaArk"
            monthlyfee = 3000
        else:
            print("You did not select a circuit. Please try again.")
            time.sleep(1)
            print("")
            print("")
            continue
        loopone = 1
    
time.sleep(1)

def race():
    global bal
    global horse1
    global horse1speed
    global horse1stam
    global horse1surface
    global horse1age
    global horse1sex
    global horse1wins
    global horse1seconds
    global horse1thirds
    global horse1races
    global horse1record
    global foalage
    global horse1earnings
    global horseinjury
    global day
    global month
    global year
    global raceform1
    global raceform2
    global raceform3
    global raceform4
    global raceform5
    global raceform6
    global raceform7
    global raceform8
    global raceform9
    global raceform10
    global raceform11
    global raceform12
    global raceform13
    global raceform14
    global raceform15
    global raceform16
    global raceform17
    global raceform18
    global raceform19
    global raceform20
    global raceform21
    global raceform22
    global raceform23
    global raceform24
    global raceform25
    global raceform26
    global raceform27
    global raceform28
    global raceform29
    global raceform30
    raceclaim = 0
    global monthlypayment
    global loan
    sexrest = 0
    global breakrest
    global numskipbreak
    
    print("")
    time.sleep(1)
    print("Race Entry System")
    print("")
    time.sleep(1)
    
    print("These are the race tracks that are currently holding a meet. Select the track you would like to race at. Note: racing at a track outside of your circuit will incur a $1,000 shipping and stabling fee.")
    
    if (month >= 1 and month < 6) or (month == 6 and day <= 20) or (month == 12 and day >= 26) or month == 10:
        trackopt1 = "Santa Anita"
    elif (month == 7 and day >= 16) or (month == 9 and day <= 6) or month == 8 or month == 11:
        trackopt1 = "Del Mar"
    else:
        trackopt1 = "Los Alamitos"
    
    if (month >= 1 and month < 5) or (month == 5 and day <= 24) or (month == 8 and day >= 18) or month >= 9:
        trackopt2 = "Golden Gate"
    elif month == 5 or (month == 6 and day <= 14):
        trackopt2 = "Pleasanton"
    elif month == 6 or (month == 7 and day <= 26):
        trackopt2 = "Santa Rosa"
    elif month == 7 or month == 8:
        trackopt2 = "Ferndale"
    else:
        trackopt2 = "Golden Gate"
        
    if (month == 1 and day >= 10) or (month > 1 and month < 5) or (month == 5 and day <= 8) or (month == 11 and day >= 5) or (month == 12 and day <= 2):
        trackopt3 = "Turf Paradise"
    elif (month == 5 and day >= 9) or (month == 6 and day <= 2) or (month == 7 and day >= 4) or month == 8 or (month == 9 and day <= 13):
        trackopt3 = "Arizona Downs"
    elif (month == 6 and day >= 3) or (month == 7 and day <= 3) or (month == 12 and day >= 3 and day <= 17):
        trackopt3 = "Las Vegas Race Course"
    else:
        trackopt3 = "*Circuit inactive*"
    
    if (month == 12 and day >= 3) or (month >= 1 and month <= 4) or (month == 5 and day <= 8):
        trackopt4 = "Oaklawn Park"
    elif (month == 5 and day >= 13) or (month >= 6 and month <= 10) or (month == 11 and day <= 29):
        trackopt4 = "Remington Park"
    else:
        trackopt4 = "*Circuit inactive*"
    
    time.sleep(3)
    print("")
    print("Date: " + str(month) + "/" + str(day) + "/" + str(year))
    print("[1]... " + trackopt1)
    print("[2]... " + trackopt2)
    print("[3]... " + trackopt3)
    print("[4]... " + trackopt4)
    print("[5]... Other (for stakes race)")
    print("[6]... Cancel")
    pick = input()
    
    if pick == "1":
        racetrack = trackopt1
        circuitselect = "1"
    elif pick == "2":
        racetrack = trackopt2
        circuitselect = "2"
    elif pick == "3":
        racetrack = trackopt3
        circuitselect = "3"
    elif pick == "4":
        racetrack = trackopt4
        circuitselect = "4"
    elif pick == "5":
        print("")
        print("")
        time.sleep(2)
        print("Enter race track (i.e. Churchill Downs)")
        racetrack = input()
        circuitselect = "6"
    elif pick == "6":
        return
    else:
        print("Invalid entry")
        time.sleep(3)
        return
    
    if racetrack == "Circuit inactive":
        print("Invalid entry")
        time.sleep(3)
        return
    
    
    #if racetrack == "Santa Anita":
        #racelist = ["Allowance N1X","Allowance N2X","Allowance N3X","Starter Allowance 50000 N2L","Starter Allowance 25000 N2L","Claiming 50000","Claiming 32000","Claiming 25000","Claiming 16000","Claiming 10000","Claiming 35000 N3L","Claiming 16000 N2L","Maiden","Maiden Claiming 100000","Maiden Claiming 75000","Maiden Claiming 50000","Maiden Claiming 20000"]
    #elif racetrack == "Los Alamitos":
        #racelist = ["Allowance","Allowance N1X","Starter Allowance 50000 N2L","Starter Allowance 25000 N2L","Starter Allowance 8000 N2L","Claiming 50000","Claiming 32000","Claiming 16000","Claiming 8000","Claiming 25000 N2L","Claiming 16000 N2L","Claiming 6250 N2L","Maiden","Maiden Claiming 50000","Maiden Claiming 20000"]
    #elif racetrack == "Del Mar":
        #racelist = ["Allowance N1X","Allowance N2X","Allowance N3X","Starter Allowance 50000 N2L","Starter Allowance 16000 N2L","Claiming 50000","Claiming 32000","Claiming 20000","Claiming 12500","Claiming 20000 N3L","Claiming 32000 N2L","Claiming 16000 N2L","Maiden","Maiden Claiming 150000","Maiden Claiming 80000","Maiden Claiming 50000","Maiden Claiming 20000"]
    #elif racetrack == "Golden Gate":
        #racelist = ["Allowance N1X","Allowance N2X","Starter Allowance 50000 N2L","Starter Allowance 12500","Starter Allowance 4000","Claiming 40000","Claiming 32000","Claiming 25000","Claiming 12500","Claiming 8000","Claiming 4000","Claiming 20000 N2L","Claiming 5000 N2L","Maiden","Maiden Claiming 35000","Maiden Claiming 25000","Maiden Claiming 16000","Maiden Claiming 12500","Maiden Claiming 5000"]
    #elif racetrack == "Pleasanton" or racetrack == "Santa Rosa" or racetrack == "Ferndale":
        #racelist = ["Allowance N1X","Allowance N2X","Starter Allowance 50000 N3L","Claiming 20000","Claiming 16000","Claiming 8000","Claiming 5000","Claiming 2500","Claiming 16000 N2L","Claiming 8000 N2L","Claiming 4000 N2L","Maiden","Maiden Claiming 40000","Maiden Claiming 25000","Maiden Claiming 18000","Maiden Claiming 12500","Maiden Claiming 8000"]
    #elif racetrack == "Turf Paradise":
        #racelist = ["Allowance","Allowance N1X","Starter Allowance 8500","Starter Allowance 4000","Claiming 16000","Claiming 10000","Claiming 8000","Claiming 3500","Maiden","Maiden Claiming 15000","Maiden Claiming 7500"]
    #elif racetrack == "Arizona Downs":
        #racelist = ["Allowance N1X","Allowance N2X","Starter Allowance 5000","Starter Allowance 3000","Claiming 10000","Claiming 5000","Claiming 4000","Claiming 8500 N3L","Claiming 3500 N3L","Claiming 3500 N2L","Maiden","Maiden Claiming 30000","Maiden Claiming 15000","Maiden Claiming 5000"]
    #elif racetrack == "Las Vegas Race Course":
        #racelist = ["Allowance","Allowance N1X","Allowance N2X","Starter Allowance 50000","Claiming 50000","Claiming 30000","Maiden","Maiden Claiming 100000"]
    #elif racetrack == "Oaklawn Park" and month == 2 or month == 4:
        #racelist = ["Allowance","Allowance N1X","Allowance N2X","Allowance N3X","Starter Allowance 40000 N1X","Starter Allowance 10000","Claiming 30000","Claiming 20000","Claiming 10000","Claiming 10000 N3L","Claiming 10000 N2L","Maiden","Maiden Claiming 40000","Maiden Claiming 20000"]
    #elif racetrack == "Oaklawn Park":
        #racelist = ["Allowance N1X","Allowance N2X","Allowance N3X","Starter Allowance 40000 N1X","Starter Allowance 10000","Claiming 30000","Claiming 20000","Claiming 10000","Claiming 10000 N3L","Claiming 10000 N2L","Maiden","Maiden Claiming 40000","Maiden Claiming 20000"]
    #elif racetrack == "Remington Park":
        #racelist = ["Allowance N1X","Allowance N2X","Allowance N3X","Starter Allowance 25000","Starter Allowance 10000","Claiming 25000","Claiming 15000","Claiming 7500","Claiming 25000 N3L","Claiming 15000 N2L","Claiming 7500 N2L","Maiden","Maiden Claiming 25000","Maiden Claiming 15000","Maiden Claiming 7500"]
    
    
    
    
    print("")
    print("")
    print("Select race type")
    print("[1]... Maiden")
    print("[2]... Maiden Claiming")
    print("[3]... Allowance")
    print("[4]... Claiming")
    print("[5]... Starter Allowance")
    print("[6]... Stakes")
    
    try:
        pick = int(input())
    except ValueError:
        print("Invalid entry")
        time.sleep(2)
        return
    
    if (pick == 1 or pick == 2) and horse1wins > 0:
        print("")
        print("You are not eligible for this race.")
        time.sleep(3)
        return
    
    print("")
    time.sleep(1)
    if pick == 1:
        racetype = "Maiden"
        race = racetype
        racenum = random.randint(1,10)
    elif pick == 2:
        racetype = "Maiden Claiming"
        print("")
        print("Enter race claim price: (i.e. 25000)")
        try:
            raceclaim = int(input())
        except ValueError:
            print("")
            print("You have made an incorrect entry. Please try again.")
            time.sleep(3)
            return
        race = racetype + " $" + str(raceclaim)
        racenum = random.randint(1,8)
    elif pick == 3:
        racetype = "Allowance"
        print("")
        print("Select the type of allowance race (see rules for defintion of conditions)")
        print("[1]... Allowance N1X")
        print("[2]... Allowance N2X")
        print("[3]... Allowance N3X")
        print("[4]... Allowance")
        alwtype = input()
        
        if alwtype == "1":
            race = racetype + " N1X"
        elif alwtype == "2":
            race = racetype + " N2X"
        elif alwtype == "3":
            race = racetype + " N3X"
        elif alwtype == "4":
            race = racetype
        else:
            print("Invalid entry")
            time.sleep(3)
            return
        racenum = random.randint(1,10)
    elif pick == 4:
        racetype = "Claiming"
        print("Note: the race you are trying to enter may have a condition tag attached. This will not be noted in the race history but you may still run in races that you meet the condition for.")
        print("")
        print("Enter race claim price: (i.e. 25000)")
        try:
            raceclaim = int(input())
        except ValueError:
            print("")
            print("You have made an incorrect entry. Please try again.")
            time.sleep(3)
            return
        race = racetype + " $" + str(raceclaim)
        racenum = random.randint(1,8)
    elif pick == 5:
        racetype = "Starter Allowance"
        racenum = random.randint(1,8)
        race = racetype
        print("Note: the race you are trying to enter may have a condition tag attached. This will not be noted in the race history but you may still run in races that you meet the condition for.")
        print("")
        print("Enter the starter allowance restriction attached to the race: (i.e. 25000)")
        try:
            starteralwr = int(input())
        except ValueError:
            print("")
            print("You have made an incorrect entry. Please try again.")
            time.sleep(3)
            return
    elif pick == 6:
        racenum = random.randint(8,12)
        racetype = "Stakes"
        print("")
        print("Enter the date of the stakes race")
        try:
            racemonth = int(input("Month: "))
        except ValueError:
            print("Invalid entry")
            time.sleep(3)
            return
        try:
            raceday = int(input("Day: "))
        except ValueError:
            print("Invalid entry")
            time.sleep(3)
            return
        try:
            raceyear = int(input("Year: "))
        except ValueError:
            print("Invalid entry")
            time.sleep(3)
            return
        
        sexmod = 0
        agerest = 0
        print("")
        print("Select the grade of the race")
        print("[1]... Grade 1")
        print("[2]... Grade 2")
        print("[3]... Grade 3")
        print("[4]... Ungraded")
        grade = int(input())
        if grade == 4:
            grade = 0
        print("")
        print("Enter the name of the stakes race. The grade should be prefixed. i.e. Grade 2 Example Stakes")
        race = input()
        print("")
        
        if horse1age == 3 and month < 10:
            print("Is this stake for three-year-olds only or for three-year-olds and upwards?")
            print("[1]... 3yo Only")
            print("[2]... 3yo+")
            try:
                agerest = int(input())
            except ValueError:
                print("Invalid entry")
                time.sleep(3)
                return
            if agerest == 2:
                agerest += 3
        
        if horse1sex == "Filly" or horse1sex == "Mare":
            print("Is this an open stakes race or is it restricted to females?")
            print("[1]... Open")
            print("[2]... Females only (fillies or fillies and mares)")
            try:
                sexrest = int(input())
            except ValueError:
                print("Invalid entry")
                time.sleep(3)
                return
            if sexrest == 2:
                sexmod -= 3
        sexmod = sexmod + agerest
    
    ploop = 1
    while ploop == 1:
        print("")
        print("Enter purse: (i.e. 50000)")
        try:
            racepurse = int(input())
        except ValueError:
            print("")
            print("You have made an incorrect entry. Please try again.")
            time.sleep(3)
            return
        ploop = 2
    
    
    if pick == 1:
        if racepurse <= 100000:
            racerating = 24 + racepurse/10000
        else:
            racerating = 34
    elif pick == 2:
        if raceclaim <= 50000:
            racerating = (raceclaim+racepurse)/4200 + 3
        elif raceclaim > 90000:
            racerating = 29
        elif raceclaim > 75000:
            racerating = 28
        elif raceclaim > 50000:
            racerating = 27
    elif pick == 3:
        if racepurse <= 100000:
            racerating = 27 + racepurse/10000
        else:
            racerating = 37
        if alwtype == "2":
            racerating += 1.5
        elif alwtype == "3":
            racerating += 3
        elif alwtype == "4":
            racerating += 3.5
    elif pick == 4:
        racerating = (raceclaim+racepurse)/3500
    elif pick == 5:
        racerating = racepurse/1700
    elif pick == 6:
        if racepurse < 75000:
            racerating = 37
        elif racepurse < 100000:
            racerating = 38
        elif racepurse < 125000:
            racerating = 39
        elif racepurse < 150000:
            racerating = 40
        elif racepurse < 200000:
            racerating = 41
        elif racepurse < 250000:
            racerating = 42
        elif racepurse < 300000:
            racerating = 43
        elif racepurse < 400000:
            racerating = 44
        elif racepurse < 500000:
            racerating = 45
        elif racepurse < 750000:
            racerating = 46
        elif racepurse < 1000000:
            racerating = 47
        elif racepurse < 1500000:
            racerating = 48
        elif racepurse < 2000000:
            racerating = 49
        elif racepurse < 3000000:
            racerating = 50
        else:
            racerating = 51
        racerating += sexmod
        racerating = random.uniform(racerating-1,racerating+1)
    
    print("")
    
    if pick != 6:
        if racetrack == "Santa Anita" or racetrack == "Santa Anita Park":
            distoptions = ["6.5f","8.5f","6.5f(T)","8f(T)"]
        elif racetrack == "Los Alamitos" or racetrack == "Los Alamitos Race Course":
            distoptions = ["5.5f","8f"]
        elif racetrack == "Del Mar":
            distoptions = ["6f","8f","5f(T)","8.5f(T)"]
        elif racetrack == "Golden Gate" or racetrack == "Golden Gate Fields":
            distoptions = ["5.5f(A)","8f(A)","5f(T)","8f(T)"]
        elif racetrack == "Pleasanton":
            distoptions = ["5f","8.5f"]
        elif racetrack == "Santa Rosa":
            distoptions = ["5.5f","8.5f"]
        elif racetrack == "Ferndale":
            distoptions = ["5f","8f"]
        elif racetrack == "Turf Paradise":
            distoptions = ["5f","8f","7.5f(T)"]
        elif racetrack == "Arizona Downs":
            distoptions = ["5.5f","8f"]
        elif racetrack == "Las Vegas" or racetrack == "Las Vegas Race Course":
            distoptions = ["6f","8.5f","5.5f(T)","8.5f(T)"]
        elif racetrack == "Oaklawn" or racetrack == "Oaklawn Park":
            distoptions = ["6f","8.5f"]
        elif racetrack == "Remington" or racetrack == "Remington Park":
            distoptions = ["6f","8f","5f(T)","8f(T)"]
        if horse1age == 2 and month <= 6:
            distoptions = ["5f"]
        elif horse1age == 2 and month <= 7:
            distoptions = ["5.5f"]
        distopts = len(distoptions)
        
        if distopts == 1:
            print("Select distance")
            print("[1]... " + distoptions[0])
        elif distopts == 2:
            print("Select distance")
            print("[1]... " + distoptions[0])
            print("[2]... " + distoptions[1])
        elif distopts == 3:
            print("Select distance")
            print("[1]... " + distoptions[0])
            print("[2]... " + distoptions[1])
            print("[3]... " + distoptions[2])
        elif distopts == 4:
            print("Select distance")
            print("[1]... " + distoptions[0])
            print("[2]... " + distoptions[1])
            print("[3]... " + distoptions[2])
            print("[4]... " + distoptions[3])
            
        distselect = input()

        if distselect == "1":
            distselection = distoptions[0]
        elif distselect == "2":
            distselection = distoptions[1]
        elif distselect == "3":
            distselection = distoptions[2]
        elif distselect == "4":
            distselection = distoptions[3]
        else:
            print("Invalid entry.")
            time.sleep(3)
            return

        if distselection == "5f":
            distance = 5.0
            racesurface = 1
        elif distselection == "5.5f":
            distance = 5.5
            racesurface = 1
        elif distselection == "6f":
            distance = 6.0
            racesurface = 1
        elif distselection == "6.5f":
            distance = 6.5
            racesurface = 1
        elif distselection == "7f":
            distance = 7.0
            racesurface = 1
        elif distselection == "7.5f":
            distance = 7.5
            racesurface = 1
        elif distselection == "8f":
            distance = 8.0
            racesurface = 1
        elif distselection == "8.5f":
            distance = 8.5
            racesurface = 1
        elif distselection == "9f":
            distance = 9.0
            racesurface = 1
        elif distselection == "9.5f":
            distance = 9.5
            racesurface = 1
        elif distselection == "10f":
            distance = 10.0
            racesurface = 1
        elif distselection == "10.5f":
            distance = 10.5
            racesurface = 1
        elif distselection == "11f":
            distance = 11.0
            racesurface = 1
        elif distselection == "11.5f":
            distance = 11.5
            racesurface = 1
        elif distselection == "12f":
            distance = 12.0
            racesurface = 1
        elif distselection == "5f(T)":
            distance = 5.0
            racesurface = 2
        elif distselection == "5.5f(T)":
            distance = 5.5
            racesurface = 2
        elif distselection == "6f(T)":
            distance = 6.0
            racesurface = 2
        elif distselection == "6.5f(T)":
            distance = 6.5
            racesurface = 2
        elif distselection == "7f(T)":
            distance = 7.0
            racesurface = 2
        elif distselection == "7.5f(T)":
            distance = 7.5
            racesurface = 2
        elif distselection == "8f(T)":
            distance = 8.0
            racesurface = 2
        elif distselection == "8.5f(T)":
            distance = 8.5
            racesurface = 2
        elif distselection == "9f(T)":
            distance = 9.0
            racesurface = 2
        elif distselection == "9.5f(T)":
            distance = 9.5
            racesurface = 2
        elif distselection == "10f(T)":
            distance = 10.0
            racesurface = 2
        elif distselection == "10.5f(T)":
            distance = 10.5
            racesurface = 2
        elif distselection == "11f(T)":
            distance = 11.0
            racesurface = 2
        elif distselection == "11.5f(T)":
            distance = 11.5
            racesurface = 2
        elif distselection == "12f(T)":
            distance = 12.0
            racesurface = 2
        elif distselection == "5f(A)":
            distance = 5.0
            racesurface = 3
        elif distselection == "5.5f(A)":
            distance = 5.5
            racesurface = 3
        elif distselection == "6f(A)":
            distance = 6.0
            racesurface = 3
        elif distselection == "6.5f(A)":
            distance = 6.5
            racesurface = 3
        elif distselection == "7f(A)":
            distance = 7.0
            racesurface = 3
        elif distselection == "7.5f(A)":
            distance = 7.5
            racesurface = 3
        elif distselection == "8f(A)":
            distance = 8.0
            racesurface = 3
        elif distselection == "8.5f(A)":
            distance = 8.5
            racesurface = 3
        elif distselection == "9f(A)":
            distance = 9.0
            racesurface = 3
        elif distselection == "9.5f(A)":
            distance = 9.5
            racesurface = 3
        elif distselection == "10f(A)":
            distance = 10.0
            racesurface = 3
        elif distselection == "10.5f(A)":
            distance = 10.5
            racesurface = 3
        elif distselection == "11f(A)":
            distance = 11.0
            racesurface = 3
        elif distselection == "11.5f(A)":
            distance = 11.5
            racesurface = 3
        elif distselection == "12f(A)":
            distance = 12.0
            racesurface = 3
        print("")
        print("")
        racedist = int(2 * distance)
            
    if pick == 6:
        print("Enter the distance in furlongs")
        try:
            distance = float(input())
        except ValueError:
            print("")
            print("You have made an incorrect entry. Please try again.")
            time.sleep(3)
            return
        racedist = int(2 * distance)
            
        print("")
        print("Select surface")
        print("[1]... Dirt")
        print("[2]... Turf")
        print("[3]... Synthetic")
        racesurface = int(input())
        if racesurface != 1 and racesurface != 2 and racesurface != 3:
            print("Invalid entry.")
            time.sleep(1)
            print("")
            print("")
            return
        print("")
    
        if grade == 0:
            fee = 200
        elif grade == 1 and racepurse <= 500000:
            fee = 3500
        elif grade == 1 and racepurse <= 1000000:
            fee = 5000
        elif grade == 1 and racepurse <= 2000000:
            fee = 10000
        elif grade == 1 and racepurse <= 5000000:
            fee = 20000
        elif grade == 1 and racepurse > 5000000:
            fee = 50000
        elif grade == 2:
            fee = 2500
        elif grade == 3:
            fee = 1000
        print("")
        print("There will be a $" + str(fee) + " fee for entering this stakes race. It will be deducted from your balance.")
        print("Would you still like to enter the stakes?")
        print("[1]... Yes")
        print("[2]... No")
        choice7 = input()
        if choice7 == "1":
            bal = bal - fee
            print("")
        else:
            print("")
            return
            
    if racesurface == 1:
        racesurfacee = "Dirt"
    elif racesurface == 2:
        racesurfacee = "Turf"
    elif racesurface == 3:
        racesurfacee = "Synthetic"
    
    if racetype != "Stakes":
        raceday = random.randint(1,4) + day
        racemonth = month
        raceyear = year
        if raceday > 31:
            raceday = raceday - 31
            racemonth = month + 1
            if racemonth > 12:
                raceyear = year + 1
                racemonth = racemonth - 12
                horse1age = horse1age + 1
                if horse1age == 3:
                    horse1speed = horse1speed + random.randint(2, 6)
                elif horse1age == 4:
                    horse1speed = horse1speed + random.randint(1, 4)
                elif horse1age > 4:
                    horse1speed = horse1speed - random.randint(0, 4)
                    horse1stam = horse1stam - 1
    racedate = str(racemonth) + "/" + str(raceday) + "/" + str(raceyear)
    newmonth = racemonth
    newday = raceday
    newyear = raceyear
    
    print(racedate)
    print(racetrack + " Race #" + str(racenum))
    print(race + " Purse $" + str(racepurse))
    print(str(distance) + " furlongs " + racesurfacee)
    print("")
    print("")
    time.sleep(1)
    print("Would you like to enter this race?")
    print("[1]... Yes")
    print("[2]... No")
    choice = input()
    print("")
    if choice == "2":
        return
    
    print("")
    time.sleep(1)
    print("")
    
    if racetrack == "Santa Anita Park" or racetrack == "Santa Anita" or racetrack == "Golden Gate" or racetrack == "Golden Gate Fields" :
        fieldsize = random.randint(6, 10)
    elif racetrack == "Los Alamitos" or racetrack == "Turf Paradise" or racetrack == "Arizona Downs" or racetrack == "Pleasanton" or racetrack == "Sacramento" or racetrack == "Ferndale" or racetrack == "Remington Park" or racetrack == "Los Alamitos Race Course" or racetrack == "Santa Rosa" or racetrack == "Arizona Downs" or racetrack == "Turf Paradise" or racetrack == "Remington":
        fieldsize = random.randint(6, 9)
    elif racetrack == "Del Mar" or racetrack == "Las Vegas Race Course" or racetrack == "Oaklawn Park" or racetrack == "Oaklawn":
        fieldsize = random.randint(8, 13)
    else:
        fieldsize = random.randint(8, 13)
    if race == "Grade 1 Kentucky Derby":
        fieldsize = 20
    field = float(fieldsize)
    competition = (field - 6) / 3
    speed = int(horse1speed - competition)
    difference = int(speed - racerating)
    
    
    print("")
    print("The race at " + racetrack + " is ready to go!")
    print("There are " + str(fieldsize) + " horses in this race.")
    print("")
    time.sleep(2)
    print("Would you like to bet on your horse?")
    h1dif = horse1speed - racerating
    
    if h1dif > 3:
        oddscalc = random.randint(1,3)
    elif h1dif > 2:
        oddscalc = random.randint(2,5)
    elif h1dif > 1:
        oddscalc = random.randint(3,6)
    elif h1dif > 0:
        oddscalc = random.randint(3,6)
    elif h1dif > -1:
        oddscalc = random.randint(4,9)
    elif h1dif > -2:
        oddscalc = random.randint(5,10)
    elif h1dif > -3:
        oddscalc = random.randint(6,15)
    elif h1dif > -4:
        oddscalc = random.randint(6,15)
    elif h1dif > -5:
        oddscalc = random.randint(7,20)
    elif h1dif > -6:
        oddscalc = random.randint(7,20)
    else:
        oddscalc = random.randint(8,30)
    
    if horse1races == 0:
        oddscalc = random.randint(3,15)
    print("Odds: " + str(oddscalc) + "/1")
    print("[1]... Yes")
    print("[2]... No")
    choice8 = input()
    if choice8 == "1":
        betloop = 1
        while betloop == 1:
            print("Enter the amount you would like to bet")
            try:
                choice9 = int(input())
                maxbet = int(racepurse/10)
                if choice9 > maxbet:
                    print("You have exceeded the maximum bet. The maximum bet for this race is $" + str(maxbet) + ".")
                    continue
                if choice9 > bal:
                    print("You can not bet more than you have.")
                    continue
                betloop = 2
            except ValueError:
                print("Invalid entry. Please enter a number.")
                continue
    print("")
    print("When the race ends, close the race viewer window. Do not close the window until all horses have finished the race.")
    time.sleep(4)
    if circuitselect != circuitnum and (circuitselect == "1" or circuitselect == "4"):
        bal = bal - 1000
    elif circuitselect != circuitnum and (circuitselect == "2" or circuitselect == "3"):
        bal = bal - 500
    
    if horseinjury == 1:
        uhoh = random.randint(1, 3)
        if uhoh == 1:
            print("Oh no. Your horse was injured during the race and requires more than two years off before the possibility of running again. " + horse1 + "'s career is over :( ")
            time.sleep(5)
            resethorse()
            return
           
    horse1races = horse1races + 1
    
    horse1speed = float(horse1speed)
    racerating = float(racerating)
    
    pp = random.randint(1,fieldsize)
    
    roundspeed = int(racerating-horse1speed)
    
    userspeed = horse1speed
    
    userspeed = float(userspeed)
    
    distdiff = horse1stam - racedist
    if distdiff > 3 or distdiff < -3:
        userspeed -= abs(distdiff)
    
    if racesurface != horse1surface:
        userspeed -= 5
    if racesurface == 3 or horse1surface == 3:
        userspeed += 5
        
    userdif = userspeed - racerating
    

    window = tk.Tk()
    canvas_width = 1500
    canvas_height = 500
    if racesurface == 1:
        canvas = tk.Canvas(window,width=canvas_width,height=canvas_height,bg='#C4A484')
    elif racesurface == 2:
        canvas = tk.Canvas(window,width=canvas_width,height=canvas_height,bg='#348C31')
    elif racesurface == 3:
        canvas = tk.Canvas(window,width=canvas_width,height=canvas_height,bg='#454545')
    else:
        return
    canvas.pack()
    headertext = tk.Label(window,anchor='ne',text=str(newmonth) + "/" + str(newday) + "/" + str(newyear) + " | " + racetrack + " Race #" + str(racenum) + " | " + race,font=("Arial Bold",17))
    headertext.pack()

    horse_width = 50
    horse_height = 50
    horse_positions = [0] * fieldsize
    x1 = [0] * fieldsize
    x2 = [0] * fieldsize
    x3 = [0] * fieldsize
    horse_images = []
    horse_speeds = []
    for i in range(fieldsize):
        horse_image = tk.PhotoImage(file="horse.png")
        horse_images.append(horse_image)
        x1[i] = random.randint(250,500)
        x2[i] = random.randint(600,850)
        x3[i] = random.randint(950,1200)
 
    horse_speeds = [random.uniform(0.06,0.085) for i in range(fieldsize)]
    userspd = (userdif / 500) + 0.078
    if userspd < 0.06:
        userspd = 0.06
    if userspd > 0.093:
        userspd = 0.093
    horse_speeds[pp-1] = random.uniform(userspd-0.005,userspd+0.005)
    
    horse_image = tk.PhotoImage(file="horse1.png")
    horse_images[pp-1] = horse_image
    
    horse_ids = []
    for i in range(fieldsize):
        x = 0
        y = i * (canvas_height - horse_height) / (fieldsize - 1)
        horse_id = canvas.create_image(x, y, anchor="nw", image=horse_images[i])
        horse_ids.append(horse_id)

    finish_line_x = canvas_width - 50
    finish_line_y1 = 0
    finish_line_y2 = canvas_height
    canvas.create_line(finish_line_x, finish_line_y1, finish_line_x, finish_line_y2, width=2)
    
    you_label = tk.Label(window, text=f"Your horse is #{pp}")
    you_label.pack()
    race_button = tk.Button(window, text="Race!")
    race_button.pack()
    
    def race2d():
        race_button.config(state="disabled")  # disable button during race
        finished = []
        winner = None
        second = None
        third = None
        fourth = None
        fifth = None
        sixth = None
        seventh = None
        eighth = None
        ninth = None
        tenth = None
        eleventh = None
        twelfth = None
        thirt = None
        fourt = None
        fift = None
        sixt = None
        sevent = None
        eightt = None
        ninet = None
        twenty = None
        global result
        global you_label
        a = 0
        while len(finished) < fieldsize:
            for i in range(fieldsize):
                if i not in finished:
                    if horse_positions[i] > x1[i] and a == 0:
                        horse_speeds[i] = random.uniform(horse_speeds[i]-.015,horse_speeds[i]+.015)
                        if pp == i+1:
                            horse_speeds[i] = random.uniform(userspd-0.015,userspd+0.015)
                        a = 1
                    if horse_positions[i] > x2[i] and a == 1:
                        horse_speeds[i] = random.uniform(horse_speeds[i]-.015,horse_speeds[i]+.015)
                        if pp == i+1:
                            horse_speeds[i] = random.uniform(userspd-0.015,userspd+0.015)
                        a = 2
                    if horse_positions[i] > x3[i] and a == 2:
                        horse_speeds[i] = random.uniform(horse_speeds[i]-.025,horse_speeds[i]+.025)
                        if pp == i+1:
                            horse_speeds[i] = random.uniform(userspd-0.025,userspd+0.025)
                        a = 3
                    horse_positions[i] += horse_speeds[i]
                    canvas.move(horse_ids[i], horse_speeds[i], 0)
                    if horse_positions[i] + 66 > finish_line_x:
                        horse_positions[i] = finish_line_x
                        finished.append(i)
                        if winner is None:
                            winner = i+1
                            if winner == pp:
                                result = 1
                        elif second is None:
                            second = i+1
                            if second == pp:
                                result = 2
                        elif third is None:
                            third = i+1
                            if third == pp:
                                result = 3
                        elif fourth is None:
                            fourth = i+1
                            if fourth == pp:
                                result = 4
                        elif fifth is None:
                            fifth = i+1
                            if fifth == pp:
                                result = 5
                        elif sixth is None:
                            sixth = i+1
                            if sixth == pp:
                                result = 6
                        elif seventh is None:
                            seventh = i+1
                            if seventh == pp:
                                result = 7
                        elif eighth is None:
                            eighth = i+1
                            if eighth == pp:
                                result = 8
                        elif ninth is None:
                            ninth = i+1
                            if ninth == pp:
                                result = 9
                        elif tenth is None:
                            tenth = i+1
                            if tenth == pp:
                                result = 10
                        elif eleventh is None:
                            eleventh = i+1
                            if eleventh == pp:
                                result = 11
                        elif twelfth is None:
                            twelfth = i+1
                            if twelfth == pp:
                                result = 12
                        elif thirt is None:
                            thirt = i+1
                            if thirt == pp:
                                result = 13
                        elif fourt is None:
                            fourt = i+1
                            if fourt == pp:
                                result = 14
                        elif fift is None:
                            fift = i+1
                            if fift == pp:
                                result = 15
                        elif sixt is None:
                            sixt = i+1
                            if sixt == pp:
                                result = 16
                        elif sevent is None:
                            sevent = i+1
                            if sevent == pp:
                                result = 17
                        elif eightt is None:
                            eightt = i+1
                            if eightt == pp:
                                result = 18
                        elif ninet is None:
                            ninet = i+1
                            if ninet == pp:
                                result = 19
                        elif twenty is None:
                            twenty = i+1
                            if twenty == pp:
                                result = 20
                        
            canvas.update()
        race_button.destroy()
        winner_label = tk.Label(window, text=f"#{winner} wins!")
        second_label = tk.Label(window, text=f"#{second} was second.")
        third_label = tk.Label(window, text=f"#{third} was third.")
        fourth_label = tk.Label(window, text=f"#{fourth} was fourth.")
        fifth_label = tk.Label(window, text=f"#{fifth} was fifth.")
        
        winner_label.pack()
        second_label.pack()
        third_label.pack()
        fourth_label.pack()
        fifth_label.pack()
        
        if result > 5:
            poorfinish_label = tk.Label(window, text=f"You finished {result}th.")
            poorfinish_label.pack()
        
        
    race_button.config(command=race2d)

    window.mainloop()


 
    
    
    if newmonth - month > 0:
        bal = bal - (monthlyfee * (newmonth - month))
        if loan > 0:
            bal = bal - monthlypayment
            loan = loan - 1
    if newyear - year > 0:
        bal = bal - monthlyfee
        if loan > 0:
            bal = bal - monthlypayment
            loan = loan - 1
        horse1age = horse1age + 1
        if horse1age == 3:
            horse1speed = horse1speed + random.randint(1, 6)
        elif horse1age == 4:
            horse1speed = horse1speed + random.randint(1, 4)
        elif horse1age > 5:
            horse1speed = horse1speed - 5
            horse1stam = horse1stam - 3
        if horse1age == 4 and horse1sex == "Colt":
            horse1sex = "Horse"
        elif horse1age == 4 and horse1sex == "Filly":
            horse1sex = "Mare"
        if foalage >= 0:
            foalage = foalage + 1
            if foalage == 1:
                print("")
                print("Your foal is now 1 year old. Would you like to sell them?")
                print("[1]... Yes")
                print("[2]... No")
                choice15 = input()
                if choice15 == "1":
                    print("")
                    foalsale = studfee * (random.randint(7,20) / 10)
                    if foalspeed <= 10 and studfee >= 50000:
                        foalsale = 20000
                    print("Your foal sold for $" + str(foalsale))
                    bal = bal + foalsale
                    foalage = -1000
            elif foalage == 2:
                print("")
                print("Your foal is now 2 years old. You must either sell your horse now or retire your current horse, if you have one, to make way for this new horse.")
                print("[1]... Retire current horse/Keep 2yo")
                print("[2]... Sell 2yo")
                choice16 = input()
                if choice16 == "1":
                    resethorse()
                    print("")
                    horse1age = 2
                    horse1speed = foalspeed
                    horse1stam = foalstam
                    horse1sex = foalsex
                    horse1surface = random.randint(1,3)
                    foalspeed = 0
                    foalstam = 0
                    foalsex = ""
                    foalage = -1000
                    print("Your horse is a " + horse1sex + ". What would you like to name your horse?")
                    horse1 = input()
                    print("")
                    print("The horse just got back to your trainer. Let's see what he thinks.")
                    print("")
                    time.sleep(2)
                    print("Trainer:")
                    if horse1speed < 15:
                        print("This horse does not seem to have much talent.")
                    elif horse1speed < 25:
                        print("This horse should win some races.")
                    else:
                        print("This horse has talent. Only time will tell!")
                elif choice16 == "2":
                    print("")
                    foalsale = studfee * (random.randint(7,20) / 10)
                    if foalspeed <= 10 and studfee >= 50000:
                        foalsale = 20000
                    print("Your foal sold for $" + str(foalsale))
                    bal = bal + foalsale
                    foalage = -1000
    month = newmonth
    year = newyear
    day = newday
    
    time.sleep(1)
    
    print(horse1 + " finished " + str(result) + " place in a field of " + str(fieldsize) + ".")
    
    if breakrest > 0:
        numskipbreak += 1
    
    if choice8 == "1" and result != 1:
        print("You lost $" + str(choice9) + " from betting on your horse.")
        bal -= choice9
    elif choice8 == "1" and result == 1:
        print("You won $" + str(choice9 * oddscalc) + " from betting on your horse!")
        bal += choice9 * oddscalc
        
    if distdiff > 3 or distdiff < -3 or (racesurface != horse1surface and racesurface != 3 and horse1surface != 3):
        print("")
        print("Your horse either did not like the distance or the surface of the race.")
    
#Southern California
    if racetrack == "Santa Anita" or racetrack == "Santa Anita Park":
        tr = "SA"
    elif racetrack == "Los Alamitos" or racetrack == "Los Alamitos Race Course":
        tr = "LRC"
    elif racetrack == "Del Mar":
        tr = "DMR"
#Northern California
    elif racetrack == "Golden Gate" or racetrack == "Golden Gate Fields":
        tr = "GGF"
    elif racetrack == "Ferndale":
        tr = "FER"
    elif racetrack == "Sacramento":
        tr = "SAC"
    elif racetrack == "Santa Rosa":
        tr = "SR"
    elif racetrack == "Pleasanton":
        tr = "PLN"
#Las Vegas
    elif racetrack == "Las Vegas" or racetrack == "Las Vegas Race Course":
        tr = "LV"
#Oaklawn & Arkansas
    elif racetrack == "Oaklawn" or racetrack == "Oaklawn Park":
        tr = "OP"
    elif racetrack == "Remington Park":
        tr = "RP"
#Arizona
    elif racetrack == "Turf Paradise":
        tr = "TUP"
    elif racetrack == "Arizona Downs":
        tr = "AZD"
#International
    elif racetrack == "Gulfstream Park" or racetrack == "Gulfstream":
        tr = "GP"
    elif racetrack == "Churchill Downs" or racetrack == "Churchill":
        tr = "CD"
    elif racetrack == "Aqueduct":
        tr = "AQU"
    elif racetrack == "Belmont Park" or racetrack == "Belmont":
        tr = "BEL"
    elif racetrack == "Saratoga":
        tr = "SAR"
    elif racetrack == "Keeneland":
        tr = "KEE"
    elif racetrack == "Woodbine":
        tr = "WO"
    elif racetrack == "Turfway" or racetrack == "Turfway Park":
        tr = "TP"
    elif racetrack == "Pimlico":
        tr = "PIM"
    elif racetrack == "Monmouth Park" or racetrack == "Monmouth":
        tr = "MTH"
    else:
        tr = "XX"
    print("")
    print("")
    
    
    raceform = str(month) + "/" + str(day) + "/" + str(year) + tr + str(racenum) + " " + str(distance) + "f " + race + "  " + str(result) + "  " + str(oddscalc) + ".00  " + "PP" + str(pp) + "/" + str(fieldsize)
    if racesurface == 2:
        raceform = str(month) + "/" + str(day) + "/" + str(year) + tr + str(racenum) + " T" + str(distance) + "f " + race + "  " + str(result) + "  " + str(oddscalc) + ".00  " + "PP" + str(pp) + "/" + str(fieldsize)
    if racesurface == 3:
        raceform = str(month) + "/" + str(day) + "/" + str(year) + tr + str(racenum) + " A" + str(distance) + "f " + race + "  " + str(result) + "  " + str(oddscalc) + ".00  " + "PP" + str(pp) + "/" + str(fieldsize)
    print("")
    
    if raceform1 == 0:
        raceform1 = raceform
    elif raceform2 == 0:
        raceform2 = raceform
    elif raceform3 == 0:
        raceform3 = raceform
    elif raceform4 == 0:
        raceform4 = raceform
    elif raceform5 == 0:
        raceform5 = raceform
    elif raceform6 == 0:
        raceform6 = raceform
    elif raceform7 == 0:
        raceform7 = raceform
    elif raceform8 == 0:
        raceform8 = raceform
    elif raceform9 == 0:
        raceform9 = raceform
    elif raceform10 == 0:
        raceform10 = raceform
    elif raceform11 == 0:
        raceform11 = raceform
    elif raceform12 == 0:
        raceform12 = raceform
    elif raceform13 == 0:
        raceform13 = raceform
    elif raceform14 == 0:
        raceform14 = raceform
    elif raceform15 == 0:
        raceform15 = raceform
    elif raceform16 == 0:
        raceform16 = raceform
    elif raceform17 == 0:
        raceform17 = raceform
    elif raceform18 == 0:
        raceform18 = raceform
    elif raceform19 == 0:
        raceform19 = raceform
    elif raceform20 == 0:
        raceform20 = raceform
    elif raceform21 == 0:
        raceform21 = raceform
    elif raceform22 == 0:
        raceform22 = raceform
    elif raceform23 == 0:
        raceform23 = raceform
    elif raceform24 == 0:
        raceform24 = raceform
    elif raceform25 == 0:
        raceform25 = raceform
    elif raceform26 == 0:
        raceform26 = raceform
    elif raceform27 == 0:
        raceform27 = raceform
    elif raceform28 == 0:
        raceform28 = raceform
    elif raceform29 == 0:
        raceform29 = raceform
    
    horseinjury = random.randint(1, 12)
    if horseinjury == 1:
        global timeoff
        timeoff = random.randint(2, 6)
        time.sleep(2)
        print("Oh no! Upon returning to the stable, your trainer noticed that " + horse1 + " was injured!")
        print(horse1 + " will need " + str(timeoff) + " months off.")
        surgery = random.randint(1, 3)
        if surgery == 1:
            surgerycost = random.randint(1, 10)
            surgerycost = surgerycost * 1000
            print(horse1 + " will need surgery. It will cost $" + str(surgerycost) + ".")
            time.sleep(1)
            bal = bal - surgerycost
    else:
        horseinjury = 0
    
    if raceclaim != 0 and userdif > 0:
        print("")
        time.sleep(1)
        if h1dif > 5:
            chance = 50
        elif h1dif > 0:
            chance = 20
        else:
            chance = 10
        claimchance = chance - 10
        cla1 = random.choices([1, 2], weights=[claimchance, (100 - claimchance)], k=(1))
        if cla1 == [1]:
            print("Shoot! " + horse1 + " was claimed!")
            if horseinjury == 1 and surgery == 1:
                print("You will be refunded for the surgery.")
                bal = bal + surgerycost
            print("You earned $" + str(raceclaim) + " for your horse being claimed.")
            print("")
            time.sleep(1)
            print("Here are the final PPs for your horse.")
            print("")
            if raceform1 != 0:
                print(str(raceform1))
            if raceform2 != 0:
                print(str(raceform2))
            if raceform3 != 0:
                print(str(raceform3))
            if raceform4 != 0:
                print(str(raceform4))
            if raceform5 != 0:
                print(str(raceform5))
            if raceform6 != 0:
                print(str(raceform6))
            if raceform7 != 0:
                print(str(raceform7))
            if raceform8 != 0:
                print(str(raceform8))
            if raceform9 != 0:
                print(str(raceform9))
            if raceform10 != 0:
                print(str(raceform10))
            if raceform11 != 0:
                print(str(raceform11))
            if raceform12 != 0:
                print(str(raceform12))
            if raceform13 != 0:
                print(str(raceform13))
            if raceform14 != 0:
                print(str(raceform14))
            if raceform15 != 0:
                print(str(raceform15))
            if raceform16 != 0:
                print(str(raceform16))
            if raceform17 != 0:
                print(str(raceform17))
            if raceform18 != 0:
                print(str(raceform18))
            if raceform19 != 0:
                print(str(raceform19))
            if raceform20 != 0:
                print(str(raceform20))
            if raceform21 != 0:
                print(str(raceform21))
            if raceform22 != 0:
                print(str(raceform22))
            if raceform23 != 0:
                print(str(raceform23))
            if raceform24 != 0:
                print(str(raceform24))
            if raceform25 != 0:
                print(str(raceform25))
            if raceform26 != 0:
                print(str(raceform26))
            if raceform27 != 0:
                print(str(raceform27))
            if raceform28 != 0:
                print(str(raceform28))
            if raceform29 != 0:
                print(str(raceform29))
            if raceform30 != 0:
                print(str(raceform30))
            print("")
            print("")
            time.sleep(1)
            bal = bal + raceclaim
            
        elif cla1 == [2]:
            print(horse1 + " was not claimed.")
            print("")
            time.sleep(1)
    elif raceclaim != 0 and difference <= 0:
        print("")
        time.sleep(1)
        print(horse1 + " was not claimed.")
        print("")
    
    time.sleep(1)
    print("")
    racepurs = float(racepurse)
    if result == 1:
        mult = 0.6
        horse1wins += 1
    elif result == 2:
        mult = 0.2
        horse1seconds += 1
    elif result == 3:
        mult = 0.11
        horse1thirds += 1
    elif result == 4:
        mult = 0.06
    elif result == 5:
        mult = 0.03
    else:
        mult = 0
    mul = float(mult)
    pursewinnings = int((racepurs * mul) * 0.8)
    if mult > 0:
        print("Congratulations, you won $" + str(pursewinnings) + " in purse winnings.")
    print("")
    
    earnings = racepurse * mult
    horse1earnings = horse1earnings + earnings
    
    bal = bal + pursewinnings
    
    time.sleep(2)
    
    if horse1 != "":
        print("This is the updated record for " + horse1 + ".")
        horse1record = str(horse1races) + ": " + str(horse1wins) + "-" + str(horse1seconds) + "-" + str(horse1thirds)
        print(horse1record)
    print("")
           
    print("You will now advance to the day after the race.")
    time.sleep(2)
    day = day + 1
    if day == 32:
        day = 1
        month = month + 1
        bal = bal - monthlyfee
        if loan > 0:
            bal = bal - monthlypayment
            loan = loan - 1
    
    if month == 13:
        numskipbreak = 0
        year = year + 1
        month = 1
        horse1age = horse1age + 1
        if horse1age == 3:
            horse1speed = horse1speed + random.randint(2, 6)
        elif horse1age == 4:
            horse1speed = horse1speed + random.randint(1, 4)
        elif horse1age > 4:
            horse1speed = horse1speed - random.randint(2, 5)
            horse1stam = horse1stam - 3
        if horse1age == 4 and horse1sex == "Colt":
            horse1sex = "Horse"
        elif horse1age == 4 and horse1sex == "Filly":
            horse1sex = "Mare"
        
    if raceclaim != 0 and userdif > 0:
        if cla1 == [1]:
            resethorse()
    
    breakrest = 1

def bank():
    global loan
    global bal
    print("")
    if loan > 0:
        print("You already have a loan out. You may not take out another until the current one is paid out fully.")
        time.sleep(3)
        return
    print("Would you like to take out a loan?")
    print("[1]... Yes")
    print("[2]... No")
    choice4 = input()
    if choice4 == "1":
        maxloan = bal * 2
        if maxloan < 50000:
            maxloan = 50000
        print("")
        print("How much would you like to loan? The maximum amount you can loan is $" + str(maxloan) + ".")
        loanamount = input()
        loanamount = int(loanamount)
        if loanamount > maxloan:
            print("You can not loan that much")
            return
        print("")
        fullloan = loanamount * 1.2
        global monthlypayment
        monthlypayment = fullloan / 24
        print("In order to take out a loan of $" + str(loanamount) + ", you will need to pay $" + str(monthlypayment) + " for 2 years.")
        print("Would you like to takeout this loan?")
        print("[1]... Yes")
        print("[2]... No")
        choice5 = input()
        if choice5 == "1":
            time.sleep(1)
            loan = 24
            print("Loan complete.")
            bal = bal + loanamount
            time.sleep(4)
        elif choice5 == "2":
            return
    elif choice4 == "2":
        return

def breeding():
    global day
    global bal
    global mare1
    global mare1speed
    global mare1stam
    global foalage
    global foalsex
    global foalspeed
    global foalstam
    global studfee
    global loan
    global breedingfarm
    print("")
    time.sleep(1)
    print("")
    
    if foalage > 0:
        print("You already have a foal.")
        time.sleep(4)
        return
    
    if breedingfarm == 0:
        print("You currently do not own a farm.")
        print("It costs $100,000 to rent a spot on a farm to have a mare.")
        print("Would you like to purchase a farm spot?")
        print("[1]... Yes")
        print("[2]... No")
        choice10 = input()
        if choice10 == "1":
            if bal < 100000:
                print("You do not have enough money")
                time.sleep(2)
                return
            bal = bal - 100000
            breedingfarm = 1
            print("You can now own mares.")
        elif choice10 == "2":
            return
    print("Breeding Barn")
    print("")
    print("Current Mares:")
    print(mare1)
    print("")
    print("Would you like to breed your mare?")
    print("[1]... Yes")
    print("[2]... No")
    marechoice = input()
    print("")
    if marechoice == "1":
        print("Select a sire from the list")
        print("")
        print("Into Mischief - $250,000")
        print("Tapit - $185,000")
        print("Curlin - $175,000")
        print("Uncle Mo - $160,000")
        print("Quality Road - $150,000")
        print("Gun Runner - $125,000")
        print("Medaglia d'Oro - $100,000")
        print("War Front - $100,000")
        print("Speightstown - $90,000")
        print("Candy Ride - $75,000")
        print("Ghostzapper - $75,000")
        print("Street Sense - $75,000")
        print("Twirling Candy - $60,000")
        print("Nyquist - $55,000")
        print("More Than Ready - $50,000")
        print("Liam's Map - $40,000")
        print("Hard Spun - $35,000")
        print("Flatter - $35,000")
        print("Runhappy - $12,500")
        print("Paynter - $10,000")
        print("")
        print("There will be an additional $10,000 cost incurred for stabling of the mare and the foal.")
        print("")
        sirechoice = input()
        print("Are you sure you want to breed your mare " + mare1 + " to " + sirechoice + "?")
        print("[1]... Yes")
        print("[2]... No")
        choice12 = input()
        if choice12 != "1":
            return
        if sirechoice == "Into Mischief":
            studfee = 250000
            sire1speed = 60
            sire1stam = 14
        elif sirechoice == "Tapit":
            studfee = 185000
            sire1speed = 58
            sire1stam = 17
        elif sirechoice == "Curlin":
            studfee = 175000
            sire1speed = 57
            sire1stam = 17
        elif sirechoice == "Uncle Mo":
            studfee = 160000
            sire1speed = 57
            sire1stam = 16
        elif sirechoice == "Quality Road":
            studfee = 150000
            sire1speed = 56
            sire1stam = 16
        elif sirechoice == "Gun Runner":
            studfee = 125000
            sire1speed = 55
            sire1stam = 14
        elif sirechoice == "Medaglia d'Oro":
            studfee = 100000
            sire1speed = 54
            sire1stam = 17
        elif sirechoice == "War Front":
            studfee = 100000
            sire1speed = 54
            sire1stam = 16
        elif sirechoice == "Speightstown":
            studfee = 90000
            sire1speed = 54
            sire1stam = 15
        elif sirechoice == "Candy Ride":
            studfee = 75000
            sire1speed = 53
            sire1stam = 16
        elif sirechoice == "Ghostzapper":
            studfee = 75000
            sire1speed = 53
            sire1stam = 15
        elif sirechoice == "Street Sense":
            studfee = 75000
            sire1speed = 53
            sire1stam = 16
        elif sirechoice == "Twirling Candy":
            studfee = 60000
            sire1speed = 52
            sire1stam = 14
        elif sirechoice == "Nyquist":
            studfee = 55000
            sire1speed = 51
            sire1stam = 15
        elif sirechoice == "Liam's Map":
            studfee = 40000
            sire1speed = 50
            sire1stam = 15
        elif sirechoice == "Hard Spun":
            studfee = 35000
            sire1speed = 49
            sire1stam = 15
        elif sirechoice == "Flatter":
            studfee = 35000
            sire1speed = 48
            sire1stam = 15
        elif sirechoice == "Runhappy":
            studfee = 12500
            sire1speed = 46
            sire1stam = 14
        elif sirechoice == "Paynter":
            studfee = 10000
            sire1speed = 45
            sire1stam = 15
        print("")
        time.sleep(1)
        print("")
        
        bal = bal - studfee - 10000
        
        foalspeed = int((mare1speed + sire1speed + random.randint(5,65)) / 3)
        foalstam = int((mare1stam + sire1stam + random.randint(9,20)) / 3)
        if foalspeed < 5:
            foalspeed = 5
        if foalstam < 9 or foalstam > 20:
            foalstam = random.randint(9,20)
        foalage = 0
        s = random.randint(0,1)
        if s == 0:
            foalsex = "Colt"
        elif s == 1:
            foalsex = "Filly"
        
        time.sleep(4)
        print("Congratulations, you have a healthy foal!")
        print("The foal is currently zero years old.")
        print("You can choose to sell or race the foal. They must be at least 1 year old to sell, but you will not find out about the foal's potential until they turn two.")
        time.sleep(1)
        print("")

def sale():
    global bal
    global horse1
    global horse1speed
    global horse1stam
    global horse1surface
    global horse1age
    global horse1sex
    global horse1wins
    global horse1seconds
    global horse1thirds
    global horse1races
    global horse1record
    global foalage
    global horse1earnings
    global horseinjury
    global day
    global month
    global year
    global raceform1
    global raceform2
    global raceform3
    global raceform4
    global raceform5
    global raceform6
    global raceform7
    global raceform8
    global raceform9
    global raceform10
    global raceform11
    global raceform12
    global raceform13
    global raceform14
    global raceform15
    global raceform16
    global raceform17
    global raceform18
    global raceform19
    global raceform20
    global raceform21
    global raceform22
    global raceform23
    global raceform24
    global raceform25
    global raceform26
    global raceform27
    global raceform28
    global raceform29
    global raceform30
    loopthree = 1
    while loopthree == 1:
        print("")
        print("")
        print("Welcome to the sale. Here you can find your next thoroughbred champion")
        print("Please select your price range.")
        print("[1]... $20k - $50k")
        print("[2]... $50k - $100k")
        print("[3]... $100k - $200k")
        print("[4]... $200k - $500k")
        print("[5]... $500k - $1M")
        print("[6]... $1M - $3M")
        print("[7]... Exit sale")
        prange = input()
        if prange == "1":
            rawcost = random.randint(2,5)
            base = random.randint(0,45)
            chance = random.randint(5,100)
        elif prange == "2":
            rawcost = random.randint(5,10)
            base = random.randint(5,45)
            chance = random.randint(15,100)
        elif prange == "3":
            rawcost = random.randint(10,20)
            base = random.randint(10,45)
            chance = random.randint(25,100)
        elif prange == "4":
            rawcost = random.randint(20,50)
            base = random.randint(20,45)
            chance = random.randint(40,100)
        elif prange == "5":
            rawcost = random.randint(50,100)
            base = random.randint(30,45)
            chance = random.randint(55,110)
        elif prange == "6":
            rawcost = random.randint(100,300)
            base = random.randint(40,45)
            chance = random.randint(70,120)
        else:
            return
        chance = chance / 100
        horse1speed = int(base * chance)
        horse1stam = random.randint(9,20)
        horse1surface = random.randint(1,3)
        horse1age = 2
        horse1earnings = 0
        if horse1speed < 7:
            horse1speed = 7
        if horse1speed < 10:
            horse1surface = 1
            if horse1stam > 18:
                horse1stam = 18
        cost = rawcost * 10000
        if cost <= 50000:
            sireopts = ["Paynter","Runhappy","Flatter","Hard Spun"]
        elif cost <= 100000:
            sireopts = ["Hard Spun","Liam's Map","Nyquist","Twirling Candy","Street Sense"]
        elif cost <= 200000:
            sireopts = ["Liam's Map","Nyquist","Twirling Candy","Street Sense","Ghostzapper","Candy Ride","Speightstown","War Front","Medaglia d'Oro"]
        elif cost <= 500000:
            sireopts = ["Nyquist","Street Sense","Ghostzapper","Candy Ride","War Front","Medaglia d'Oro","Gun Runner","Quality Road","Uncle Mo"]
        else:
            sireopts = ["Nyquist","Street Sense","Ghostzapper","Candy Ride","War Front","Medaglia d'Oro","Gun Runner","Quality Road","Uncle Mo","Curlin","Tapit","Into Mischief"]
        horse1sire = random.choice(sireopts)
        sexoptions = ["Colt","Filly"]
        horse1sex = random.choice(sexoptions)
        
        if horse1sire == "Hard Spun" and cost <= 50000:
            horse1speed += 1
        elif horse1sire == "Street Sense" and cost <= 100000:
            horse1speed += 1
        elif horse1sire == "Medaglia d'Oro" and cost <= 200000:
            horse1speed += 1
        elif horse1sire == "Uncle Mo" and cost <= 500000:
            horse1speed += 1
        elif horse1sire == "Into Mischief" and cost > 500000:
            horse1speed += 1
        
        time.sleep(2)
        print("")
        print("")
        print("There is a " + horse1sex + " in the sale by " + horse1sire + " that will go for $" + str(cost) + ". Would you like to purchase the horse?")
        print("[1]... Yes")
        print("[2]... No")
        print("[3]... Exit sale")
        pick = input()
        if pick == "2" or pick == "No":
            continue
        elif pick == "3":
            return
            
        bal = bal - cost
        if bal < 0:
            print("Buying this horse would put you in debt. You can not buy this horse.")
            time.sleep(3)
            bal = bal + cost
            continue
        loopthree = 0
        print("")
        print("Congratulations!")
        print("")
        time.sleep(1)
        print("What would you like to name your horse?")
        horse1 = input()
        time.sleep(1)
        print("The horse just got back to your trainer. Let's see what he thinks.")
        print("")
        time.sleep(2)
        if horse1speed < 15:
            print("Trainer: 'This horse is not much.'")
        elif horse1speed < 30:
            print("Trainer: 'This horse should win some races.'")
        else:
            print("This horse has talent. Only time will tell!")
        time.sleep(1)
        print("")
        print("")
        print("This two-year-old will need two months of preparation prior to racing.")
        time.sleep(2)
        global breakrest
        global numskipbreak
        breakrest = 1
        numskipbreak = 2
    
a = 1
while a == 1:
    if bal < 0:
        print("")
        print("")
        print("You have a negative balance. If your balance reaches -$5,000, the game will end.")
        time.sleep(2)
        if bal < -4999:
            print("You have less than -$5,000. The game is now over. You suck.")
            time.sleep(4)
            sys.exit()
    randomEvent = random.randint(1,20)
    if randomEvent == 1:
        if bal < 100000:
            goodOrBad = 1
        else:
            goodOrBad = random.randint(1,2)
    print("")
    print("")
    print("My Stable " + str(month) + "/" + str(day) + "/" + str(year))
    print("Balance: $" + str(bal))
    print("")
    if horse1 != "":
        print(horse1 + "   " + str(horse1age) + "yo " + horse1sex + " $" + str(horse1earnings))
    time.sleep(1)
    print("")
    print("Actions:")
    if horse1 != "":
        print("[1]... Enter race")
        if horseinjury == 1:
            print("[2]... Advance to end of injury")
        elif horse1age == 2 and horse1races == 0:
            print("[2]... Advance 2 months")
        elif horse1age == 2:
            print("[2]... Advance 5 weeks")
        elif horse1age == 3 and month < 6:
            print("[2]... Advance 4 weeks")
        elif horse1age == 3 and month >= 6:
            print("[2]... Advance 3 weeks")
        elif horse1age > 3 and horse1age < 15:
            print("[2]... Advance 3 weeks")
        print("[3]... Advance to date")
        print("[4]... View horse records")
        print("[5]... Retire horse")
        print("[6]... Bank")
        print("[7]... Sell horse")
        print("[8]... Change circuit")
        print("[9]... Save game")
        print("[10]... Load game")
        if mare1 != 0:
            print("[11]... Breeding Barn")
        choice = input()
        if choice == "1":
            if horseinjury == 1:
                print("This horse is injured and should NOT race.")
                print("Racing this horse could result in a career-ending injury.")
            if breakrest > 0:
                if numskipbreak >= 2:
                    print("")
                    print("Your horse is not ready to run. They must wait a few weeks in between races, and you have not met this time.")
                    print("")
                    time.sleep(2)
                    continue
            if horse1age == 2 and month < 5:
                print("Your two year old can not race yet. They must wait until May to race.")
                time.sleep(3)
                continue
            race()
        elif choice == "2":
            if horseinjury == 1:
                day = timeoff * 30 + day
                horseinjury = 0
            elif horse1age == 2 and horse1races == 0:
                day = day + 60
            elif horse1age == 2:
                day = day + 35
                if horseinjury == 1:
                        timeoff = timeoff - 1
                        if timeoff <= 1:
                            horseinjury = 0
            elif horse1age == 3 and month < 6:
                day = day + 28
                if horseinjury == 1:
                        timeoff = timeoff - 1
                        if timeoff <= 1:
                            horseinjury = 0
            elif horse1age == 3 and month >= 6:
                day = day + 21
                if horseinjury == 1:
                        timeoff = timeoff - 1
                        if timeoff <= 1:
                            horseinjury = 0
            elif horse1age > 3 and horse1age < 15:
                day = day + 21
                if horseinjury >= 1:
                        timeoff = timeoff - 1
                        if timeoff <= 1:
                            horseinjury = 0
            if day > 31:
                month = month + 1
                day = day - 31
                bal = bal - monthlyfee
                if day > 31:
                    month = month + 1
                    day = day - 31
                    bal = bal - monthlyfee
                    if day > 31:
                        month = month + 1
                        day = day - 31
                        bal = bal - monthlyfee
                        if day > 31:
                            month = month + 1
                            day = day - 31
                            bal = bal - monthlyfee
                            if day > 31:
                                month = month + 1
                                day = day - 31
                                bal = bal - monthlyfee
                                if day > 31:
                                    month = month + 1
                                    day = day - 31
                                    bal = bal - monthlyfee
                if loan > 0:
                    bal = bal - monthlypayment
                    loan = loan - 1
            if month > 12:
                numskipbreak = 0
                year = year + 1
                month = month - 12
                horse1age = horse1age + 1
                if horse1age == 3:
                    horse1speed = horse1speed + random.randint(2, 6)
                elif horse1age == 4:
                    horse1speed = horse1speed + random.randint(1, 4)
                elif horse1age > 4:
                    horse1speed = horse1speed - random.randint(0, 4)
                    horse1stam = horse1stam - 1
                if horse1age == 5 and horse1sex == "Colt":
                    horse1sex = "Horse"
                elif horse1age == 5 and horse1sex == "Filly":
                    horse1sex = "Mare"
            breakrest = 0
                
        elif choice == "3":
            print("Enter the date you would like to advance to.")
            try:
                newday = int(input("Day of the month: "))
            except ValueError:
                print("Invalid entry.")
                time.sleep(3)
                continue
            try:
                newmonth = int(input("Month number: "))
            except ValueError:
                print("Invalid entry.")
                time.sleep(3)
                continue
            try:
                newyear = int(input("Year: "))
            except ValueError:
                print("Invalid entry.")
                time.sleep(3)
                continue
            
            monthdif = newmonth - month
            daydif = newday - day
            yeardif = newyear - year
            if yeardif >= 1:
                days = (monthdif*30)+(yeardif*360)+daydif
            elif monthdif >= 1:
                days = daydif+(monthdif*30)
            else:
                days = daydif
            breakweeks = float(days/7)
            
            if horse1age == 2 and horse1races == 0 and days >= 60:
                breakrest = 0
            elif horse1age == 2 and breakweeks >= 5:
                breakrest = 0
            elif horse1age == 3 and month < 6 and breakweeks >= 4:
                breakrest = 0
            elif horse1age == 3 and month >= 6 and breakweeks >= 3:
                breakrest = 0
            elif horse1age > 3 and horse1age < 15 and breakweeks >= 3:
                breakrest = 0
            
            if loan > 0:
                bal = bal - monthlypayment
                loan = loan - 1
            if newmonth - month >= 1:
                bal = bal - ((newmonth - month) * monthlyfee)
                if horseinjury == 1:
                    timeoff = timeoff - (newmonth - month)
                    if timeoff < 1:
                        horseinjury = 0
            if newyear - year >= 1:
                if horseinjury == 1:
                    injuremonth = newmonth + 12
                    timeoff = timeoff - (injuremonth - month)
                    if timeoff < 1:
                        horseinjury = 0
                monthsp = newmonth - month + 12
                bal = bal - (monthsp * monthlyfee)
                horse1age = horse1age + 1
                if horse1age == 3:
                    horse1speed = horse1speed + random.randint(1, 6)
                elif horse1age == 4:
                    horse1speed = horse1speed + random.randint(1, 4)
                elif horse1age > 5:
                    horse1speed = horse1speed - 5
                    horse1stam = horse1stam - 3
                if horse1age == 5 and horse1sex == "Colt":
                    horse1sex = "Horse"
                elif horse1age == 5 and horse1sex == "Filly":
                    horse1sex = "Mare"
                if 'foalage' in globals():
                    foalage = foalage + 1
                    if foalage == 1:
                        print("")
                        print("Your foal is now 1 year old. Would you like to sell them?")
                        print("[1]... Yes")
                        print("[2]... No")
                        choice15 = input()
                        if choice15 == "1":
                            print("")
                            foalsale = studfee * (random.randint(7,20) / 10)
                            if foalspeed <= 10 and studfee >= 50000:
                                foalsale = 20000
                            print("Your foal sold for $" + str(foalsale))
                            bal = bal + foalsale
                            foalage = -1000
                    elif foalage == 2:
                        print("")
                        print("Your foal is now 2 years old. You must either sell your horse now or retire your current horse, if you have one, to make way for this new horse.")
                        print("[1]... Retire current horse/Keep 2yo")
                        print("[2]... Sell 2yo")
                        choice16 = input()
                        if choice16 == "1":
                            resethorse()
                            print("")
                            horse1age = 2
                            horse1speed = foalspeed
                            horse1stam = foalstam
                            horse1sex = foalsex
                            horse1surface = random.randint(1,3)
                            foalspeed = 0
                            foalstam = 0
                            foalsex = ""
                            foalage = -1000
                            print("Your horse is a " + horse1sex + ". What would you like to name your horse?")
                            horse1 = input()
                            print("")
                            print("The horse just got back to your trainer. Let's see what he thinks.")
                            print("")
                            time.sleep(2)
                            print("Trainer:")
                            if horse1speed < 15:
                                print("This horse does not seem to have much talent.")
                            elif horse1speed < 25:
                                print("This horse should win some races.")
                            else:
                                print("This horse has talent. Only time will tell!")
                        elif choice16 == "2":
                            print("")
                            foalsale = studfee * (random.randint(7,20) / 10)
                            if foalspeed <= 10 and studfee >= 50000:
                                foalsale = 20000
                            print("Your foal sold for $" + str(foalsale))
                            bal = bal + foalsale
                            foalage = -1000
            elif newyear - year < 0:
                print("You can not travel back in time.")
                time.sleep(3)
                continue

            day = newday
            month = newmonth
            year = newyear
        elif choice == "4":
            print("")
            time.sleep(1)
            print(horse1 + "  " + str(horse1age) + "yo " + horse1sex + "  " + horse1record + " $" + str(horse1earnings))
            #print("Would you like to see the horse's hidden stats?")
            #print("[1]... Yes")
            #print("[2]... No")
            #choice9 = input()
            #if choice9 == "1":
                #print("")
                #print("Speed: " + str(horse1speed))
                #print("Stamina: " + str(horse1stam))
                #if horse1surface == 1:
                    #horse1surfacee = "Dirt"
                #elif horse1surface == 2:
                    #horse1surfacee = "Turf"
                #elif horse1surface == 3:
                    #horse1surfacee = "No preference"
                #print("Surface: " + horse1surfacee)
                #time.sleep(3)
            print("")
            print("")
            time.sleep(1)
            if raceform1 != 0:
                print(str(raceform1))
            if raceform2 != 0:
                print(str(raceform2))
            if raceform3 != 0:
                print(str(raceform3))
            if raceform4 != 0:
                print(str(raceform4))
            if raceform5 != 0:
                print(str(raceform5))
            if raceform6 != 0:
                print(str(raceform6))
            if raceform7 != 0:
                print(str(raceform7))
            if raceform8 != 0:
                print(str(raceform8))
            if raceform9 != 0:
                print(str(raceform9))
            if raceform10 != 0:
                print(str(raceform10))
            if raceform11 != 0:
                print(str(raceform11))
            if raceform12 != 0:
                print(str(raceform12))
            if raceform13 != 0:
                print(str(raceform13))
            if raceform14 != 0:
                print(str(raceform14))
            if raceform15 != 0:
                print(str(raceform15))
            if raceform16 != 0:
                print(str(raceform16))
            if raceform17 != 0:
                print(str(raceform17))
            if raceform18 != 0:
                print(str(raceform18))
            if raceform19 != 0:
                print(str(raceform19))
            if raceform20 != 0:
                print(str(raceform20))
            if raceform21 != 0:
                print(str(raceform21))
            if raceform22 != 0:
                print(str(raceform22))
            if raceform23 != 0:
                print(str(raceform23))
            if raceform24 != 0:
                print(str(raceform24))
            if raceform25 != 0:
                print(str(raceform25))
            if raceform26 != 0:
                print(str(raceform26))
            if raceform27 != 0:
                print(str(raceform27))
            if raceform28 != 0:
                print(str(raceform28))
            if raceform29 != 0:
                print(str(raceform29))
            if raceform30 != 0:
                print(str(raceform30))
            time.sleep(5)
            print("")
            print("")
            
        elif choice == "5":
            print("")
            time.sleep(1)
            print("Which horse would you like to retire? Please enter their name.")
            choice1 = input()
            if choice1 == horse1:
                print("")
                if horse1sex == "Filly" or horse1sex == "Mare":
                    print("Would you like to make your " + horse1sex + " a broodmare?")
                    print("[1]... Yes")
                    print("[2]... No")
                    choice3 = input()
                    if choice3 == "1":
                        horse1sex = "Mare"
                        mare1 = horse1
                        mare1speed = horse1speed
                        mare1stam = horse1stam
                        print("")
                        time.sleep(1)
                        print("Your horse is now a mare. You can breed to her once a year, however you may still only race one horse at a time.")
                    
                print("Ok. " + horse1 + " has been retired.")
                resethorse()
                time.sleep(3)
                print("")
        elif choice == "6":
            bank()
        elif choice == "7":
            print("")
            if horse1earnings < 200000:
                print("Your horse has not accomplished much. You can sell them privately for $10,000.")
                print("Would you like to sell your horse for $10,000?")
                print("[1]... Yes")
                print("[2]... No")
                choice11 = input()
                if choice11 == "1":
                    print("")
                    print("You have sold your horse.")
                    bal = bal + 10000
                    resethorse()
            elif horse1earnings < 1000000:
                print("Your horse is solid. You can sell them at a public auction. They will go for somewhere around what they earned in their career.")
                print("Would you like to do that?")
                print("[1]... Yes")
                print("[2]... No")
                choice11 = input()
                if choice11 == "1":
                    print("")
                    auctionsale = horse1earnings * (random.randint(85,115) / 100)
                    print("Your horse sold for $" + str(auctionsale) + ".")
                    bal = bal + auctionsale
                    print("")
                    time.sleep(3)
                    resethorse()
            else:
                print("You have quite the horse! You can sell them at public auction. They will go for somewhere around twice their career earnings.")
                print("Would you like to sell them?")
                print("[1]... Yes")
                print("[2]... No")
                choice11 = input()
                if choice11 == "1":
                    print("")
                    auctionsale = horse1earnings * (random.randint(150,250) / 100)
                    print("Your horse sold for $" + str(auctionsale) + ".")
                    bal = bal + auctionsale
                    print("")
                    time.sleep(3)
                    resethorse()
        elif choice == "8":
            print("")
            print("It will cost $5,000 to change your circuit. What would you like your new circuit to be?")
            print("[1]... Southern California (Santa Anita, Los Alamitos, & Del Mar)")
            print("[2]... Northern California (Golden Gate)")
            print("[3]... Arizona (Turf Paradise)")
            print("[4]... Cancel")
            circuitnum = input()
            if circuitnum == "1":
                circuit = "Southern California"
                bal = bal - 5000
            elif circuitnum == "2":
                circuit = "Northern California"
                bal = bal - 5000
            elif circuitnum == "3":
                circuit = "Arizona"
                bal = bal - 5000
            elif circuitnum == "4":
                continue
        elif choice == "11":
            breeding()
        elif choice == "9":
            with open('save.pkl', 'wb') as f:
                pickle.dump([b,bal,horse1,horse1speed,horse1stam,horse1surface,horse1age,horse1sex,horse1wins,horse1seconds,horse1thirds,horse1races,horse1record,horse1earnings,horseinjury,raceform1,raceform2,raceform3,raceform4,raceform5,raceform6,raceform7,raceform8,raceform9,raceform10,raceform11,raceform12,raceform13,raceform14,raceform15,raceform16,raceform17,raceform18,raceform19,raceform20,raceform21,raceform22,raceform23,raceform24,raceform25,raceform26,raceform27,raceform28,raceform29,raceform30,loan,day,month,year,breedingfarm,circuitnum,circuit,numskipbreak,breakrest,mare1,mare1speed,mare1stam,foalspeed,foalstam,foalage,foalsex,monthlypayment,timeoff], f)
                print("Save successful")
                time.sleep(3)
                sys.exit()
        elif choice == "10":
            with open('save.pkl', 'rb') as f:
                b,bal,horse1,horse1speed,horse1stam,horse1surface,horse1age,horse1sex,horse1wins,horse1seconds,horse1thirds,horse1races,horse1record,horse1earnings,horseinjury,raceform1,raceform2,raceform3,raceform4,raceform5,raceform6,raceform7,raceform8,raceform9,raceform10,raceform11,raceform12,raceform13,raceform14,raceform15,raceform16,raceform17,raceform18,raceform19,raceform20,raceform21,raceform22,raceform23,raceform24,raceform25,raceform26,raceform27,raceform28,raceform29,raceform30,loan,day,month,year,breedingfarm,circuitnum,circuit,numskipbreak,breakrest,mare1,mare1speed,mare1stam,foalspeed,foalstam,foalage,foalsex,monthlypayment,timeoff = pickle.load(f)
                print("")
                print("")
                time.sleep(1)
    else:
        print("[1]... Purchase horse")
        print("[2]... Advance to date")
        print("[3]... Bank")
        print("[4]... Save game")
        print("[5]... Load game")
        if mare1 != 0:
            print("[6]... Breeding Barn")
        choice = input()
        if choice == "1":
            print("")
            time.sleep(1)
            print("You have two options when purchasing a horse. You can claim a horse in a claiming race or you can go to a two year old sale. Two year old sales are held on March 15, April 26, May 24, and June 15.")
            print("Would you like to claim a horse or go to a two year old sale?")
            print("[1]... Claim")
            print("[2]... Sale")
            choice1 = input()
            if choice1 == "1":
                print("")
                print("This area is under construction.")
                time.sleep(3)
                continue
                print("The claim system is still being worked out. In the meantime, you can purchase a random unraced three year old for $40,000.")
                print("")
                print("Would you like to purchase an unraced three year old?")
                print("[1]... Yes")
                print("[2]... No")
                choice3 = input()
                if choice3 == "1":
                    print("")
                    time.sleep(1)
                    print("Generating your horse")
                    print("")
                    time.sleep(1)
                    horse1speed = random.randint(5,30)
                    horse1stam = random.randint(9,20)
                    horse1surface = random.randint(1,3)
                    horse1age = 3
                    
                    if horse1speed < 5:
                        horse1speed = 5
                    time.sleep(1)
                    print("")
                    s = random.randint(0,1)
                    s = 1
                    if s == 0:
                        horse1sex = "Colt"
                    elif s == 1:
                        horse1sex = "Filly"
                    
                    horse1earnings = 0
                    bal = bal - 40000
                    if bal < 0:
                        print("Buying this horse would put you in debt. You can not buy this horse.")
                        time.sleep(3)
                        bal = bal + 40000
                        continue
                    print("Congratulations! You bought a horse!")
                    time.sleep(3)
                    print("What would you like to name your horse?")
                    horse1 = input()
                    print("Great name!")
                    time.sleep(2)
                    print("The horse just got back to your trainer. Let's see what he thinks.")
                    print("")
                    time.sleep(2)
                    print("Trainer:")
                    print("")
                    if horse1speed < 15:
                        print("This horse does not seem to have much talent.")
                    elif horse1speed < 25:
                        print("This horse should win some races.")
                    else:
                        print("This horse has talent. Only time will tell!")
                    
                    print("")
                    print("")
                    time.sleep(4)
                    day = day + 1
                    
            elif choice1 == "2":
                if (month == 3 and day == 15) or (month == 4 and day == 26) or (month == 5 and day == 24) or (month == 6 and day == 15):
                    sale()
                else:
                    time.sleep(1)
                    print("There is no sale today. Please advance to a day when there is a sale.")
                    time.sleep(1)
        elif choice == "2":
            print("Enter the date you would like to advance to.")
            try:
                newday = int(input("Day of the month: "))
            except ValueError:
                print("Invalid entry.")
                time.sleep(3)
                continue
            try:
                newmonth = int(input("Month number: "))
            except ValueError:
                print("Invalid entry.")
                time.sleep(3)
                continue
            try:
                newyear = int(input("Year: "))
            except ValueError:
                print("Invalid entry.")
                time.sleep(3)
                continue
            if newday > 31 or newmonth > 12 or newyear < 2020:
                print("You have entered an invalid date.")
                time.sleep(2)
                continue
            if newyear - year > 0:
                if 'foalage' in globals():
                    foalage = foalage + 1
                    if foalage == 1:
                        print("")
                        print("Your foal is now 1 year old. Would you like to sell them?")
                        print("[1]... Yes")
                        print("[2]... No")
                        choice15 = input()
                        if choice15 == "1":
                            print("")
                            foalsale = studfee * (random.randint(7,20) / 10)
                            if foalspeed <= 10 and studfee >= 50000:
                                foalsale = 20000
                            print("Your foal sold for $" + str(foalsale))
                            bal = bal + foalsale
                            foalage = -1000
                    elif foalage == 2:
                        print("")
                        print("Your foal is now 2 years old. You must either sell your horse now or retire your current horse, if you have one, to make way for this new horse.")
                        print("[1]... Retire current horse/Keep 2yo")
                        print("[2]... Sell 2yo")
                        choice16 = input()
                        if choice16 == "1":
                            resethorse()
                            print("")
                            horse1age = 2
                            horse1speed = foalspeed
                            horse1stam = foalstam
                            horse1sex = foalsex
                            horse1surface = random.randint(1,3)
                            foalspeed = 0
                            foalstam = 0
                            foalsex = ""
                            foalage = -1000
                            print("Your horse is a " + horse1sex + ". What would you like to name your horse?")
                            horse1 = input()
                            print("")
                            print("The horse just got back to your trainer. Let's see what he thinks.")
                            print("")
                            time.sleep(2)
                            print("Trainer:")
                            if horse1speed < 15:
                                print("This horse does not seem to have much talent.")
                            elif horse1speed < 25:
                                print("This horse should win some races.")
                            else:
                                print("This horse has talent. Only time will tell!")
                        elif choice16 == "2":
                            print("")
                            foalsale = studfee * (random.randint(7,20) / 10)
                            if foalspeed <= 10 and studfee >= 50000:
                                foalsale = 20000
                            print("Your foal sold for $" + str(foalsale))
                            bal = bal + foalsale
                            foalage = -1000
            if newyear - year < 0:
                print("You can not travel back in time.")
                time.sleep(3)
                continue
            day = newday
            month = newmonth
            year = newyear
            time.sleep(2)
        elif choice == "3":
            bank()
        elif choice == "4":
            with open('save.pkl', 'wb') as f:
                pickle.dump([b,bal,horse1,horse1speed,horse1stam,horse1surface,horse1age,horse1sex,horse1wins,horse1seconds,horse1thirds,horse1races,horse1record,horse1earnings,horseinjury,raceform1,raceform2,raceform3,raceform4,raceform5,raceform6,raceform7,raceform8,raceform9,raceform10,raceform11,raceform12,raceform13,raceform14,raceform15,raceform16,raceform17,raceform18,raceform19,raceform20,raceform21,raceform22,raceform23,raceform24,raceform25,raceform26,raceform27,raceform28,raceform29,raceform30,loan,day,month,year,breedingfarm,circuitnum,circuit,numskipbreak,breakrest,mare1,mare1speed,mare1stam,foalspeed,foalstam,foalage,foalsex,monthlypayment,timeoff], f)
                print("Save successful")
                time.sleep(3)
                sys.exit()
        elif choice == "5":
            with open('save.pkl', 'rb') as f:
                b,bal,horse1,horse1speed,horse1stam,horse1surface,horse1age,horse1sex,horse1wins,horse1seconds,horse1thirds,horse1races,horse1record,horse1earnings,horseinjury,raceform1,raceform2,raceform3,raceform4,raceform5,raceform6,raceform7,raceform8,raceform9,raceform10,raceform11,raceform12,raceform13,raceform14,raceform15,raceform16,raceform17,raceform18,raceform19,raceform20,raceform21,raceform22,raceform23,raceform24,raceform25,raceform26,raceform27,raceform28,raceform29,raceform30,loan,day,month,year,breedingfarm,circuitnum,circuit,numskipbreak,breakrest,mare1,mare1speed,mare1stam,foalspeed,foalstam,foalage,foalsex,monthlypayment,timeoff = pickle.load(f)
                print("")
                print("")
                time.sleep(1)
        elif choice == "6":
            breeding()
        elif choice == "46565":
            bal = int(input())