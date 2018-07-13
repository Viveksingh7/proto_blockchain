import hashlib as hl
"""for hashing"""
import json
"""for string conversion"""


def hash_string_256(string):
    return hl.sha256(string).digest()

def hash_block(block):
    """Arguments:
    The block that should be hashed"""
    return hash_string_256(json.dumps(block, sort_keys=True).encode())
