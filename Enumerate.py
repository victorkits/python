from enum import Enum
import requests


class X(Enum):
    ONE = 'one'
    TWO = 'two'
    THREE = 'three'

    def __str__(self):
        if self.value in a:
            return self.__class__.__name__
        else:
            return "Error"


# class Numbers(Enum):
#
#     def __str__(self):
#         if self.value in a:
#             return str(self.name)
#         else:
#             return "Error"


# def enum(**named_values):
#     return type('Enum', (), named_values)



if __name__ == '__main__':


    url = "https://auth-int.simon-cloud.com/oauth/v2/token"

    payload = "{\"grant_type\": \"client_credentials\",\n\"client_id\": \"29_uak2m5jko1wgo00owo8gcs4owowo8ww0gckos04oo00s0sskk\",\n\"client_secret\": \"375cfsofn4e8k4cw04g44gg04wkco4o04s4gco0ck0c0ggsgkc\"}"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'PHPSESSID=e5mpok46ph45h6iil1aclc80lt'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)

    # a = ['one']
    # tech = X('one')
    # print(tech)
    # print(type(tech))
    # pass
