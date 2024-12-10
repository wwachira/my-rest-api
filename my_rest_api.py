import requests
import json

response = requests.get('https://api.stackexchange.com//2.3/comments?order=desc&sort=creation&site=stackoverflow')

# Convert the response to JSON
data = response.json()

# Ensure the response contains 'items'
if 'items' in data:
    for item in data['items']:
        # Check if 'owner' exists in the item
        if 'owner' in item:
            owner = item['owner']
            # Print the 'link' and 'account_id' if they exist
            print(owner.get('link', 'No link available'))
            print(owner.get('account_id', 'No account ID available'))
            print()
else:
    print("No items found in the response.")