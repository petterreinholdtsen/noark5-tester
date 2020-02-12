Enklere opplasting av nye filer til arkivet
===========================================

 ------------------  ---------------------------------
           Prosjekt  Noark 5 Tjenestegrensesnitt
           Kategori  Noark 5.5.0 TG versjon 1.0
        Alvorlighet  kommentar
       Meldingstype  trenger klargjøring
    Brukerreferanse  pere@hungry.com
        Dokumentdel  6.1.1.9
         Sidenummer  ?
        Linjenummer  n/a
    Innsendingsdato  ikke sendt inn
 ------------------  ---------------------------------

Denne teksten er del av en samling innspill til Noark5-standarden
tilgjengelig fra [https://github.com/petterreinholdtsen/noark5-tester/](https://github.com/petterreinholdtsen/noark5-tester/).

Beskrivelse
-----------

I dag må API-klienter som ønsker å laste opp en fil til en
registering, gjøre minst tre HTTP-forespørsler:

 - Opprette dokumentbeskrivelse
 - Opprette dokumentobjekt
 - Laste opp innholdet i filen

Et alternativ er å lage et nytt endepunkt koblet til registrering for
å laste opp en fil, og som hvis opplastingen går bra returnerer både
en dokumentbeskrivelse og et dokumentobjekt med informasjon fylt ut
fra metadata i den opplastede filen.

Problemstillingen ble også diskutert i
https://github.com/arkivverket/noark5-tjenestegrensesnitt-standard/issues/25,
som har litt nyttig bakgrunnsinformasjon.

Relasjonsnøkkel for opplasting av filer til dokumentobjekt er i dag
https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/fil/ og samme
nøkkel kan implementeres i registrering.

Responsen kan bruke _embedded-konseptet fra
https://tools.ietf.org/html/draft-kelly-json-hal-08 og for eksempel se
slik ut:

```
{
    "systemID": "9e249205-700a-14cc-8170-0a335aff0033", 
    "tilknyttetAv": "admin@example.com", 
    "tittel": "Title of the test document description created 2020-02-03T09:38:13.341767 modified", 
    "dokumentnummer": 1, 
    "dokumentstatus": {
        "kode": "F", 
        "kodenavn": "Dokumentet er ferdigstilt"
    }, 
    "tilknyttetDato": "2020-02-03T09:38:22+01:00", 
    "oppdatertAv": "admin@example.com", 
    "tilknyttetRegistreringSom": {
        "kode": "H", 
        "kodenavn": "Hoveddokument"
    }, 
    "oppdatertDato": "2020-02-03T09:38:58+01:00", 
    "dokumenttype": {
        "kode": "B", 
        "kodenavn": "Brev"
    }, 
    "_links": {
        "https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/merknad/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/merknad/"
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/ny-merknad/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/ny-merknad/"
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/metadata/dokumentmedium/": {
            "href": "https://n5.example.com/api/metadata/dokumentmedium"
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/dokumentbeskrivelse/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/"
        }, 
        "https://nikita.arkivlab.no/noark5/v5/ny-oppbevaringssted/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/ny-oppbevaringssted/"
        }, 
        "self": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/"
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/dokumentobjekt/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/dokumentobjekt/"
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/ny-partperson/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/ny-partperson/"
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/ny-dokumentobjekt/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/ny-dokumentobjekt/"
        }, 
        "https://nikita.arkivlab.no/noark5/v5/ny-forfatter/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/ny-forfatter/"
        }, 
        "https://nikita.arkivlab.no/noark5/v5/forfatter/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/forfatter/", 
            "templated": true
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/metadata/dokumenttype/": {
            "href": "https://n5.example.com/api/metadata/dokumenttype"
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/part/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/part/", 
            "templated": true
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/metadata/dokumentstatus/": {
            "href": "https://n5.example.com/api/metadata/dokumentstatus"
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/ny-partenhet/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/ny-partenhet/"
        }, 
        "https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/registrering/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/registrering"
        }, 
        "https://nikita.arkivlab.no/noark5/v5/oppbevaringssted/": {
            "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a335aff0033/oppbevaringssted/"
        }
    },
    "_embedded": {
	"https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/dokumentobjekt/": {
	    "mimeType": "application/xml", 
	    "oppdatertAv": "admin@example.com", 
	    "format": {
		"kode": "fmt/101", 
		"kodenavn": "XML"
	    }, 
	    "versjonsnummer": 1, 
	    "variantformat": {
		"kode": "P", 
		"kodenavn": "Produksjonsformat"
	    }, 
	    "sjekksumAlgoritme": "SHA-256", 
	    "systemID": "9e249205-700a-14cc-8170-0a33d00f0069", 
	    "sjekksum": "c59e720ac991a31c956c37eca53b8dd14516638e6e8640622f7a5a8755ff2367", 
	    "filstoerrelse": 50, 
	    "oppdatertDato": "2020-02-03T09:38:53+01:00", 
	    "_links": {
		"https://rel.arkivverket.no/noark5/v5/api/metadata/variantformat/": {
		    "href": "https://n5.example.com/api/metadata/variantformat"
		}, 
		"https://nikita.arkivlab.no/noark5/v5/konverterFil/": {
		    "href": "https://n5.example.com/api/arkivstruktur/dokumentobjekt/9e249205-700a-14cc-8170-0a33d00f0069/konverterFil"
		}, 
		"https://rel.arkivverket.no/noark5/v5/api/metadata/format/": {
		    "href": "https://n5.example.com/api/metadata/format"
		}, 
		"https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/dokumentbeskrivelse/": {
		    "href": "https://n5.example.com/api/arkivstruktur/dokumentbeskrivelse/9e249205-700a-14cc-8170-0a33ced80067"
		}, 
		"self": {
		    "href": "https://n5.example.com/api/arkivstruktur/dokumentobjekt/9e249205-700a-14cc-8170-0a33d00f0069/"
		}, 
		"https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/dokumentobjekt/": {
		    "href": "https://n5.example.com/api/arkivstruktur/dokumentobjekt/9e249205-700a-14cc-8170-0a33d00f0069/"
		}, 
		"https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/konvertering/": {
		    "href": "https://n5.example.com/api/arkivstruktur/dokumentobjekt/9e249205-700a-14cc-8170-0a33d00f0069/konvertering/"
		}, 
		"https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/ny-konvertering/": {
		    "href": "https://n5.example.com/api/arkivstruktur/dokumentobjekt/9e249205-700a-14cc-8170-0a33d00f0069/ny-konvertering/"
		}, 
		"https://rel.arkivverket.no/noark5/v5/api/arkivstruktur/fil/": {
		    "href": "https://n5.example.com/api/arkivstruktur/dokumentobjekt/9e249205-700a-14cc-8170-0a33d00f0069/referanseFil/"
		}
	    }
	}
    }
}
```

Det vil fortsatt være behov for å kunne laste opp enkeltfiler knyttet
til samme dokumentbeskrivelse, for eksterne API-klienter som tar seg
av filkonvertering.

Ønsket endring
--------------

Beskriv dette alternativet i spesifikasjonen.
