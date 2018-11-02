#!/usr/bin/python2
#
# Muuntaa roomalaisen numeron kymmenjarjestelmaan kometorivilla
# kaytto python numeromuunnin.py 'Muunnettava roomalainen numero'

import sys
from parsettaja import * #Oma funktio

if len(sys.argv)<2:
    print 'Unohdit antaa komentorivilla syotteen. Anna Roomalainen numero jonka haluat kaantaa'
    sys.exit('Tyhjasta paha nyhjasta')

roomalainen = str(sys.argv[1]) # perinne javasta, pitaa varmistaa et python tulkitsee tyypin oikein

print 'Annoit syotteen: ' + roomalainen
print ''

########################################
# HUOMIOIDAAN PERUSMERKIT SEURAAVASTI  #
#
# I = 1 
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
#########################################

####### Quick validation tests #######
### Consecutive same symbols        ##
######################################

## Luodaan dictionary tyylinen rakenne sallituista, jotta tarkastetaan onko numerot oikeanlaisia.
## tarkastus tehdaan dictionaryn in tyokalulla.

sallitut = { "I":"ykkonen",
             "V":"V",
             "X": "X",
             "L":"L",
             "C":"C",
             "D":"D",
             "M":"M" }


for i in range (0,len(roomalainen)):
    if roomalainen[i] in sallitut:
        #print roomalainen[i] +' on sallittu merkki'
        pass # Ei voi olla tyhjaa if-lausetta
    else:
        print 'VIRHE, Ohjelma keskeytetaan'
        sys.exit(roomalainen[i] + ' on laiton merkki')
        
#kaytetaan toisaalla maariteltya hajotelma-funktiota
# Antaa roomalaisen numeron ja lisaksi ehtona sallittujen perattaisten numeroiden maaran
# Antaa ulos datan listamuodossa, jossa ensimmaisena viimeinen kirjain ja sen lukumaara

max_consecutive = 3; #jotta voidaan sallia halutessa myos syntaksit IIII

lista = parsettaja(roomalainen,max_consecutive) #Maaritelty omassa filessa
laskettavia = len(lista)

print ''
print lista

lukuarvot = []
for i in range(0,laskettavia):
    if lista[i][0] == 'I':
        normiluku = 1
    elif lista[i][0] == 'V':
        normiluku = 5
    elif lista[i][0] == 'X':
        normiluku = 10
    elif lista[i][0] == 'L':
        normiluku = 50
    elif lista[i][0] == 'C':
        normiluku = 100
    elif lista[i][0] == 'D':
        normiluku = 500
    elif lista[i][0] == 'M':
        normiluku = 1000
    lista[i][0]= normiluku
print lista
##########################################
####### Suoritetaan lopuksi laskenta #####
##########################################

alkuluku = lista[0][0]*lista[0][1] #Ensimmainen luku on aina positiivinen

##########################################################################################
### Toinen luku on positiivinen jos sen numeroarvo on isompi kuin edellisessa kohdassa ###
### Jos luku on pienempi, niin luku vahennetaan, jos hahmotin numerot oikein           ###
##########################################################################################

for i in range(1,laskettavia):
    if lista[i][0] < lista[i-1][0]: # Negatiivinen luku
        alkuluku = alkuluku - lista[i][0]*lista[i][1]
        if lista[i][1] > 1:
            sys.exit('Ala kayta liikaa vahentavia lukuja, merkinta laiton')
    else:
        alkuluku = alkuluku + lista[i][0]*lista[i][1]
### Jos halutaan olla tarkkoja etta mitka luvut hyvaksytaan, niin ylapuolelle voisi rakentaa logiikkaa
### jossa errori tulee silloin jos perattaisten lukujen ero on liian suuri
### Nyt esim MMMCMXCIX = MMMIM = 3999 vaikka MMMIM on laiton
### Oikeaoppisesti luvun edessa voisi ilmeisesti olla vain vahentava luku joka ei ole yli 10x edeltajaa pienempi
###
### Ohjelma sallii viela myos peilikuvaluvut, jossa lisattava ja vahennettava osuus on sama, esim IVI=5 tai IVII =6

print ''
print 'Roomalainen numero ' + roomalainen + ' on kymmenkantaisena lukuna '        
print alkuluku


