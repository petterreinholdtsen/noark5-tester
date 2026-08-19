IMAP Shim for Noark 5 Tjenestegrensesnitt
=========================================

**What it does**
----------------

The IMAP shim is a lightweight IMAP frontend that exposes message objects from a
Noark 5 archive as an IMAP mailbox. Any standard IMAP client (Mutt, Thunderbird,
etc.) can read archived e-mail without knowing about the Noark 5 API underneath.

It runs as a standalone Python 3 script and translates between IMAP protocol (RFC 9051) on one
side and REST calls to the Noark 5 ``tjenestegrensesnitt`` API on the other.

**Running the shim**
--------------------

Start it in the background, pointing at your Noark 5 instance::

    python3 imap-shim --baseurl http://your-host:8092/noark5v5/ --port 14143

Options:

.. list-table::
   :widths: 20 60
   :header-rows: 1

   * - Argument
     - Description
   * - ``--baseurl URL``
     - Noark 5 API base URL (default: ``http://localhost:8092/noark5v5/``)
   * - ``--port PORT``
     - IMAP listen port (default: 143, use a high number to avoid root requirement)

The shim listens on ``127.0.0.1`` only. It logs protocol activity to stdout/stderr;
redirect as desired::

    python3 imap-shim --baseurl http://your-host:8092/noark5v5/ --port 14143 \
        >> /tmp/shim.log 2>&1 &

**Configuring Mutt**
--------------------

Add these lines to your ``~/.muttrc``::

    set imap_user = 'your-username'
    set imap_pass = 'your-password'
    set folder = 'imap://localhost:14143'
    set spoolfile = 'imap://localhost:14143/YourMailboxName'
    set imap_check_subscribed = yes

Replace the credentials with your Noark 5 API user. The ``spoolfile`` mailbox name
must match a fonds (arkiv) title returned by the API — run ``mutt`` and press ``c`` to
change folder, then pick from the LIST.

The shim implements IMAP4rev1 per RFC 9051 and advertises: ``IMAP4rev1 IDLE UIDPLUS``

Implemented commands:

- ``CAPABILITY``, ``LOGIN``, ``LOGOUT``, ``NOOP``
- ``LIST``, ``LSUB`` — enumerates fonds as mailboxes
- ``SELECT``, ``EXAMINE`` — opens a mailbox, returns FLAGS/EXISTS/PERMANENTFLAGS/UIDVALIDITY/UIDNEXT
- ``FETCH`` (sequence and UID) — returns UID, FLAGS, INTERNALDATE, RFC822.SIZE, BODY[] full message, BODY.PEEK[HEADER.FIELDS (...)] filtered headers, ENVELOPE
- ``UID FETCH``, ``UID SEARCH``
- ``STATUS`` — stub values for buffy polling
- ``CLOSE``

**Architecture**
----------------

The shim walks the Noark 5 hierarchy (arkiv → arkivdel → klassifikasjonssystem → klasse/subklasse → mappe/undermappe → registrering → dokumentbeskrivelse → dokumentobjekt) and collects all objects with MIME type ``message/rfc822``. Each becomes an IMAP message in the selected mailbox, served on-demand from the API's file endpoint.

Sequence numbers are assigned 1..N at SELECT time. UIDs map 1:1 to sequence
numbers (no persistent UID store — re-SELECT resets).
