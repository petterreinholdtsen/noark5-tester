Feil i definsjonen av  arkivskaperNavn og tilknyttetRegistreringSom i metadatakatalogen
============================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Metadatakatalog
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  
        Dokumentdel  
         Sidenummer  10
        Linjenummer  n/a
    Innsendingsdato  Ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------
I [metadatakatalogen](https://www.arkivverket.no/forvaltning-og-utvikling/noark-standarden/noark-5/noark5-standarden/_/attachment/download/9f16ce02-80e7-48d4-b6ac-a01bcaa27858:e31d3dd2f0b988cda2d254d9e1f3004b668bca4c/Noark%205%20v%205%20vedl1%20Metadatakatalog.pdf) 
(side 10) for Noark 5 versjon 5 er det en feil tilknyttet definisjonen av 
attributtet 'M023 arkivskaperNavn'. Det står at arkivskaperNavn er tilknyttet 
arkivenheten *arkiv*. Det skal stå at  arkivskaperNavn er tilknyttet 
arkivenheten *arkivskaper*. Videre står det at attributtet forekommer
mange ganger, men fra XSD ser vi at dette ikke stemmer. Det skal forekomme
en gang.

Attributtet 'M217 tilknyttetRegistreringSom' (side 23/24) har også en feil der det står at
tilknyttetRegistreringSom forekommer mange ganger under dokumentbeskrivelse.
Utifra XSD definisjonen, ser vi at det forekommer en gang.

Merk feilen gjelder også for Noark 5 versjon 4.

Ønsket endring
--------------
Attributtet 'M023 arkivskaperNavn' blir endret i metadatakatalogen 
slik at det har en  tilknytning til arkivenhet *arkivskaper* og
forekomst egenskapen blir en endret til 'En'. 

Forekomst egenskapen til attributtet 'M217 tilknyttetRegistreringSom' blir 
endret til 'En'.

Respons
-------

Ingen respons fra Arkivverket så langt.
