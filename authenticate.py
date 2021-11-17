import hashlib

def check(input):
    if isinstance(input, int):
        return False
    
    if isinstance(input, float):
        return False

    # Hash the password for comparison
    encoded = input.encode()
    result = hashlib.sha256(encoded)
    hexadecimal = result.hexdigest()

    #print(hexadecimal)
    
    if hexadecimal != "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918":
        return False
    
    return True