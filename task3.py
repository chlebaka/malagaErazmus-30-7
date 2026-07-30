import json
import requests

url = "https://api.github.com/repos/python/cpython"

r = requests.get(url, timeout=10)
r.raise_for_status()
data = r.json()

print(data["full_name"])
print(data["stargazers_count"], "stars")
print(data["forks_count"], "forks")
print(data["open_issues_count"], "open issues")

with open("snapshot.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("snapshot.json saved")