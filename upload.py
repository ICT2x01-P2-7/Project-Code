import requests

class uploadCode:
    def __init__(self, input: str, ip: str) -> None:
        self.input = input
        self.ip = ip
    
    # This method sends the text in the code text box to the car
    # Input: String
    # Output: Boolean
    def send(self):
        URL = "http://" + self.ip + "/" + self.input
        print(URL)

        try:
            response = requests.get(URL)
        except:
            return False
        print(response.status_code)
        print(response.text)

        if response.status_code == 200:
            return True
        else:
            return False