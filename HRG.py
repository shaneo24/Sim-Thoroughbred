import time
import random

b = 50000
bal = float(b)
horse1speed = 0
horse1age = 2
horse1sex = "Filly"
horse1wins = 0
horse1seconds = 0
horse1thirds = 0
horse1races = 0
horse1record = "Unraced"
horse1earnings = 0
horsenum = 1 
horsegenspeed = random.randint(5,35)
horse1stam = random.randint(9,24)
week = 18
month = 5
year = 2021

print("Horse Racing Game")
print("")
print("Welcome to the game. Starting cash is $50,000. You can use this money to buy more horses or just pay the bills and be safe.")
print("You get your first horse for free. It will be a 2 year old.")
print("You can choose to purchase this horse yourself, or purchase it through an agent, which will increase the chance of finding a good horse.")
time.sleep(5)

print("[1]... Use top bloodstock agent (costs $5,000)")
print("[2]... Use small-time bloodstock agent (costs $2,500)")
print("[3]... Purchase yourself")

choice = input()
if choice == "1":
    m = random.randint(1,10)
    horse1speed = horsegenspeed + m
    bal = bal - 5000
if choice == "2":
    m = random.randint(1,5)
    horse1speed = horsegenspeed + m
    bal = bal - 2500
if choice == "3":
    horse1speed = horsegenspeed
time.sleep(1)
print("Choose a name for the horse")
horse1 = input()
time.sleep(1)
print("")

if horse1speed < 15:
    print("This horse does not seem to have any talent.")
elif horse1speed < 28:
    print("This horse could win a race or two, but nothing crazy.")
elif horse1speed < 40:
    print("This is a solid horse. They will have some success.")
elif horse1speed >= 40:
    print("This horse appears to be special. Only time will tell!")

