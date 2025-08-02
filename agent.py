from mastodon import Mastodon
from dotenv import load_dotenv
import os

# Φόρτωσε μεταβλητές από το .env
load_dotenv()

# Από το .env αρχείο
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")
API_BASE_URL = os.getenv("MASTODON_API_BASE_URL")

# Σύνδεση με Mastodon
mastodon = Mastodon(
    access_token=ACCESS_TOKEN,
    api_base_url=API_BASE_URL
)

# Το μήνυμα που θέλεις να δημοσιεύσεις
message = "🧠 SparkEthos Agent ενεργοποιήθηκε! #AI #Ethics #SparkEthos"

# Κάνε post!
mastodon.toot(message)
print("✅ Δημοσιεύτηκε στο Mastodon!")
