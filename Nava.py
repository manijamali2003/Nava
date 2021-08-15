from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Key Creator #

class KeyCreator:
    public = ''  # get public  key
    private = '' # get private key

    # create keys for wallet or bank
    def __init__(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        self.private = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        self.public = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

# Bank #
class Bank:
    def __init__(self):
        pass

    # get public key of bank #
    def publicKey (self):
        f = open('Etc/Bank Keys/Public Key.pem','rb')
        strv = f.read()
        f.close()
        return strv

    # get private key of bank #
    def privateKey (self):
        f = open('Etc/Bank Keys/Private Key.pem','rb')
        strv = f.read()
        f.close()
        return strv

    # create dynamic key for bank #
    def createKeys (self):
        key = KeyCreator()

        f = open('Etc/Bank Keys/Private Key.pem','wb')
        f.write(key.private)
        f.close()

        f = open('Etc/Bank Keys/Public Key.pem', 'wb')
        f.write(key.public)
        f.close()