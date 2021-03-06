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
    Innsendingsdato  2019-03-05 (github issue #72)
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I punkt 6.1.1.9 (Hente og overføre data) side 25 står det ikke hvordan
Accept-hodefeltet skal håndteres i en GET-forespørsel mot href til
relasjonsnøkkelen
'http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil/'.  Hva skal skje
hvis en API-klient forsøker å bruke GET når GET-forespørselens
Accept-hodefelt ikke har en verdi som stemmer overens med MIME-typen
til filen som etterspøres?  Hvis Accept-verdi og filens MIME-type er
like, er det klart at at filen skal returneres.  Usikkerheten oppstår
med forespørsler det Accept-verdien ikke passer med filens MIME-type.
Da har jo klienten eksplisitt sagt at den ikke ønsker en fil med det
aktuelle formatet.

Anta at en XML-fil er lagret med MIME-type application/xml, og
deretter bes lastet ned med denne forespørselen:

```
GET .../referanseFil
Accept: application/pdf
```

Skal filen returneres, eller skal det returneres en feilkode i stedet?
Alternativt, skal bruken av Accept-hodefeltet i dette API-kallet
forbys?

HTTP-standarden ([IETF RFC
2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)) sier
at Accept-hodefeltet er frivillig, men hvis det finnes og
tjenermaskinen ikke kan sende en akseptabel respons så skal statuskode
406 (not acceptable) returneres.

En enkel tilnærming er å beskrive i spesifikasjonen hvorvidt en
GET-forespørsel for å hente ut en fil skal ha Accept-hodefeltet satt,
og hvis det er satt og ikke er identisk med MIME-typestrengen i
dokumentobjekt så skal det returneres statuskode 406.

Ønsket endring
--------------

Foreslår at standarden enkelt dokumenterer at Accept enten ikke skal være
satt, inneholde samme MIME-type som i dokumentobjekt eller «*/*» som betyr
at et hvilket som helst format aksepteres.

Foreslår derfor at kapittel 6.1.1.9 (Hente og overføre filer) endres,
avsnittet «Gir Content-type=filens mime type feks «application/pdf» og
filen streames til klient» byttes ut med:

> «Returnerer filens innhold.  Hodefeltet Content-type settes til
> filens MIME-type hentet fra dokumentobjekt-entiteten.  Merk,
> GET-forespørselen bør ikke inneholde HTTPs Accept-hodefelt.
> HTTP-hodefeltet Accept brukes til å gi beskjed hvilket helst format
> som ønskes lastet ned, og klienten har ikke noe valg av format og
> bør derfor ikke forsøke å styre valg av format.  Hvis
> Accept-hodefeltet er satt, og ikke inneholder enten «*/*» eller er
> identisk med verdien i mimeType-feltet til tilhørende
> dokumentobjekt, så skal resultatkoden 406 returneres i stedet for
> 200.»


Respons
-------

Ingen respons fra arkivverket så langt.

Rapportert til
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/72
