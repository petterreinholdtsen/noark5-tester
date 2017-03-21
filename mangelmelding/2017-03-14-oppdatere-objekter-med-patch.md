Følge OData anbefalinger for CRUD - Update
=================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  6.1.1.5
         Sidenummer  19
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Når det gjelder komposisjoner som er beskrevet på side 18 så står det
«Heleide objekter(komposisjoner) kan opprettes sammen med hovedobjektet».

Det må også være mulig å opprette/oppdatere slike komposisjoner på et senere
tidspunkt. Valget står da mellom en PUT på hele objektet der objektet
inngår eller at det er egne relasjonslenker for slike operasjoner.

Slik vi forstår tjenestegrensesnittet er det mening at hele objektet skal
lastes fram og tilbake og kjernen må ta stilling til om felter er blitt
endret. Dette kompliseres enda mer ved at det ikke er lov å endre noen
felter etter at objektet er opprettet/avsluttet.

Man løper en stor dataintegritetsrisiko hvis man tvinger klienten til å holde
hele objektet med alle komposisjoner i minne og sende hele objektet tilbake
til kjernen. Dette mener vi er unødvendig og en dårlig tilnærming
(bad practice).

Tjenestegrensesnitt i sitt nåværende form virker å være utviklet utifra et
"Noark 5 komplett" synspunkt, framfor synspunktet, "frittstående kjerne" som
kan integreres med sak/arkiv og fagsystemer. Det er viktig å huske at
Riksarkivet godkjenner kjernen, ikke klienter. Det er en viktig forskjell som
 Riksarkivet bør ta innover seg. Eksisterende Noark-komplett systemer blir
 godkjent som en helhet. En frittstående kjerne med integrasjoner til
fagsystemer vil stå over mange flere utfordringer når det gjelder
 datakvaliteten når data unødvendig flyttes fram og tilbake mellom
kjernen og en klient. Diverse klienter vil ikke nødvendigvis forstå viktigheten
og betydningen av Noark metadata og sammenhenger mellom entiteter!

For å understøtte argumentet at kjernen må støtte PATCH. Tjenestegrensesnittet
 sier selv at noen steder bygges det på OData. [OData-retningslinjene](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html#_Toc406398329) sier 
følgende for oppdateringer:

> Update an Entity
>
> _The OData services SHOULD support PATCH as the preferred means of updating an entity.
> But also services MAY additionally support PUT_.

Vi mener prinsippet som ligger til grunn for en slik anbefaling er at du skal
isolere og kun jobbe med data som trenger oppdatering, framfor å risikere
uønsket hendelser på data.

Hvis vi forstår OData anbefalingene riktig så anbefales det følgende strategi.
Entiteter opprettes / oppdateres (i sin helhet) med POST/PUT mens felter
oppdateres med en PATCH, der feltets attributtnavn og ny verdi angies.

Det må da taes stilling til hvordan komposisjoner opprettes og oppdateres.
I tjenestegrensesnittet opprettes komposisjoner sammen med entiteten.

Vi ser ikke noe problem med nøstet komposisjoner når entititer opprettes
og det står ingenting om det i [Odata-anbefalingene](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html#_Toc406398328),
men når vi ser på [OData anbefalinger for oppdateringer](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html#_Toc406398329) står det følgende:

> The entity MUST NOT contain related entities as inline content. It
> MAY contain binding information for navigation properties.

Tjenestegrensesnittet nøster komposisjoner. Det er litt uklart om anbefalinger
 over også gjelder for disse eller bare arkivenhetene (arkivdel, mappe osv).

Hvis komposisjoner også omfattes av OData anbefalingene så må det utvikles nye
relasjons-URL-er for alle entiteter med komposisjoner. Slik vi forstår det, vil en
tilknytting av en komposisjon til en entitet være en oppdatering av entiteten
og da vil det måtte brukes en PATCH forespørsel.

Vi antar at dette ikke gjelder kodelister, selv om kodelister også oppfører
seg som entiteter.

Nye REL som trengs da for feks klasse vil være:

  REST_REL http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-skjerming  
  REST_REL http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-gradering  
  REST_REL http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-sletting  
  REST_REL http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-kassasjon  
  REST_REL http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-kassasjonutfoert  

Ønsket endring
--------------

Vi ønsker at tjenestegrensesnitt følger en identifisert best-practice for CRUD.
Selv om tjenestegrensesnittet ikke defineres utelukkende som en OData kilde
så kan OData standarden brukes som veiledende. Vi ønsker at det utvikles en
beskrivelse av hvilken best-practice tjenestegrensesnitt forholder seg til,
eventuelt om det er avvik til etablerte tilnærminger og hvorfor.

OData som best practice innebærer en generell endring i hvordan CRUD er beskrevet:

1. En entitet opprettes med en POST.
2. En entitet oppdateres, i sin helhet, med en PUT.
3. Et felt oppdateres med en PATCH.
4. Komposisjoner nøstes ikke ved oppdateringer
5. Komposisjoner knyttes til entiteter via PATCH
