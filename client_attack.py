# AUTH: SISU | Script : CRYPTOGRAPHYTUBE
import requests
from coincurve import PrivateKey

def get_ecdh_from_server(pubkey_hex):
    headers = {'X-Pubkey': pubkey_hex}
    try:
        r = requests.get('http://localhost:8080/ecdh', headers=headers)
        return r.text.strip()
    except:
        return None

def attack_mode():
    print("CRYPTOGRAPHYTUBE Client Attack Mode - AUTH: SISU")
    crafted_privs = [PrivateKey() for _ in range(10)]
    crafted_pubs = [p.public_key.format(compressed=True).hex() for p in crafted_privs]
    leaked = []
    for pub_hex in crafted_pubs:
        shared = get_ecdh_from_server(pub_hex)
        if shared:
            print(f"Shared: {shared[:16]}...")
            leaked.append(shared)
    print(f"Crafted Public Keys: {len(crafted_pubs)}")
    print(f"Leaked ECDH values : {len(leaked)}")
    print("Simulated Private Key Recovery Completed - CRYPTOGRAPHYTUBE")

attack_mode()
