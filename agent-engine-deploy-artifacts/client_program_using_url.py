import json
import requests
from google.auth import default
from google.auth.transport.requests import Request

# Get default credentials and access token
creds, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
creds.refresh(Request())
access_token = creds.token

# API endpoint for session creation
url_session = "https://us-central1-aiplatform.googleapis.com/v1/projects/learn-adk-476816/locations/us-central1/reasoningEngines/3847468262518423552:query"

# Payload for session creation
payload_session = {
    "class_method": "create_session",
    "input": {
        "user_id": "testId"
    }
}

# Headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# POST request
response = requests.post(url_session, headers=headers, data=json.dumps(payload_session))

if response.status_code == 200:
    data = response.json()
    session_id = data["output"]["id"]
    print(f"Session created successfully! Session ID: {session_id}")
else:
    print(f"Request failed ({response.status_code}):")
    print(response.text)

payload_query = {
    "class_method": "async_stream_query",
    "input": {
        "user_id": "testId",
        "session_id": session_id,
        "message": "Tell me about world war 2"
    }
}

url_query = "https://us-central1-aiplatform.googleapis.com/v1/projects/learn-adk-476816/locations/us-central1/reasoningEngines/3847468262518423552:streamQuery?alt=sse"
"""
with requests.post(url_query, headers=headers, data=json.dumps(payload_query), stream=True) as response:
    print("Status:", response.status_code)
    if response.status_code != 200:
        print("Error:", response.text)
    else:
        print("Streaming response:\n")
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                print(decoded_line)

"""
response = requests.post(url_query, headers=headers, data=json.dumps(payload_query))
import json
data = json.loads(response.text)

# Extract the text safely
text = data.get("content", {}).get("parts", [{}])[0].get("text", "")

print("\nAgent Response:\n")
print(text)