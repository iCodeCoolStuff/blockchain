import hashlib
import time

class Block(object):
    def __init__(self, timestamp, last_hsh, hsh, data):
        self.timestamp = timestamp
        self.last_hsh   = last_hsh
        self.hsh       = hsh
        self.data      = data

    def __str__(self):
        return f'Block -\n'\
            + f'\tTimestamp: {self.timestamp}\n' \
            + f'\tLast Hash: {self.last_hsh[0:10]}\n' \
            + f'\tHash: {self.hsh[0:10]}\n' \
            + f'\tData: {self.data}'


class GenesisBlock(Block):
    def __init__(self):
       return super().__init__('Genesis Time', '-----', 'first hash', []) 


class MineBlock(Block):
    def __init__(self, lastblock, data):
        timestamp = time.time()
        hsh = hashlib.sha256(f'{timestamp}{lastblock.hsh}{data}'.encode('utf-8'))
        return super().__init__(timestamp, lastblock.hsh, hsh.hexdigest(), data)


class Blockchain(object):
    def __init__(self):
        self.chain = [GenesisBlock()]

    def add_block(self, data):
        block = MineBlock(self.chain[-1], data)
        self.chain.append(block)
        return block
