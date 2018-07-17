# Example 1: synchronous requests
import requests

num_requests = 10

# めちゃ時間かかる
responses = [
    requests.get('http://example.org/')
    for i in range(num_requests)
]

print(responses)
