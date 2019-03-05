Klargjør entydige krav til innloggingssystem
============================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  4.1 Autentisering
         Sidenummer  9
        Linjenummer  n/a
    Innsendingsdato  Ikke sendt inn
 ------------------  ---------------------------------

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

Her er det som står i spesifikasjonen om innlogging i dag:

  Autentisering
  ~~~~~~~~~~~~~
  
  NOARK5 kjerne må ha metoder for å autentisere brukere og gi de
  riktige tilganger til kjernen.

  Single Sign On bør støttes.

  For REST er Basic autentication minimum for autentisering og en bør
  støtte SAML 2.0 og OpenID Connect.

Det mangler en forklaring på hva som menes med "Single Sign On bør
støttes", og referanser til standardene som definerer
Basic-autentisering, SAML 2.0 og OpenID Connect.  Det mangler videre
en presis beskrivelse av hvordan de ulike innloggingsmetodene skal
tilbys.  Det vil være en stor fordel om det finnes en mekanisme for
API-klienter å oppdage hvilke autentiseringsmekanismer som er
tilgjengelig.

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
hodefeltet til "Bearer" (5 ganger, merkelig nok).  Dette illustrerer
behovet for å definere nærmere hvordan innlogging skal gjøres.
"Bearer" er forøvrig beskrevet relatert til Oauth 2.0 i [RFC
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

I Nikita gjøres dette ved å legge inn en egen relasjon i _links pa
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
_links på toppnivå i API-et skal være tilgjengelig

Forklar klarere hva som menes med "Single Sign On bør støttes".

Forslag til relasjoner:

 * http://rel.kxml.no/noark5/v4/api/login/rfc6749/ - Oauth2
 * http://rel.kxml.no/noark5/v4/api/login/rfc7617/ - Basic

Respons
-------

Ingen respons fra Arkivverket så langt.