def race():
    global horse1
    global horse1sex
    print("")
    print("")
    print("Enter Race")
    print("")
    global month
    global racebook
    racebook = month
    print("Current Racebook: " + str(racebook))
    print("Please open the current racebook to view your options.")
    time.sleep(1)
    
    print("")
    print("Which race would you like to enter?")
    choice = input()
    
    grade = 0
    fee = 0
    raceoptional = 0
    raceclaim = 0
    
    if racebook == 1 or racebook == 2 or racebook == 3 or racebook == 4 or racebook == 5 or racebook == 6 or racebook == 10:
        track = "Santa Anita Park"
    elif racebook == 9 or racebook == 12:
        track = "Los Alamitos Race Course"
    elif racebook == 7 or racebook == 8 or racebook == 11:
        track = "Del Mar Thoroughbred Club"
        
    if racebook == 1 and choice == "1":
        race = "Starter Allowance"
        racepurse = 36000
        racedes = "For three year olds and upward which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 12
        racerating = 19
    elif racebook == 1 and choice == "2":
        race = "Claiming $40,000"
        racepurse = 42000
        racedes = "For three year olds and upward."
        raceclaim = 40000
        racedist = 17
        racerating = 22
    elif racebook == 1 and choice == "3":
        race = "Claiming $12,500"
        racepurse = 24000
        racedes = "For fillies and mares three years old and upward."
        raceclaim = 12500
        racedist = 16
        racerating = 12
    elif racebook == 1 and choice == "4":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 16
        racerating = 10
    elif racebook == 1 and choice == "4":
        race = "Claiming $25,000"
        racepurse = 36000
        racedes = "For three year olds and upward."
        raceclaim = 25000
        racedist = 16
        racerating = 18
    elif racebook == 1 and choice == "5":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 12
        racerating = 11
    elif racebook == 1 and choice == "6":
        race = "Starter Allowance"
        racepurse = 36000
        racedes = "For fillies and mares three years old and upward which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 12
        racerating = 18
    elif racebook == 1 and choice == "7":
        race = "Grade 3 Sham Stakes"
        racepurse = 100000
        racedes = "For three-year-olds."
        grade = 3
        fee = 1600
        racedist = 16
        racerating = 42
    elif racebook == 1 and choice == "8":
        race = "Allowance Optional Claiming N2X"
        racepurse = 65000
        racedes = "For three year olds and upward which have never won $15,000 twice other than maiden, claiming, starter or which have never won three races or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 17
        racerating = 33
    elif racebook == 1 and choice == "9":
        race = "Claiming $10,000"
        racepurse = 22000
        racedes = "For three year olds and upward."
        raceclaim = 10000
        racedist = 12
        racerating = 11
    elif racebook == 1 and choice == "10":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 16
        racerating = 11
    elif racebook == 1 and choice == "11":
        race = "Grade 2 Santa Ynez Stakes"
        racepurse = 200000
        racedes = "For fillies, three-year-olds."
        grade = 2
        fee = 3100
        racedist = 14
        racerating = 44
    elif racebook == 1 and choice == "12":
        race = "Claiming $25,000"
        racepurse = 36000
        racedes = "For fillies and mares three years old and upward."
        raceclaim = 25000
        racedist = 12
        racerating = 17
    elif racebook == 1 and choice == "13":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For fillies and mares three years old and upward which have never won two races."
        raceclaim = 16000
        racedist = 12
        racerating = 12
    elif racebook == 1 and choice == "14":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, fillies three years old."
        racedist = 16
        racerating = 29
    elif racebook == 1 and choice == "15":
        race = "Claiming $10,000"
        racepurse = 22000
        racedes = "For fillies and mares three years old and upward."
        raceclaim = 10000
        racedist = 12
        racerating = 11
    elif racebook == 1 and choice == "16":
        race = "Claiming $20,000"
        racepurse = 24000
        racedes = "For fillies and mares three years old and upward which have never won three races."
        raceclaim = 20000
        racedist = 12
        racerating = 12
    elif racebook == 1 and choice == "17":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, three years old and upward."
        racedist = 14
        racerating = 31
    elif racebook == 1 and choice == "18":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 16000
        racedist = 12
        racerating = 13
    elif racebook == 1 and choice == "19":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 12
        racerating = 11
    elif racebook == 1 and choice == "20":
        race = "Grade 3 La Canada Stakes"
        racepurse = 200000
        racedes = "For fillies and mares, four years old and upward."
        grade = 3
        fee = 3100
        racedist = 17
        racerating = 43
    elif racebook == 1 and choice == "21":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, fillies and mares three years old and upward."
        racedist = 14
        racerating = 30
    elif racebook == 1 and choice == "22":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, fillies three years old."
        racedist = 12
        racerating = 29
    elif racebook == 1 and choice == "23":
        race = "Claiming $20,000"
        racepurse = 31000
        racedes = "For four year olds and upward."
        raceclaim = 20000
        racedist = 12
        racerating = 16
    elif racebook == 1 and choice == "24":
        race = "Allowance N1X"
        racepurse = 63000
        racedes = "For fillies and mares four years old and upward which have never won $15,000 once other than maiden, claiming or starter or which have never won two races."
        racedist = 12
        racerating = 31
    elif racebook == 1 and choice == "25":
        race = "Kalookan Queen Stakes"
        racepurse = 75000
        racedes = "For fillies and mares, four-years-old and upward."
        fee = 800
        racedist = 13
        racerating = 39
    elif racebook == 1 and choice == "26":
        race = "Grade 3 Palos Verdes Stakes"
        racepurse = 200000
        racedes = "For four-year-olds and upward."
        grade = 3
        fee = 3100
        racedist = 12
        racerating = 44
    elif racebook == 1 and choice == "27":
        race = "Grade 2 San Pasqual Stakes"
        racepurse = 200000
        racedes = "For four-year-olds and upward."
        grade = 2
        fee = 3100
        racedist = 18
        racerating = 46
    elif racebook == 1 and choice == "28":
        race = "Claiming 25,000"
        racepurse = 36000
        racedes = "For three year olds."
        raceclaim = 25000
        racedist = 16
        racerating = 17
    
    elif racebook == 2 and choice == "1":
        race = "Claiming $12,500"
        racepurse = 24000
        racedes = "For three year olds and upward."
        raceclaim = 12500
        racedist = 16
        racerating = 12
    elif racebook == 2 and choice == "2":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 16
        racerating = 11
    elif racebook == 2 and choice == "3":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, fillies and mares three years old and upward."
        racedist = 12
        racerating = 30
    elif racebook == 2 and choice == "4":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, fillies three years old."
        racedist = 14
        racerating = 29
    elif racebook == 2 and choice == "5":
        race = "Claiming $50,000"
        racepurse = 47000
        racedes = "For three year olds and upward."
        raceclaim = 50000
        racedist = 16
        racerating = 24
    elif racebook == 2 and choice == "6":
        race = "Grade 3 Las Virgenes Stakes"
        racepurse = 200000
        racedes = "For fillies, three-year-olds."
        grade = 3
        fee = 3100
        racedist = 16
        racerating = 42
    elif racebook == 2 and choice == "7":
        race = "Grade 2 San Vicenete Stakes"
        racepurse = 200000
        racedes = "For three-year-olds."
        grade = 2
        fee = 3100
        racedist = 14
        racerating = 46
    elif racebook == 2 and choice == "8":
        race = "Allowance Optional Claiming N2X"
        racepurse = 65000
        racedes = "For three year olds and upward which have never won $15,000 twice other than maiden, claiming, starter or state bred or which have never won three races or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 18
        racerating = 33
    elif racebook == 2 and choice == "9":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 16000
        racedist = 13
        racerating = 12
    elif racebook == 2 and choice == "10":
        race = "Maiden Claiming $75,000"
        racepurse = 40000
        racedes = "For maidens, fillies three years old."
        raceclaim = 75000
        racedist = 12
        racerating = 18
    elif racebook == 2 and choice == "11":
        race = "Claiming $12,500"
        racepurse = 24000
        racedes = "For fillies and mares three years old and upward."
        raceclaim = 12500
        racedist = 16
        racerating = 11
    elif racebook == 2 and choice == "12":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 12
        racerating = 11
    elif racebook == 2 and choice == "13":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, three years old."
        racedist = 13
        racerating = 29
    elif racebook == 2 and choice == "14":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For fillies and mares three years old and upward."
        raceclaim = 16000
        racedist = 13
        racerating = 11
    elif racebook == 2 and choice == "15":
        race = "Allowance Optional Claiming N2X"
        racepurse = 65000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 twice other than maiden, claiming, starter or which have never won three races or which have not won $37,000 since October 7 or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 12
        racerating = 32
    elif racebook == 2 and choice == "16":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 16000
        racedist = 17
        racerating = 12
    elif racebook == 2 and choice == "17":
        race = "Maiden Claiming $40,000"
        racepurse = 31000
        racedes = "For maidens, fillies three years old."
        raceclaim = 40000
        racedist = 12
        racerating = 14
    elif racebook == 2 and choice == "18":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, three years old and upward."
        racedist = 12
        racerating = 31
    elif racebook == 2 and choice == "19":
        race = "Claiming $10,000"
        racepurse = 22000
        racedes = "For three year olds and upward."
        raceclaim = 10000
        racedist = 12
        racerating = 11
    elif racebook == 2 and choice == "20":
        race = "Allowance Optional Claiming N1X"
        racepurse = 63000
        racedes = "For three year olds and upward which have never won $15,000 once other than maiden, claiming, or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 14
        racerating = 32
    elif racebook == 2 and choice == "21":
        race = "Claiming $32,000"
        racepurse = 39000
        racedes = "For three year olds and upward."
        raceclaim = 32000
        racedist = 10
        racerating = 25
    elif racebook == 2 and choice == "22":
        race = "Maiden Claiming $40,000"
        racepurse = 31000
        racedes = "For maidens, three years old."
        racedist = 12
        racerating = 14
    elif racebook == 2 and choice == "23":
        race = "Grade 2 Santa Monica Stakes"
        racepurse = 200000
        racedes = "For fillies and mares four-year-olds and upward."
        grade = 2
        fee = 3100
        racedist = 14
        racerating = 46
    elif racebook == 2 and choice == "24":
        race = "Claiming $32,000"
        racepurse = 39000
        racedes = "For three year olds."
        raceclaim = 32000
        racedist = 12
        racerating = 19
    elif racebook == 2 and choice == "25":
        race = "Claiming $10,000"
        racepurse = 22000
        racedes = "For fillies and mares three years old and upward."
        raceclaim = 10000
        racedist = 12
        racerating = 11
    elif racebook == 2 and choice == "26":
        race = "Grade 3 Robert B. Lewis Stakes"
        racepurse = 100000
        racedes = "For three-year-olds."
        grade = 3
        fee = 1600
        racedist = 17
        racerating = 42
    elif racebook == 2 and choice == "27":
        race = "Allowance Optional Claiming N1X"
        racepurse = 63000
        racedes = "For three year old fillies which have never won $15,000 once other than maiden, claiming, or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 14
        racerating = 32
    
    elif racebook == 3 and choice == "1":
        race = "Claiming $16,000"
        racepurse = 26000
        racedes = "For three year olds."
        raceclaim = 16000
        racedist = 12
        racerating = 12
    elif racebook == 3 and choice == "2":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, three years old."
        racedist = 16
        racerating = 29
    elif racebook == 3 and choice == "3":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For fillies and mares four years old and upward which have never won two races."
        raceclaim = 16000
        racedist = 12
        racerating = 12
    elif racebook == 3 and choice == "4":
        race = "Maiden Special Weight"
        racepurse = 76000
        racedes = "For maidens, three years old."
        racedist = 12
        racerating = 36
    elif racebook == 3 and choice == "5":
        race = "Allowance Optional Claiming N2X"
        racepurse = 80000
        racedes = "For four year olds and upward which have never won $15,000 twice other than maiden, claiming, or starter or which have never won three races or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 17
        racerating = 40
    elif racebook == 3 and choice == "6":
        race = "Grade 2 San Carlos Stakes"
        racepurse = 200000
        racedes = "For four-year-olds and upward."
        grade = 2
        fee = 3100
        racedist = 14
        racerating = 47
    elif racebook == 3 and choice == "7":
        race = "Grade 2 San Felipe Stakes"
        racepurse = 300000
        racedes = "For three-year-olds."
        grade = 2
        fee = 4600
        racedist = 17
        racerating = 46
    elif racebook == 3 and choice == "8":
        race = "Grade 1 Santa Anita Handicap"
        racepurse = 400000
        racedes = "For four-year-olds and upward."
        grade = 1
        fee = 6100
        racedist = 20
        racerating = 50
    elif racebook == 3 and choice == "9":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 12
        racerating = 11
    elif racebook == 3 and choice == "10":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, fillies three years old."
        racedist = 16
        racerating = 28
    elif racebook == 3 and choice == "11":
        race = "Maiden Claiming $50,000"
        racepurse = 35000
        racedes = "For maidens, three years old."
        raceclaim = 50000
        racedist = 12
        racerating = 16
    elif racebook == 3 and choice == "12":
        race = "Grade 3 Santa Ysabel Stakes"
        racepurse = 100000
        racedes = "For three-year-olds fillies."
        grade = 3
        fee = 1600
        racedist = 17
        racerating = 42
    elif racebook == 3 and choice == "13":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, three years old and upward."
        racedist = 16
        racerating = 31
    elif racebook == 3 and choice == "14":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 16
        racerating = 11
    elif racebook == 3 and choice == "15":
        race = "Maiden Claiming $50,000"
        racepurse = 35000
        racedes = "For maidens, fillies three years old."
        raceclaim = 50000
        racedist = 12
        racerating = 16
    elif racebook == 3 and choice == "16":
        race = "Allowance Optional Claiming N1X"
        racepurse = 63000
        racedes = "For four year olds and upward which have never won $15,000 once other than maiden, claiming or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 12
        racerating = 32
    elif racebook == 3 and choice == "17":
        race = "Claiming $35,000"
        racepurse = 36000
        racedes = "For fillies and mares four years old and upward which have never won three races."
        raceclaim = 35000
        racedist = 14
        racerating = 17
    elif racebook == 3 and choice == "18":
        race = "Claiming $32,000"
        racepurse = 39000
        racedes = "For fillies and mares four years old and upward."
        raceclaim = 32000
        racedist = 14
        racerating = 19
    elif racebook == 3 and choice == "19":
        race = "Claiming $12,500"
        racepurse = 24000
        racedes = "For four year olds and upward."
        raceclaim = 12500
        racedist = 14
        racerating = 12
    elif racebook == 3 and choice == "20":
        race = "Maiden Claiming $50,000"
        racepurse = 35000
        racedes = "For maidens, three years old."
        raceclaim = 50000
        racedist = 16
        racerating = 16
    elif racebook == 3 and choice == "21":
        race = "Allowance Optional Claiming N2X"
        racepurse = 65000
        racedes = "For four year olds and upward which have never won $15,000 twice other than maiden, claiming, or starter or which have never won three races or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 12
        racerating = 33
    elif racebook == 3 and choice == "22":
        race = "Grade 1 Beholder Mile"
        racepurse = 300000
        racedes = "For fillies and mares four-year-olds and upward."
        grade = 1
        fee = 4600
        racedist = 16
        racerating = 48
    elif racebook == 3 and choice == "23":
        race = "Starter Allowance"
        racepurse = 42000
        racedes = "For four year olds and upward which have started for a claiming price of $25,000 or less in 2020 - 2021."
        racedist = 12
        racerating = 21
    elif racebook == 3 and choice == "24":
        race = "Claiming $35,000"
        racepurse = 36000
        racedes = "For four year olds and upward which have never won three races."
        raceclaim = 35000
        racedist = 16
        racerating = 18
    elif racebook == 3 and choice == "25":
        race = "Santana Mile"
        racepurse = 75000
        racedes = "For four-year-olds and upward."
        fee = 800
        racedist = 16
        racerating = 41
    
    elif racebook == 4 and choice == "1":
        race = "Claiming $10,000"
        racepurse = 22000
        racedes = "For four year olds and upward."
        raceclaim = 10000
        racedist = 12
        racerating = 11
    elif racebook == 4 and choice == "2":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 17
        racerating = 11
    elif racebook == 4 and choice == "3":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For fillies three years old or fillies and mares four years old and upward which have never won two races."
        raceclaim = 16000
        racedist = 13
        racerating = 11
    elif racebook == 4 and choice == "4":
        race = "Allowance Optional Claiming N1X"
        racepurse = 63000
        racedes = "For fillies and mares four years old and upward which have never won $15,000 once other than maiden, claiming, or starter, or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 16
        racerating = 30
    elif racebook == 4 and choice == "5":
        race = "Maiden Claiming $30,000"
        racepurse = 25000
        racedes = "For maidens, fillies three years old."
        raceclaim = 30000
        racedist = 16
        racerating = 11
    elif racebook == 4 and choice == "6":
        race = "Starter Allowance"
        racepurse = 60000
        racedes = "For four year olds and upward which have started for a claiming price of $50,000 or less."
        racedist = 16
        racerating = 30
    elif racebook == 4 and choice == "7":
        race = "Maiden Special Weight"
        racepurse = 76000
        racedes = "For maidens, three years old."
        racedist = 13
        racerating = 36
    elif racebook == 4 and choice == "8":
        race = "Grade 2 Santa Anita Oaks"
        racepurse = 400000
        racedes = "For fillies, three-year-olds."
        grade = 2
        fee = 6100
        racedist = 17
        racerating = 42
    elif racebook == 4 and choice == "9":
        race = "Grade 1 Santa Anita Derby"
        racepurse = 750000
        racedes = "For three-year-olds."
        grade = 1
        fee = 11350
        racedist = 18
        racerating = 44
    elif racebook == 4 and choice == "10":
        race = "Claiming $10,000"
        racepurse = 22000
        racedes = "For fillies and mares four years old and upward."
        raceclaim = 10000
        racedist = 12
        racerating = 11
    elif racebook == 4 and choice == "11":
        race = "Maiden Claiming $75,000"
        racepurse = 40000
        racedes = "For maidens, three years old."
        raceclaim = 75000
        racedist = 12
        racerating = 20
    elif racebook == 4 and choice == "12":
        race = "Allowance Optional Claiming N1X"
        racepurse = 63000
        racedes = "For three year olds which have never won $15,000 other than maiden, claiming, or starter or which have never won two races or optional claiming $100,000."
        raceclaim = 100000
        raceoptional = 1
        racedist = 13
        racerating = 31
    elif racebook == 4 and choice == "13":
        race = "Grade 3 Las Flores Stakes"
        racepurse = 100000
        racedes = "For fillies and mares-four-years-old and upward."
        grade = 3
        fee = 1600
        racedist = 12
        racerating = 43
    elif racebook == 4 and choice == "14":
        race = "Starter Allowance"
        racepurse = 36000
        racedes = "For fillies and mares three years old and upward which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 12
        racerating = 18
    elif racebook == 4 and choice == "15":
        race = "Claiming $40,000"
        racepurse = 42000
        racedes = "For four year olds and upward."
        raceclaim = 40000
        racedist = 12
        racerating = 21
    elif racebook == 4 and choice == "16":
        race = "Claiming $20,000"
        racepurse = 24000
        racedes = "For fillies and mares four years old and upward which have never won three races."
        raceclaim = 20000
        racedist = 12
        racerating = 12
    elif racebook == 4 and choice == "17":
        race = "Maiden Claiming $25,000"
        racepurse = 22000
        racedes = "For maidens, three years old and upward."
        raceclaim = 25000
        racedist = 11
        racerating = 11
    elif racebook == 4 and choice == "18":
        race = "Maiden Claiming $30,000"
        racepurse = 25000
        racedes = "For maidens, fillies three years old."
        raceclaim = 30000
        racedist = 12
        racerating = 10
    elif racebook == 4 and choice == "19":
        race = "Claiming $10,000"
        racepurse = 22000
        racedes = "For fillies and mares four years old and upward."
        raceclaim = 10000
        racedist = 16
        racerating = 11
    elif racebook == 4 and choice == "20":
        race = "Allowance Optional Claiming N1X"
        racepurse = 63000
        racedes = "For four year olds and upward which have never won $15,000 once other than maiden, claiming, or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 14
        racerating = 32
    elif racebook == 4 and choice == "21":
        race = "Allowance Optional Claiming N2X"
        racepurse = 65000
        racedes = "For four year olds and upward which have never won $15,000 twice other than maiden, claiming, or starter or which have never won three races or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 16
        racerating = 35
    elif racebook == 4 and choice == "22":
        race = "Starter Allowance"
        racepurse = 33000
        racdes = "For fillies and mares four years old and upward which have started for a claiming price of $50,000 or less and which have never won three races."
        racedist = 13
        racerating = 16
    elif racebook == 4 and choice == "23":
        race = "Claiming $32,000"
        racepurse = 31000
        racedes = "For fillies three years old or fillies and mares four years old and upward which have never won two races."
        raceclaim = 32000
        racedist = 16
        racerating = 15
    elif racebook == 4 and choice == "24":
        race = "Claiming $20,000"
        racepurse = 31000
        racedes = "For four year olds and upward."
        raceclaim = 20000
        racedist = 16
        racerating = 16
    elif racebook == 4 and choice == "25":
        race = "Grade 2 Californian Stakes"
        racepurse = 200000
        racedes = "For three-year-olds and upward."
        grade = 2
        fee = 3100
        racedist = 18
        racerating = 46
    elif racebook == 4 and choice == "26":
        race = "Grade 3 Tokyo City Cup"
        racepurse = 100000
        racedes = "For four-year-olds and upward."
        grade = 3
        fee = 1600
        racedist = 24
        racerating = 43
    elif racebook == 4 and choice == "27":
        race = "Grade 3 Kona Gold Stakes"
        racepurse = 100000
        racedes = "For three-year-olds and upward."
        grade = 3
        fee = 1600
        racedist = 13
        racerating = 43
    elif racebook == 4 and choice == "28":
        race = "Grade 2 Santa Margarita Stakes"
        racepurse = 200000
        racedes = "For fillies and mares, four year olds and upward."
        grade = 2
        fee = 3100
        racedist = 18
        racerating = 45
        
    elif racebook == 5 and choice == "1":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, fillies two years old."
        raceclaim = 0
        raceoptional = 0
        racedist = 9
        racerating = 26
    elif racebook == 5 and choice == "2":
        race = "Starter Allowance"
        racepurse = 42000
        racedes = "For four year olds and upward which have started for a claiming price of $25,000 or less in one of their last three starts."
        racedist = 12
        racerating = 22
    elif racebook == 5 and choice == "3":
        race = "Claiming $50,000"
        racepurse = 47000
        racedes = "For four year olds and upward."
        raceclaim = 50000
        racedist = 17
        racerating = 25
    elif racebook == 5 and choice == "4":
        race = "Angels Flight Stakes"
        racepurse = 75000
        racedes = "For fillies three years old."
        fee = 800
        racedist = 14
        racerating = 38
    elif racebook == 5 and choice == "5":
        race = "Claiming $12,500"
        racepurse = 24000
        racedes = "For four year olds and upward."
        raceclaim = 12500
        racedist = 16
        racerating = 12
    elif racebook == 5 and choice == "6":
        race = "Claiming $35,000"
        racepurse = 36000
        racedes = "For four year olds and upward which have never won three races."
        raceclaim = 35000
        racedist = 16
        racerating = 19
    elif racebook == 5 and choice == "7":
        race = "Starter Allowance"
        racepurse = 44000
        racedes = "For fillies and mares four years old and upward which have never started for a claiming price of $32,000 or less in 2020-2021."
        racedist = 12
        racerating = 22
    elif racebook == 5 and choice == "8":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 14
        racerating = 12
    elif racebook == 5 and choice == "9":
        race = "Starter Allowance"
        racepurse = 36000
        racedes = "For three year olds which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 16
        racerating = 17
    elif racebook == 5 and choice == "10":
        race = "Claiming $12,500"
        racepurse = 24000
        racedes = "For fillies and mares four years old and upward."
        raceclaim = 12500
        racedist = 16
        racerating = 12
    elif racebook == 5 and choice == "11":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 16
        racerating = 11
    elif racebook == 5 and choice == "13":
        race = "Starter Allowance"
        racepurse = 36000
        racedes = "For three year olds and upward which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 17
        racerating = 18
    elif racebook == 5 and choice == "14":
        race = "Allowance Optional Claiming N1X"
        racepurse = 63000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 once other than maiden, claiming, or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 14
        racerating = 31
    elif racebook == 5 and choice == "15":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For three year olds or four year olds and upward which have never won two races."
        raceclaim = 16000
        racedist = 17
        racerating = 12
    elif racebook == 5 and choice == "16":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 12
        racerating = 11
    elif racebook == 5 and choice == "17":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, three years old and upward."
        racedist = 16
        racerating = 31
    elif racebook == 5 and choice == "18":
        race = "Allowance Optional Claiming N3X"
        racepurse = 70000
        racedes = "For four year olds and upward which have never won $15,000 three times other than maiden, claiming, starter or which have not won $45,000 or which have never won four races or claiming price $100,000."
        raceclaim = 100000
        raceoptional = 1
        racedist = 16
        racerating = 38
    elif racebook == 5 and choice == "19":
        race = "Claiming $25,000"
        racepurse = 36000
        racedes = "For four year olds and upward."
        raceclaim = 25000
        racedist = 17
        racerating = 18
    elif racebook == 5 and choice == "20":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, two years old."
        racedist = 9
        racerating = 25
    elif racebook == 5 and choice == "21":
        race = "Starter Allowance"
        racepurse = 36000
        racedes = "For three year olds and upward which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 12
        racerating = 18
    elif racebook == 5 and choice == "22":
        race = "Allowance Optional Claiming N1X"
        racepurse = 63000
        racedes = "For three year olds and upward which have never won $15,000 once other than maiden, claiming or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 16
        racerating = 32
    elif racebook == 5 and choice == "23":
        race = "Allowance Optional Claiming N2X"
        racepurse = 63000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 other than maiden, claiming, or starter or which have never won two races or claiming price $100,000."
        raceclaim = 100000
        raceoptional = 1
        racedist = 17
        racerating = 34
    elif racebook == 5 and choice == "24":
        race = "Grade 3 Lazaro Barrera Stakes"
        racepurse = 100000
        racedes = "For three-year-olds."
        grade = 3
        fee = 1600
        racedist = 13
        racerating = 42
    elif racebook == 5 and choice == "25":
        race = "Grade 3 Desert Stormer Stakes"
        racepurse = 100000
        racedes = "For fillies and mares three-year-olds and upward."
        grade = 3
        fee = 1600
        racedist = 12
        racerating = 42
    elif racebook == 5 and choice == "26":
        race = "Grade 2 Santa Maria Stakes"
        racepurse = 200000
        racedes = "For fillies and mares, three year olds and upward."
        grade = 2
        fee = 3100
        racedist = 17
        racerating = 45
    elif racebook == 5 and choice == "27":
        race = "Grade 2 Triple Bend Stakes"
        racepurse = 200000
        racedes = "For four-year-olds and upward."
        grade = 2
        fee = 3100
        racedist = 14
        racerating = 46
    elif racebook == 5 and choice == "28":
        race = "Grade 2 Summertime Oaks"
        racepurse = 200000
        racedes = "For fillies, three years old."
        grade = 2
        fee = 3100
        racedist = 17
        racerating = 45
    elif racebook == 5 and choice == "29":
        race = "Grade 1 Hollywood Gold Cup"
        racepurse = 300000
        racedes = "For three-year-olds and upward."
        grade = 1
        fee = 4600
        racedist = 20
        racerating = 49
    elif racebook == 5 and choice == "30":
        track = "Churchill Downs"
        race = "Grade 1 Kentucky Derby"
        racepurse = 3000000
        racedes = "For three-year-olds."
        grade = 1
        fee = 30000
        racedist = 20
        racerating = 53
        
    elif racebook == 6 and choice == "1":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For fillies three years old or fillies and mares four years old and upward which have never won two races."
        raceclaim = 16000
        racedist = 16
        racerating = 12
    elif racebook == 6 and choice == "2":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 13
        racerating = 12
    elif racebook == 6 and choice == "3":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, fillies and mares three years old and upward."
        racedist = 12
        racerating = 31
    elif racebook == 6 and choice == "4":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, fillies two years old."
        racedist = 10
        racerating = 26
    elif racebook == 6 and choice == "5":
        race = "Starter Allowance"
        racepurse = 33000
        racedes = "For three year olds and upward which have started for a claiming price of $50,000 or less and which have never won three races."
        racedist = 12
        racerating = 17
    elif racebook == 6 and choice == "6":
        race = "Claiming $25,000"
        racepurse = 36000
        racedes = "For fillies and mares three years old and upward."
        raceclaim = 25000
        racedist = 12
        racerating = 18
    elif racebook == 6 and choice == "7":
        race = "Claiming $12,500"
        racepurse = 24000
        racedes = "For four year olds and upward."
        raceclaim = 12500
        racedist = 12
        racerating = 13
    elif racebook == 6 and choice == "8":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, two years old."
        racedist = 10
        racerating = 24
    elif racebook == 6 and choice == "9":
        race = "Allowance Optional Claiming N1X"
        racepurse = 63000
        racedes = "For three year olds and upward which have never won $15,000 once other than maiden, claiming, or starter, or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 17
        racerating = 32
    elif racebook == 6 and choice == "10":
        race = "Starter Allowance"
        racepurse = 36000
        racedes = "For three year olds and upward which have started for a claiming price of $50,000 or less and which have never won two races or claiming price $50,000 and which have never won two races."
        racedist = 12
        racerating = 19
    elif racebook == 6 and choice == "11":
        race = "Claiming $10,000"
        racepurse = 22000
        racedes = "For fillies and mares four years old and upward."
        raceclaim = 10000
        racedist = 16
        racerating = 11
    elif racebook == 6 and choice == "12":
        race = "Starter Allowance"
        racepurse = 33000
        racedes = "For fillies and mares four years old and upward which have started for a claiming price of $20,000 or less in 2020 - 2021."
        racedist = 16
        racerating = 16
    elif racebook == 6 and choice == "13":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 16
    elif racebook == 6 and choice == "14":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For three year olds or four year olds and upward which have never won two races."
        raceclaim = 16000
        racedist = 12
        racerating = 13
    elif racebook == 6 and choice == "15":
        race = "Grade 3 Affirmed Stakes"
        racepurse = 100000
        racedes = "For three-year-olds."
        grade = 3
        fee = 1600
        racedist = 17
        racerating = 41
    elif racebook == 6 and choice == "16":
        race = "Fasig-Tipton Futurity"
        racepurse = 100000
        racedes = "For two year olds."
        fee = 400
        racedist = 10
        racerating = 33
    elif racebook == 6 and choice == "17":
        race = "Fasig-Tipton Debutante"
        racepurse = 100000
        racedes = "For fillies, two years old."
        fee = 400
        racedist = 10
        racerating = 31
    elif racebook == 6 and choice == "18":
        race = "Allowance Optional Claiming N1X"
        racepurse = 63000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 once other than maiden, claiming or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 12
        racerating = 31
    elif racebook == 6 and choice == "19":
        race = "Claiming $30,000"
        racepurse = 33000
        racedes = "For fillies and mares three years old and upward which have never won three races."
        raceclaim = 30000
        racedist = 16
        racerating = 16
    elif racebook == 6 and choice == "20":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, fillies and mares three years old and upward."
        racedist = 16
        racerating = 29
    elif racebook == 6 and choice == "21":
        race = "Allowance Optional Claiming N2X"
        racepurse = 65000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 twice other than maiden, claiming, starter or which have never won three races or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 12
        racerating = 32
    elif racebook == 6 and choice == "22":
        race = "Starter Allowance"
        racepurse = 33000
        racedes = "For four year olds and upward which have started for a claiming price of $20,000 or less in the past 18 months."
        racedist = 16
        racerating = 17
    elif racebook == 6 and choice == "23":
        race = "Claiming $12,500"
        racepurse = 24000
        racedes = "For fillies and mares four years old and upward."
        raceclaim = 12500
        racedist = 13
        racerating = 11
    elif racebook == 6 and choice == "24":
        race = "Starter Allowance"
        racepurse = 33000
        racedes = "For four year olds and upward which have started for a claiming price of $20,000 or less in the past 18 months."
        racedist = 12
        racerating = 17
    elif racebook == 6 and choice == "25":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, three years old and upward."
        racedist = 16
        racerating = 31
    elif racebook == 6 and choice == "26":
        race = "Maiden Claiming $50,000"
        racepurse = 35000
        racedes = "For maidens, two years old."
        racedist = 10
        raceclaim = 50000
        racerating = 17
        
    elif racebook == 7 and choice == "1":
        race = "Claiming $16,000"
        racepurse = 30000
        racedes = "For three year olds and upward."
        raceclaim = 16000
        racedist = 16
        racerating = 16
    elif racebook == 7 and choice == "2":
        race = "Maiden Claiming $150,000"
        racepurse = 50000
        racedes = "For maidens, two years old."
        raceclaim = 150000
        racedist = 11
        racerating = 21
    elif racebook == 7 and choice == "3":
        race = "Starter Allowance"
        racepurse = 38000
        racedes = "For three year olds and upward which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 16
        racerating = 20
    elif racebook == 7 and choice == "4":
        race = "Allowance Optional Claiming N1X"
        racepurse = 72000
        racedes = "For three year olds and upward which have never won $15,000 once other than maiden, claiming, or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 13
        racerating = 37
    elif racebook == 7 and choice == "5":
        race = "Claiming $20,000"
        racepurse = 28000
        racedes = "For three year olds and upward which have never won three races."
        raceclaim = 20000
        racedist = 13
        racerating = 15
    elif racebook == 7 and choice == "6":
        race = "Claiming $20,000"
        racepurse = 33000
        racedes = "For three year olds."
        raceclaim = 20000
        racedist = 16
        racerating = 16
    elif racebook == 7 and choice == "7":
        race = "Claiming $20,000"
        racepurse = 28000
        racedes = "For fillies and mares three years old and upward which have never won three races."
        raceclaim = 20000
        racedist = 13
        racerating = 14
    elif racebook == 7 and choice == "8":
        race = "Maiden"
        racepurse = 70000
        racedes = "For maidens, three years old and upward."
        racedist = 13
        racerating = 36
    elif racebook == 7 and choice == "9":
        race = "Claiming $16,000"
        racepurse = 25000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 16000
        racedist = 13
        racerating = 13
    elif racebook == 7 and choice == "10":
        race = "Maiden"
        racepurse = 70000
        racedes = "For maidens, fillies two years old."
        racedist = 10
        racerating = 30
    elif racebook == 7 and choice == "11":
        race = "Claiming $20,000"
        racepurse = 33000
        racedes = "For three year olds."
        raceclaim = 20000
        racedist = 11
        racerating = 16
    elif racebook == 7 and choice == "12":
        race = "Allowance Optional Claiming N1X"
        racepurse = 72000
        racedes = "For three year olds and upward which have never won $15,000 once other than maiden, claiming, or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 16
        racerating = 37
    elif racebook == 7 and choice == "13":
        race = "Grade 2 San Diego Handicap"
        racepurse = 250000
        racedes = "A handicap for three-year-olds and upward."
        grade = 2
        fee = 4000
        racedist = 17
        racerating = 47
    elif racebook == 7 and choice == "14":
        race = "Maiden Claiming $40,000"
        racepurse = 31000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 40000
        racedist = 12
        racerating = 15
    elif racebook == 7 and choice == "15":
        race = "Grade 3 Courgar II Stakes"
        racepurse = 100000
        racedes = "For three-year-olds and upward."
        grade = 3
        fee = 1600
        racedist = 24
        racerating = 43
    elif racebook == 7 and choice == "16":
        race = "Grade 1 Bing Crosby Stakes"
        racepurse = 300000
        racedes = "For three-year-olds and upward."
        grade = 1
        fee = 4800
        racedist = 12
        racerating = 49
    elif racebook == 7 and choice == "17":
        race = "Claiming $20,000"
        racepurse = 28000
        racedes = "For three year olds and upward which have never won three races."
        raceclaim = 20000
        racedist = 16
        racerating = 15
    elif racebook == 7 and choice == "18":
        race = "Maiden Claiming $32,000"
        racepurse = 27000
        racedes = "For maidens, two years old."
        raceclaim = 32000
        racedist = 11
        racerating = 10
    elif racebook == 7 and choice == "19":
        race = "Maiden"
        racepurse = 70000
        racedes = "For maidens, two years old."
        racedist = 10
        racerating = 31
    elif racebook == 7 and choice == "20":
        race = "Claiming $20,000"
        racepurse = 33000
        racedes = "For three year olds and upward."
        raceclaim = 20000
        racedist = 13
        racerating = 17
    elif racebook == 7 and choice == "21":
        race = "Maiden Claiming $20,000"
        racepurse = 25000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 12
        racerating = 13
    elif racebook == 7 and choice == "22":
        race = "Maiden Claiming $50,000"
        racepurse = 36000
        racedes = "For maidens, fillies two years old."
        raceclaim = 50000
        racedist = 10
        racerating = 13
    elif racebook == 7 and choice == "23":
        race = "Allowance Optional Claiming N2X"
        racepurse = 74000
        racedes = "For three year olds and upward which have never won $15,000 twice other than maiden, claiming, or starter or which have never won three races or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 16
        racerating = 38
    elif racebook == 7 and choice == "24":
        race = "Allowance Optional Claiming N2X"
        racepurse = 74000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 twice other than miaden, claiming, or starter or which have never won three races or which have not won a race since August 1 or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 12
        racerating = 37
    elif racebook == 7 and choice == "25":
        race = "Claiming $16,000"
        racepurse = 25000
        racedes = "For fillies and mares three years old and upward which have never won two races."
        raceclaim = 16000
        racedist = 12
        racerating = 12
    elif racebook == 7 and choice == "26":
        race = "Maiden Claiming $32,000"
        racepurse = 27000
        racedes = "For maidens, two years old."
        raceclaim = 32000
        racedist = 11
        racerating = 14
    
    elif racebook == 8 and choice == "1":
        race = "Claiming $8,000"
        racepurse = 23000
        racedes = "For three year olds and upward."
        raceclaim = 8000
        racedist = 12
        racerating = 12
    elif racebook == 8 and choice == "2":
        race = "Maiden"
        racepurse = 70000
        racedes = "For maidens, two years old."
        racedist = 10
        racerating = 31
    elif racebook == 8 and choice == "3":
        race = "Allowance Optional Claiming N1X"
        racepurse = 72000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 once other than maiden, claiming, or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 12
        racerating = 36
    elif racebook == 8 and choice == "4":
        race = "Grade 1 Clement L. Hirsch Stakes"
        racepurse = 300000
        racedes = "For fillies and mares, three-year-olds and upward."
        grade = 1
        fee = 4800
        racedist = 17
        racerating = 48
    elif racebook == 8 and choice == "5":
        race = "Starter Allowance"
        racepurse = 40000
        racedes = "For fillies and mares three years old and upward which have started for a claiming price of $50,000 or less and which have never won three races."
        racedist = 16
        racerating = 20
    elif racebook == 8 and choice == "6":
        race = "Claiming $16,000"
        racepurse = 30000
        racedes = "For fillies and mares three years old and upward."
        raceclaim = 16000
        racedist = 16
        racerating = 15
    elif racebook == 8 and choice == "7":
        race = "Maiden Claiming $40,000"
        racepurse = 31000
        racedes = "For maidens, three years old and upward."
        raceclaim = 40000
        racedist = 13
        racerating = 16
    elif racebook == 8 and choice == "8":
        race = "Claiming $8,000"
        racepurse = 23000
        racedes = "For three year olds and upward."
        raceclaim = 8000
        racedist = 16
        racerating = 12
    elif racebook == 8 and choice == "9":
        race = "Maiden"
        racepurse = 70000
        racedes = "For maidens, fillies and mares three years old and upward."
        racedist = 16
        racerating = 35
    elif racebook == 8 and choice == "10":
        race = "Maiden Claiming $20,000"
        racepurse = 25000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 16
        racerating = 12
    elif racebook == 8 and choice == "11":
        race = "Maiden Claiming $80,000"
        racepurse = 44000
        racedes = "For maidens, fillies two years old."
        raceclaim = 80000
        racedist = 11
        racerating = 18
    elif racebook == 8 and choice == "12":
        race = "Grade 2 Sorrento Stakes"
        racepurse = 200000
        racedes = "For fillies, two-year-olds."
        grade = 2
        fee = 3200
        racedist = 12
        racerating = 39
    elif racebook == 8 and choice == "13":
        race = "Grade 2 Best Pal Stakes"
        racepurse = 200000
        racedes = "For two-year-olds."
        grade = 2
        fee = 3200
        racedist = 12
        racerating = 41
    elif racebook == 8 and choice == "14":
        race = "Grade 3 Rancho Bernardo Handicap"
        racepurse = 100000
        racedes = "For fillies and mares, three-year-olds and upward."
        grade = 3
        fee = 1600
        racedist = 13
        racerating = 41
    elif racebook == 8 and choice == "15":
        race = "Grade 1 TVG Pacific Classic"
        racepurse = 750000
        racedes = "For three-year-olds and upward."
        grade = 1
        fee = 10000
        racedist = 20
        racerating = 51
    elif racebook == 8 and choice == "16":
        race = "Grade 3 Torrey Pines Stakes"
        racepurse = 100000
        racedes = "For fillies, three-year-olds."
        grade = 3
        fee = 1600
        racedist = 16
        racerating = 39
    elif racebook == 8 and choice == "17":
        race = "Tranquility Lake Stakes"
        racepurse = 80000
        racedes = "For fillies and mares, three-year-olds and upward which are non-winners of a sweepstakes of $50,000 (to the winner) at one mile or over since February 1."
        fee = 500
        racedist = 16
        racerating = 39
    elif racebook == 8 and choice == "18":
        race = "Grade 2 Pat O'Brien Stakes"
        racepurse = 200000
        racedes = "For three-year-olds and upward."
        grade = 2
        fee = 3200
        racedist = 14
        racerating = 46
    elif racebook == 8 and choice == "19":
        race = "Shared Belief Stakes"
        racepurse = 100000
        racedes = "For three-year-olds."
        fee = 800
        racedist = 16
        racerating = 39
    elif racebook == 8 and choice == "20":
        race = "Claiming $16,000"
        racepurse = 25000
        racedes = "For fillies and mares three years old and upward which have never won two races."
        raceclaim = 16000
        racedist = 16
        racerating = 12
    elif racebook == 8 and choice == "21":
        race = "Maiden"
        racepurse = 70000
        racedes = "For maidens, three years old and upward."
        racedist = 16
        racerating = 36
    elif racebook == 8 and choice == "22":
        race = "Maiden Claiming $80,000"
        racepurse = 44000
        racedes = "For maidens, two years old."
        raceclaim = 80000
        racedist = 11
        racerating = 18
    elif racebook == 8 and choice == "23":
        race = "Claiming $16,000"
        racepurse = 25000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 16000
        racedist = 11
        racerating = 13
    elif racebook == 8 and choice == "24":
        race = "Maiden"
        racepurse = 70000
        racedes = "For maidens, two years old."
        racedist = 12
        racerating = 31
    elif racebook == 8 and choice == "25":
        race = "Maiden Claiming $20,000"
        racepurse = 25000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 11
        racerating = 12
    elif racebook == 8 and choice == "26":
        race = "Maiden Claiming $50,000"
        racepurse = 36000
        racedes = "For maidens, fillies two years old."
        raceclaim = 50000
        racedist = 10
        racerating = 17
    elif racebook == 8 and choice == "27":
        race = "Starter Optional Claiming"
        racepurse = 45000
        racedes = "For fillies two years old which have started for a claiming price of $50,000 or less and which have never won two races or claiming price $50,000."
        raceclaim = 50000
        racedist= 12
        racerating = 21
    elif racebook == 8 and choice == "28":
        race = "Starter Optional Claiming"
        racepurse = 45000
        racedes = "For two year olds which have started for a claiming price of $50,000 or less and which have never won two races or claiming price $50,000."
        raceclaim = 50000
        racedist= 12
        racerating = 21
        
    elif racebook == 9 and choice == "1":
        race = "Claiming $6,250"
        racepurse = 12000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 6250
        racedist = 10
        racerating = 7
    elif racebook == 9 and choice == "2":
        race = "Maiden Claiming $20,000"
        racepurse = 20000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 10
        racerating = 10
    elif racebook == 9 and choice == "3":
        race = "Maiden Claiming $30,000"
        racepurse = 23000
        racedes = "For maidens, three years old."
        raceclaim = 30000
        racedist = 11
        racerating = 11
    elif racebook == 9 and choice == "4":
        race = "Maiden Special Weight"
        racepurse = 45000
        racedes = "For maidens, two years old."
        racedist = 10
        racerating = 19
    elif racebook == 9 and choice == "5":
        race = "Maiden Claiming $20,000"
        racepurse = 20000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 16
        racerating = 11
    elif racebook == 9 and choice == "6":
        race = "Starter Allowance"
        racepurse = 22000
        racedes = "For fillies and mares three years old and upward which have never started for a claiming price of $16,000 or less in 2020 - 2021 and since have not won a claiming, starter or optional race exceeding $16,000."
        racedist = 16
        racerating = 10
    elif racebook == 9 and choice == "7":
        race = "Allowance Optional Claiming N1X"
        racepurse = 48000
        racedes = "For three year olds and upward which have never won $15,000 once other than maiden, claiming or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 12
        racerating = 25
    elif racebook == 9 and choice == "8":
        race = "Claiming $10,000"
        racepurse = 17000
        racedes = "For three year olds and upward."
        raceclaim = 10000
        racedist = 16
        racerating = 9
    elif racebook == 9 and choice == "9":
        race = "Starter Allowance"
        racepurse = 28000
        racedes = "For three year olds and upward which have started for a claiming price of $20,000 or less and which have never won two races."
        racedist = 12
        racerating = 15
    elif racebook == 9 and choice == "10":
        race = "Starter Allowance"
        racepurse = 16000
        racedes = "For three year olds and upward which have started for a claiming price of $8,000 or less in 2020 - 2021 and since have not won a claiming, starter or optional race exceeding $8,000."
        racedist = 10
        racerating = 9
    elif racebook == 9 and choice == "11":
        race = "Starter Allowance"
        racepurse = 16000
        racedes = "For fillies and mares three years old and upward which have started for a claiming price of $8,000 or less in the past 18 months and since have not won a claiming, starter, or optional race exceeding $8,000."
        racedist = 10
        racerating = 7
    elif racebook == 9 and choice == "12":
        race = "Maiden Claiming $20,000"
        racepurse = 20000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 10
        racerating = 10
    elif racebook == 9 and choice == "13":
        race = "Maiden Claiming $30,000"
        racepurse = 23000
        racedes = "For maidens, fillies three years old."
        raceclaim = 30000
        racedist = 11
        racerating = 10
    elif racebook == 9 and choice == "14":
        race = "Maiden Special Weight"
        racepurse = 45000
        racedes = "For maidens, fillies two years old."
        racedist = 10
        racerating = 17
    elif racebook == 9 and choice == "15":
        race = "Starter Allowance"
        racepurse = 29000
        racedes = "For three year olds and upward which have started for a claiming price of $25,000 or less in the past 18 months and since have not won a claiming, starter or optional race exceeding $25,000."
        racedist = 16
        racerating = 15
    elif racebook == 9 and choice == "16":
        race = "Allowance Optional Claiming N1X"
        racepurse = 48000
        racedes = "For three year olds and upward which have never won $15,000 once other than maiden, claiming or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 16
        racerating = 25
    elif racebook == 9 and choice == "17":
        race = "Maiden Claiming $40,000"
        racepurse = 28000
        racedes = "For maidens, three years old and upward."
        raceclaim = 40000
        racedist = 16
        racerating = 14
    elif racebook == 9 and choice == "18":
        race = "Starter Allowance"
        racepurse = 33000
        racedes = "For fillies and mares three years old and upward which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 11
        racerating = 15
    elif racebook == 9 and choice == "19":
        race = "Claiming $6,250"
        racepurse = 12000
        racedes = "For fillies and mares three years old and upward which have never won two races."
        raceclaim = 6250
        racedist = 10
        racerating = 5
    elif racebook == 9 and choice == "20":
        race = "Maiden Special Weight"
        racepurse = 45000
        racedes = "For maidens, three years old and upward."
        racedist = 12
        racerating = 23
    elif racebook == 9 and choice == "21":
        race = "Maiden Claiming $40,000"
        racepurse = 28000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 40000
        racedist = 16
        racerating = 13
    elif racebook == 9 and choice == "22":
        race = "Claiming $16,000"
        racepurse = 20000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 16000
        racedist = 12
        racerating = 32
    elif racebook == 9 and choice == "23":
        race = "Starter Allowance"
        racepurse = 33000
        racedes = "For three year olds and upward which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 11
        racerating = 17
    elif racebook == 9 and choice == "24":
        race = "Allowance Optional Claiming N1X"
        racepurse = 48000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 once other than maiden, claiming or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 16
        racerating = 23
    elif racebook == 9 and choice == "25":
        race = "Allowance Optioncal Claiming N2X"
        racepurse = 50000
        racedes = "For three year olds and upward which have never won $15,000 twice other than maiden, claiming, or starter or which have never won three races or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 17
        racerating = 25
    elif racebook == 9 and choice == "26":
        track = "Del Mar Thoroughbred Club"
        race = "Grade 1 Del Mar Debutante"
        racepurse = 300000
        racedes = "For fillies, two-year-olds."
        grade = 1
        fee = 4000
        racedist = 14
        racerating = 42
    elif racebook == 9 and choice == "27":
        track = "Del Mar Thoroughbred Club"
        race = "Grade 1 Del Mar Futurity"
        racepurse = 300000
        racedes = "For two-year-olds."
        grade = 1
        fee = 4000
        racedist = 14
        racerating = 44
    
    elif racebook == 10 and choice == "1":
        race = "Claiming $40,000"
        racepurse = 42000
        racedes = "For three year olds and upward."
        raceclaim = 40000
        racedist = 12
        racerating = 22
    elif racebook == 10 and choice == "2":
        race = "Starter Allowance"
        racepurse = 28000
        racedes = "For three year olds and upward which have started for a claiming price of $25,000 or less and which have never won two races."
        racedist = 16
        racerating = 15
    elif racebook == 10 and choice == "3":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 16
        racerating = 11
    elif racebook == 10 and choice == "4":
        race = "Maiden Special Weight"
        racepurse = 61000
        racedes = "For maidens, three years old."
        racedist = 12
        racerating = 30
    elif racebook == 10 and choice == "5":
        race = "Claiming $10,000"
        racepurse = 22000
        racedes = "For three year olds and upward."
        raceclaim = 10000
        racedist = 17
        racerating = 12
    elif racebook == 10 and choice == "6":
        race = "Allowance N1X"
        racepurse = 63000
        racedes = "For three year olds and upward which have never won $15,000 once other than maiden, claiming or starter or which have never won two races."
        racedist = 17
        racerating = 32
    elif racebook == 10 and choice == "7":
        race = "Starter Allowance"
        racepurse = 36000
        racedes = "For fillies three years old which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 12
        racerating = 17
    elif racebook == 10 and choice == "8":
        race = "Claiming $20,000"
        racepurse = 24000
        racedes = "For three year olds and upward which have never won three races."
        raceclaim = 20000
        racedist = 16
        racerating = 12
    elif racebook == 10 and choice == "9":
        race = "Claiming $10,000"
        racepurse = 22000
        racedes = "For fillies and mares three years old and upward."
        raceclaim = 10000
        racedist = 17
        racerating = 10
    elif racebook == 10 and choice == "10":
        race = "Maiden Claiming $40,000"
        racepurse = 31000
        racedes = "For maidens, three years old."
        raceclaim = 40000
        racedist = 16
        racerating = 15
    elif racebook == 10 and choice == "11":
        race = "Grade 1 American Pharoah Stakes"
        racepurse = 300000
        racedes = "For two year olds."
        grade = 1
        fee = 4800
        racedist = 17
        racerating = 44
    elif racebook == 10 and choice == "12":
        race = "Grade 2 Chandelier Stakes"
        racepurse = 200000
        racedes = "For fillies, two years old."
        grade = 2
        fee = 3100
        racedist = 17
        racerating = 42
    elif racebook == 10 and choice == "13":
        race = "Grade 1 Awesome Again"
        racepurse = 300000
        racedes = "For three-year-olds and upward."
        grade = 1
        fee = 4800
        racedist = 18
        racerating = 48
    elif racebook == 10 and choice == "14":
        race = "Grade 2 Santa Anita Sprint Championship"
        racepurse = 200000
        racedes = "For three-year-olds and upward."
        grade = 2
        fee = 3100
        racedist = 12
        racerating = 46
    elif racebook == 10 and choice == "15":
        race = "Grade 2 Zenyatta Stakes"
        racepurse = 200000
        racedes = "For fillies and mares, three year olds and upward."
        grade = 2
        fee = 3100
        racedist = 17
        racerating = 45
    elif racebook == 10 and choice == "16":
        race = "Grade 3 Chillingsworth Stakes"
        racepurse = 100000
        racedes = "For fillies and mares, three year olds and upward."
        grade = 3
        fee = 1600
        racedist = 13
        racerating = 42
    elif racebook == 10 and choice == "17":
        race = "Anoakia Stakes"
        racepurse = 75000
        racedes = "For fillies, two years old."
        fee = 800
        racedist = 12
        racerating = 33
    elif racebook == 10 and choice == "18":
        race = "Starter Allowance"
        racepurse = 36000
        racedes = "For three year olds which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 13
        racerating = 18
    elif racebook == 10 and choice == "19":
        race = "Allowance N1X"
        racepurse = 63000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 once other than maiden, claiming or starter which have never won two races."
        racedist = 16
        racerating = 31
    elif racebook == 10 and choice == "20":
        race = "Claiming $50,000"
        racepurse = 47000
        racedes = "For fillies and mare three years old and upward."
        raceclaim = 50000
        racedist = 17
        racerating = 23
    elif racebook == 10 and choice == "21":
        race = "Claiming $25,000"
        racepurse = 36000
        racedes = "For three year olds."
        raceclaim = 25000
        racedist = 12
        racerating = 16
    elif racebook == 10 and choice == "22":
        race = "Claiming $16,000"
        racepurse = 26000
        racedes = "For three year olds and upward."
        raceclaim = 16000
        racedist = 16
        racerating = 14
    elif racebook == 10 and choice == "23":
        race = "Claiming $16,000"
        racepurse = 24000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 16000
        racedist = 16
        racerating = 13
    elif racebook == 10 and choice == "24":
        race = "Maiden Claiming $20,000"
        racepurse = 22000
        racedes = "For maidens, three year olds and upward."
        raceclaim = 20000
        racedist = 13
        racerating = 12
    elif racebook == 10 and choice == "25":
        race = "Allowance N1X"
        racepurse = 63000
        racedes = "For three year olds and upward which have never won $15,000 once other than maiden, claiming or starter or which have never won two races."
        racedist = 12
        racerating = 32
    elif racebook == 10 and choice == "26":
        race = "Claiming $32,000"
        racepurse = 39000
        racedes = "For fillies and mares three years old and upward."
        raceclaim = 32000
        racedist = 12
        racerating = 19
    elif racebook == 10 and choice == "27":
        race = "Starter Allowance"
        racepurse = 33000
        racedes = "For three year olds and upward which have started for a claiming price of $50,000 or less and which have never won three races."
        racedist = 17
        racerating = 17
    elif racebook == 10 and choice == "28":
        race = "Maiden Claiming $40,000"
        racepurse = 31000
        racedes = "For maidens, fillies three years old."
        raceclaim = 40000
        racedist = 16
        racerating = 13
    elif racebook == 10 and choice == "29":
        race = "Maiden Claiming $50,000"
        racepurse = 35000
        racedes = "For maidens, two years old."
        racedist = 16
        raceclaim = 50000
        racerating = 17
    elif racebook == 10 and choice == "30":
        race = "Starter Optional Claiming"
        racepurse = 45000
        racedes = "For fillies two years old which have started for a claiming price of $50,000 or less and which have never won two races or claiming price $50,000."
        raceclaim = 50000
        racedist= 12
        racerating = 21
    elif racebook == 10 and choice == "30":
        race = "Starter Optional Claiming"
        racepurse = 45000
        racedes = "For two year olds which have started for a claiming price of $50,000 or less and which have never won two races or claiming price $50,000."
        raceclaim = 50000
        racedist= 12
        racerating = 21
        
    elif racebook == 11 and choice == "1":
        race = "Claiming $16,000"
        racepurse = 21000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 16000
        racedist = 10
        racerating = 9
    elif racebook == 11 and choice == "2":
        race = "Maiden Claiming $20,000"
        racepurse = 20000
        racedes = "For maiden, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 12
        racerating = 9
    elif racebook == 11 and choice == "3":
        race = "Claiming $16,000"
        racepurse = 26000
        racedes = "For three year olds and upward."
        raceclaim = 16000
        racedist = 16
        racerating = 13
    elif racebook == 11 and choice == "4":
        race = "Claiming $12,500"
        racepurse = 23000
        racedes = "For three year olds."
        raceclaim = 12500
        racedist = 12
        racerating = 11
    elif racebook == 11 and choice == "5":
        race = "Claiming $20,000"
        racepurse = 23000
        racedes = "For three year olds and upward which have never won three races."
        raceclaim = 20000
        racedist = 16
        racerating = 12
    elif racebook == 11 and choice == "6":
        race = "Maiden"
        racepurse = "57000"
        racedes = "For maidens, two years old."
        racedist = 16
        racerating = 24
    elif racebook == 11 and choice == "7":
        race = "Claiming $16,000"
        racepurse = 21000
        racedes = "For fillies and mares three years old and upward which have never won two races."
        raceclaim = 16000
        racedist = 10
        racerating = 10
    elif racebook == 11 and choice == "8":
        race = "Maiden Claiming $20,000"
        racepurse = 20000
        racedes = "For maidens, three years old and upward."
        raceclaim = 20000
        racedist = 13
        racerating = 10
    elif racebook == 11 and choice == "9":
        race = "Claiming $8,000"
        racepurse = 20000
        racedes = "For three year olds and upward."
        raceclaim = 8000
        racedist = 13
        racerating = 10
    elif racebook == 11 and choice == "10":
        race = "Claiming $20,000"
        racepurse = 23000
        racedes = "For fillies and mares three years old and upward which have never won three races."
        raceclaim = 20000
        racedist = 10
        racerating = 11
    elif racebook == 11 and choice == "11":
        race = "Maiden"
        racepurse = 57000
        racedes = "For maidens, fillies and mares three years old and upward."
        racedist = 16
        racerating = 27
    elif racebook == 11 and choice == "12":
        race = "Desi Arnaz Stakes"
        racepurse = 100000
        racedes = "For fillies, two years old."
        fee = 1100
        racedist = 13
        racerating = 36
    elif racebook == 11 and choice == "13":
        race = "Grade 3 Bob Hope Stakes"
        racepurse = 100000
        racedes = "For two-year-olds."
        grade = 3
        fee = 1600
        racedist = 14
        racerating = 38
    elif racebook == 11 and choice == "14":
        race = "Grade 3 Native Diver Stakes"
        racepurse = 100000
        racedes = "For three-year-olds and upward."
        grade = 3
        fee = 1600
        racedist = 18
        racerating = 41
    elif racebook == 11 and choice == "15":
        race = "Starter Allowance"
        racepurse = 28000
        racedes = "For fillies and mares three years old and upward which have started for a claiming price of $12,500 or less in the past 18 months."
        racedist = 12
        racerating = 13
    elif racebook == 11 and choice == "16":
        race = "Maiden"
        racepurse = 57000
        racedes = "For maidens, fillies two years old."
        racedist = 12
        racerating = 22
    elif racebook == 11 and choice == "17":
        race = "Claiming $25,000"
        racepurse = 33000
        racedes = "For three year olds and upward."
        raceclaim = 25000
        racedist = 16
        racerating = 17
    elif racebook == 11 and choice == "18":
        race = "Maiden Claiming $50,000"
        racepurse = 31000
        racedes = "For maidens, two years old."
        raceclaim = 50000
        racedist = 13
        racerating = 12
    elif racebook == 11 and choice == "19":
        race = "Claiming $50,000"
        racepurse = 43000
        racedes = "For three year olds and upward."
        raceclaim = 50000
        racedist = 16
        racerating = 22
    elif racebook == 11 and choice == "20":
        race = "Claiming $40,000"
        racepurse = 38000
        racedes = "For three year olds."
        raceclaim = 40000
        racedist = 14
        racerating = 18
    elif racebook == 11 and choice == "21":
        race = "Maiden"
        racepurse = 57000
        racedes = "For maidens, two years old."
        racedist = 12
        racerating = 24
    elif racebook == 11 and choice == "22":
        race = "Allowance Optional Claiming N1X"
        racepurse = 59000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 once other than maiden, claiming, or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 13
        racerating = 28
    elif racebook == 11 and choice == "23":
        race = "Allowance Optional Claiming N3X"
        racepurse = 65000
        racedes = "For three year olds and upward which have never won $15,000 three times other than maiden, claiming, or starter or which have never won four races or which have not won $40,000 since September 1 or claiming price $100,000."
        raceclaim = 100000
        raceoptional = 1
        racedist = 13
        racerating = 34
    elif racebook == 11 and choice == "24":
        race = "Starter Allowance"
        racepurse = 37000
        racedes = "For three year olds and upward which have started for a claiming price of $55,000 or less and which have never won three races."
        racedist = 17
        racerating = 19
    elif racebook == 11 and choice == "25":
        race = "Starter Allowance"
        racepurse = 35000
        racedes = "For three year olds and upward which have started for a claiming price of $50,000 or less and which have never won two races."
        racedist = 13
        racerating = 18
    elif racebook == 11 and choice == "26":
        race = "Maiden Claiming $50,000"
        racepurse = 31000
        racedes = "For maidens, fillies two years old."
        raceclaim = 50000
        racedist = 13
        racerating = 10
    elif racebook == 11 and choice == "27":
        track = "Del Mar Thoroughbred Club"
        race = "Grade 1 Breeders' Cup Classic"
        racepurse = 6000000
        racedes = "For three year olds and upward."
        grade = 1
        fee = 50000
        racedist = 20
        racerating = 56
    elif racebook == 11 and choice == "28":
        track = "Del Mar Thoroughbred Club"
        race = "Grade 1 Breeders' Cup Distaff"
        racepurse = 2000000
        racedes = "For fillies and mares three years old and upward."
        grade = 1
        fee = 50000
        racedist = 18
        racerating = 54
    elif racebook == 11 and choice == "29":
        track = "Del Mar Thoroughbred Club"
        race = "Grade 1 Breeders' Cup Filly and Mare Sprint"
        racepurse = 1000000
        racedes = "For fillies and mares three years old and upward."
        grade = 1
        fee = 50000
        racedist = 14
        racerating = 54
    elif racebook == 11 and choice == "30":
        track = "Del Mar Thoroughbred Club"
        race = "Grade 1 Breeders' Cup Dirt Mile"
        racepurse = 1000000
        racedes = "For three year olds and upward."
        grade = 1
        fee = 50000
        racedist = 16
        racerating = 54
    elif racebook == 11 and choice == "31":
        track = "Del Mar Thoroughbred Club"
        race = "Grade 1 Breeders' Cup Sprint"
        racepurse = 2000000
        racedes = "For three year olds and upward."
        grade = 1
        fee = 50000
        racedist = 12
        racerating = 55
    elif racebook == 11 and choice == "32":
        track = "Del Mar Thoroughbred Club"
        race = "Grade 1 Breeders' Cup Juvenile"
        racepurse = 2000000
        racedes = "For two year olds."
        grade = 1
        fee = 50000
        racedist = 17
        racerating = 48
    elif racebook == 11 and choice == "33":
        track = "Del Mar Thoroughbred Club"
        race = "Grade 1 Breeders' Cup Juvenile Fillies"
        racepurse = 2000000
        racedes = "For fillies, two years old."
        grade = 1
        fee = 50000
        racedist = 17
        racerating = 46

    elif racebook == 12 and choice == "1":
        race = "Claiming $12,500"
        racepurse = 21000
        racedes = "For three year olds and upward."
        raceclaim = 12500
        racedist = 11
        racerating = 11
    elif racebook == 12 and choice == "2":
        race = "Grade 1 Malibu Stakes"
        racepurse = 300000
        racedes = "For three-year-olds."
        grade = 1
        fee = 4800
        racedist = 14
        racerating = 47
    elif racebook == 12 and choice == "3":
        race = "Grade 1 La Brea Stakes"
        racepurse = 300000
        racedes = "For fillies, three years old."
        grade = 1
        fee = 4800
        racedist = 14
        racerating = 45
    elif racebook == 12 and choice == "4":
        race = "Grade 2 San Antonio Stakes"
        racepurse = 200000
        racedes = "For three year olds and upward."
        grade = 2
        fee = 3100
        racedist = 17
        racerating = 47
    elif racebook == 12 and choice == "5":
        race = "Claiming $8,000"
        racepurse = 15000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 8000
        racedist = 10
        racerating = 8
    elif racebook == 12 and choice == "6":
        race = "Maiden Claiming $20,000"
        racepurse = 20000
        racedes = "For maidens, fillies and mares three years old and upward."
        raceclaim = 20000
        racedist = 16
        racerating = 9
    elif racebook == 12 and choice == "7":
        race = "Maiden Special Weight"
        racepurse = 45000
        racedes = "For maidens, three years old and upward."
        racedist = 16
        racerating = 23
    elif racebook == 12 and choice == "8":
        race = "Starter Allowance"
        racepurse = 21000
        racedes = "For fillies and mares three years old and upward which have started for a claiming price of $12,500 or less in the past 18 months and since have not won a claiming, starter or optional race exceeding $12,500."
        racedist = 11
        racerating = 10
    elif racebook == 12 and choice == "9":
        race = "Starter Allowance"
        racepurse = 22000
        racedes = "For three year olds and upward which have started for a claiming price of $16,000 or less in the past 18 months and since have not won a claiming, starter or optional race exceeding $16,000."
        racedist = 16
        racerating = 12
    elif racebook == 12 and choice == "10":
        race = "Starter Allowance"
        racepurse = 28000
        racedes = "For fillies and mares three years old and upward which have started for a claiming price of $20,000 or less and which have never won two races."
        racedist = 12
        racerating = 13
    elif racebook == 12 and choice == "11":
        race = "Allowance Optional Claiming N2X"
        racepurse = 50000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 twice other than maiden, claiming, or starter or which have never won three races or claiming price $62,500."
        raceclaim = 62500
        raceoptional = 1
        racedist = 17
        racerating = 24
    elif racebook == 12 and choice == "12":
        race = "Claiming $16,000"
        racepurse = 22000
        racedes = "For three year olds."
        raceclaim = 16000
        racedist = 11
        racerating = 10
    elif racebook == 12 and choice == "13":
        race = "Claiming $8,000"
        racepurse = 15000
        racedes = "For fillies and mares three years old and upward which have never won two races."
        raceclaim = 8000
        racedist = 10
        racerating = 7
    elif racebook == 12 and choice == "14":
        race = "Maiden Special Weight"
        racepurse = 45000
        racedes = "For maidens, fillies and mares three years old and upward."
        racedist = 16
        racerating = 22
    elif racebook == 12 and choice == "15":
        race = "Claiming $12,500"
        racepurse = 18000
        racedes = "For three year olds and upward which have never won two races."
        raceclaim = 12500
        racedist = 12
        racerating = 9
    elif racebook == 12 and choice == "16":
        race = "Claiming $16,000"
        racepurse = 20000
        racedes = "For fillies and mares three years old and upward which have never won two races."
        raceclaim = 16000
        racedist = 12
        racerating = 9
    elif racebook == 12 and choice == "17":
        race = "Starter Allowance"
        racepurse = 29000
        racedes = "For fillies and mares three years old and upward which have started for a claiming price of $25,000 or less in the past 18 months and since have not won a claiming, starter or optional race exceeding $25,000."
        racedist = 16
        racerating = 14
    elif racebook == 12 and choice == "18":
        race = "Allowance Optional Claiming N1X"
        racepurse = 48000
        racedes = "For fillies and mares three years old and upward which have never won $15,000 once other than maiden, claiming, or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 12
        racerating = 23
    elif racebook == 12 and choice == "19":
        race = "Grade 3 Bayakoa Stakes"
        racepurse = 100000
        racedes = "For fillies and mares three year olds and upward."
        grade = 3
        fee = 2100
        racedist = 17
        racerating = 40
    elif racebook == 12 and choice == "20":
        race = "Grade 2 Los Alamitos Futurity"
        racepurse = 200000
        racedes = "For two year olds."
        grade = 2
        fee = 4300
        racedist = 17
        racerating = 41
    elif racebook == 12 and choice == "21":
        race = "Grade 1 Starlet Stakes"
        racepurse = 300000
        racedes = "For two year old fillies."
        grade = 1
        fee = 5100
        racedist = 17
        racerating = 41
    elif racebook == 12 and choice == "22":
        race = "Allowance Optional Claiming N1X"
        racepurse = 48000
        racedes = "For two year olds which have never won $15,000 once other than maiden, claiming, or starter or which have never won two races or claiming price $40,000."
        raceclaim = 40000
        raceoptional = 1
        racedist = 12
        racerating = 21
    
    else:
        print("That race does not exist. Please try again.")
        time.sleep(2)
        return

    global year
    global bal
    
    print("")
    time.sleep(1)
    print("")
    print(track)
    print("Race #" + str(choice) + ", " + str(month) + "/" + str(year))
    print(race + " Purse $" + str(racepurse))
    print(racedes)

    dist = racedist / 2

    print(str(dist) + " furlongs")
    print("")
    print("")
    time.sleep(2)
    print("Would you like to enter this race?")
    print("[1]... Yes")
    print("[2]... No")
    choice = input()
    print("")
    if choice == "1":
        if raceoptional == 1:
            print("")
            print("Would you like to enter " + horse1 + " for a claim? Note that depending on the conditions of the race and your horse, you may be required to.")
            print("[1]... Yes")
            print("[2]... No")
            choice1 = input()
            if choice1 == "1":
                print("")
                print("Entered for a claim of $" + str(raceclaim) + ".")
            else:
                raceoptional = 0
        elif raceoptional == 0 and raceclaim != 0:
            print("")
            print("Your horse is in a claiming race. They have been entered for a tag of $" + str(raceclaim) + ". Anyone may purchase your horse.")
            print("")
            print("Confirm you would like to enter in this race.")
            print("[1]... Yes")
            print("[2]... No")
            choice = input()
            if choice == "2":
                return
            raceoptional = 1
        elif fee != 0:
            print("")
            print("There is a fee of $" + str(fee) + " to enter this stakes race.")
            print("Confirm you would like to enter in this race.")
            print("[1]... Yes")
            print("[2]... No")
            choice = input()
            if choice == "1":
                print("")
                time.sleep(1)
                bal = bal - fee
            elif choice == "2":
                return
        time.sleep(1)
        print("")
        print("Successfully entered")
    else:
        return
    
    time.sleep(1)
    
    global speed
    global horse1speed
    
    if track == "Santa Anita Park":
        fieldsize = random.randint(6, 11)
    if track == "Los Alamitos Race Course":
        fieldsize = random.randint(6, 8)
    if track == "Del Mar Thoroughbred Club":
        fieldsize = random.randint(8, 12)
    if track == "Del Mar Thoroughbred Club" and racepurse > 1000000:
        fieldsize = 14
    if race == "Grade 1 Kentucky Derby":
        fieldsize = 20
        
    field = float(fieldsize)
    competition = (field - 6) / 2
    speed = int(horse1speed - competition)
    difference = int(speed - racerating)
    
    print("")
    print("The race at " + track + " is ready to go!")
    print("There are " + str(fieldsize) + " horses in this race.")
    print("")
    print("Press enter to view the results.")
    choice = input()
    
    global horse1stam
    global horse1wins
    global horse1seconds
    global horse1thirds
    global horse1races
    
    horse1races = horse1races + 1
    
    if (horse1stam - dist) <= -3 or (horse1stam - dist) >= 11:
        print("")
        time.sleep(1)
        print(horse1 + " lost! It seems they didn't like the distance.")
        if difference <= 0:
            result = random.randint(5, fieldsize)
            chance = 0
            if result == 5:
                mult = 0.02
            else:
                mult = 0
        elif difference > 0 and difference < 5:
            result = random.randint(3, 4)
            chance = 10
            if result == 4:
                mult = 0.06
            elif result == 3:
                mult = 0.12
                horse1thirds = horse1thirds + 1
        elif difference >= 5:
            chance = 20
            result = 2
            mult = 0.2
            horse1seconds = horse1seconds + 1
        
    else:
        print("")
        time.sleep(1)
        
        if difference == 1 or difference == 2:
            chance = 40
        elif difference == 3:
            chance = 45
        elif difference == 4:
            chance = 50
        elif difference == 5:
            chance = 55
        elif difference == 6:
            chance = 60
        elif difference == 7:
            chance = 70
        elif difference == 8:
            chance = 75
        elif difference == 9:
            chance = 80
        elif difference >= 10:
            chance = 85
        elif difference == 0:
            chance = 35
        elif difference == -1:
            chance = 30
        elif difference == -2:
            chance = 27.5
        elif difference == -3:
            chance = 25
        elif difference == -4:
            chance = 22.5
        elif difference == -5:
            chance = 20
        elif difference <= -6 and difference > -10:
            chance = 10
        elif difference <= -10:
            chance = 1

        res1 = random.choices([1, 2], weights=[chance, (100 - chance)], k=(1))
        if res1 == [1]:
            result = 1
            horse1wins = horse1wins + 1
            mult = 0.6
        else:
            res2 = random.choices([1, 2], weights=[(chance + 15), (100 - chance)], k=(1))
            if res2 == [1]:
                result = 2
                horse1seconds = horse1seconds + 1
                mult = 0.2
            else:
                res3 = random.choices([1, 2], weights=[(chance + 20), (100 - chance)], k=(1))
                if res3 == [1]:
                    result = 3
                    horse1thirds = horse1thirds + 1
                    mult = 0.12
                else:
                    res4 = random.choices([1, 2], weights=[(chance + 10), (100 - chance)], k=(1))
                    if res4 == [1]:
                        result = 4
                        mult = 0.06
                    else:
                        res5 = random.choices([1, 2], weights=[(chance + 5), (100 - chance)], k=(1))
                        if res5 == [1]:
                            result = 5
                            mult = 0.02
                        else:
                            res6 = random.choices([1, 2], weights=[(chance + 5), (100 - chance)], k=(1))
                            if res6 == [1] or fieldsize == 6:
                                result = 6
                                mult = 0
                            else:
                                res7 = random.choices([1, 2], weights=[(chance + 2.5), (100 - chance)], k=(1))
                                if res7 == [1] or fieldsize == 7:
                                    result = 7
                                    mult = 0
                                else:
                                    res8 = random.choices([1, 2], weights=[(chance + 2.5), (100 - chance)], k=(1))
                                    if res8 == [1] or fieldsize == 8:
                                        result = 8
                                        mult = 0
                                    else:
                                        res9 = random.choices([1, 2], weights=[(chance + 2.5), (100 - chance)], k=(1))
                                        if res9 == [1] or fieldsize == 9:
                                            result = 9
                                            mult = 0
                                        else:
                                            res10 = random.choices([1, 2], weights=[(chance + 2.5), (100 - chance)], k=(1))
                                            if res10 == [1] or fieldsize == 10:
                                                result = 10
                                                mult = 0
                                            else:
                                                res11 = res10 = random.choices([1, 2], weights=[(chance + 2.5), (100 - chance)], k=(1))
                                                if res11 == [1] or fieldsize == 11:
                                                    result = 11
                                                    mult = 0
                                                else:
                                                    result = 12
                                                    mult = 0
            
    time.sleep(1)
    if result == 1:
        print("Yes! " + horse1 + " won!!")
        print("")
    else: 
        print(horse1 + " finished " + str(result) + " place in a field of " + str(fieldsize) + ".")
    
    global horse1record
    global horse1age
    global horse1earnings
    global horsenum
    
    if raceoptional == 1 and raceclaim != 0 and difference > 0:
        print("")
        time.sleep(1)
        claimchance = chance - 10
        cla1 = random.choices([1, 2], weights=[claimchance, (100 - claimchance)], k=(1))
        if cla1 == [1]:
            print("Shoot! " + horse1 + " was claimed!")
            print("You earned $" + str(raceclaim) + " for your horse being claimed.")
            print("")
            time.sleep(1)
            bal = bal + raceclaim
            horsenum = horsenum - 1
            
            horse1 = ""
            horse1speed = 0
            horse1age = 0
            horse1sex = ""
            horse1wins = 0
            horse1seconds = 0
            horse1thirds = 0
            horse1races = 0
            horse1record = "Unraced"
            horse1earnings = 0
            
        elif cla1 == [2]:
            print(horse1 + " was not claimed.")
            print("")
            time.sleep(1)
    elif raceoptional == 1 and raceclaim != 0 and difference <= 0:
        print("")
        time.sleep(1)
        print(horse1 + " was not claimed.")
        print("")
    
    time.sleep(1)
    racepurs = float(racepurse)
    mul = float(mult)
    pursewinnings = (racepurs * mul) * 0.8
    if mult > 0:
        print("Congratulations, you won $" + str(pursewinnings) + " in purse winnings.")
    print("")
    
    earnings = racepurse * mult
    
    horse1earnings = horse1earnings + earnings
    
    bal = bal + pursewinnings
    time.sleep(1)
    
    if horse1 != "":
        print("This is the updated record for " + horse1 + ".")
    
        horse1record = str(horse1races) + ": " + str(horse1wins) + "-" + str(horse1seconds) + "-" + str(horse1thirds)
        print(horse1record)
    
    print("")
    
    print("The month will now automatically advance. You may enter another race.")
    time.sleep(2)
    month = month + 1
    bal = bal - (3500*horsenum)
    
    if month == 13:
        year = year + 1
        month = 1
        horse1age = horse1age + 1
        if horse1age == 3:
            horse1speed = horse1speed + random.randint(3, 9)
            horse1stam
        elif horse1age == 4:
            horse1speed = horse1speed + random.randint(1, 4)
        elif horse1age > 5:
            horse1speed = horse1speed - 5
            horse1stam = horse1stam - 3
        if horse1age == 4 and horse1sex == "Colt":
            horse1sex = "Horse"
        elif horse1age == 4 and horse1sex == "Filly":
            horse1sex = "Mare"

