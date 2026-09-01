print("Start , Stop, Help")
started = false
command = ""
while True:
  command = input(">> ").lower()
  if command == "start":
    if strated:
      print("Car already started")
    else: print("Car started...")
  elif command == "stop":
     if not started:
       print("Car already stopped")
     else: print("Car stopped...")
  elif command == "help":
    print("""
  start - to start the car
  stop - to stop the car
  quit - to exit the program
    """)
  elif command == "quit":
    break
  else: print("Sorry, I dont understand that")
