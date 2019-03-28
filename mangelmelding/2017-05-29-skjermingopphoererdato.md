Korriger staving av attributtnavn «skjermingOpphørerDato»
=========================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.19 (Skjerming)
         Sidenummer  40
        Linjenummer  n/a
    Innsendingsdato  Ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Gjelder side 40, 44, 55 og 152.

Spesifikasjonen bruker attributtnavnet «skjermingOpphørerDato» (med ø)
i beskrivelsen av datatype Skjerming og i UML-diagrammene
uml-arkivenheter-som-har-noe-med-bevaring-og-kassasjon-aa-gjoere
uml-arkivstruktur-arkiv-og-arkivdel og uml-arkivstruktur-skjerming.
Dette er en skrivefeil for metadatafelt M505 skjermingOpphoererDato.

Merk at tilsvarende gjelder for en rekke andre felt i UML-skjemaene.
Ved å gjøre "egrep -i '[æøå].*:' media/*uml|cut -d: -f2-|cut -d+
-f2-|awk '{print $1}'|sort -u" ser en følgende felter med æøå i seg:
avskrivningsmåte, elektroniskSignaturSikkerhetsnivå,
endringsløpenummer, filstørrelse, fødselsnummer, gårdsnummer,
journalår, konverteringsverktøy, møtedato, møtenummer,
møteregistreringsstatus, møteregistreringstype, møtesakstype,
møtested, nøkkelord, referanseForløper, referanseForrigeMøte,
referanseFraMøteregistrering, referanseNesteMøte,
referanseTilMøteregistrering, referanseUtlånttil, referanseUtlåntTil,
saksår, skjermingOpphørerDato, utførtKassasjon, utlåntDato og
utlåntTil.  Jeg vil sende inn egen mangelmelding for hver av disse
disse hvis de ikke blir fikset i spesifikasjonsteksten raskt.

Ønsket endring
--------------

Endre alle forekomster av «skjermingOpphørerDato» til «skjermingOpphoererDato»
