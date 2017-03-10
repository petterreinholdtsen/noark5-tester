Discrepancy in handling inheritance
==============================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  2017-03-10
 ------------------  ---------------------------------

Beskrivelse
-----------

When it comes to inheritance in the data model, it is visible in the
relationships

  mappe -> saksmape

  registrering -> basisregistrering -> journalpost

There appears to be a discrepancy in how this is handled. If we take the
relationship mappe -> saksmape we see that the rels when creating a new
arkivdel include:

   "href": "http://localhost:49708/api/arkivstruktur/Arkivdel/12345/ny-mappe",
   "rel": "http://rel.kxml.no/noark5/v4/api/ny-mappe",

To realise a saksmappe you need to use utvid-til-saksmappe:

   "uri": "http://n5test.kxml.no/api/sakarkiv/Saksmappe/12345/utvid-til-saksmappe",
   "rel": "http://rel.kxml.no/noark5/v4/utvid-til-saksmappe",

If we take the relationship registrering -> basisregistrering we see that under
 series, you can only create a registrering

  "href": "http://localhost:49708/api/arkivstruktur/Arkivdel/12345/ny-registrering",
  "rel": "http://rel.kxml.no/noark5/v4/api/ny-registrering",

 while under mappe you can create both a registrering as well as a basisregistrering

  "uri": "http://n5test.kxml.no/api/arkivstruktur/Mappe/12345/ny-registrering",
  "rel": "http://rel.kxml.no/noark5/v4/ny-registrering",

  "uri": "http://n5test.kxml.no/api/arkivstruktur/Mappe/12345/ny-basisregistrering",
  "rel": "http://rel.kxml.no/noark5/v4/ny-basisregistrering",

There is a discrepancy here in how inheritance is handled. Further the creation
 of a mappe will result in a mappe being assigned to an arkivdel. An arkivdel
 may already have a classificationsystem associated with it and allowing the
 mappe to change "type" may result in errors that break with the current
 thinking in Noark, one arkivdel means one classificationsystem.

The notion of "utvid-til-saksmappe", may not be compatible with the current way
 Noark is used.


Ønsket endring
--------------

This issue needs further attention. From an implementation point-of-view, my
personal opinion is to drop the "utvid-til-" strategy and force the client to
 to make an active decision about what it wants to create.
 Create just one of the following, a mappe, a saksmappe, a byggesaksmappe or a
 møtemappe. If the "utvid-til-" strategy is to be continued, RA need to provide
 documentation how this is handled with classificationsystems assigned to
 arkivdeler.

Respons
-------

Ingen respons fra arkivverket så langt.
