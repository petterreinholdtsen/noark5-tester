Uklar beskrivelse om opprettelse av journalpost og bruken av arv
================================================================

------------------ ---------------------------------
          Prosjekt NOARK 5 Tjenestegresesnitt
          Kategori Versjon 1.0 beta
       Alvorlighet protest
      Meldingstype utelatt
   Brukerreferanse thomas.sodring@hioa.no
       Dokumentdel 7.2.3.11
        Sidenummer 239
       Linjenummer n/a
   Innsendingsdato 20177-05-09
------------------ ---------------------------------

Beskrivelse
-----------

Gjelder også side 66, 117 og 131.

Det er uklart fra spesifikasjonen hvordan en journalpost skal
opprettes.  Det virker mest fornuftig å tro at følgende
HTTP-forespørsel vil kunne opprette en journalpost.

`[contextpath][api]/sakarkiv/saksmappe/{systemID}/ny-journalpost`

Del 7.2.3.11 (Saksmappe) Side 239 viser en liste av relasjoner som
hører til saksmappe og der mangler det en relasjon for å opprette en
journalpost. Imidlertid ser vi at det er en relasjon

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-saksmappe/`

og kanskje denne skulle egentlig være

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-journalpost/` ?

Videre ser vi at hvordan journalpost skal opprettes gjøres enda mer
uklart med måten arv er håndtert.  Både `mappe/saksmappe` og
`registrering/basisregistrering/journalpost` bruker arv og
[webbeskrivelsen](http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/)
viser noe annet enn tjenestegrensesnittet når det gjelder
arveforholdet `mappe/saksmappe`.  I webbeskrivelsen er det en relasjon

`http://rel.kxml.no/noark5/v4/utvid-til-saksmappe`

som ikke finnes på listen med relasjon i del 7.2.1.16 (Mappe) på side
131.  Det er heller ikke noe relasjon på arkivdel eller klasse for å
opprette en saksmappe, kun mappe.

`http://rel.kxml.no/noark5/v4/api/arkivstruktur/ny-mappe/`

så den virker som om den eneste måten å opprette en saksmappe er å
lage en mappe for så å utvide den til saksmappe.  Men dette er ikke
spesifisert i tjenestegrensesnitt-spesifikasjonen, men finnes som et
'hint' i webbeskrivelsen.

Hvordan arv håndteres blir enda mer uklart ved at
[mappe](http://rel.kxml.no/noark5/v4/api/arkivstruktur/mappe/) har
relasjon for å opprette registrering og basisregistrering.

`http://rel.kxml.no/noark5/v4/ny-registrering`

`http://rel.kxml.no/noark5/v4/ny-basisregistrering`

Her brukes ikke utvid-til-* metoden for å opprette basisregistrering
eller eventuelt journalpost.

Det er ingen informasjon på
http://rel.kxml.no/noark5/v4/api/sakarkiv/journalpost/ og heller ingen
informasjon på
http://rel.kxml.no/noark5/v4/api/arkivstruktur/registrering/ om dette.

Vi forstår at dette er noe som kanskje er litt komplisert å få til da
grensesnittene for arkivstruktur og sakarkiv vil overlappe hverandre.
Dette ser vi også i `Noark 5 Standard for elektronisk arkiv`, versjon
5v4. `Del 5.4 Mappe` (sidenummer mangler i standarden).

Slik vi tolker Tjenestegrensesnitt-spesifikasjonen er det i dag
ikke spesifisert hvordan en kan opprette en journalpost koblet til en
saksmappe.  Det er viktig at det finnes en tydelig beskrivelse i
spesifikasjonen om hvordan en saksmappe og en journalpost skal
opprettes.  Det er fordeler og ulemper med utvid-til-* metoden, men
det ville gjøre tjenestegrensesnittet enklere å utvikle hvis det var
mulig å opprette en saksmappe uten `utvid-til-saksmappe`. Det vil
imidlertid kreve at arkivdel og klasse får en relasjon til

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-saksmappe/`

Ønsket endring
--------------

Det introduseres en relasjon for å tillate opprettelse av journalpost
til en saksmappe på side 131.

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-journalpost/`

Det introduseres en relasjon for å tillate opprettelse av en saksmappe
til en arkivdel på side 66, Del (7.2.1.2).

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-saksmappe/`

Det bør antagelig nevnes i teksten at denne kun skal være tilgjengelig
hvis det finnes en
`http://rel.kxml.no/noark5/v4/api/sakarkiv/`-relasjon på toppnivå.

Det introduseres en relasjon for å tillate opprettelse av en saksmappe
til en arkivdel på side 117, Del (7.2.1.12).

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-saksmappe/`

Tilsvarende her bør det nevnes at den kun skal være tilgjengelig hvis
det finnes en `http://rel.kxml.no/noark5/v4/api/sakarkiv/`-relasjon på
toppnivå.

I del 7.2.3.11 (Saksmappe) side 239 endres relasjon

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-saksmappe/`

til

`http://rel.kxml.no/noark5/v4/api/sakarkiv/ny-journalpost/`

Respons
-------

Ingen respons fra arkivverket så langt.
