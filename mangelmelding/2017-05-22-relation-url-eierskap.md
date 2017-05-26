Bør relasjonnavn bruke DNS-navn eid av Arkivverket?
===================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.1
         Sidenummer  12
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Dette gjelder de fleste sider, fra side 12 og utover.

De offisielle relasjonsnavnene i spesifikasjonen starter med
http://rel.kxml.no/, og fungerer som nettadresser til dokumentasjon om
de ulike relasjonene.  Dette er en god ide.  I dag kontrolleres
DNS-domenet rel.kxml.no og kxml.no i følge WHOIS-databasen til Uninett
Norid av det private selskapet [Arkitektum
AS](https://w2.brreg.no/enhet/sok/detalj.jsp?orgnr=914994780):

```
Domain Information

NORID Handle...............: KXM3D-NORID
Domain Name................: kxml.no
Domain Holder Handle.......: AA9438O-NORID
Registrar Handle...........: REG5-NORID
Legal-c Handle.............: TKN177P-NORID
Tech-c Handle..............: WAR19R-NORID
Name Server Handle.........: NSDA68H-NORID
Name Server Handle.........: NSDA81H-NORID

Additional information:
Created:         2015-07-12
Last updated:    2016-07-12

NORID Handle...............: AA9438O-NORID
Type.......................: organization
Name.......................: ARKITEKTUM AS
Id Type....................: organization_number
Id Number..................: 914994780
Registrar Handle...........: REG5-NORID
Post Address...............: Kyrkjevegen 6
Postal Code................: NO-3800
Postal Area................: BØ I TELEMARK
Country....................: NO
Email Address..............: post@arkitektum.no

Additional information:
Created:         2015-07-12
Last updated:    2015-07-12
```

Kan det være en ide å heller bruke relasjonsnavn i den åpne standarden
for Noark 5 Tjenestegrensesnitt som peker til nettsider eid og
kontrollert av arkivverket?

Det vil helt klart ikke være noe problem hvis eierskap for kxml.no
overføres til Arkivverket, men kan bli problematisk i fremtiden hvis
det ikke gjøres og Arkitektum og Arkivverket blir uenige om videre
forvaltning av standarden.

Ønsket endring
--------------

Enten bør eierskap for kxml.no flyttes til Arkivverket som står bak
Noark-standarden, eller så bør alle relasjonsnavn endres til å bruke
DNS-navn som kontrolleres av Arkivverket,
f.eks. rel.noark5.arkivverket.no.
