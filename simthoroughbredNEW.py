import time
import random
import sys
import pickle
import tkinter as tk
import os

month = 1
year = 2025
day = 1

class Player:
    def __init__(player, stableName):
        player.bal = 100000
        player.horseCount = 0
        player.stableName = stableName

class Horse:
    def __init__(horse, name, age, speed, stam, surface, sex, wins):
        horse.name = name
        horse.age = age
        horse.speed = speed
        horse.stam = stam
        horse.surface = surface
        horse.sex = sex
        horse.wins = wins
        
def intro():
    os.system("cls")
    print("Sim Thoroughbred\nThe Premier Horse Racing Stable Sim")
    time.sleep(2)
    print("\nPlease see the game manual here: https://bit.ly/sim-thoroughbred \nYour home racing circuit will be Southern California\n")
    stableName = input("Enter your stable name: ")
    global player1
    player1 = Player(stableName)

def showDate():
    print(str(month)+"/"+str(day)+"/"+str(year))

def menu():
    os.system("cls")
    showDate()
    print(player1.stableName + " | $" + str(player1.bal))

intro()
menu()