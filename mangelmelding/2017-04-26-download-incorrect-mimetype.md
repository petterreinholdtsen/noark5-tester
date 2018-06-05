Hvordan skal HTTP-hodefeltet Accept tolkes ved forsøk på filnedlasting?
=======================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.9
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I punkt 6.1.1.9 (Hente og overføre data) side 25 står det ikke hvordan
Accept-hodefeltet skal håndteres i en GET-forespørsel.  Hva skal skje
hvis en API-klient forsøker å bruke GET mot href til relasjonsnøkkelen
'http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil/' når
GET-forespørselens Accept-hodefelt ikke har en verdi som stemmer
overens med MIME-typen til filen som etterspøres?  Hvis Accept-verdi
og filens MIME-type er like, virker det klart at at filen skal
returneres.  Men skal den også returneres det Accept-verdien ikke
passer med filens MIME-type?

Hvis en antar at en XML-fil er lagret med MIME-type application/xml,
og så forsøkes nedlastet med denne forespørselen:

```
GET .../referanseFil
Accept: application/pdf
```

Skal filen returneres, eller skal det returneres en feilmelding?
Alternativt, skal bruken av Accept-hodefeltet i dette API-kallet
forbys?

[IETF RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)
sier at at Accept-hodefeltet er frivillig, men hvis det finnes og
tjenermaskinen ikke kan sende en akseptabel respons så skal statuskode
406 (not acceptable) returneres.

Accept-verdien i HTTP kan brukes til å la tjenermaskinen velge beste
utgave av filen som skal returneres, hvilket gir mest mening når det
finnes flere varianter av en fil å velge blant, slik en kan ha på
dokumentbeskrivelse-nivå, men ikke på dokumentobjekt-nivå.

Kan det være en ide å gjøre det mulig å be om å få laste ned en av
flere filer fra et dokumentbeskrivelse-objekt, med relasjonsnøkkelen
'http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil/' i \_links og
dermed kunne laste ned enten PDF- eller XLS-fil ved å gjøre en slik
forespørsel:

```
GET .../referanseFil
Accept: application/pdf; q=0.5, application/vnd.ms-excel,
```

FIXME beskriv forslag og hvorfor forslaget vi kommer med er en god ide.

Ønsket endring
--------------

> GET http://localhost:49708/api/arkivstruktur/Dokumentobjekt/a895c8ed-c15a-43f6-86de-86a626433785/referanseFil
>
> Gir Content-type=filens mime type feks “application/pdf” og filen
> streames til klient

FIXME kom opp med et forslag om hvordan Accept skal tolkes?