def sale():
    print("")
    print("Welcome to the sale. The bloodstock agent is looking for a horse for you. About how much would you like to spend?")
    print("[1]... 20k to 50k")
    print("[2]... 51k to 80k")
    print("[3]... 81k to 110k")
    print("[4]... 111k to 150k")
    print("[5]... 151k to 200k")
    print("[6]... 201k to 300k")
    print("[7]... 301k to 500k")
    print("[8]... 501k to 850k")
    print("[9]... 851k to 1500k")
    print("[10]... > 1500k")
    choice = input()
    print("")
    print("Ok. The agent is going to try to find you a horse in your price range.")
    print("")
    time.sleep(3)
    
    global horse1stam
    global horse1age
    global horsenum
    global horse1speed
    global horse1sex
    global horse1name
    global bal
    global horse1
    
    horse1stam = random.randint(9,24)
    horse1age = 2
    
    if choice == "1":
        chance = random.randint(-10, 0)
        base = random.randint(0, 50)
        price1 = random.randint(20, 50)
    elif choice == "2":
        chance = random.randint(-8, 0)
        base = random.randint(5, 50)
        price1 = random.randint(51, 80)
    elif choice == "3":
        chance = random.randint(-6, 0)
        base = random.randint(5, 50)
        price1 = random.randint(81, 110)
    elif choice == "4":
        chance = random.randint(-4, 0)
        base = random.randint(5, 50)
        price1 = random.randint(111, 150)
    elif choice == "5":
        chance = random.randint(-2, 0)
        base = random.randint(10, 50)
        price1 = random.randint(151, 200)
    elif choice == "6":
        chance = random.randint(0, 2)
        base = random.randint(10, 50)
        price1 = random.randint(201, 300)
    elif choice == "7":
        chance = random.randint(0, 4)
        base = random.randint(15, 50)
        price1 = random.randint(301, 500)
    elif choice == "8":
        chance = random.randint(0, 6)
        base = random.randint(19, 50)
        price1 = random.randint(501, 850)
    elif choice == "9":
        chance = random.randint(0, 8)
        base = random.randint(23, 50)
        price1 = random.randint(851, 1500)
    elif choice == "10":
        chance = random.randint(0, 10)
        base = random.randint(26, 50)
        price1 = random.randint(1501, 2500)
    
    horse1speed = base + chance
    if horse1speed < 0:
        horse1speed = 0
    price = price1 * 1000
    sex = random.randint(1, 2)
    if sex == 1:
        horse1sex = "Colt"
    if sex == 2:
        horse1sex = "Filly"
    print("The agent has found you a " + horse1sex + " that costs $" + str(price) + ". Would you like to purchase it?")
    print("[1]... Yes")
    print("[2]... No")
    choice = input()
    if choice != "1":
        print("Ok.")
        time.sleep(2)
        return
    horsenum = horsenum + 1
    print("Congratulations! You bought a 2 year old " + horse1sex + " for $" + str(price) + "!")
    time.sleep(3)
    bal = bal - price
    print("What would you like to name your horse?")
    horse1 = input()
    print("Great name!")
    time.sleep(2)
    
    print("The horse just got into your trainer. Let's see what he thinks.")
    print("")
    time.sleep(1)
    print("Trainer:")
    
    if horse1speed < 10:
        print("This horse does not seem to have much talent.")
    elif horse1speed < 20:
        print("This horse could win a race or two, but nothing crazy.")
    elif horse1speed < 35:
        print("This is a solid horse. They will have some success.")
    elif horse1speed >= 35:
        print("This horse appears to be special. Only time will tell!")
    time.sleep(3)
        
