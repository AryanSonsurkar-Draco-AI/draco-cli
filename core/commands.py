def command_prompt():
    while True:
        cmd = input("Enter your command: \n")
        cmd = cmd.lower()

        if cmd=="who are you":
            print("I am Draco CLI. A project made for automating tasks.")
        
        elif cmd=="who created you":
            print("My master Aryan Sonsurkar created me to learn python deeply and automate his tasks.")

        elif cmd=="exit":
            print("Goodbye Bro!!!")
            break

        else:
            print("This is not in cmd list!!!")