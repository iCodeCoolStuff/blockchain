from hashlib import sha256
from Crypto.Signature import DSS

class Transaction(object):
    def __init__(self, public_key, last_transaction, signature):
        self.public_key             = public_key
        self.last_transaction_hash  = sha256(last_transaction)
        self.signature              = signature

    def verify(self):
        verifier = DSS.new(self.public_key, 'fips-186-3') 
        try:
            verifier.verify(self.last_transaction_hash, self.signature)
            return True
        except:
            return False
