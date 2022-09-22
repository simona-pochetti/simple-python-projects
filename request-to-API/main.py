from requests import get 

reponse = get("https://gitlab.com/api/v4/users/nanuchi/projects")
her_projects = reponse.json()

for project in her_projects:
    name = project["name"]
    url = project["web_url"]
    creation_date = project["created_at"]
    print(f"Project Name: {name}\nProject Url: {url}\nProject Creation: {creation_date}\n")
