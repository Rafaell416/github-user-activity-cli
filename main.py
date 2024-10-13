import argparse
import sys
import json
import urllib.error
import urllib.request


def main():
  parser = argparse.ArgumentParser(description="GitHub user activity CLI")
  subparser = parser.add_subparsers(dest="command")

  parser_check = subparser.add_parser("check", help="check user activities")
  parser_check.add_argument("username", type=str, help="Github username")

  args = parser.parse_args()

  username = args.username
  url = f"https://api.github.com/users/{username}/events"

  try:
    with urllib.request.urlopen(url) as response:
      rate_limit_remaining = response.headers.get('X-RateLimit-Remaining')
      if rate_limit_remaining == '0':
        print(f"API rate limit exceeded. Please try again later")
        sys.exit(1)
      data = json.loads(response.read().decode())  
  except urllib.error.HTTPError as error:
    if error.code == 404:
      print(f"User {username} not found")
    else:
      print(f"HTTP Error {error.code}")
    sys.exit(1)
  except urllib.error.URLError as error:
    print(f"Failed to reach the server: {error.reason}")
    sys.exit(1)
  except urllib.error.JSONDecodeError:
    print(f"Failed to parse JSON response")
    sys.exit(1)
  
  event_messages = []


  for event in data:
    event_type = event["type"] # event.get("type")
    repo_name = event["repo"]["name"]
    print(f"event_type: {event_type} - repo_name: {repo_name}")
  



if __name__ == '__main__':
  main()


"""
- crear la  linea de comandos ✅
- obtener el nombre de usuario a consultar ✅
- conectarme a github y traerme los eventos ✅
- mostrar los eventos en la consola
"""


"""
git     commit      "mensaje de mi commit"
[tool]  [command]  [argument]

(command='check', username='rafa')

"""


"""
[
  {
      "id":"42778450755",
      "type":"PushEvent",
      "actor":{
         "id":114835266,
         "login":"MateoSnatch",
         "display_login":"MateoSnatch",
         "gravatar_id":"",
         "url":"https://api.github.com/users/MateoSnatch",
         "avatar_url":"https://avatars.githubusercontent.com/u/114835266?"
      },
      "repo":{
         "id":867716613,
         "name":"MateoSnatch/Expense-Tracker",
         "url":"https://api.github.com/repos/MateoSnatch/Expense-Tracker"
      },
      "payload":{
         "repository_id":867716613,
         "push_id":20674743099,
         "size":1,
         "distinct_size":1,
         "ref":"refs/heads/main",
         "head":"4e281f6233030a622b81ab08c6842808e56944e6",
         "before":"28dc6d384ab1edb64ba1218d4a0e447aecb28acd",
         "commits":[]
      },
      "public":true,
      "created_at":"2024-10-11T21:53:51Z"
   },
]:)
"""