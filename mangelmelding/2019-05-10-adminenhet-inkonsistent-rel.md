To ulike relasjonsnøkler til administrativenhet?
================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.4.2 (Bruker)
         Sidenummer  259
        Linjenummer  n/a
    Innsendingsdato  Ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det ser ut til at relasjonsnøkkellisten for Bruker og
AdministrativEnhet ikke er enige om hvilke relasjonsnøkler som gjelder
for AdministrativEnhet.

Følgende står 7.2.4.2 (Bruker):

| **Relasjonsnøkkel**                                                               |
| --------------------------------------------------------------------------------- |
| http://rel.kxml.no/noark5/v4/api/admin/enhet/                                     |
| http://rel.kxml.no/noark5/v4/api/admin/ny-administrativenhet/                     |

Mens følgende står i 7.2.4.1 (AdministrativEnhet):

| **Relasjonsnøkkel**                                                               |
| --------------------------------------------------------------------------------- |
| http://rel.kxml.no/noark5/v4/api/admin/administrativenhet/                        |
| http://rel.kxml.no/noark5/v4/api/admin/ny-administrativenhet/                     |

Jeg er overbevist om at dette gjelder samme entitet, og bør bruke
samme relasjonsnøkler.  Foreslår at nøkkel bruker samme streng som
entiteten, dvs. `administrativenhet`, ikke `enhet`.

Ønsket endring
--------------

Endre relasjonsnøkkel `http://rel.kxml.no/noark5/v4/api/admin/enhet/` i
7.2.4.2 (Bruker) til
`http://rel.kxml.no/noark5/v4/api/admin/administrativenhet/`.
