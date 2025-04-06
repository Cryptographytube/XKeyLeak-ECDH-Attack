# AUTH: SISU | Script : CRYPTOGRAPHYTUBE
from coincurve import PrivateKey, PublicKey

def precompute_ecdh_outputs(pubkey_hex, limit):
    pub = PublicKey(bytes.fromhex(pubkey_hex))
    with open("ecdh_table.txt", "w") as f:
        for i in range(1, limit):
            priv = PrivateKey.from_int(i)
            try:
                shared = pub.ecdh(priv.secret)
                f.write(f"{shared.hex()}:{i}\n")
            except:
                continue

print("CRYPTOGRAPHYTUBE Precomputation Module Started - AUTH: SISU")
# Example call: precompute_ecdh_outputs('02abc...', 1000000)
