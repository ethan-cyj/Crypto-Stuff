from ecdsa import SigningKey, SECP256k1

class Wallet:
    def __init__(self):
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def sign_transaction(self, transaction):
        transaction_data = f"{transaction.sender}{transaction.receiver}{transaction.amount}"
        return self.private_key.sign(transaction_data.encode())

    @staticmethod
    def verify_signature(public_key, transaction, signature):
        transaction_data = f"{transaction.sender}{transaction.receiver}{transaction.amount}"
        return public_key.verify(signature, transaction_data.encode())