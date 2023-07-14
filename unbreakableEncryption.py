from secrets import token_bytes
from typing import Tuple

def random_key(length:int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(original: str)->Tuple[int, int]:
    original_bytes: bytes = original.encode()
    original_key: int = int.from_bytes(original_bytes, "big")
    dummy: int = random_key(len(original_bytes))
    encrypted: int = original_key ^ dummy
    return (dummy, encrypted)

def decrypt(key1: int, key2: int)->str:
    original_int: int = key1 ^ key2 
    original_bytes: bytes = original_int.to_bytes((original_int.bit_length()+7)//8, 'big')
    return original_bytes.decode()

original = "ALI"
key1, key2 = encrypt(original)
decrypted = decrypt(key1, key2)

print(original ,key1, key2, decrypted)