Bruk enhetlige href-eksempler i spesifikasjonen
===============================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  krever klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6 (Konsepter og prinsipper)
         Sidenummer  11
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I kapittel 6 er det brukt tre ulike nett-addresser i href-eksemplene:

 * http://localhost:49708/api/
 * http://localhost/api/
 * http://n5test.kxml.no/api/

Det fremgår ikke fra spesifikasjonen hvorfor det brukes ulike
nett-adresser, og så vidt jeg kan forstå er dette kun resultat av
tilfeldigheter.  Jeg foreslår at dette standardiseres slik at kun en
type nett-addresser brukes i hele spesifikasjonen.  I trad med [RFC
2606](https://tools.ietf.org/html/rfc2606) foreslår jeg at det brukes
et navn under example.com, f.eks. https://n5.example.com/api/.  Merk
at jeg har bytter fra http til https, hvilket generelt anses som en
god ide.

Hvis det ikke er tilfeldig at det brukes flere ulike nett-adresser
her, så bør det forklares i spesifikasjonen hva som er forskjellen på
dem og når de ulike brukes.

Ønsket endring
--------------

Bytt alle forekomster av de tre overnevnte nettadressene i
spesifikasjonen med https://n5.example.com/api/.
