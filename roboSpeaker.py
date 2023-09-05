import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0.0 Created by AdiSuyash")
    text_to_speech = pyttsx3.init()
    while True:
        words = input("Enter your command to speak: ")
        if ((words == "exit") or (words == "Exit") or (words == "EXIT")):
            print("Terminated Robo Speaker 1.0.0")
            break
        text_to_speech.say(words)
        text_to_speech.runAndWait()