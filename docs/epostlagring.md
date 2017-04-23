Hvordan lagre epost i en Noark 5-struktur
=========================================

Her følger en beskrivelse om hvordan epost kan lagres i en Noark
5-struktur via et Noark 5 Tjenstegrensesnitt på en slik måte at en kan
gjenskape eposttråder og sjekke kryptosignaturer basert på S/MIME
eller OpenPGP er brukt, samt kontrollere [Domain Keys Identified
Message](http://dkim.org/)-signaturer ([IETF RFC
6376](https://tools.ietf.org/html/rfc4180)).

Epostformatet er standardisert i [IETC RFC
822](https://tools.ietf.org/html/rfc822) og etterfølgende RFCer ([RFC
2822](https://tools.ietf.org/html/rfc2822) og [RFC
5322](https://tools.ietf.org/html/rfc5322)).  Jeg bruker videre i
teksten RFC 822 om dette formatet, for enkelhets skyld.  En epost
består i grove trekk av tekstlinjer, først tekstlinjer som utgjør
epostens hode/metadata, så en blank linje og tekstlinjer som utgjør
epostens kropp/innhold.  Epostenkroppens format og tegnsett er oppgitt
i hodet.  Tegnsett for tittelfeltet (Subject) er oppgitt som del av
tittelfeltet.  Epostens kropp kan bestå av flere deler (såkalte
MIME-vedlegg), som kan hentes ut separat og ha hvert sitt format og
tegnsett.

En mye brukt måte å lagre epost på er som en fil per epost, slik for
eksempel [Maildir-](https://en.wikipedia.org/wiki/Maildir) og
[MH-lagringsformatene](https://en.wikipedia.org/wiki/MH_Message_Handling_System)
gjør.  En annen mye brukt lagringsmåte er flere epost i samme fil slik
for eksempel [mbox-formatet](https://en.wikipedia.org/wiki/Mbox)
([IETC RFC 4155](https://tools.ietf.org/html/rfc4155)) gjør.  I bunnen
av alle disse lagringsformatene ligger formatbeskrivelsen fra RFC 822,
som er det et epostprogram er laget for å tolke.

Epost kan lagres i Noark i sitt opprinnelige format.  I tillegg kan
det være lurt å hente ut enkeltdelene i eposten der det er aktuelt
(f.eks. ved PDF-vedlegg), slik at disse filene er tilgjengelig separat
og kan omformes til PDF/A for langtidslagring.

Eposter kan enten lagres som basisregistrering eller journalpost.
Førstnevnte er for epost som ikke skal med i den offentlige journalen.

Epost inneholder følgende hodefelter relevant for lagring i Noark 5:

 * Subject:
 * From:
 * To:
 * Cc:
 * Reply-To:
 * Sender:
 * Date:
 * In-Reply-To:
 * References:
 * Message-ID:

FIXME: Bestem og beskriv hvordan epost skal lagres:

Hver arkiverte epost får en basisregistrering eller journalpost, alt
etter om eposten skal være journalført eller ikke.  Feltet 'forfatter'
registreres ikke i basisregistreringsdelen, for å unngå
dobbeltregistrering i korrespondansepart og dokumentbeskrivelse.

registrering / basisregistrering / journalpost: {
	    # registrering
	    
            # basisregistrering / journalpost
            "tittel"         : subject,
	    "oppbevaringssted" til første message-id i References?

	    # Journalpost
	    "dokumentDato"   : date
}

For Journalpost registreres det en korrespondansepart for hver adresse
oppgitt i From/Reply-To/Sender, To og Cc.

korrespondansepart: {
	    "korrespondansepartType" : 'avsender' / 'mottaker' / 'kopimottaker' / ...
	    "navn" : from / to / cc / reply-to / sender
	    "kontaktinformasjon.epostadresse" : from / to / cc / reply-to / sender
}

dokumentbeskrivelse: {
            "tittel"         : subject,
	    "forfatter"      : from / sender / reply-to,
	    "tilknyttetRegistreringSom" : "Hoveddkokument"
}

dokumentobjekt: {
            "format"         : 'RFC822',
            "mimeType"       : 'message/rfc822',
            "filnavn"        : message-id,
}

Hvis eposten består av flere vedlegg, så bør det lages separate
dokumentbeskrivelse-/dokumentobjekt-instanser for vedleggene.  Det bør
være mulig å angi av det av disse vedleggene som er følgebrevet /
selve meldingen får tilknyttetRegistreringSom 'Hoveddokument'.


Eksempel
--------

Eksempel uten vedlegg


Eksempel med vedlegg
