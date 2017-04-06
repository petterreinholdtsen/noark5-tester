Hvordan gjøres SystemdID unik og persistent på tvers av andre systemer?
=======================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.3
         Sidenummer  28
        Linjenummer  ?
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I følge del 6.3 (Identifikatorer) skal arkivkjernen sørge for at
systemID blir en unik og persistent identifikator på tvers av andre
systemer.  Men hvordan skal dette gjøres uten sentral koordinering?
En enkelt leverandør kan jo ikke garantere at ingen andre lager ID-er
som får samme verdi som det leverandøren selv lager.  Slik teksten
står i dag i spesifikasjonen kan jo én leverandør velge UUID og en
annen velge en annen algoritme som gir samme verdier som leverandøren
som bruker UUID, uten å vite om hverandre.  Er det meningen at
leverandørene skal koordinere seg imellom for å unngå ID-kollisjoner
uten sentralisert styring?  Holder det at det er liten sjanse for
kollisjoner, ved å bruke for eksempel tilfeldig UUID slik det er
definert i [IETF RFC 4122](http://www.ietf.org/rfc/rfc4122.txt),
ISO/IEC 9834-8:2004 og ITU-T Rec. X.667?

I så fall, bør systemID avledes fra verdier i objektet det henviser
til, eller bør det være frakoblet dette?  Svaret på dette spørsmålet
avgjør hvilken algoritme fra RFC 4122 som er aktuell hvis en skal lage
en UUID.  Det kan være problematisk å avlede systemID fra verdier i
objektet den omhandler hvis objekter med samme innhold skal ha ulik
systemID.

Hvis ikke UUID foreslås, så bør det beskrives en annen metode som
sikrer at leverandører er i stand til å velge unike ID-er som ikke gir
ID-kollisjoner.

Ønsket endring
--------------

Foreslå tilfeldig UUID som akseptabel systemID-verdi ved å legge inn
følgende under 6.3 på side 28:

> En mulig måte å lage systemID-verdier er å følge UUID-algoritmen
> beskrevet i [IETF RFC 4122](http://www.ietf.org/rfc/rfc4122.txt),
> ISO/IEC 9834-8:2004 og ITU-T Rec. X.667.  Slike UUID-verdier bør
> være frakoblet verdiene i objektet det henviser til.
