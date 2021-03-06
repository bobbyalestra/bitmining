from hashlib import sha256
MAX_NONCE = 10000000


def SHA256(text):
    return sha256("ABC".encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        nonce = 3
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay you got bitcoins of nonce value :{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct after trying {MAX_NONCE} times")


if __name__=='__main__':
    transactions = '''
    
    '''
    difficulty=6
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5, transactions, 'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78', difficulty)
    total_time = str((time.time() - start))
    print(f"end of mining. Mining took: {total_time} seconds")
    print(new_hash)