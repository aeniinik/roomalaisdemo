import sys
######## Parsettaja roomalaisten numeroiden kasittelyyn ##########
##
## Kaksi inputtia
## 
## Ekana muutettava numerosarja, tokana suurin sallittu perattaisten symbolien maara
## 
## Luo ja palauttaa listan esiintyvista kirjaimista lopusta alkuun siten, etta listaan lisataan lukuparit seuraavasti
##
## [Viimeisena jaljella oleva kirjain][kirjainten lukumaara]


def parsettaja(x,y):
    peilikuva = str(x)[::-1] #Kaannetaan roomalaisten numeroiden syote peilikuvaksi, kivempi tyostaa

    print 'Tehdaan numerosta peilikuva:' #Helpottaa syotteen tsekkaamista konsolissa
    print 'jaannos on: ' + peilikuva

    lista2 = []

    #poistetaan numerosta aina samat pois. Muttuja peilikuva lyhenee prosessissa
    while len(peilikuva) > peilikuva.count(peilikuva[0]):
        tunnus = peilikuva[0] #otetaan aina typistetyn sarjan eka osio
        tunnusLkm = 1
        while peilikuva[tunnusLkm-1] == peilikuva[tunnusLkm]:
            #print  'tunnusLkm: ' + str(tunnusLkm)
            #print  'len(peilikuva) ' + str(len(peilikuva))
            tunnusLkm = tunnusLkm +1
            if tunnusLkm > y: #virheen tsekkaus lukumaaran osalta, y syotteena funtioon
                sys.exit('\n\rVirhe: Liian monta perakkaista numeroa, tarkasta syote')
        lista2.append([tunnus, tunnusLkm])
        #debugging jatetty print-komennoilla
        #print 'tunnus: ' + tunnus
        #print 'tunnusLkm: ' + str(tunnusLkm)

        #Poistetaan syotteesta kirjaimet, jotka lisattiin taulukkoon
        peilikuva = peilikuva[tunnusLkm:]
        print 'jaannos on: ' + peilikuva

    #Lisataan vimeinen numero ja sen lukumaara taulukkoon
    #Kaikki jaljella olevat samaa, koska edellinen while-looppi loppuu kun enaa samaa jaljella.
    tunnus = peilikuva[0]
    tunnusLkm = len(peilikuva)

    if tunnusLkm > y: # Virheen tsekkaus lukumaaran osalta, y syotteena funktioon
        sys.exit('\n\rVirhe: Liian monta perakkaista numeroa, tarkasta syote')
    lista2.append([tunnus, tunnusLkm])
    
    return lista2
