Beskriv hvordan lister skal formatteres i JSON
==============================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  6.1.1.2
         Sidenummer  16
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Det er ingen entydig beskrivelse i spesifikasjonen hvordan resultater
som inneholder lister med objekter skal se ut.  Relaterte nettsider
har to forskjellige måter å løse dette på.  I korte trekker er dette de
to ulike måtene:

  a. { "entitetsnavn": [ { obj }, { obj } ] }  
  b. [ { obj }, { obj } ]

Den første måten brukes på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/, som viser frem
følgende:

```
{
 "mappe": [
   {
     "mappeID": "1234/2014",
     "tittel": "testmappe 12345",
     ...
   }
 ]
}
```

Den andre måten brukes på
http://n5test.kxml.no/api/arkivstruktur/arkiv, som viser frem
følgende:

```
[
  {
    tittel: "Høflig arkiv",
    beskrivelse: "lorem ipsum høflig"
    ...
  }
]
```
Er det en god grunn at klienten skal måtte forholde seg til to
forskjellige måter å strukturere lister? Flere ulike måter å 
formattere lister på gjør klient-implementasjoner unødig komplisert.
Slik situasjonen er i dag må klient-implementasjoner enten 
implementere flere måter å lese lister, eller bli hemmet 
(fra et interoperabilitets perspeketiv) med integrasjoner
til Noark 5 kjerner fra forskjellige leverandører. Dette bety at klienter
kun fungerer med noen få API-implementasjoner.

Vi ser det er også mulig å enten bruke entitetsnavn eller et mer
generisk navn som 'data' eller 'liste'. Fordelen med å bruke et generisk
navn som 'liste' er å forenkle klientutvikling. 

Noe annet som det bør taes høyde for når dere beslutter dette er at
{ objekt } ligner litt på JavaScript og kanskje skape problemer mens
{ "entitetsnavn": [ { obj }, { obj } ] ungår dette.

Jeg mistenker alternativ (b) bør unngås, da det ikke er åpenbart
hvordan relasjoner med operasjoner på listene skal tas med.  I følge
spesifikasjonens side 13 kan alle lister ha en 'next'-relasjon i sin
liste med relasjoner.  Det står ingenting der om hvordan dette skal
formatteres, men det virker mest rett frem å gjøre dette slik:

```
{
 "data": [
   {
     "mappeID": "1234/2014",
     "tittel": "testmappe 12345",
     ...
   },
   ...
 ],
 "_links": [
   {
     "rel": "next"
     "href": "http://localhost:8092/noark5v4/hateoas-api/arkivstruktur/mappe/?top=10&skip=10",
   }
 ]
}
```

Dermed mistenker jeg at det er formatteringen på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/ som er den
tiltenkte måten å formattere lister.  Jeg har i
https://github.com/Arkitektum/N5-net/issues/4 spurt om det kan vises
frem et eksempel på hvordan 'next'-relasjoner skal håndteres for
lister.

Et relatert spørsmål er om det kan være en 'self'-relasjon på lister?
6.1.1.7 side 22 sier at alle ressurslenker med 'self'-relasjon kan
potensielt slettes.  Det virker mest nærliggende å kreve at lister
"slettes" ved å slette hver enkelt element i listen, og at det dermed
ikke skal være en 'self'-relasjon for lister.

Eksemplene over omtaler JSON-formattering.  Det er tilsvarende
utfordringer for XML-formattering, og det bør beskrives entydig i
spesifikasjonen hvordan XML-lister skal se ut, i tillegg til
relasjonslenkeformatteringen på side 12.  Det kommer egen
mangelmelding om dette.

Det hadde vært nyttig om antall objekter totalt i resultatsettet var
del av resultatet som ble returnert, dvs. å la $inlineCount-tilvalget
i Odata være aktiv som standard.  Det gjør det enklere for en klient å
vite hvor mange sider med resultater som finnes og dermed hvor mange
'next'-lenker som må følges for å hente hele resultatsettet.

Ønsket endring
--------------

Teksten under 6.1.1.2 (Finne objekter (Read)) bør utvides med
eksempler på hvordan et søkeresultat som returnerer en liste med
objekter bør se ut.

Det kan f.eks. legges inn avsnitt på slutten av punktet på side 16,
før "resultatkoder ned navigering/søk", som lyder noe ala dette:

> Et søkeresultat kan se ut som følger.
>
> Forespørsel:
>
> GET http://localhost:49708/api/arkivstruktur/mappe/
> Accept: application/vnd.noark5-v4+json
> 
> Respons:

```
{ "result" : [
    {
      "mappeID": "1234/2017",
      "tittel": "testmappe 1",
      ...
    },
    {
      "mappeID": "1235/2017",
      "tittel": "testmappe 2",
      ...
    }
  ],
  "count" : 3,
  "_links" : [
    {
      "rel": "next",
      "href": "http://localhost:8092/noark5v4/hateoas-api/arkivstruktur/mappe/?top=2&skip=2",
    }
  ]
}
```
