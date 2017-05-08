Uklar beskrivelse om opprettelse av journalpost og bruken av arv
================================================================

------------------ ---------------------------------
          Prosjekt NOARK 5 Tjenestegresesnitt
          Kategori Versjon 1.0 beta
       Alvorlighet
      Meldingstype
   Brukerreferanse thomas.sodring@hioa.no
       Dokumentdel 7.2.3.11
        Sidenummer 238
       Linjenummer n/a
   Innsendingsdato ikke sendt inn
------------------ ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er uklart hvordan en journalpost skal opprettes. Det vil være mest
fornuftig å tro at følgende HTTP forespørsel vil kunne opprette en
journalpost.

`[contextpath][api]/sakarkiv/saksmappe/{systemID}/ny-journalpost`

Side 238 viser en liste av relasjoner og der mangler det en relasjon
for å opprette en journalpost. Imldertid ser vi at det er en relasjon

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-saksmappe/`

og kanskje denne skulle egentlig være

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-journalpost/`

Videre ser vi at dette gjøres enda mer uklart med måten arv er
håndtert.

FIXME hvordan ser vi det?

Både `mappe/saksmappe` og `registrering/basisregistrering/journalpost`
bruker arv og
[webbeskrivelsen](http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/)
viser noe annet enn tjenestegrensesnittet når det gjelder
arveforholdet `mappe/saksmappe`.  I webbeskrivelsen er det en relasjon

`http://rel.kxml.no/noark5/v4/utvid-til-saksmappe`

som ikke finnes på listen av relasjon som gjelder for mappe på side
131. Det er heller ikke noe relasjon på arkivdel eller klasse for å
opprette en saksmappe, kun mappe.

`http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-mappe/`

så den virker som om den eneste måten å opprette en saksmappe er å
lage en mappe for så å utvide den til saksmappe.  Men dette er ikke
spesifisert i tjenestegrensesnittet, men finnes som en 'hint' i web
beskrivelsen.

Situasjonen med arv gjøres enda mer uklart da
[mappe](http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/) har
relasjon for å opprette registrering og basisregistrering.

`http://rel.kxml.no/noark5/v4/ny-registrering`
`http://rel.kxml.no/noark5/v4/ny-basisregistrering`

Her brukes ikke utvid-til-* metoden for å opprette basisregistrering
eller eventuelt journalpost.

Det er ingen informasjon på
http://rel.kxml.no/noark5/v4/api/sakarkiv/journalpost/ og heller noe
informasjon på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/ om dette.

FIXME _KOMMENTAR Petter. Kanskje problemet de støtter på her er at de
vil ha en ren arkivstruktur sett av relasjon og en ren sett av
sakarkiv rel. Men dette ser du i Noark 5-standarden også hvis jeg
husker rett.  sakarkiv er definert i ytre kjerne men nevnt i indre
kjerne._

Vi forstår at dette er noe som kanskje er litt komplisert å få til da
arkivstruktur og sakarkiv grensesnittene da vil overlappe hverandre.
Dette ser vi også i `Noark 5 Standard for elektronisk arkiv`, Noark
5v4. `Del 5.4 Mappe` (sidenummer mangler i standarden).

Slik vi tolker Tjenestegrensesnitt-spesifikasjonen er det ikke mulig å
opprette en journalpost koblet til en saksmappe. Det er viktig at det
finnes en tydelig beskrivelse i spesifikasjonen om hvordan en
saksmappe og en journalpost skal opprettes.  Det er fordeler og
ulemper med utvid-til-* metoden, men det ville gjøre
tjenestegrensesnittet enklere å utvikle hvis det var mulig å opprette
en saksmappe uten `utvid-til-saksmappe`. Det vil imidlertid kreve at
arkivdel og klasse får en relasjon til

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-saksmappe/`

Ønsket endring
--------------

Det introduseres en relasjon for å tillate opprettelse av journalpost
til en saksmappe på side 131.

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-journalpost/`

Det introduseres en relasjon for å tillate opprettelse av en saksmappe
til en arkivdel på side 66, Del (7.2.1.2).

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-saksmappe/`

Det introduseres en relasjon for å tillate opprettelse av en saksmappe
til en arkivdel på side 117, Del (7.2.1.12).

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-saksmappe/`

FIXME _KOMMENTAR Petter. Det er kanskje litt mer vi må be de legge
til. Skal tenke litt mer på det_
