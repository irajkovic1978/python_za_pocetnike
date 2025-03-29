 ##### OPERATORI #####

 # Vrste operatora #
    #Aritmetički
    # Operatori dodjele
    #  Opreratori poređenja
    # Logički operatori

### PRIMJERI ###



##############################
# Aritmetički operatori (zbrajanje, oduzimanje, ostaka prilikom djeljenja, ....
##############################

# Zbrajanje +
print(10+20)
a = 10
b = 5
c = a+b
print (c)

a = "Renault"
b = "4"
print (a + "" + str(b))

# Oduzimanje    -

a = 100
b = 20
print (a-b)

# Množenje
a = 8
b = 5
b="Loop"
print (a*b)

# Djeljenje /
a = 25
b = 5
c = a/b
print (c)
print (type(c))

# Cjelobrojno djeljenje     //
a = 100
b = 50
c = a//b
print (c)
print (type(c))

# Ostatak prilikom djeljenja   %
a = 15
b = 4
c = a % b
print (c)
print (type(c))

# Eksponent
print (4 ** 3)

# REdoslijed operacija
print(3 + 4 + 5 - 2 * 10)
print ((2*5) + (10//3))

##############################
### OPERATORI DODJELE ####
##############################

# =
a = 100
print(a)

# +=
a = 50
a += 30 # a = 50 + 30
print (a)

# -=
a = 50
a -= 10 # a = 50 - 10
print(a)

# Množenj *=
a = 5
a *= 20 # a = 5 * 20
print (a)

# Podijeljeno /=
a = 100
a //= 5 # a = 100 /5
print(a)

##############################
### OPERATORI POREĐENJA #### ili je true ili je false (boolean)
##############################

# == a == b (jednako sa)
print (4 == 4)
print (4 == "4")

print ("Python" == "python")
print ("Python" == "Python")

a = 5
b = 5
print (a == b)

print (4 == 4.0)

# != (nije jednako)
print (100 != 1000)

# > Veće od
print (100 > 1)

# < Manje od
print (20 < 200)

# >= Veče i jednako
print (10 <=10)

# <= Manje i jednako
print (10 + 100 <= 100)

##############################
### LOGIČKI OPERATORI ####
##############################
# and
# or
# not

print (10 < 20 and 100 > 80)

a = 5
print (a == 5 and a == 10)


a = 5
print (a == 5 or a == 10)


a = 100
b = 10
print (not(a == b))
print (not(200 > 10))