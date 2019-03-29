Forvirrende om systemID-attributten til Arkivskaper
===================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1.4
         Sidenummer  81
        Linjenummer  ?
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Beskrivelsen av del 7.2.1.4 (Arkivskaper) på side 81 og 82 er litt
forvirrende.  Under restriksjoner står det at systemID skal være
utfylt, men ingen forklaring om hvorfor det er omtalt der og heller
ingen forklaring om hvorfor beskrivelsen som er en del av Arkivenhet 
ikke er tilstrekkelig.

Ønsket endring
--------------

Fjern informasjonen om restriksjoner på Arkivskapers systemID, da den
kun forvirrer og er redundant.

Konkret er det snakk om følgende endring:

```
diff --git a/kapitler/07-tjenester_og_informasjonsmodell.md b/kapitler/07-tjenester_og_informasjonsmodell.md
index 96e18b2..9f95936 100644
--- a/kapitler/07-tjenester_og_informasjonsmodell.md
+++ b/kapitler/07-tjenester_og_informasjonsmodell.md
@@ -426,12 +426,6 @@ Table: Attributter
 | arkivskaperNavn | Definisjon: Navn på organisasjonen som har skapt arkivet . Kilde: Registreres manuelt ved opprettelsen av arkivet. Kommentarer: (ingen). M023 | \[1..1\] | | string | 
 | beskrivelse | Definisjon: Tekstlig beskrivelse av arkivenheten. Kilde: Registreres  manuelt. Kommentarer: Tilsvarende attributt finnes ikke i Noark 4 (men noen tabeller hadde egne attributter for merknad som kunne brukes som et beskrivelsesfelt). M021 | \[0..1\] | | string |
 
-Table: Restriksjoner
-
-| **Navn**                                          | **Merknad** |
-| ------------------------------------------------- | ----------- |
-| Ny - Etter registrering skal systemID være utfylt |             |
-
 #### Basisregistrering
 
 *Type:* ***Class***
```