a = 1
while a == 1:
    print("")
    print("")
    print("Stable, " + str(month) + "/" + str(year))
    print("Balance: $" + str(bal))
    print("")
    if horse1 != "":
        print(horse1 + ", " + str(horse1age) + "yo " + horse1sex + "  $" + str(horse1earnings))
    time.sleep(1)
    print("")
    print("Actions:")
    print("[1]... Enter race")
    print("[2]... Advance month (Pay $3,500/horse training fees)")
    print("[3]... View horses' records")
    print("[4]... Purchase horse")
    print("[5]... Retire horse")
    print("[6]... Sell horse")
    time.sleep(1)
    choice = input()
    if choice == "2":
        month = month + 1
        bal = bal - (3500*horsenum)
        if month == 13:
            year = year + 1
            month = 1
            horse1age = horse1age + 1
            if horse1age == 3:
                horse1speed = horse1speed + random.randint(3, 9)
                horse1stam
            elif horse1age == 4:
                horse1speed = horse1speed + random.randint(1, 4)
            elif horse1age > 5:
                horse1speed = horse1speed - 5
                horse1stam = horse1stam - 3
            if horse1age == 4 and horse1sex == "Colt":
                horse1sex = "Horse"
            elif horse1age == 4 and horse1sex == "Filly":
                horse1sex = "Mare"
    if choice == "1":
        race()
    if choice == "3":
        print("")
        time.sleep(1)
        print(horse1 + ", " + str(horse1age) + "yo " + horse1sex + "  " + horse1record + " $" + str(horse1earnings))
        time.sleep(3)
    if choice == "4":
        print("")
        time.sleep(1)
        if horse1 != "":
            print("You already have a horse! Retire or sell them to purcahse a new horse.")
            time.sleep(2)
            continue
        print("Let's go to a two year old sale and get you a horse")
        time.sleep(3)
        sale()
    if choice == "5":
        print("")
        time.sleep(1)
        print("Which horse would you like to retire? Please enter their name.")
        choice = input()
        if choice == horse1:
            print("Ok. " + horse1 + " has been retired. You may now purchase a new horse.")
            print("Here were the horses stats:")
            print("Speed: " + str(horse1speed))
            print("Stamina: " + str(horse1stam))
            horse1 = ""
            horse1speed = 0
            horse1stam = random.randint(9,24)
            horse1age = 0
            horse1sex = ""
            horse1wins = 0
            horse1seconds = 0
            horse1thirds = 0
            horse1races = 0
            horse1record = "Unraced"
            horse1earnings = 0
            horsenum = horsenum - 1
            time.sleep(2)
            print("")
