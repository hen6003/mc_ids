import json, os.path, sys

ids_array = []

if not os.path.isfile("ids.json"):
    print("run 'mc_ids_gen.py' and try again")
    exit(1)

with open("ids.json", "r") as read_file:
        ids_array = json.load(read_file)

user_input = ""

if len(sys.argv) == 1:
    user_input = input("Minecraft id: ")
else:
    for i in sys.argv:
        user_input += " " + i

user_input = user_input[len(sys.argv[0]) + 2:]
user_input = user_input.lower()
user_input = user_input.strip()
user_input = user_input.replace(" ", "_")

found = False

for i in ids_array:
    if i == user_input:
        print("Found id: " + i)
        found = True

if found == False:
    print("Block doesn't exist")