Beskriv krav til innloggingssystem og definer relasjon for OpenID Connect-oppsett
=================================================================================

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
standardisering av innloggingsmekanisme vil klienter ikke kunne koble
seg til tjenestegrensesnitt fra ulike leverandører.  Dagens
spesifikasjon sier veldig lite om innlogging, og innlogging er gjort
svært ulikt i utkast til tjenestegrensesnitt fra Nikita og Evry.  Her
er det som står i spesifikasjonen om innlogging i dag:

  Autentisering
  ~~~~~~~~~~~~~
  
  NOARK5 kjerne må ha metoder for å autentisere brukere og gi de
  riktige tilganger til kjernen.

  Single Sign On bør støttes.

  For REST er Basic autentication minimum for autentisering og en bør
  støtte SAML 2.0 og OpenID Connect.

En måte å annonsere at OpenID Connect er støttet i
tjenestegrensesnittet, er å annonsere en relasjon i _links på toppnivå
til ".well-known/openid-configuration", som så kan følges for å finne
detaljene om hvordan logge inn med OpenID Connect.  Dette forutsetter
at _links på toppnivå er tilgjengelig uten innlogging, slik det er i
Nikita.

Spesifikasjonen for openid-configuration er tilgjengelig fra
`https://openid.net/specs/openid-connect-discovery-1_0.html`_ og en
beskrivelse av brukes finnes på
`https://auth0.com/docs/protocols/oidc/openid-connect-discovery`_.  Et
par eksempler finnes på
`https://id.signicat.com/oidc/.well-known/openid-configuration`_
`https://oidc.difi.no/idporten-oidc-provider/.well-known/openid-configuration`_.

Ønsket endring
--------------

Definer innloggingsmetoden så entydig at enhver API-klient kan koble
seg til et hvilket som helt tjenestegrenisesnitt-API så sant
innloggingsinformasjon (brukernavn og passord) er tilgjengelig.

Definer relasjon for å annonsere OpenID Connect-støtte, samt krev at
_links på toppnivå i API-et skal være tilgjengelig

Respons
-------

Ingen respons fra Arkivverket så langt.
