import socket
import requests

# This method checks to make sure that the input from the user is valid
# Input: String
# Output: Boolean
def validate_ip_address(address):
    parts = address.split(".")

    if len(parts) != 4:
        #print("IP address {} is not valid".format(address))
        return False

    for part in parts:
        if not isinstance(int(part), int):
            #print("IP address {} is not valid".format(address))
            return False

        if int(part) < 0 or int(part) > 255:
            #print("IP address {} is not valid".format(address))
            return False
 
    #print("IP address {} is valid".format(address))
    return True

# This method actually starts the connection with the car
# Input: String
# Output: Boolean
def start_connect(address):
    URL = "http://" + address + "/"
    response = requests.get(URL)
    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        return True
    else:
        return False        
       