## tipovi podataka -- mogu da ponesu jednu vrijednost
    # integers
    # floats
    # bool
    # strings

# Strukture podataka - ako želimo da u jednu promjenjivu smestimo više podataka i na taj način rješavamo
# problem da nemamo samo jednu vrijednost
    # liste
    # torke (tuples)
    # sets (skupovi)
    # dictionary (riječnici)


#############
## LISTE ####
#############

vozac = "Ivan"
automobili = ["Renault", "Peugeout", "BMW", "Mercedes", "Audi"]
#               0           1           2       3           4
print (vozac + " preferira u zadnjih desetak godina " + automobili[0])
print (len(automobili))

kurs = ["backend", 3, "Ivan"]
#           0       1   2
print (kurs [0] + " kurs traje " + str(kurs [1]) + "mjeseca i predavač je " + kurs [2])

lista = [6, "string neki", True, False, ["pythnos", "sql"]]
print (type(lista))

#############
## TORKE (TUPLES) ####
######################

program = ("html i css", "python", "django", "sql")
print (program)
print (type(program))

ww_predavaci = ("Ivan", "Boban", "Danijel", "Jovana", "Zoran", "Sloba M.")
print (ww_predavaci)
print (len(ww_predavaci))

termini = ("pythnos i sql kurs", 3, True, "Zoran", "Slobodan")
print(termini)
print (termini[0] + " traje " + str(termini[1]) + " mjeseca")

programski_jezici = "python", "sql", "php", "java", "dart", "php", "c##"
print (type(programski_jezici))
print (programski_jezici[0] + " je odličan izbor za bekend")

test = ("jedan",)
print(type(test))

######################
## SETS (SETOVI   ####
######################

upis = {"februar", "maj", "septembar", "decembar", "februar", "maj", "septembar"}
print (upis)
print (type(upis))

test = {"stringovi", 3, 3.14, True}
print (test)


######################
## DICTIONARY   ####
######################

#           key         value
kursevi = {"Sloba": "PHP i MySQL",  "Boban": "HTML i CSS", "Danijel": "JavaScript", "Jovana": "React", "Zoran": "Python i MySQL", "Sloba Z.": "Pythno i MySql"}

print (kursevi)
print (type(kursevi))

print (kursevi["Sloba"])
print (kursevi["Boban"])
print ("Danijel predaje " + kursevi ["Danijel"] + " a " + "Jovana predaje " + kursevi ["Jovana"])

projekti = {"prvi projekat": 6, "drugi projekat": [2,2,2]}
print ("Prvi projekat traje " + str(projekti["prvi projekat"]) + " mjeseci")
print ("Drugi projekat traje" + str(projekti["drugi projekat"]) + " mjeseci")