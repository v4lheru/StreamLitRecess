#!pip install requests
import requests

YOUR_GENERATED_SECRET = "your_secret_here"

url = "https://api.promptperfect.jina.ai/q2jb2ZpjQ23hUPjN4Xza"

headers = {
    "x-api-key": f"token {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}",
    "Content-Type": "application/json"
}


response = requests.post(url, headers=headers, json={"parameters": {"2":"YOUR_VALUE","3":"YOUR_VALUE","10":"YOUR_VALUE","Markdown":"YOUR_VALUE"}})
if response.status_code == 200:
  print(response.json())
else:
  print(response.text)
