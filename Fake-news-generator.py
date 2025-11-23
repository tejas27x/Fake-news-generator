import random
import pyttsx3

engine = pyttsx3.init()

names = ["Narendra Modi","Amit Shah","Rahul Gandhi","Virat Kohli",
"Rohit Sharma","MS Dhoni","Shah Rukh Khan","Akshay Kumar",
"Mukesh Ambani","Ratan Tata","ISRO Scientists"]

actions = ["launching a scheme","addressing a rally","meeting diplomats",
"reviewing security","participating in a Yatra","criticizing policies",
"meeting students","training","practicing","breaking a record",
"shooting a scene","testing rockets","donating","investing"]

locations = ["New Delhi","Mumbai","Bengaluru","Hyderabad","Chennai",
"Kolkata","Jaipur","Goa","Ahmedabad","Varanasi","Kerala","IIT Delhi",
"Sriharikota","Film City Mumbai"]


def speak(t):
    try:
        engine.say(t)
        engine.runAndWait()
    except:
        print("voice problem")


while True:

    n = random.choice(names)
    a = random.choice(actions)
    l = random.choice(locations)

    news = "BREAKING NEWS: " + n + " " + a + " in " + l + " !!"
    print()
    print(news)
    speak(news)

    again = input("More news? (Y/N): ")

    if again.lower() != "y":
        break


print("Thanks for using this news generator")
speak("Thanks for using this news generator")
