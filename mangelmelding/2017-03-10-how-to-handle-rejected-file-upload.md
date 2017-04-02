Filopplasting som del av dokumentobjekt-transaksjon
===================================================

 ------------------  ---------------------------------
           Prosjekt  NOARK 5 Tjenestegresesnitt
           Kategori  Versjon 1.0 beta
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  thomas.sodring@hioa.no
        Dokumentdel  6.1.9
         Sidenummer  25
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Beskrivelse
-----------

Prosessen med å laste opp en fil kan ses på som en transaksjon som
inkluderer opprettelsen av dokumentbeskrivelse, dokumentobjekt og
selve filen.  Hvis det skulle skje at det er problemer med
lagringssystemet, for eksempel hvis filsystemet er fullt eller
opplever en annen forstyrrelse, så kan det hende at dokumentobjekt
opprettes og lagres til persistent lager, men selve filopplastingen
blir avvist.  Dette vil returnere først 200 OK for dokumentobjekt og
deretter en 50X Error ved opplastingen.

Det er uklart fra spesifikasjonen hva som skal gjøres i et slikt
tilfelle, og det er ingen dokumentert mekanisme for klienten å be om
at det filløse dokumentobjekt-instansen slettes når det skjer.  Det er
dermed ikke mulig for klienten å rydde opp etter seg når feilen
oppstår.  Den eneste muligheten for klienten er å forsøkte opplasting
på nytt og på nytt frem til den lykkes, og det er ikke alltid mulig
for en klient å fortsette til evig tid.  Det er bedre om klienten kan
rydde opp og så forsøke på nytt når det passer.

Ønsket endring
--------------

FIXME formuler konkret forslag til endring.

Dette tilfellet trenger en avklaring.  En mulig løsning er å lage et
API-kall til kjernen der dokumentbeskrivelse, dokumentobjekt og selve
filen lastes opp sammen.  En slik løsning gjør det mulig for kjernen å
behandle opprettelsen som en transaksjon og la alle tre stegene feile
hvis en av dem feiler.  Dermed kan klienten vite om hele transaksjonen
var vellykket og filen er lagret slik den skal.
