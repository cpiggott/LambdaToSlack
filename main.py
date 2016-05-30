import requests

def handler(event, context):
    requests.post('insert your url between these quotes',json={"text" : "Insert your message between these quotes, slack emotes such as :coffee: and slash commafds " })
