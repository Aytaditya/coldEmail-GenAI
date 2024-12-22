import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()

print(data)

#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