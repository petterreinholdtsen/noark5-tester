Er relasjonen '.../sakarkiv/saksparter' en skrivefeil?
======================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.3.11
         Sidenummer  239
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I del 7.2.3.11 (Saksmappe) på side 239 er det ført opp to relasjoner:

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/saksparter/
 * http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-sakspart/

I del 7.2.3.12 (Sakspart) på side 247 er det derimot ført opp følgende
relasjoner som virker å være tilsvarende men med litt andre navn:

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/sakspart/
 * http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-sakspart/

I resten av spesifikasjonen for tjenestegrensesnittet så er det brukt
samme benevnelse på listen over entiteter og oppretting av entiteter,
dvs arkiv - ny-arkiv, mappe -> ny-mappe osv.  Bruken av 'saksparter' i
flertallsform er dermed litt spesiellt, og vi lurer på om dette
kanskje er en skrivefeil for 'sakspart'?  Hvis ikke, bør det forklares
i spesifikasjonen hva som er forskjellen på
`http://rel.kxml.no/noark5/v4/api/sakarkiv/saksparter/` og
`http://rel.kxml.no/noark5/v4/api/sakarkiv/sakspart/`.

Ønsket endring
--------------

Endre del 7.2.3.11 (Saksmappe) på side 239, bytt ut

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/saksparter/

med

 * http://rel.kxml.no/noark5/v4/api/sakarkiv/sakspart/
