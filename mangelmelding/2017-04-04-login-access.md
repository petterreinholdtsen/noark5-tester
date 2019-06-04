Klargjør entydige krav til innlogging og tilgangskontroll
=========================================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  4.1 (Autentisering)
         Sidenummer  9
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Innlogging er et kritisk punkt i ethvert REST-API, og uten
standardisering av innloggingsmekanisme må enhver klient tilpasses
hver enkelt variant av innlogging, i praksis kan det kreve tilpassing
til hver leverandør.  Dagens API-spesifikasjon sier veldig lite om
innlogging, og innlogging er gjort på forskjellig vis i utkast til
tjenestegrensesnitt fra Nikita og Evry.  Dette blokkerer for
leverandøruavhengige klienter og bidrar til innlåsing.  Det bør derfor
spesifiseres i mer detalj hvordan innlogging skal fungere, for å sikre
at alle leverandører gjør det på samme måte.

Her er det som står i spesifikasjonen om innlogging/autentisering i dag:

> NOARK5 kjerne må ha metoder for å autentisere brukere og gi de
> riktige tilganger til kjernen.
>
> Single Sign On bør støttes.
>
> For REST er Basic autentication minimum for autentisering og en bør
> støtte SAML 2.0 og OpenID Connect.

Det mangler en forklaring på hva som menes med "Single Sign On bør
støttes".  Hva konkret betyr dette?  Er det Kerberos-autentisering ala
det Microsoft Active Directory tilbyr, eller noe annet?

Det mangler også referanser til standardene som definerer
Basic-autentisering, SAML 2.0 og OpenID Connect.  Det mangler videre
en presis beskrivelse av hvordan de ulike innloggingsmetodene skal
tilbys.  Det vil være en stor fordel om det finnes en mekanisme for
API-klienter å oppdage hvilke autentiseringsmekanismer som er
tilgjengelig.

Et relatert spørsmål er om en må logge inn før en kan bruke API-et,
eller er det noen deler som er tilgjengelig uten innlogging?

Det viser seg at det er mange måter å gjøre Basic-autentisering, og
API-et bør beskrive en bestemt måte å gjøre dette.  Det bør f.eks stå
om oppførselen skal være slik RFC 7617 anbefaler, dvs. at
ikke-autentiserte HTTP-forespørsler skal sette WWW-Authenticate med
realm, slik at nettlesere vet at de skal spørre brukeren om brukernavn
og passord, og klienter automatisk kan se at Basic autentisering er
støttet.  Det bør gjøres klart om Basic-innlogging skal brukes på en
bestemt URL til å sette en "cookie" som så brukes videre i
grensesnittet, eller om brukernavn og passord skal brukes til enhver
REST-forespørsel i hele grensesnittet.  Førstnevnte alternativ kan
gjøre det enklere å støtte ulike innloggingsmekanismer.

