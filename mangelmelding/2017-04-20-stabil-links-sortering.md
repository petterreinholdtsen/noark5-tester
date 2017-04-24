Kreves stabil rekkefølge på listene i \_links?
==============================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.2
         Sidenummer  13
        Linjenummer  n/a
    Innsendingsdato  2017-04-24
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Spesifikasjonen sier ingenting om rekkefølgen på relasjonene i \_links
skal være stabil, dvs. at det returneres samme rekkefølge hver gang en
API-et returnerer et resultat.  For å sikre at alle som implementerer
API-et, det være seg tjenere eller klienter, vet hva de kan forvente,
bør det nevnes i spesifikasjonen om rekkefølgen er stabil eller ikke.

For å sikre forutsigbare resultater fra API-et, og gjøre det enklere å
teste om API-et er korrekt (gjør det mulig å sammenligne resultatet
med forhåndslagrede resultater i stedet for å måtte sammenligne
individuelle elementer i returnerte lister), er det kanskje best om
det kreves stabil rekkefølge på listene i \_links?

Da «href»-verdiene ikke er standardiserte i spesifikasjonen, mens
«rel»-verdiene er standardiserte, er det antagelig best å sortere på
«rel»-verdiene.  Sortering er i utgangspunktet land og språkspesifikt,
og det kan være lurt å sikre stabilt resultat fra
tjenestegrensesnittet uansett hvilket språk som brukes på tjenermaskin
og klient.  Hvis en kan anta at relasjoner kun inneholder tegn
definert i ASCII (som er en delmengde av UTF-8), så kan en få entydig
sorteringsrekkefølge som ikke er avhengig av språk ved å henvise til
ASCII-verdi for tegnene.

Hvis verdiene ikke skal ha forutsigbar rekkefølge, så er det fint om
dette nevnes eksplisitt i spesifikasjonsteksten.

Ønsket endring
--------------

Legg inn en setning på slutten av første avsnitt av 6.1.1.2 (Finne
objekter (Read)) på side 13:

> Ressurslisten i _links er alfabetisk sortert på «rel»-feltet i
> henhold til ASCII-verdi.
