Beskriv hvordan lister skal formatteres (JSON og XML)
=====================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Det er ingen entydig beskrivelse i spesifikasjonen hvordan resultater
som inneholder lister skal se ut, mens relaterte nettsider viser to
forskjellige måter dette kan løses på.

Lister struktureres på tom forskjellige måter:

  a. { "entitetsnavn": [ { obj }, { obj } ] }  
  b. [ { obj }, { obj } ]  

Konkrete eksempler fra webløsningen er følgende:

http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/ genererer

```
{
 "mappe": [
   {
     "mappeID": "1234/2014",
     "tittel": "testmappe 12345",
     .... 
   }
 ]
}
```

http://n5test.kxml.no/api/arkivstruktur/arkiv genererer

```
[
  {
    tittel: "Høflig arkiv",
    beskrivelse: "lorem ipsum høflig"
    ....
  }
]
```

Flere ulike måter å formattere lister på gjør klient-implementasjoner
unødig komplisert. Er det en god grunn at klienten skal måtte forholde
seg til to forskjellige måter å strukturere lister?

I følge spesifikasjonens side 13 kan alle lister ha en 'next'-relasjon
i sin liste med relasjoner.  Det står ingenting der om hvordan dette
skal formatteres, men det virker mest rett frem å gjøre dette slik:

```
{
 "mappe": [
   {
     "mappeID": "1234/2014",
     "tittel": "testmappe 12345",
     .... 
   }
 ],
 "_links": [
   {
     "rel": "next"
     "href": "...",
   }
 ]
}
```

Ønsket endring
--------------

FIXME skriv om med konkrete formuleringer og annet format.

1. Det utvikles en strukturbeskrivelse for resultater som inneholder lister
2. Liste beskrivelse for objekter blir enklest mulig. Vi ønsker at følgende
   struktur skal være gjeldende [ { obj }, { obj } ]

Respons
-------

Ingen respons fra arkivverket så langt.
