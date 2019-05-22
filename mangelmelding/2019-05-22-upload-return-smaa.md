Hva skal statuskode være etter opplasting av små filer?
=======================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.9 (Hente og overføre filer)
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Dette er relatert til mangelmelding #25 og endringsforslag #70, og
inneholder en klargjøring som manglet der.

Det står ikke noe i spesifikasjonen om hvilken statuskode som skal
returneres etter at en liten fil er lastet opp.  For store filer som
lastes opp i bulk, så skal det returneres 201 når opplastingen er
ferdig.  Tidligere returnerte Nikita 200 ved opplasting (før den fikk
støtte for bulkopplasting), men nå returnerer den 201 også for små
filer.  Jeg oppdaget endringen og problemet da et av mine skript
sluttet å fungere.  Hvilken kode skal brukes?  Det bør stå eksplisitt
i spesifikasjonen.

Ønsket endring
--------------

Foreslår at begge opplastingsmetodene, for både små og store filer,
returnerer samme statuskode når opplastingen er vellykket, og at dette
er 201.  Det bør legges inn en 'Respons: 201 Created' etter
POST-eksemplet under overskriften **Overføre små filer** i kapittel 6,
like før overskriften **Overføre store filer**.  I tillegg bør det
nevnes eksplisitt i teksten hvilken returkode som skal returneres.

Jeg tror meg følgende endring burde gjøre det klart hvilken statuskode
som skal returneres.

```
diff --git a/kapitler/06-konsepter_og_prinsipper.md b/kapitler/06-konsepter_og_prinsipper.md
index eeede3e..24ff88a 100644
--- a/kapitler/06-konsepter_og_prinsipper.md
+++ b/kapitler/06-konsepter_og_prinsipper.md
@@ -982,8 +982,9 @@ streames til klient
 **Overføre små filer**
 
 For å overføre en ny fil brukes POST til href til
-rel="http://rel.kxml.no/noark5/v4/api/arkivstruktur/fil/" med headere for
-content-type og content-length.
+rel="https://rel.arkivverket.no/noark5/v4/api/arkivstruktur/fil/" med
+headere for content-type og content-length.  Når overføringen er
+fullført og filopplastingen vellykket, så returneres statuskode 201.
 
 ```
 POST http://localhost:49708/api/arkivstruktur/Dokumentobjekt/a895c8ed-c15a-43f6-86de-86a626433785/referanseFil
@@ -993,12 +994,16 @@ Content-Length: 111111
 Pdf data
 ```
 
+Respons: 201 Created
+
 **Overføre store filer**
 
 For store filer (over 150MB) så kan filen overføres i
 bolker. Prosessen for å overføre store filer er inspirert av APIet til
 Google Drive,
-https://developers.google.com/drive/v3/web/resumable-upload .
+https://developers.google.com/drive/v3/web/resumable-upload .  For
+hver bolk returneres statuskode 200, unntatt den siste når
+overføringen er fullført der det returneres statuskode 201.
 
 For å starte en opplastingssesjon:
 
```
