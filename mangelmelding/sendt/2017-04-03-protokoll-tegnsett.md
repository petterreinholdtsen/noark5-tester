Klargjør standard tegnsett og om flere tegnsett aksepteres
==========================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.8
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  2017-04-03
 ------------------  ---------------------------------

Beskrivelse
-----------

Spesifikasjonen nevner ikke hvilket tegnsett og tegnrepertoar som skal
brukes i JSON-feltverdier eller XML-filer.  Det burde vel nevnes i del
6.1.1.8 om overføringsformat.  En anerkjent definisjon av
JSON-formatet finnes i [RFC
4627](https://www.ietf.org/rfc/rfc4627.txt), og den sier at en
JSON-streng er definert som «a sequence of zero or more Unicode
characters».  Hvis denne definisjonen legges til grunn innebærer dette
at et Noark 5 tjenestegrensesnitt må kunne motta en hvilken som helst
måte å kode Unicode-tegn, f.eks. UTF-8, UTF-16 eller UTF-32 når JSON
brukes som overføringsformat.

Når det gjelder bruk og overføring av XML innebærer det vel at
tjenestegrensesnittet må støtte alle tegnsett som støttes av
[XML](https://www.w3.org/TR/REC-xml/#charencoding) og ytterste
konsekvens betyr det at klient og tjener må være forberedt på å ta
imot ethvert tegnsett, det være seg EBCDIC, ISO-8859-1, UTF-8 eller
UTF-32.

For XML er det veldefinert hvordan en spesifiserer hvilket tegnsett
som brukes, selv om naturligvis fil-innhold og tegnsett oppgitt i
Content-Type bør stemme overens.  For JSON vil en være avhengig av
hvilket tegnsett som oppgis i hodefeltet Content-Type i
HTTP-forespørselen for å vite hvordan innholdet skal tolkes.  Feltet
Content-Type er definert i [IETFs RFC 2616 del
14.17](https://tools.ietf.org/html/rfc2616#page-124).

Det blir enklere å lage både klient- og tjenerimplementasjoner hvis
tegnsett brukt i protokollen begrenses, og helst reduseres til et
tegnsett og repertoar.  Listen over obligatoriske og anbefalte
IT-standarder som gjelder for offentlig sektor sier at nye
datasystemer [skal bruke
UTF-8](https://www.difi.no/artikkel/2015/10/tegnsett) med mindre det
er gode grunner til å bruke noe annet.  Det virker dermed naturlig å
la UTF-8 være utgangspunktet, og eventuelt vurdere å tillate andre
tegnsett i unntakstilfeller.  UTF-8 er beskrevet i [IETF RFC
3629](https://tools.ietf.org/html/rfc3629) og ISO/IEC 10636.

For bruk av JSON i slike unntakstilfeller bør en i så fall nevne i
spesifikasjonen at tegnsett skal oppgis i tråd med IETF RFC 2616, dvs. slik
at forespørsler med JSON kodet som ISO-8859-1 ville ha
«application/vnd.noark5-v4+json; charset=ISO-8859-1» som Content-Type.

Relatert til dette bør det jo nevnes at krav 5.12.4 i Noark
5-standarden angir at UTF-8 er eneste gyldig tegnsett for uttrekk.
Det blir enklere å sikre korrekte uttrek hvis tjenestegrensesnittet
kun tar imot UTF-8, slik at en slipper å implementere omkoding av
innholdet i databasen når det skal lages uttrekk.

Ønsket endring
--------------

Det legges inn et nytt avsnitt i del 6.1.1.8 (Overføringsformat) på
side 25 under tabell over «Innholdstype (Content-Type)» med følgende
innhold:

> Tjenestegrensesnittet skal bruke UTF-8 som beskrevet i IETF RFC 3629
> i alle REST-forespørsler, både for JSON og XML.

Respons
-------

Ingen respons fra arkivverket så langt.
