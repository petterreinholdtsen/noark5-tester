Hva skal returneres når lister er tomme?
========================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.1
         Sidenummer  13
        Linjenummer  ?
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Oppsummering
------------

Klargjør hva som skal returneres for når databasen eller lister er
tomme.

Beskrivelse
-----------

Det er ikke klart fra spesifikasjonen hvilke relasjonsnøkler som skal
returneres i \_links hvis databasen ikke inneholder objekter av en
bestemt type.  Et eksempel er oppslag som pekes til av relasjonsnøkkel
http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkiv/, et annet er
http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentbeskrivelse/ .
Bør \_links-elementet ikke eksistere, være en tom liste, eller
inneholde «self»-lenke?

Demo-nettstedet http://n5test.kxml.no/api/ har så vidt jeg har klart å
finne ut ingen «tomme» datasett, slik at det er lite hjelp å finne der
om hvordan spesifikasjonen skal tolkes.

Jeg foreslår at det returneres en tom liste, slik at API-klienter kan
forvente at det alltid finnes et \_links-element.  For JSON kan det som
returneres se slik ut: «{ "\_links" : [ ] }»

Ønsket endring
--------------

Del 6.1.1.1 bør utvides til å forklare hva slags JSON som returneres
hvis en type objekter mangler i databasen.  F.eks. ved å legge inn et
avsnitt ala dette på slutten av delen på side 13:

> Når den forespurte typen ressurser mangler i databasen returneres
>  det et tomt dokument med tom liste med lenker, dvs. «{ "\_links" :
>  [ ] }»

Respons
-------

Ingen respons fra arkivverket så langt.
