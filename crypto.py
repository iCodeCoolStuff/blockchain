from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

def generate_keys():
    priv_key = ECC.generate(curve='P-256')
    return priv_key.public_key(), priv_key

#pub, priv = generate_keys()

