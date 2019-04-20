Klarere, entydig og mer kompakt representasjon av kodeliste-verdier i JSON for instanser
========================================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  versjon git 2019-04-19
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.6 (Utvid objekter til andre typer)
         Sidenummer  34
        Linjenummer  n/a
    Innsendingsdato  2019-04-20
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I kapittel 6 vises det hvordan verdier fra kodelister skal
representeres i JSON.  Det er ikke gjort konsistent.  Flere eksempler 
viser det slik:

```Python
"saksstatus": {
    "kode": "R",
    "beskrivelse": "Opprettet av saksbehandler"
},
```

Et annet eksempel inneholder ikke «beskrivelse» (også lenger ned i den
samme JSON-strukturen som bruker både «kode» og «beskrivelse» i
overnevnte eksempel):

```Python
"graderingskode": {
    "kode": "B"
},
```

Det er ikke beskrevet når «beskrivelse» skal brukes og når den kan
droppes i JSON som representerer en kodelisteverdi.  Det er også
uklart hvorfor «beskrivelse» er tatt med i hver JSON-representasjon av
instanser, når den kan hentes ut fra kodelistene ved behov.

Det er enklere for API-klienter og kortere som JSON (hvilket betyr en
mer nettverkseffektiv protokoll) hvis slike henvisninger til
kodelisteverdier dropper bruken av JSON-objekt (aka {...}) og i stedet
bruker kodeverdien direkte som string, dvs. slik:

```Python
"graderingskode": "B",
```

Dette krever at alle kodeliste-koder er unike for en gitt kodeliste,
hvilket bør stå eksplisitt i spesifikkasjonen.

Se forøvrig [mangelmelding
#147](https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/147),
med forslag om ny attributt «aktiv» for kodelister, hvis bruk
antagelig bør beskrives på samme sted hvis det forslaget blir tatt inn
i spesifikasjonen.

Ønsket endring
--------------

Beskriv i kapittel 6 hvordan JSON-strukturer som bruker
kodeliste-verdier skal se ut, hva som skal sendes inn ved oppretting
og endring og hva som sendes tilbake når en ber om en eller flere
instanser.  Endre alle eksempler til å følge denne notasjonen.
Beskriv kodeliste-attributten «aktiv» og forklar hvordan klienter skal
forholde seg til den ved å ikke bruke verdier der «aktiv» er «false».

Bruk kortformen der kun kode-verdi brukes ved oppretting, endring og
opplisting av instanser.  Nevn i kapittel 7.2.2 (Kodelister) at alle
oppføringer i kodelister må ha unike kode-verdier.

Jeg sender inn konkret forslag til endring som patch via github.

Respons
-------

Ingen respons fra arkivverket så langt.

Også registrert som
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/148 .
