Samle systemID i en entitet og gjør det mulig å søke på feltet
===========================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  
       Meldingstype  
    Brukerreferanse  tsodring@oslomet.no
        Dokumentdel  
         Sidenummer  
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det bør være mulig å spørre en arkivkjerne om et systemID felt er brukt og 
at det er mulig å hente ut tilsvarende arkivenhet.

Hvis en arkivkjerne tvinges til å ha en liste over alle systemID som er i bruk
vil det være mulig å slå opp i denne listen og få tilbake en lenke til den aktuelle
arkivenheten. Et eksempel på dette er:

```
{
    "_links": [
        {
            "href": "http://localhost:8092/noark5v4/api/systemID/", 
            "rel": "http://rel.kxml.no/noark5/v4/api/systemID/"
        }, 

{

```

Et eksempel respons vil da være

```
{

    "results": [
        {
            "href": "http://localhost:8092/noark5v4/api/systemID/c7d2c5c2-08e6-4e7c-87ab-92c17715b475", 
            "rel": "http://rel.kxml.no/noark5/v4/api/systemID/"
        }, 
        {
            "href": "http://localhost:8092/noark5v4/api/systemID/96dc8fd4-f0b9-45fe-914f-2106e1e6e0fb", 
            "rel": "http://rel.kxml.no/noark5/v4/api/systemID/"
        }
		],
   "_links": [
        {
            "href": "http://localhost:8092/noark5v4/api/systemID/", 
            "rel": "self"
        }
}

```
Hven en klient følger den første lenken vil de da komme til en arkiv arkivenhet. 
Som feks :

```
{
    "systemID": "c7d2c5c2-08e6-4e7c-87ab-92c17715b475", 
    "tittel": "Eksempel kommune hovedarkiv", 
    "beskrivelse": "Eksempel kommune sitt arkivsystem ...", 
    "arkivstatus": "Opprettet", 
    "opprettetDato": "2017-04-21T07:56:36", 
    "opprettetAv": "arkivansvarlig", 
}

```


Dette vil gjøre det enklere å administrere data i kjernen men kan også
brukes for å sikre at duplikater ikke forekommer. Selv om UUID algoritmisk sett 
er unike kan det forekomme tilfeldgvis forekomme duplikater i en dårlig 
implementasjon .

Merk! Det finnes en kodelister kapitell *7.2.2.32 SystemID*. Det er uklart hvorvidt
dette løser det overnevnte problemstilling.

Ønsket endring
--------------


Det introduseres en relasjon på rotnivå i APIet.

`http://rel.kxml.no/noark5/v4/api/systemID/`

med følgende beskrivelse:

Det skal være må å hente ut en liste av alle systemID som er i bruk 
i arkivkjernen. 


Kommentar: Hvilken side??


Respons
-------

Ingen respons fra arkivverket så langt.

