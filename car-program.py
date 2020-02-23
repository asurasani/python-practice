command = ""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car has already started stupid!")
        else:
            started = True
            print("Car started...ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped stupid!")
        else:
            started = False
            print("Car has stopped.")
    elif command == "help":
        print("""
start-start the car
stop-stop the car
quit-to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand")
