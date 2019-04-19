Entydig og mer kompakt representasjon av kodeliste-verdier i JSON?
==================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  
         Sidenummer  
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I kapittel 6 vises det hvordan verdier fra kodelister skal
representeres i JSON.  Det er ikke gjort konsistent.  Flere eksempel
viser det slik:

```Python
"saksstatus": {
    "kode": "R",
    "beskrivelse": "Opprettet av saksbehandler"
},
```

Andre eksempel viser det slik (også lenger den i samme JSON-struktur
som viser overnevte eksempel):

```Python
"graderingskode": {
    "kode": "B"
},
```

Det er ikke beskrevet når "beskrivelse" skal brukes og når den kan
droppes.  Det er også uklart hvorfor "beskrivelse" er tatt med i hver
JSON-representasjon av instanser, når den kan hentes ut fra
kodelistene ved behov.

Det er enklere for API-klienter og kortere som JSON (dvs. mer effektiv
protokoll) hvis slike henvisninger til kodelisteverdier dropper
JOSN-objekt og i stedet bruker kodeverdien direkte, dvs. slik:

```Python
"graderingskode": "B",
```

Ønsket endring
--------------

Beskriv i kapittel 6 hvordan JSON-strukturer som bruker
kodeliste-verdier skal se ut, hva som skal sendes inn ved oppretting
og endring og hva som sendes tilbake når en ber om en eller
flereinstans.  Endre alle eksempler til å følge denne notasjonen.

Bruk kortformen der kun kode-verdi brukes ved oppretting, endring og
opplisting av instanser.
