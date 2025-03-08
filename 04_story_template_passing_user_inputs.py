
with open("utils/story.txt", "r") as f:
    story = f.read()

print("Before replace: ")
print(story)

name = story.replace("<NAME>", "Harsha").replace("<PLACE>", "Salem").replace("<OBJECT>", "Sealed box")

print("After replace: ")
print(name)
