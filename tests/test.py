from blockchain import Blockchain, Wallet, Transaction

my_blockchain = Blockchain()

alice = Wallet()
bob = Wallet()

transaction1 = Transaction(sender=alice.public_key.to_string().hex(), receiver=bob.public_key.to_string().hex(), amount=50)

#sign transaction
signature = alice.sign_transaction(transaction1)
if Wallet.verify_signature(alice.public_key, transaction1, signature):
    my_blockchain.add_transaction(transaction1.to_dict())
else:
    print("Transaction is invalid!")

#mine block
my_blockchain.mine_pending_transactions(miner_address="Miner1")

# Display blockchain
for block in my_blockchain.chain:
    print(f"Index: {block.index}, Hash: {block.hash}, Data: {block.data}")