def greet(name):
    print(f"Hi {name}")
greet("Benjamin")

def get_greetings(name):
    return f"Hi {name}"
message = get_greetings("Benjamin")
#print(message)
file = open("context.txt","w")
file.write(message)