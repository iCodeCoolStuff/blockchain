import block

if __name__ == '__main__':
    bc = block.Blockchain()
    bc.add_block('hello')
    print(bc.chain)
