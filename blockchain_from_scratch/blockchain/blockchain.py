from config import DIFFICULTY, MINING_REWARD
from blockchain import Block
import time
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = DIFFICULTY
        self.pending_transactions = []
        self.mining_reward = MINING_REWARD
    
    def create_genesis_block(self):
        return Block(0,"0", time.time(), "Genesis Block" )

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction): 
        # transaction must first be converted to dict from Transaction object
        # assume the transaction has signed and verified to be valid. For now handled in main code
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        #creates a new block
        #mines this block (finding a valid hash based on difficulty)
        #add block to chain, and rewards the miner
        new_block = Block(
            index = len(self.chain),
            previous_hash = self.get_latest_block().hash,
            timestamp = time.time(),
            data = self.pending_transactions
            #hash calculated on creation is not yet valid
        )
        self.mine_block(new_block)
        self.chain.append(new_block)
        self.pending_transactions = [{"from": "network", "to": miner_address, "amount": self.mining_reward}]


    def mine_block(self, block):
        prefix = "0" * self.difficulty
        while not block.hash.startswith(prefix):
            block.nonce += 1
            block.hash = block.calculate_hash() #update hash

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True