# -*- coding: utf-8 -*-

""" CELCIUS (SANTIGRAT) - START """
# Celcius(santigrat) to Fahrenheit
celcius = input("Fahrenheit'a çevirmek istediğiniz Celcius(santigrat) değerini giriniz: ")
fahrenheit = celcius*1.8+32
print ("%s Celcius %s Fahrenheit a eşittir" % (celcius, fahrenheit))

# Celcius(santigrat) to Kelvin
celcius = input("Kelvin'e çevirmek istediğiniz Celcius(santigrat) değerini giriniz: ")
kelvin = celcius+273.15
print ("%s Celcius %s Kelvin  a eşittir" % (celcius, kelvin))

# Celcius(santigrat) to Rankine
celcius = input("Rankine'ye çevirmek istediğiniz Celcius(santigrat) değerini giriniz: ")
rankine = (celcius+273.15)*9/5
print ("%s Celcius %s Rankine  a eşittir" % (celcius, rankine))

""" CELCIUS (SANTIGRAT) - FINISH """

# <-----------------------------------------------------------------------------------------------> #

""" Fahrenheit - START """
# Fahrenheit to Celcius(santigrat)
fahrenheit = input("Celcius(santigrat)'a çevirmek istediğiniz Fahrenheit değerini giriniz: ")
celcius = (fahrenheit-32) / 1.8
print ("%s Fahrenheit %s Celcius a eşittir" % (fahrenheit, celcius))

# Fahrenheit to Kelvin
fahrenheit = input("Kelvin'e Çevirmek istediğiniz Fahrenheit değerini giriniz: ")
kelvin = (fahrenheit+459.67) * 5/9
print ("%s Fahrenheit %s Kelvin a eşittir" % (fahrenheit, kelvin))

# Fahrenheit to Rankine
fahrenheit = input("Rankine'ye çevirmek istediğiniz Fahrenheit değerini giriniz: ")
rankine = fahrenheit+459.67
print ("%s Fahrenheit %s Rankine a eşittir" % (fahrenheit, rankine))

""" Fahrenheit - FINISH """

# <-----------------------------------------------------------------------------------------------> #

""" KELVİN - START """
# Kelvin to Celcius(santigrat)
kelvin = input("Celcius(santigrat)'a çevirmek istediğiniz Kelvin değerini giriniz: ")
celcius = kelvin-273.15
print ("%s Kelvin %s Celcius  a eşittir" % (kelvin, celcius))

# Kelvin to Fahrenheit
kelvin = input("Fahrenheit'a çevirmek istediğiniz Kelvin değerini giriniz: ")
fahrenheit = kelvin*9/5-459.67
print ("%s Kelvin %s Fahrenheit  a eşittir" % (kelvin, fahrenheit))

# Kelvin to Rankine
kelvin = input("Rankine'ye çevirmek istediğiniz Kelvin değerini giriniz: ")
rankine = kelvin*9/5
print ("%s Kelvin %s Rankine  a eşittir" % (kelvin, rankine))

""" KELVİN - FINISH """

# <-----------------------------------------------------------------------------------------------> #

""" RANKİNE - START """
# Rankine to Celcius(santigrat)
rankine = input("Celcius(santigrat)'a çevirmek istediğiniz Rankine değerini giriniz: ")
celcius = (rankine-491.67)*5/9
print ("%s Rankine %s celcius  a eşittir" % (rankine, celcius))

# Rankine to Fahrenheit
rankine = input("Fahrenheit'a çevirmek istediğiniz Rankine değerini giriniz: ")
fahrenheit = rankine-459.67
print ("%s Rankine %s Fahrenheit  a eşittir" % (rankine, fahrenheit))

# Rankine to Kelvin
rankine = input("Kelvin'e çevirmek istediğiniz Rankine değerini giriniz: ")
kelvin = rankine*5/9
print ("%s Rankine %s Kelvin  a eşittir" % (rankine, kelvin))

""" RANKİNE - FINISH """

# by erhan 2019
