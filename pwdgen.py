import random
import re
import string

# User Input Domain ohne http(s) und www
domain = list(input("Gib die Secondlevel Domain ein: "))
# Passwortvariable als Liste
pwd = []
# temporäre Variable mit domain
tempdom = domain
# temp var umgekehrt
tempdom2 = list(reversed(domain))


# Algorithmus Schritt 1
# Iteration durch die ersten zwei Zeichen der Domain
for i in domain[:3]:

    # verarbeiten des ersten Listenelements
    getlet = tempdom[0]
    # Konvertierng in ASCII Nummer
    letasc = ord(getlet)
    # Zufällige ROT Verschiebung im Range
    modasc = letasc + random.randint(1, 9)
    # Zufallsgenerator der zwei Werte erlaubt
    generator = random.randint(0, 1)
    # je nach Wert wird Buchstabe groß oder kleingeschrieben
    if generator == 0:
        # chr() wandelt ASCII Nummer in Zeichen
        # str wandelt dies in string
        pwd.append(str(chr(modasc).capitalize()))
    else:
        pwd.append(str(chr(modasc)))
    # Entfernen des ersten Elements
    tempdom.pop(0)

# Algorthmusschritt 2
# findall findet alle Ziffern im Namen
step2 = re.findall('[0-9]+', str(domain))
# Wenn Ziffern vorhanden
if len(step2) > 0:
    # Durch Ziffernliste iterieren
    for elements in step2:
        # Erstes Listenelement in integer wandeln
        j = int(step2[0])
        # Um zufälligen integer / ROT Wert verschieben
        j = j + random.randint(1, 9)
        # Zufällige Zahl wird als string dem Passwort beigefügt
        pwd.append(str(j))

# Algorithmusschritt 3
# Hänge ein zufälliges Sonderzeichen an das Passwort
special = string.punctuation
pwd.append(random.choice(special))

# Algorithmusschritt 4
# Hänge 2 zufällige Zahlen als string an das Passwort
for i in range(1, 3):
    pwd.append(str(random.randint(0, 9)))

# Algorithmusschritt 5
core = input("Gib einen beliebigen Passwortkern ein: ")
pwd.append(core)

# Algorithmusschritt 6
# Hänge ein zufälliges Sonderzeichen an das Passwort
special = string.punctuation
pwd.append(random.choice(special))

# Algorithmus Schritt 7
# Iteration durch die ersten zwei Elemente
# von tempdom2 welche eine umgekehrte tempdom ist
for i in tempdom2[0:3]:

    # verarbeiten des ersten Listenelements
    getlet = tempdom2[0]
    # Konvertierng in ASCII Nummer
    letasc = ord(getlet)
    # Zufällige ROT Verschiebung im Range
    modasc = letasc + random.randint(1, 9)
    # Zufallsgenerator der zwei Werte erlaubt
    generator = random.randint(0, 1)
    # je nach Wert wird Buchstabe groß oder kleingeschrieben
    if generator == 0:
        # chr() wandelt ASCII Nummer in Zeichen
        pwd.append(chr(modasc).capitalize())
    else:
        pwd.append(chr(modasc))
    # Entfernen des ersten Elements
    tempdom2.pop(0)

# Algirithmus Schritt 8
# pwd Liste wird in String umgewandelt
strpwd = ''.join([str(elem) for elem in pwd])

# Überprüfung ob Großbuchstaben in pwd vorkommen
if (any(x.isupper() for x in strpwd)):
    print(strpwd)

# Wenn nicht, wird ein Großbuchstabe hinzugefügt
else:
    upper = (chr(random.randint(ord('A'), ord('Z'))))
    strpwd = strpwd + upper
    print(strpwd)
