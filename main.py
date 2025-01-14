from flask import Flask, jsonify, request
from blockchain import Blockchain, Transaction, Wallet

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """
    Endpoint to mine a new block with pending transactions.
    """
    miner_address = "Miner1"  # Replace with your wallet address
    blockchain.mine_pending_transactions(miner_address)
    return jsonify({"message": "Block mined successfully!", "chain": get_chain_data()}), 200

@app.route('/transactions/new', methods=['POST'])
def add_transaction():
    """
    Endpoint to add a new transaction to the blockchain.
    """
    data = request.get_json()
    required_fields = ['sender', 'receiver', 'amount']

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Invalid transaction data"}), 400

    transaction = Transaction(
        sender=data['sender'],
        receiver=data['receiver'],
        amount=data['amount']
    )
    blockchain.add_transaction(transaction.to_dict())
    return jsonify({"message": "Transaction added successfully!"}), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    """
    Endpoint to get the current blockchain.
    """
    return jsonify({"chain": get_chain_data(), "length": len(blockchain.chain)}), 200

def get_chain_data():
    """
    Helper function to serialize the blockchain data for the API response.
    """
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            "index": block.index,
            "previous_hash": block.previous_hash,
            "timestamp": block.timestamp,
            "data": block.data,
            "hash": block.hash,
        })
    return chain_data

if __name__ == '__main__':
    app.run(port=5000, debug=True)
