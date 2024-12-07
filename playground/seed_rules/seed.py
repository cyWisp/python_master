import requests
import json

BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjkwNCwib2t0YUlkIjoicm9iZXJ0by5kYWdsaW9AZXNpbXBsaWNpdHkuY29tIiwiaGFycElkIjoicm9iZXJ0by5kYWdsaW9AZXNpbXBsaWNpdHkuY29tIiwiZmlyc3ROYW1lIjoiUm9iIiwibGFzdE5hbWUiOiJEYWdsaW8iLCJlbWFpbCI6InJvYmVydG8uZGFnbGlvQGVzaW1wbGljaXR5LmNvbSIsInJvbGVzIjpbeyJvcmdhbml6YXRpb25fY29udHJhY3RfaWQiOjEyLCJkYXRhX2FjY2Vzc19ncm91cCI6ImNkci1wZGEtcWRhcyIsInJvbGVfaWQiOjQsInJvbGVfbmFtZSI6ImV4dGVybmFsYWRtaW4iLCJyb2xlX2Rlc2NyaXB0aW9uIjpudWxsLCJkYXRlX2NyZWF0ZWQiOiIyMDI0LTEyLTA2VDE2OjA1OjA2LjkyM1oifSx7Im9yZ2FuaXphdGlvbl9jb250cmFjdF9pZCI6MTIsImRhdGFfYWNjZXNzX2dyb3VwIjoiY2RyLXBkYS1xZGFzIiwicm9sZV9pZCI6Miwicm9sZV9uYW1lIjoiZHVhb3duZXIiLCJyb2xlX2Rlc2NyaXB0aW9uIjpudWxsLCJkYXRlX2NyZWF0ZWQiOiIyMDI0LTEyLTA2VDE2OjA0OjUzLjYyMFoifV0sImlhdCI6MTczMzUwMTExOSwiZXhwIjoxNzMzNTQ0MzE5fQ.9YnOVAWFhMwjemO8Z0j3-YBX9l73HI7Vu5WscnEwiws'

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



    for i in range(5000):
        body = {
          "name": f"python-org-{i}",
          "organizationName": f"python-org-{i}",
          "iamRole": "Dua Owner"
        }


        response = requests.post(URL, headers=HEADERS, data=json.dumps(body))

        print(response.content.decode('utf-8'))
        print(response.status_code)
        print()