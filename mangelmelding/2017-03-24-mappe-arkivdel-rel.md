Samkjør relasjonsliste for mappe i spesifikasjon og på rel.kxml.no
==================================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.16
         Sidenummer  133
        Linjenummer  
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Gjelder side 133 og 134.

Spesifikasjonens del 7.2.1.16 (Mappe) lister opp en rekke relasjoner
aktuelle for en mappe, men når en ser på eksemplet på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/ er det ingen av
relasjonene der som er omtalt i spesifikasjonen.  Base-URL er
forskjellig, dvs. at http://rel.kxml.no/noark5/v4/api/arkivstruktur/
og http://rel.kxml.no/noark5/v4/api/metadata/ brukes i
spesifikasjonen, mens http://rel.kxml.no/noark5/v4/ brukes i
eksempelet.

Selv om vi antar eksempelet har en skrivefeil, og
http://rel.kxml.no/noark5/v4/ skulle vært
http://rel.kxml.no/noark5/v4/api/arkivstruktur/, så er det likefult
noen relasjoner som ikke er omtalt i spesifikasjonen:

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/avslutt-mappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-basisregistrering/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-journalpost/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-presedens/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-sakspart/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-sekundaerklassifikasjon/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-undermappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/presedens/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/referanseArkivdel/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/referanseKlasse/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/referanseSekundaerKlassifikasjon/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/sakspart/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/utvid-til-moetemappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/utvid-til-saksmappe/

Flere av disse relasjonene ser ut til å være operasjoner det ville
vært nyttig å ha med i spesifikasjonen.

Det er til gjengjeld også noen relasjoner som kun finnes i
spesifikasjonen og ikke i eksempelet.

 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivdel/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/klasse/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/nasjonaleidentifikator/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-arkivdel/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-klasse/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-mappe/
 * http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-nasjonalidentifikator/
 * http://rel.kxml.no/noark5/v4/api/metadata/dokumentmedium/
 * http://rel.kxml.no/noark5/v4/api/metadata/mappetype/

Jeg mistenker f.eks at /arkivdel/ og /referanseArkivdel/ omhandler
samme relasjon, dvs. hvordan finne "foreldrearkivdel" for den gitte
mappen.  Jeg mistenker det samme for /klasse/ og /referanseKlasse/.

Ønsket endring
--------------

FIXME beskriv konkret forslag til endring
