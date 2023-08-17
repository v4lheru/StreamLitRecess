#!pip install requests
import requests

YOUR_GENERATED_SECRET = "your_secret_here"

url = "https://api.promptperfect.jina.ai/q2jb2ZpjQ23hUPjN4Xza"

headers = {
    "x-api-key": f"token {YOUR_GENERATED_SECRET}",
    "Content-Type": "application/json"
}


response = requests.post(url, headers=headers, json={"parameters": {"2":"YOUR_VALUE","3":"YOUR_VALUE","10":"YOUR_VALUE","Markdown":"YOUR_VALUE"}})
if response.status_code == 200:
  print(response.json())
else:
  print(response.text)
