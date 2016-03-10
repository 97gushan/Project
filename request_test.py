import requests

s = requests.post("http://97gushan.pythonanywhere.com/hub/", data={"command":"highscore", "score":"460"})

print(s.text)


