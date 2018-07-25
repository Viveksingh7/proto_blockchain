import hashlib as hl
"""for hashing"""
import json
"""for string conversion"""


def hash_string_256(string):
    return hl.sha256(string).hexdigest()

def hash_block(block):
    """Arguments:"""
    """ JSON """
    hashable_block = block.__dict__.copy()

    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