Evrys API støtter i dag Basic-authentisering, men det er uklart for en
klient hvordan bruke den, da WWW-Authentication-hodefeltet ikke blir
satt med realm som nettlesere kjenner igjen.  I stedet settes dette
hodefeltet til "Bearer" (5 ganger, uvisst av hvilken grunn).  Dette
illustrerer behovet for å definere nærmere hvordan innlogging skal
gjøres.  "Bearer" er forøvrig beskrevet relatert til Oauth 2.0 i [RFC
6750](https://www.rfc-editor.org/rfc/rfc6750.txt).

En måte å annonsere at OpenID Connect er støttet i
tjenestegrensesnittet, er å annonsere en relasjon i _links på toppnivå
til ".well-known/openid-configuration", som så kan følges for å finne
detaljene om hvordan logge inn med OpenID Connect.  Dette forutsetter
at _links på toppnivå er tilgjengelig uten innlogging, slik det er i
Nikita.  Ved å gjøre toppnivå tilgjengelig uten innlogging så får
API-klienter en mulighet til å hente ut informasjon om tjeneren og
hvordan den skal brukes og kan dermed tilpasse seg ulike
innloggingsmetoder.

I Nikita gjøres dette ved å legge inn en egen relasjon i _links på
toppnivå:

```
{
  "_links": [
    {
      "href": "https://nikita.hioa.no/noark5v4/oauth/token",
      "rel": "http://nikita.arkivlab.no/noark5/v4/login/rfc6749/"
    },
    ...
  ]
}
```

En kan gjøre tilsvarende for bruk av Basic autentisering, for eksempel
ved definere en relasjon for dette og skrive at Basic autentisering
skal brukes til å sette en kake som så brukes videre for
tilgangsstyring.  En ulempe med en slik tilnærming er at det er mulig
også for de som ikke skal ha tilgang til API-tjenesten å se at den
eksisterer.

Spesifikasjonen for openid-configuration er tilgjengelig fra
`https://openid.net/specs/openid-connect-discovery-1_0.html`_ og en
beskrivelse av brukes finnes på
`https://auth0.com/docs/protocols/oidc/openid-connect-discovery`_.  Et
par eksempler finnes på
`https://id.signicat.com/oidc/.well-known/openid-configuration`_
`https://oidc.difi.no/idporten-oidc-provider/.well-known/openid-configuration`_.

Se også `http://rel.kxml.no/noark5/autentisering-med-openid-connect/`_.

Under overskriften Autentisering står også at «Noark5 kjerne må ha
metoder for å autentisere brukere og gi de riktige tilganger til
kjernen».  Hva betyr dette?  Hva er «de riktige tilganger»?  Hva slags
granularitet kreves, dvs. hvor finkornet tilgangsstyring skal
tjenestegrensesnittet ha?  Er det nok med tilgang / ikke tilgang til
API-et, eller for å ta et annet ytterpunkt, må tilgangen kunne styres
pr. entitet eller attributt?  Det virker ut fra
Tilgangskategori-kodelisten i figur 32 på side 253 at tilgang skal
kunne gis pr. arkivdel, klasse, mappe, registrering og
dokumentbeskrivelse, men har ikke funnet noe klart krav i
spesifikasjonen på hva som kreves.  Er det meningen av pakken Admin
beskrevet i del 7.2.4 skal danne grunnlaget for slik tilgangskontroll?

Bør spesifikasjonen kreve at en må kunne gi tilganger ved hjelp av
rettighetsgrupper, for å slippe manuelt vedlikehold av hvem som får
lov til hva?

Ønsket endring
--------------

Definer innloggingsmetode så entydig at enhver API-klient vet hvordan
det skal koble seg til et hvilket som helt tjenestegrenisesnitt-API så
sant innloggingsinformasjon (brukernavn og passord) er tilgjengelig.

Det bør sies klart om ikke-autentiserte HTTP-forespørsler skal sette
WWW-Authenticate med realm satt, slik RFC 7617 anbefaler, og som er
nødvendig for at en nettleser skal spørre om brukernavn og passord når
Basic brukes.

Definer relasjon for å annonsere OpenID Connect-støtte, samt krev at
_links på toppnivå i API-et skal være tilgjengelig også for brukere
som ikke er logget inn, for å la API-klienter kunne oppdage hvilke
innloggingsmekanismer som er tilgjengelig.  Alternativt, definert kun
en innloggingsmekanisme og krev at alle implementasjoner bruker kun
denne.

Forklar klarere hva som menes med "Single Sign On bør støttes".

Forslag til relasjoner:

 * https://rel.arkivverket.no/noark5/v4/api/login/rfc6749/ - Oauth2
 * https://rel.arkivverket.no/noark5/v4/api/login/rfc7617/ - Basic

Legg inn referanse til del 7.2.4 (Admin) på side 253 under punkt 4.1
(Autentisering) på side 9, og forklare at det er instanser av Bruker
og AdministrativEnhet som skal brukes til tilgangskontroll.
