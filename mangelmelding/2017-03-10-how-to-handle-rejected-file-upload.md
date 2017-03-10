file upload as part of a transaction with documentObject
==============================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  6.1.9
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  2017-03-10
 ------------------  ---------------------------------

Beskrivelse
-----------

The process of uploading a file should be seen as a transaction that includes
 documentDescrition, documentObject and the file. In the event of problems with
 the storage system, i.e. storage system is experiencing disruption, the
 documentObject may be written to the persistence layer, but the file upload
 is rejected. This will result in a 200 OK and a 50X Error message.

 Currently there is no mechanism to delete the documentObject from the client
 side in such a scenario.

Ønsket endring
--------------

This issue needs further attention. One solution may be to create a call to the
core that includes documentDescription, documentObject and the file. With this
 solution, if one of the steps fail, all steps fail and the client is notified
 appropriately


Respons
-------

Ingen respons fra arkivverket så langt.
