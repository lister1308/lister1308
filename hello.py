#!/usr/bin/env python3
# aantal voorbeelde uit Python for Dummies om te leren programmeren in python.
# voor gemak verzameld in 1 file
"""
  Ook dit is volgens mij commentaar
"""
import datetime
import sys

# aanroepen functie
def hello():
    print ("functie hello")

# aanroepen functie met argument en default waarde
def hello2(bericht = "geen argument meegegeven"):
    print(bericht)

# functie met parameters aanroepen
def hello4(ArgCount, *VarArgs):
    print("Je hebt",ArgCount,"argumenten meegegeven.")
    for Arg in VarArgs:
      print (Arg)

# datum tijd
def datumtijd():
    nu = datetime.datetime.now()
    print(nu)
    nu = datetime.datetime.now().date()
    print(str(nu))
    
# oefenen met input
def wiebenjij():
    Naam = input("wat is je naam? ")
    print ("hallo",Naam)

# lussen for
def TelLetter(Woord = "default"):
    if (Woord == "default"):
        print("Geen woord meegegeven")
    else:
        LetterNum = 1
        for Letter in Woord:
            print ("Letter",LetterNum," is ",Letter)
            LetterNum += 1
            if LetterNum > 6:
                print("Woord is te lang")
                break

# lussen while
def LoopLus():
    Teller = 1
    while Teller <= 5:
        print(Teller)
        Teller += 1

# exception handling
def VraagCijfer():
    try:
        Value = int(input("Tik een getal tussen 1 en 10: "))
    # onderstaand zou alleen verkeerde waarde afvangen, laat je dit weg, wordt alles afgevangen qua errors
    #except ValueError:
    except:
            print ("Je moet een getal intikken!")
    else:
        if (Value > 0) and (Value <= 10):
            print ("Je tikte in:", Value)
        else:
            print("Getal moest tussen de 1 en 10 zijn!")

# exception handling als je bv een bestand opent
def OpenBestand(Bestand = 'myfile.txt'):
    try:
        File = open(Bestand)
    except IOError as e:
        print("Error opening file!\r\n" +
            "Error Number: {0}\r\n".format(e.errno) +
            "Error Text: {0}".format(e.strerror))
    else:
        print("File",Bestand,"opened as expected.")
        File.close()
        
def StringsVB1():
    print ("""dit is tekst
wat dan over meerdere regels
kan worden geprint door de
meerdere aanhalingstekens""")
    myString = "Hallo Wereld"
    print(myString[0])
    print(myString[0:5])
    print(myString[:5])
    print(myString[:6]*3)

def StringsVB2():
    myString = "Hallo Wereld"
    myString2 = "hallo.wereld"
    print(myString.lower())
    print(myString.upper())
    print("Lengte van",myString,"is",len(myString))
    print(myString.split())
    print(myString.split() [1])
    print(myString2.split())
    print(myString2.split(sep = '.'))

def Lists1():
    List1 = ["One", 1, "Two", "True"]
    print(List1)
    # wat kan je allemaal doen met de list
    for Item in List1:
        print(Item)
    List1.append("lucas")
    print(List1)
    print("Aantal elementen in de lijst is",len(List1))
    List1.insert(0,"tepper")
    print(List1)
    print ("Haal laatste entry er af",end=" ")
    print("Uit de lijst gehaald:",List1.pop(),end=" ")
    print(List1)
    print("en nu de lijst wissen",end=" ")
    List1.clear()
    print(List1)

def DictVB():
    Dict = {"Sam":"Blue","Sarah":"Yellow","Ton":"Red"}
    print(Dict)
    print(Dict.keys())
    for Item in Dict.keys():
        print("{0} likes the color {1}." .format(Item, Dict[Item]))
    Dict.update({"Lucas":"Green"})
    print("entry toegevoegd")
    print(Dict)
    print("entry lucas gewijzigd")
    Dict["Lucas"] = "Black"
    print(Dict)
    Dict["Lucas"] = 1
    print(Dict)
    Dict["Lucas"] += 1
    print(Dict)
    print(Dict["Lucas"])
    print(Dict)
    
    try:
        Aantal = print(Dict["Lucas"])
    except:
        print("deze bestaat niet")
        Dict["Alice"] = 1 
    else:
        print("deze entry bestaat")
        Dict["Lucas"] += 1
    print(Dict)

