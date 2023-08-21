from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime
import requests, json

class Chamada(BaseModel):
    campaign: str
    companyName: str
    emailAddress: str
    leadID: int
    lead_cnpj: str
    firstName: str
    phoneNumber: int
    product: str

url = 'https://api.sharpspring.com/pubapi/v1/'
headers = {
    "id": "123",
    "Content-Type": "application/json",
}

query_params = {
    'accountID': '7CB1260E01C728EA9A185A3CED2C68D8',
    'secretKey': '03E5065CBFF46E2931B62E5A132FACE6'
}

app = FastAPI()

async def chamada_api(firstName, emailAddress, campaign):
    body = {
        "method": "createLeads",
        "params": {
            "objects": [
                {
                    "firstName": json.dumps(firstName),
                    "lastName": json.dumps(firstName),
                    "emailAddress": json.dumps(emailAddress)
                }
            ]
        },
        "id": "123"
    }

    response = requests.post(url, params=query_params, headers=headers, json=body)
    print(response.status_code)
    print(response.text)
    print(firstName + " " + emailAddress)

@app.post("/criaLead")
async def criaLead(lead: Chamada):
    firstName = lead.firstName
    emailAddress = lead.emailAddress
    campaign = lead.campaign

    await chamada_api(firstName, emailAddress, campaign)

    return {"message": "Lead created successfully!"}
