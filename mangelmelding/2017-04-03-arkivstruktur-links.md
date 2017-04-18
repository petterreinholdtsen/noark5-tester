Hva skal returneres for arkivstruktur-relasjonen?
=================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7.2.1
         Sidenummer  37
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er uklart fra spesifikasjonen hva som skal returneres for href som
pekes til fra relasjonen
http://rel.kxml.no/noark5/v4/api/arkivstruktur/.

side 12

> "Eksempelet viser at denne arkivkjernen støtter arkivstruktur
> (http://rel.kxml.no/noark5/v4/api/arkivstruktur) og sakarkiv
> (http://rel.kxml.no/noark5/v4/api/sakarkiv). Ved å følge Href til
> disse relasjonsnøkler vil tilgjengelige ressurser innen disse
> områder annonseres på samme måte."

side 13:

> http://rel.kxml.no/noark5/v4/api/arkivstruktur
> 
>   Arkivkjerne støtter konformitetsnivå 1 arkivstruktur
>   [...]
>
> Relasjonsnøkler under de forskjellige konformitetsnivå listes ut i
> kapittel 7 sammen med beskrivelse av klasser.


http://rel.kxml.no/noark5/v4/api/arkivstruktur/

Eks http://n5test.kxml.no/api/arkivstruktur :
```
{"_links": [
    {"rel":"http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkiv",
     "href":"http://n5test.kxml.no/api/arkivstruktur/arkiv{?$filter&$orderby&$top&$skip&$search}",
     "templated":true},
    {"rel":"http://rel.kxml.no/noark5/v4/api/administrasjon/ny-arkivskaper",
     "href":"http://n5test.kxml.no/api/arkivstruktur/ny-arkivskaper",
     "templated":false},
   {"rel":"http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivskaper",
    "href":"http://n5test.kxml.no/api/arkivstruktur/arkivskaper{?$filter&$orderby&$top&$skip&$search}",
    "templated":true},
   {"rel":"http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkivdel",
    "href":"http://n5test.kxml.no/api/arkivstruktur/arkivdel{?$filter&$orderby&$top&$skip&$search}",
    "templated":true},
   {"rel":"http://rel.kxml.no/noark5/v4/api/arkivstruktur/klassifikasjonssystem",
    "href":"http://n5test.kxml.no/api/arkivstruktur/klassifikasjonssystem{?$filter&$orderby&$top&$skip&$search}",
    "templated":true},
   {"rel":"http://rel.kxml.no/noark5/v4/api/arkivstruktur/klasse",
    "href":"http://n5test.kxml.no/api/arkivstruktur/klasse{?$filter&$orderby&$top&$skip&$search}",
    "templated":true},
   {"rel":"http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe",
    "href":"http://n5test.kxml.no/api/arkivstruktur/mappe{?$filter&$orderby&$top&$skip&$search}",
    "templated":true},
   {"rel":"http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering",
    "href":"http://n5test.kxml.no/api/arkivstruktur/registrering{?$filter&$orderby&$top&$skip&$search}",
    "templated":true},
   {"rel":"http://rel.kxml.no/noark5/v4/api/arkivstruktur/basisregistrering",
    "href":"http://n5test.kxml.no/api/arkivstruktur/basisregistrering{?$filter&$orderby&$top&$skip&$search}",
    "templated":true},
   {"rel":"http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentbeskrivelse",
    "href":"http://n5test.kxml.no/api/arkivstruktur/dokumentbeskrivelse{?$filter&$orderby&$top&$skip&$search}",
    "templated":true},
   {"rel":"http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentobjekt",
    "href":"http://n5test.kxml.no/api/arkivstruktur/dokumentobjekt{?$filter&$orderby&$top&$skip&$search}",
    "templated":true}
  ]
}
```

Ønsket endring
--------------

FIXME mer konkret forslag

Beskriv under 7.2.1 hvilke relasjonslenker som skal være del av
arkivstruktur/?
