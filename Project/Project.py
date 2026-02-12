import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print("===== Information About Doxpro Robotics =====")
while True:
    print("\nType 'hi' to start conversation")
    print("1: About Doxpro")
    print("2: Project Enquiry")
    print("3: Internship Information")
    print("4: Exit")

    ip = input("Enter your choice: ")

    if ip.lower() == 'hi':
        print("Hello Sahil, how can I help you?")
        engine.say("Hello Sahil, how can I help you?")
        engine.runAndWait()

    elif ip == '1':
        print("Empowering students and institutions with cutting-edge technology and innovative solutions since 2017")
        engine.say("Empowering students and institutions with cutting-edge technology and innovative solutions since 2017")
        engine.runAndWait()

    elif ip == '2':
        print("Doxpro Robotics has successfully completed 2340 projects.")
        engine.say("Doxpro Robotics has successfully completed 2340 projects.")
        engine.runAndWait()

    elif ip == '3':
        print("Join 1738 plus successful students in our comprehensive industrial internship program.")
        engine.say("Join 1738 plus successful students in our comprehensive industrial internship program.")
        engine.runAndWait()

    elif ip == '4':
        print("Goodbye Sahil! Have a great day.")
        engine.say("Goodbye Sahil! Have a great day.")
        engine.runAndWait()
        break

    else:
        print("Invalid option. Please try again.")
        engine.say("Invalid option. Please try again.")
        engine.runAndWait()

engine.stop()
