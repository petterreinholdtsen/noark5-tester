Beskriv hvordan Kryssreferanser opprettes
=========================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  versjon git 2019-04-22
        Alvorlighet  protest
       Meldingstype  utelatt
    Brukerreferanse  pere@hungry.com
        Dokumentdel  Finn ut
         Sidenummer  Finn ut
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra
[https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

Det er uklart fra spesifikasjonen hvordan en skal opprette en ny
Kryssreferanse-instans.

arkivdel:

{
  tittel : fla
  _links : [
     ...mappe: mappe/?foreldrearkivdel=arkivdelsystemid
  ]
}

arkivdel-systemid-mappe:

{
  results : [
     {mappe},
     {mappe},
  ]
}

mappe/?foreldre=arkivdlesystemid
{
  results : [
     {mappe},
     {mappe},
  ]
}

mappe
{
  _links : 
    kryssreferanse : mappe/systemid/kryssreferanse
    kryssreferanse : kryssreferanse/?foreldremappe=mappesystemid
}

mappe/systemid/kryssreferanse:

{
  results : [
    {
       referanseTilMappe : systemid
    }
    {
       _links : [
         mappe : ...mappe/systemid/
    }
  ]
}


http://localhost:49708/api/arkivstruktur/mappe/cf8e1d0d-e94d-4d07-b5ed-46ba2df0465e/ny-kryssreferanse/$ref?$id=http://localhost:49708/api/arkivstruktur/registrering/1fa94a89-3550-470b-a220-92dd4d709044
http://localhost:49708/api/arkivstruktur/mappe/cf8e1d0d-e94d-4d07-b5ed-46ba2df0465e/ny-kryssreferanse/$ref?$id=http://localhost:49708/api/arkivstruktur/klasse/4ea94a89-3550-470b-a220-92dd4d709042

Ønsket endring
--------------

FIXME

Jeg sender inn konkret forslag til endring som patch via github.
