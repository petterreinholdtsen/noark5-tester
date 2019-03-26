Klargjør hvor listen med aksepterte formater og deres formatverdier finnes
==========================================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.9
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

se også mangelmelding/sendt/2018-09-07-format-png.txt

M701

Del 6.1.1.9 (Hente og overføre filer) skisserer hvordan lagre PDF og
JPEG i arkivet.  Her kunne det med fordel legges inn en henvisning til
kodelisten Format på side 173 for å forklare hvor listen med formater
kan finnes.

Det trengs en liste med hvilke MIME-typer som skal brukes for de ulike
formatene, og en prosedyre som de som lager arkivløsninger kan bruke
for å registrere formater som ikke er på listen over formater som kan
deponeres.  Dette vil sikre at alle arkivsystemer bruker de samme
verdiene slik at det blir enklere å migrere data fra en arkivløsning
til den neste.

Men hvor finnes listen over hvilke formater som er
akseptert inn i arkivet og hvilke MIME-typer som bør brukes for disse?
Hva med RFC 822-type epost?  SMS?  Lydfiler?

se side 173 (format)

Hva skal gjøres når det trengs å arkiveres formater som ikke er på listen?

Epost-ideer finnes i
&gt;URL: http://people.skolelinux.org/pere/blog/Hvordan_b_r_RFC_822_formattert_epost_lagres_i_en_NOARK5_database_.html >.

Noark 5 krav 8.1.8 (side 197) sier at epost skal lagres i et enhetlig,
samlet format som gjengir både e-posthode og e-postmelding, men
forklarer ikke hvordan det skal gjøres.

Ønsket endring
--------------

FIXME
