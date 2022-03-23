command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if started:
            started = False
            print("car stopped")
        else:
            print("car already stopped")
    elif command == "quit":
        break
    elif command == "help":
        print("""
start - start the car
stop - stop the car
quit - to exit the window
""")
    else:
        print("Sorry, I dont understand")


