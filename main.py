# importing required modules
import random
import requests

# gets list & selects a random line
def get():
    list = requests.get("https://raw.githubusercontent.com/feliscatusdev/thingstodo-gen/main/list.txt", stream=True).text
    return random.choice(list.splitlines())

# prints the thing
print("things to do generator (press enter to exit)")
print("----------------------")
print(get())
input()
exit(0)
