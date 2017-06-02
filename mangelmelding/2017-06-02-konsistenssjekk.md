Definer mekanisme for tilbakemelding på konsistenssjekk
=======================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  n/a
         Sidenummer  n/a
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er ønskelig at arkivsystemet gjør konsistenssjekk av data som
legges inn i arkivet, og det mangler en beskrivelse i
tjenestegrensesnittet om hvordan tilbakemelding fra slik
konsistenssjekk skal sendes tilbake til klienter som legger inn data i
arkivet.

Her er noen eksempler på slike konsistenssjekker:

 * Kontrollere at metadata gir tidsmessig mening.  For eksemepel vil
   dokumentdato være før journaldato i normale tilfeller, og
   dokumentdato vil ikke være veldig langt inn i for- eller fremtiden.

 * Graderte dokumenter er nyere enn foreldelsesfristene for
   graderingen.

 * Navn og organisasjonsnummer på KorrespondansepartEnhet stemmer ikke
   over ens med det som står i brønnøysundsregisteret.

 * Postnummeret brukt i en korrespondanseenhet finnes ikke.

 * Det opplastede dokumentet har et format som ikke aksepteres av
   arkivverket for langtidsoppbevaring.

Slike feil er ofte resultat av manuelle skrivefeil, og bør oppdages så
raskt som mulig for å holde kvaliteten i arkivsystemet oppe.

Slik konsistenssjekk kan gjøres når ny entitet opprettes med POST Til
ny-* eller når en entitet oppdateres med PUT.  Det er dermed fint om
resultatet fra slike konsistenssjekker kan være del av svaret som
kommer fra POST og PUT.

En lite inngripende måte å gjøre dette på er å legge ved en ekstra
relasjon i _links hvis konsistenssjekken har oppdaget noe rart, og så
peke href-verdien til et sted der detaljer om hva som ble oppdaget
returneres.  Det gjør at klienter som ikke forstår
konsistenssjekk-tilbakemeldingen kan ignorere den, mens klienter som
forstår relasjonen kan vise frem detaljene til brukeren i tilfelle det
bare er en skrivefeil.

Konsistenssjekk-resultatene bør antagelig ha en typeklasse,
alvorlighet og en beskrivelse.  Det kan bli en utfordring å gi gode
beskrivelser hvis resultatet skal kunne oversettes til flere språk.

Ønsket endring
--------------

FIXME dokumenter hvordan dette skal gjøres og hvordan resultatet fra
konsistenssjekken skal se ut.
