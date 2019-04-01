Mangler beskrivelse av pakken MøteOgUtvalgsbehandling
=====================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  7
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det mangler beskrivelse av pakken MøteOgUtvalgsbehandling i kapittel
7.  Aktuelle kodelister og relasjoner fra Mappe til Møtemappe og fra
Basisregistrering til Møteregistrering er allerede på plass.

Det må bestemmes innhold for aktuelle relasjons-URL.  Foreslår
«moeteutvalg» som URL-del på samme nivå som «arkivstruktur»,
«sakarkiv» og «metadata».  Aktuelle relasjoner for entitetene blir da

 * http://rel.arkivverket.no/noark5/v4/api/moeteutvalg/moetemappe/
 * http://rel.arkivverket.no/noark5/v4/api/moeteutvalg/moeteregistrering/

Foreslår videre at kodelister som kun brukes av moetemappe og
moeteregistrering flyttes til denne pakken.

Ønsket endring
--------------

Det må legges inn en ny pakke i kapittel 7 med entitetene som mangler.
Foreslår at den får navnet MoeteOgUtvalgsbehandling, basert på
pakkenavnet som er brukt i
media/uml-arkivstruktur-omfattende-forklart.emf og
media/uml-arkivstruktur-mappe-til-saksmappe.emf.

Foreslår følgende endring av navn på entiteter som inneholder «møte»
til å bruke «moete» i stedet:

| Fra                     | Til                      |
|-------------------------|--------------------------|
| Møteregistrering        | Moeteregistrering        |
| Møtemappe               | Moetemappe               |
| MøtedeltakerFunksjon    | MoetedeltakerFunksjon    |
| Møteregistreringsstatus | Moeteregistreringsstatus |
| Møteregistreringstype   | Moeteregistreringstype   |
| Møtesakstype            | Moetesakstype            |

De to første entietene er ikke beskrevet i dagens spesifikasjon.  I
tillegg bør det introduseres en ny entitet Moetedeltaker.  Atributtene
til entitetene Møteregistrering og Møtemappe var allerede beskrevet i
UML-diagrammet media/uml-arkivstruktur-omfattende-forklart.emf.  Mitt
forslag baserer seg på denne beskrivelsen, men endrer saksbehandler og
administrativEnhet til å være relasjoner til Bruker- og
AdministrativEnhet-entitetene, samt moetedeltaker til å være en
attributt.

Det konkrete endringsforslaget er for omfattende til at det gir mening
å ta det med her.  Jeg har laget en git-gren med endringene, og vil
knytte det til denne mangelmeldingen via github.  Har der med
plantuml-diagram som viser entitetene og relasjonene til denne pakken.
