import requests
import json

BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjkwNCwib2t0YUlkIjoicm9iZXJ0by5kYWdsaW9AZXNpbXBsaWNpdHkuY29tIiwiaGFycElkIjoicm9iZXJ0by5kYWdsaW9AZXNpbXBsaWNpdHkuY29tIiwiZmlyc3ROYW1lIjoiUm9iIiwibGFzdE5hbWUiOiJEYWdsaW8iLCJlbWFpbCI6InJvYmVydG8uZGFnbGlvQGVzaW1wbGljaXR5LmNvbSIsInJvbGVzIjpbeyJvcmdhbml6YXRpb25fY29udHJhY3RfaWQiOjEyLCJkYXRhX2FjY2Vzc19ncm91cCI6ImNkci1wZGEtcWRhcyIsInJvbGVfaWQiOjIsInJvbGVfbmFtZSI6ImR1YW93bmVyIiwicm9sZV9kZXNjcmlwdGlvbiI6bnVsbCwiZGF0ZV9jcmVhdGVkIjoiMjAyNC0xMi0wNlQxNjowNDo1My42MjBaIn0seyJvcmdhbml6YXRpb25fY29udHJhY3RfaWQiOjEyLCJkYXRhX2FjY2Vzc19ncm91cCI6ImNkci1wZGEtcWRhcyIsInJvbGVfaWQiOjQsInJvbGVfbmFtZSI6ImV4dGVybmFsYWRtaW4iLCJyb2xlX2Rlc2NyaXB0aW9uIjpudWxsLCJkYXRlX2NyZWF0ZWQiOiIyMDI0LTEyLTA2VDE2OjA1OjA2LjkyM1oifV0sImlhdCI6MTczMzc2MDY4NCwiZXhwIjoxNzMzODAzODg0fQ.RaSRcO16XH9WQXksHApZhnXbUeZ26IEY1UAWth80J7k'

URL = 'http://localhost:3003/api/organizations/'

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {BEARER_TOKEN}'
}

BODY = {
  "name": "test-2-python",
  "organizationName": "test-2-python",
  "iamRole": "Dua Owner"
}


if __name__ == '__main__':



    for i in range(10000):
        body = {
          "name": f"python-org-{i + 6000}",
          "organizationName": f"python-org-{i + 6000}",
          "iamRole": "Dua Owner"
        }


        response = requests.post(URL, headers=HEADERS, data=json.dumps(body))

        print(response.content.decode('utf-8'))
        print(response.status_code)
        print()