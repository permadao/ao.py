import hashlib
import arweave
from jose.utils import base64url_encode

class ARSigner:
    def __init__(self, arwallet_file_path):
        self.type = 'AR'
        self.wallet = arweave.Wallet(arwallet_file_path)
        self.address = self.wallet.address
        self.owner = self.wallet.owner

    def sign(self, msg):
        h = hashlib.sha256(msg.encode()).digest()
        sig = base64url_encode(self.wallet.sign(h)).decode()
        return sig
    
    def sign_bundle(self, msg):
        sig = self.sign(msg)
        sig = f'{sig},{self.owner}'
        return sig