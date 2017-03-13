Besrkivelse av lister 
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
1. Det er ingen entydig beskrivelse av hvordan resultater som inneholder lister
skal struktureres.

2. Webløsningen viser to forskjellige måter dette kan løses på.

Lister struktureres på tom forskjellige måter:

 a. { "entitetsnavn": [ { obj }, { obj } ] }
 b. [ { obj }, { obj } ]

Konkrete eksempler fra webløsningen er følgende:

http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/ genererer 
{
 "mappe": [
   {
     "mappeID": "1234/2014",
     "tittel": "testmappe 12345",
     .... 
   }
 ]
}

http://n5test.kxml.no/api/arkivstruktur/arkiv  genererer

[
  {
    tittel: "Høflig arkiv",
    beskrivelse: "lorem ipsum høflig"
    ....
  }
]

Dette mener vi er noe som kompliserer utvikling av klienten. Er det en god
grunn at klienten skal måtte forholde seg til to forskjellige måter å strukturere
lister? 

Ønsket endring
--------------

1. Det utvikles en strukturbeskrivelse for resultater som inneholder lister
2. Liste beskrivelse for objekter blir enklest mulig. Vi ønsker at følgende
   struktur skal være gjeldende [ { obj }, { obj } ]

Respons
-------

Ingen respons fra arkivverket så langt.
