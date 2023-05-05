import httpx


user = "github"
response = httpx.get(f"https://api.github.com/users/{user}/repos")
repos = response.json()

print(repos)
