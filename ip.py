import socket
import requests

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

def start_connect(address):
    URL = "http://" + address + "/"
    response = requests.get(URL)
    print(response.status_code)
    print(response.text)

    if response.status_code == True:
        return True
    else:
        return False        
       