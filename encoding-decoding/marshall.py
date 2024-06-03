import pickle

# Original object
data = {"name": "Alice", "age": 30, "city": "Wonderland"}

# Marshalling (serializing) the object to a byte stream
marshalled_data = pickle.dumps(data)

print("Marshalled data (pickle):", marshalled_data)

# Unmarshalling (deserializing) back to a Python object
unmarshalled_data = pickle.loads(marshalled_data)
print("Unmarshalled data:", unmarshalled_data)
