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
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Spesifikasjonen nevner ikke hvilket tegnsett og tegnreportoar som skal
brukes i JSON-feltverdier eller XML-filer.  Det burde nevnes i del
6.1.1.8 om overføringsformat.  I sin ytterste konsekvens betyr det at
tegnsett ikke nevnes at klient og tjener må være forberedt på å ta
imot ethvert tegnsett, det være seg EBCDIC, ISO-8859-1, UTF-8 eller
UTF-32.

For XML er det veldefinert hvordan en spesifiserer hvilket tegnsett
som brukes, selv om fil-innhold og Content-Type bør stemme overens,
mens for JSON vil en være avhengig av hvilket tegnsett som oppgis i
hodefeltet Content-Type i HTTP-forespørselen for å vite hvordan
innholdet skal tolkes.  Feltet Content-Type er definert i [IETFs RFC
2616 del 14.17](https://tools.ietf.org/html/rfc2616#page-124).

Det blir enklere å lage både klient- og tjenerimplementasjoner hvis
tegnsett brukt i protokollen begrenses, og helst reduseres til et
tegnsett og reportoar.  Statens liste over obligatoriske og anbefalte
IT-standarder som gjelder for offentlig sektor sier at datasystemer
[skal bruke UTF-8](https://www.difi.no/artikkel/2015/10/tegnsett) med
mindre det er gode grunner til å bruke noe annet.  Det virker dermed
naturlig å la UTF-8 være utgangspunktet, og eventuelt vurdere å
tillate andre tegnsett i unntakstilfeller.  Slike unntakstilfeller bør
i så fall oppgi tegnsett i tråd med RFC 2616, dvs. slik at
forespørsler med JSON kodet som ISO-8859-1 ville ha
«application/vnd.noark5-v4+json; charset=ISO-8859-1» som Content-Type.

Ønsket endring
--------------

Det legges inn et nytt avsnitt i del 6.1.1.8 (Overføringsformat) på
side 25 under tabell over «Innholdstype (Content-Type)» med følgende
innhold:

> Overføring av JSON og XML skal UTF-8-kodes i tråd med ISO/IEC
> 10646.
