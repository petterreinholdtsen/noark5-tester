Klargjør JSON-respons når database eller lister er tomme
========================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.1
         Sidenummer  13
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Denne mangelmeldingen bør ses i sammenheng med med mangelmelding
`Beskriv hvordan lister skal formatteres i JSON` som ble sendt inn
2017-03-28, og hva en velger for tomme lister er avhengig av hvordan
en velger å beskrive listeformattering generelt.

Det er ikke klart fra spesifikasjonen hva slags JSON som skal
returneres for tomme lister.  Delvis er det uklart hvilke
relasjonsnøkler som skal returneres i \_links hvis databasen ikke
inneholder enkeltentiteter (for eksempel en bestemt mappe), eller hvis
et søk ikke returnerer noen treff, og delvis er det uklart hvordan
selve resultatsettet skal returneres når det er tomt.

To eksempler der dette er relevant er oppslag som pekes til av
relasjonsnøkkelen for arkiv og dokumentbeskrivelse:

* http://rel.kxml.no/noark5/v4/api/arkivstruktur/arkiv/
* http://rel.kxml.no/noark5/v4/api/arkivstruktur/dokumentbeskrivelse/

Bør \_links-elementet ikke eksistere, være en tom liste, eller
inneholde «self»-lenke?  Hva med resultatsettet?

Hvis \_links ikke skal eksistere så kan det for eksempel se slik ut
når gjør oppslag i URLen som som pekes til av relasjonsnøkkelen for
arkiv:

```
{
  "results": [],
}
```

Tilsvarende hvis \_links skal være en tom liste:

```
{
  "results": [],
  "_links" : []
}
```

Tilsvarende hvis \_links skal inneholde en "self"-relasjon:

```
{
  "results": [],
  "_links" : [
    "rel": "self",
    "href": "..."
  ]
}
```

I samtlige eksempler er det tatt utgangspunkt i at resultatsettet skal
være inkludert og være tomt når resultatet er tomt.  Det gir like mye
mening å ikke returnere resultatsettet overhode i slike tilfeller, for
å spare båndbredde.  I så tilfelle kan «"results": [],» fjernes fra
eksemplene over.

For sistnevnte eksempel er det litt uklart hva en «self»-relasjon
skulle peke til hvis den var satt, i og med at spesifikasjonens del
6.1.1.7 side 22 sier at alle ressurslenker med «self»-relasjon kan
potensielt slettes.  En tom liste kan vanskelig slettes, så det er vel
et godt argument mot den siste ideen.  Men på den annen side sier jo
punkt 5.13.23 på side 89 følgende:

> Det bør være mulig å slette mange dokumentvarianter samtidig,
> f.eks. alle dokumentvarianter som er funnet etter et søk.

Dette tyder jo på at det skal være mulig å slette alle elementene i en
liste i en operasjon, i hvert fall for noen objekttyper, og det er et
godt argument for å ha en «self»-lenke i resultatet til ethvert søk,
også de med tomt resultat.

Demo-nettstedet http://n5test.kxml.no/api/ har ingen «tomme» datasett
som jeg har klart å finne, slik at det er lite hjelp der å finne
hvordan spesifikasjonen skal tolkes, og spesifikasjonen nevner ikke
dette eksplisitt.  Det bør forklares i spesifikasjonen slik at alle
implementasjoner håndterer dette likt.

Det svaret som vil forbruke minst båndbredde er jo et enkelt «{}», som
jo ganske klart representerer et tomt svar.  Alternativt kunne en
alltid returnere \_links for å gjøre det enklere for klienter som
dermed kan forvente at det alltid finnes et \_links-element i
resultatene.

Ønsket endring
--------------

Del 6.1.1.1 på side 13 bør utvides til å forklare hva slags JSON som
returneres hvis en type objekter mangler i databasen eller
søkeresultatet.  Det kan for eksempel legges inn et avsnitt ala dette
på slutten av del 6.1.1.1, like før del 6.1.1.2 starter på side 13:

> Når en forespurt listeressurs fra databasen er tom skal følgende
> JSON-struktur returneres:
> 
> ```
> {
>   "results": [],
>   "_links" : [
>     "rel": "self",
>     "href": "http://localhost/api/arkivstruktur/arkiv/"
>   ]
> }
> ```
>
> Verdien i 'href' vil variere etter hva slags listeressurs / søk som
> ble forespurt.
