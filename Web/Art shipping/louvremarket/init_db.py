import sqlite3

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL,
  message TEXT NOT NULL
);
""")

messages = [
    ('alice@protonmail.art', 'Hello, I would like to buy the Winged Victory. Please send details.'),
    ('john@hiddenframes.io', 'Do you deliver internationally?'),
    ('emily@forgotten-gallery.net', 'Is the Mona Lisa still available? Asking for a friend.'),
    ('noah@cipherbrush.org', 'What kind of encryption do you use for payment?'),
    ('sophia@lostportraits.art', 'Interested in Gabrielle d\'Estrées. Can we negotiate the price?'),
    ('liam@darkcurator.co', 'How long does shipping take? I\'m in South America.'),
    ('olivia@silenthalls.onion', 'I found your site by accident. Or was it fate?'),
    ('mason@monero-louvre.biz', 'Do you accept Monero? Asking anonymously.'),
    ('ava@ghostcanvas.org', 'I heard you have the Raft of the Medusa. Confirm?'),
    ('logan@undergroundpaint.net', 'Looking for something... more discreet.'),
    ('mia@collector-x.io', 'My collector friend is very interested in Saint John.'),
    ('elijah@fakenapoleon.gallery', 'Can you forge certificates of authenticity?'),
    ('isabella@btc-artsafe.com', 'I can offer 20 BTC upfront for the Venus.'),
    ('james@artsmuggler.email', 'Do you provide any kind of refund if intercepted?'),
    ('amelia@scrollvault.xyz', 'Do you also deal in ancient texts?'),
    ('benjamin@lostframes.art', 'Your security key seems outdated. Can you confirm the new one?'),
    ('charlotte@canvasdark.net', 'I saw movement in one of the gallery images. Easter egg?'),
    ('lucas@artdeals.sh', 'Interested in bulk purchases. What\'s the protocol?'),
    ('harper@unknownarchive.org', 'What else do you have beyond what’s on display?'),
    ('henry@louvre42.onion', 'Do you use a hidden onion service?'),
    ('evelyn@blackmarket.gallery', 'My employer is willing to double the price.'),
    ('jack@vaultedroom.art', 'Can you store the items until I can retrieve them in person?'),
    ('abigail@hollowmuseum.org', 'Your site is beautiful. Mysterious. Like the art itself.'),
    ('sebastian@strangerbrush.io', 'I accidentally stumbled on this site. Should I be worried?'),
    ('ella@hiddenhall.art', 'I need a piece that hasn’t been seen in decades.'),
    ('alexander@whispersgallery.net', 'I’m being watched. Need a secure drop point.'),
    ('scarlett@cleopatra-endgame.biz', 'What is the story behind Cleopatra dying? It fascinates me.'),
    ('daniel@relichunter.pro', 'Will I be contacted after this message?'),
    ('grace@bloodoncanvas.com', 'Can I place a reservation for Liberty Leading the People?'),
    ('matthew@crimsongallery.org', 'I have BTC ready. Waiting on your instructions.'),
    ('zoe@phantomframes.xyz', 'Is this connected to the 2009 disappearance case?'),
    ('aiden@hiddenexpo.sh', 'I saw this domain on a dark web forum.'),
    ('nora@miragevault.onion', 'What happens if someone finds this archive?'),
    ('jayden@vintageghost.art', 'My uncle used to work at the Louvre... He would not believe this.'),
    ('chloe@veilcollection.io', 'I need discretion above all else.'),
    ('david@forbidden.gallery', 'How do I prove I’m trustworthy?'),
    ('lily@museumofshadows.org', 'My professor warned me about sites like this.'),
    ('joseph@blackframe.biz', 'Any plans to expand to sculptures from Greece?'),
    ('aurora@initiate.gallery', 'How can I join the organization?'),
    ('gabriel@whitelist.zone', 'Some messages in your footer source seem encoded.'),
    ('victoria@nocturnalmasterpieces.net', 'Art is power. And you have plenty.'),
    ('samuel@silkroadpaint.art', 'I left a hidden note in one of your forms. Let me know if you find it.'),
    ('zoey@encryptedgallery.xyz', 'You should rotate your PGP key more often.'),
    ('leo@obscura.network', 'Nice touch with the Victory of Samothrace.'),
    ('layla@redtomb.art', 'Do you have any stolen pieces from South Asia?'),
    ('nathan@ghosted.art', 'How long do pieces remain in your gallery before they vanish?'),
    ('stella@secretvault.xyz', 'Can we meet in person? I know a place near the Seine.'),
    ('isaac@eagleofstdenis.org', 'What’s the story with Suger’s Eagle? It gave me chills.'),
    ('penelope@undergroundlouvre.io', 'Who are you people, really? Louvre Underground? Sounds like a legend.'),
    ('julian@cryptogallery.sh', 'I think I’ve seen one of your paintings in a private collection in Zurich.'),
]

for email, message in messages:
    cursor.execute("SELECT id FROM messages WHERE email = ? AND message = ?", (email, message))
    if cursor.fetchone() is None:  # Si le message n'existe pas déjà
        cursor.execute("INSERT INTO messages (email, message) VALUES (?, ?)", (email, message))

conn.commit()
conn.close()
