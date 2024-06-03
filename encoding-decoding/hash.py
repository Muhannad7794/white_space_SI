import hashlib

# Original data
data = "Hello, World!"

# Hashing the data using SHA-256
hash_object = hashlib.sha256(data.encode())
hash_hex = hash_object.hexdigest()

print("Hashed data (SHA-256):", hash_hex)
