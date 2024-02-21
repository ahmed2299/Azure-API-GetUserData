import requests
import json

#TODO: GLOBAL VARIABLES
client_id='' #TODO: ENTER YOUR CLIENT ID
client_secret='' #TODO: ENTER YOUR SECRET ID
tenant_id='' #TODO: ENTER YOUR TENANT ID
object_id='' #TODO: ENTER YOUR OBJECT ID

class User_Data:
    def __init__(self):
        pass

    def run(self):
        #Here to add your payload data "client id" and "client secret"
        payload = {
            'client_id':f'{client_id}',
            'scope':'https://graph.microsoft.com/.default',
            'client_secret':f'{client_secret}',
            'grant_type':'client_credentials'
        }
        #Here to add token headers
        headers_token={
            'Content-Type':'application/x-www-form-urlencoded'
        }
        #Here to post on oauth token to request on token
        access_token= requests.post(f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token',data=payload,headers=headers_token)
        access_token=access_token.json()['access_token']
        #HERE to request on the user data and get them in response
        headers={
            'Authorization':'Bearer '+access_token
        }
        #API to get user data
        user_data=requests.get(f'https://graph.microsoft.com/v1.0/users/{object_id}',headers=headers)
        formatted_user_data = json.dumps(user_data.json(), indent=1)
        #API to get login info
        login_info=requests.get(f'https://graph.microsoft.com/v1.0/auditLogs/signIns',headers=headers)
        formatted_login_data=json.dumps(login_info.json(),indent=1)

        print('##########################################')
        print(formatted_user_data)
        print('##########################################')
        print(formatted_login_data)

if __name__ == '__main__':
    user=User_Data()
    user.run()













