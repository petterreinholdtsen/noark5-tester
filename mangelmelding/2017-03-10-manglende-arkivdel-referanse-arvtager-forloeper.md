Manglende beskrivelse av referanseForloeper/referanseArvtager for arkivdel
==============================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  7.2.1.2
         Sidenummer  66
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------
Det mangler rel beskrivelser for referanseForloeper/referanseArvtager i tabellen
relasjonsnøkler på side 66.


Ønsket endring
--------------

Denne operasjonen kan utføres på to måter:

[PUT] arkivstruktur/arkivdel/{systemIdForloeper}/referanseArvtager/{systemIdArvtager}/
[PUT] arkivstruktur/arkivdel/{systemIdArvtager}/referanseForloeper/{systemIdForloeper}/

Her identifiseres arvtager og forloeper i HTTP-requesten eller

[PUT] arkivstruktur/arkivdel/{systemIdForloeper}/referanseArvtager/
[PUT] arkivstruktur/arkivdel/{systemIdArvtager}/referanseForloeper/

Her identifiseres arvtager og forloeper i HTTP-body.

Videre bør det spesifiseres om koblingen framover/tilbake utføres automatisk

dvs hvis jeg kobler A til B, der A er forløper, skal kjernen automatisk koble
B til A.
