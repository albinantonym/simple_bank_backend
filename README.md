# Simple Bank Backend
There are three API endpoints implemented to retrive data from the bank

1) http://13.48.148.198:5000/api/getbanks 

When a get request is sent to this endpoint it returns all the banks in the Postgresql server along with their bank_id
Sample output:
```JSON
{
    "banks": [
        ["STATE BANK OF INDIA",1],
        ["PUNJAB NATIONAL BANK",2],
        ["CANARA BANK",3]],
    "message": "success"
}
```
             
2) http://13.48.148.198:5000/api/getbraches

When a get request is sent to this endpoint, along with the parameter "bankid"(bank_id) it returns all the branches in a bank along with its ifsc number.

For example in case of "http://13.48.148.198:5000/api/getbranches?bankid=140" the output will be
```JSON
{
    "branches": [
        ["RTGS-HO","BARC0INBB01"],
        ["BARCLAYS BANK","BARC0INBBIR"]
    ],
    "message": "success"
}
```

3) http://13.48.148.198:5000/api/branchdetails

When a get request is sent to this endpoint, along with the parameter "ifsc" it returns all the details of that branch.

For example in case of "http://13.48.148.198:5000/api/branchdetails?ifsc=AKJB0000021" the output will be
    
```JSON
{
    "address": "NETAJI CHOWK,MAIN ROAD,DIGRAS PIN 445 203",
    "bank": "AKOLA JANATA COMMERCIAL COOPERATIVE BANK",
    "bank_id": 100,
    "branch": "DIGRAS",
    "city": "DIGRAS",
    "district": "YAVATMAL",
    "ifsc": "AKJB0000021",
    "message": "success",
    "state": "MAHARASHTRA"
}
```

The code is hosted and running in a AWS EC2 and can be accessed with the public ip: http://13.48.148.198:5000/
