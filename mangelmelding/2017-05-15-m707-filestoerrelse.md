Hvordan skal innholdet i filstørrelse (M707) tolkes?
====================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5
           Kategori  Versjon 4.0
        Alvorlighet  protest
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  7.2.1.7
         Sidenummer  105
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til NOARK5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

M707 filstørrelse (filstoerrelse i XSD) er definert med datatype
«string» i metadatakatalogen, og med følgende beskrivelse «Definisjon:
Størrelsen på fila i antall bytes oppgitt med desimaltall Kilde:
Registreres automatisk i forbindelse med eksport for avlevering
Kommentarer: (ingen)».

Et [desimaltall](https://no.wikipedia.org/wiki/Desimaltall) er i følge
den norske Wikipediasiden, «tall som er satt sammen av en heltallsdel
og en fraksjonsdel. Disse to delene er skilt med et
desimalskilletegn. Et eksempel kan være tallet «49,90» der
heltallsdelen er «49» og fraksjondelen er «90».» [Store Norske
Leksikon](https://snl.no/numerisk_metode) bekrefter denne språkbruken.

Beskrivelsen «desimaltall» tyder dermed på at størrelsen skal kunne
være brøkdeler av en byte, hvilket ikke gir mening.  Er tanken at det
skal være mulig å lagre størrelsen i kibibytes, kilobytes eller
lignende, dvs. lagre «1,2 KiB» i feltet?  Dette vil i så fall kreve
klare regler for avrunding og gjøre det vanskelig å bruke verdien til
å sjekke at komplett fil er lastet opp og ned på grunn av avrunding.
For eksempel er det vanskelig å vite hva størrelsen egentlig er hvis
det står 1,2 KiB, da 1,2*1024 jo er 1228,8, og størrelsen jo da må
være enten 1228 eller 1229 bytes.

I tillegg kommer jo tolkningsutfordringer når det gjelder f.eks. «KB»,
som både kan tolkes som verdi ganger 1000 eller 1024.  Her må
spesifikasjonen klargjøre hvordan slike verdier skal tolkes hvis det
skal være mulig med desimaltall.

En annen utfordring er at formattering av desimaltall er
språkavhengig, der noen bruker punktum som desimalskille, mens andre
bruker komma.

Det vil være enklere for alle, både API-klienter og andre
implementasjoner, hvis dette feltet har en klar og entydig betydning,
og alltid er et heltall større eller lik null som oppgir filstørrelsen
i bytes.

Feltet «filstørrelse» er brukt på sidene 29, 50, 52, 54, 105 og 203 i
spesifikasjonen for Noark 5 Tjenestegrensesnitt.

Ønsket endring
--------------

Endre feltbeskrivelsen i del 7.2.1.7 (Dokumentobjekt) på side 105 fra

> Definisjon: Størrelsen på fila i antall bytes oppgitt med
> desimaltall

til

> Definisjon: Størrelsen på fila i antall bytes i oppgitt som et
> ikke-negativt heltall i titallsystemet i en string,
> f.eks. "123456890".
