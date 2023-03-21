import speech_recognition as sr
import pyttsx3
import folium
import os
import pywhatkit
from datetime import *
import datetime
import requests
import random
import pandas as pd
import wikipedia
import random
import nltk
import flask
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
Key = 'ee791b0caed64003baa7192d54419c3f'
listener=sr.Recognizer()
engine=pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def weather():
    user_api = '0ea5c8d83df150aed1b1d4b4b823ada0'
    location = 'KISII'
    complete_api_key = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
    api_link = requests.get(complete_api_key)
    api_data = api_link.json()
    if api_data['cod'] == '404':
        talk("Invalid city: {}, Please check you city name".format(location))
    else:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        talk("Weather stats for -{} || {}".format(location.upper(),date_time))

        talk("The current temperature is:{:.2f} degrees Celcious".format(temp_city))
        talk("The current weather description is:"+ weather_desc)
        talk("The current humidity is:"+ str(hmdt)+ "percent")
        talk("Current wind speed :"+str(wind_spd) +"kilometers per hour")


def about_day():
    time = datetime.datetime.now().strftime('%H:%M')
    afternoon = '12:01'
    evening = '15:00'
    night='19:00'
    deepnight='22:00'
    if time < afternoon:
        talk("Good Morning Brian")
        date = datetime.datetime.now().strftime('%A:%B:%d:%Y')
        talk("Today is "+ date)
        talk("Current time is" + time +" in the morning")
        weather()
        talk('Should i read your schedule?')
        with sr.Microphone() as source:
            print("Listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if command == 'yes':
                     if 'Monday' in date:
                        talk("Your today schedule is as follows")
                        talk("You have COMP204 ie Database management system from 7:00 to 9:00am")
                        talk("Then Math 240 ie statistics and probability from 5:00 to 7:00 pm")
                        talk("I think you should study between the two lectures, just saying if i were you i could use it for studies or maybe coding.")
                     elif 'Tuesday' in date:
                        talk("Your today schedule is as follows")
                        talk("You have COMP220 ie Data communication and networks from 7:00 to 9:00am")
                        talk("Then Comp 200 ie C programming language from 11:00am to 1:00 pm")
                        talk("Then Phys 123 ie Electrostatics 1 from 5:00 to 7:00pm ")
                        talk("Finally you have KUCSA meeting from 6:00 pm to 9:00pm")
                        talk("Tuesday is one hell of a day sir. You need to take heavy food today")
                     elif 'Wednesday' in date:
                        talk("Your today schedule is as follows")
                        talk("You have COMP201 ie Basic circuit unit from 3:00 to 5:00pm")
                        talk("I think you should exercise today sir.")
                     elif 'Thursday' in date:
                        talk("Your today schedule is as follows")
                        talk("No class, you will study during the day and code at night")
                        talk("Finally you have KUCSA meeting from 6:00 pm to 9:00pm")
                        talk("Finally ill open Movies overnight")
                     elif 'Friday' in date:
                        talk("Your today schedule is as follows")
                        talk("No class")
                        talk("Go to school network connection and do some updates")
                     elif 'Saturday' in date:
                        talk("Your today schedule is as follows")
                        talk("Do the laundry in the morning")
                        talk("Play video game")
                        talk("Code and later on watch a movie later in the evening")
                     elif 'Sunday' in date:
                        talk("Your today schedule is as follows")
                        talk("You should go to church early in the morning")
                        talk("Study for some times then after church")
                        talk("Play video game")
                        talk("Code and later on watch a movie later on at night")

                     else:
                       pass
            else:
                pass
    elif time >= afternoon and time < evening:
            talk("Good Afternoon Brian")
            date = datetime.datetime.now().strftime('%A:%B:%d:%Y')
            time = datetime.datetime.now().strftime('%H:%M')
            talk("Current time is "+ time + "afternoon")
            weather()
            talk('Should i read your schedule?')
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
            if command == 'yes':

                if 'Monday' in date:
                    talk("You should take your lunch and wait for math 240 from 5:00 to 7:00pm")
                    talk("I hope you studied Brian!")
                elif 'Tuesday' in date:
                    talk("I hope you took heavy lunch you still to activities to call it a day")
                    talk("Phys 123 ie Electrostatics 1 from 5:00 to 7:00pm ")
                    talk("Finally you have KUCSA meeting from 6:00 pm to 9:00pm")
                elif 'Wednesday' in date:
                    talk("You should be coding website and")
                    talk("You still have COMP201 ie Basic circuit unit from 3:00 to 5:00pm")
                    talk("You should go to the field for laps")
                elif 'Thursday' in date:
                    talk("you should be studying right now")
                    talk("Finally you have KUCSA meeting from 6:00 pm to 9:00pm")
                    talk("Finally ill open Movies overnight")
                elif 'Friday' in date:
                    talk("No class")
                    talk("you should be doing laptop update in school network")
                elif 'Saturday' in date:
                    talk("Good work finishing the laundry")
                    talk("you can play video game now")
                elif 'Sunday' in date:
                    talk("i think you should be studying right now")
                    talk(" then after studying ,Play video game")


                else:
                    pass
            else:
                pass
    elif time >= evening and time <= night:
            talk("Good Evening Brian")
            date = datetime.datetime.now().strftime('%A:%B:%d:%Y')
            time = datetime.datetime.now().strftime('%H:%M')
            talk("Current time is " + time +"in the evening")
            weather()
            talk('Should i read your schedule?')
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
            if command == 'yes':
                if 'Monday' in date:
                    talk("check if there is asignment and work on it")
                    talk("You should be a sleep by now big day tommorrow")
                elif 'Tuesday' in date:
                    talk("From Physics class you should directly go to KUCSA meeting")
                elif 'Wednesday' in date:
                    talk("After field exercise you should code  a little")
                elif 'Thursday' in date:
                    talk("Go to KUCSA meeting then after you watch movie the all night")
                elif 'Friday' in date:
                    talk("After update you can code some C++ and the watching")
                elif 'Saturday' in date:
                    talk("you can play video game now")
                elif 'Sunday' in date:
                    talk("i think you should be studying right now")
                    talk(" then after studying ,Play video game")


                else:
                    pass
            else:
                pass
    elif time >= night and time <= deepnight:
        weather()
        talk('Goodnight')
    else:
            talk("you are suppose to have a 8 hour sleep, you should be sleeping by now")
            talk("Goodnight Brian!!")



about_day()
talk("What else can i do for you Brian")
def take_command():

    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'tony' in command:
                command=command.replace('tony','')
                print(command)

    except:
        pass

        return "None"
    return command
while True:
    def run_tony():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('Do you want me to play movie of music')
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
            if 'movie' in command:
                talk('Which kind of Movie Do you want me to play brian?')
                while True:
                    cout=0
                    with sr.Microphone() as source:
                        print("Listening...")
                        voice = listener.listen(source)
                        command = listener.recognize_google(voice)
                        command = command.lower()
                    if 'video' in command:
                        os.startfile(r'F:\\personal')
                        talk('hope its here Brian')
                        break
                    elif 'siris' in command:
                        os.startfile(r'E:\\MOVIES')
                        talk('you can choose your favourite series to watch here')
                        break
                    elif 'single' in command:
                        os.startfile(r'E:\\MOVIES\\single Movies')
                        talk('Here is some of the single movies you might like')
                        break
                    else:
                        talk('you dont have that')
                    talk('Try again. Let me help you we have siris, single movies and videos')
                    if cout == 2:
                        talk('Am sorry am gonna exit the programme')
                    break

            elif 'music' in command:
                talk('Do you want me to play from your playlist or from youtube')
                with sr.Microphone() as source:
                    print("Listening...")
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                if 'playlist' in command:
                    os.startfile(r'C:\\Users\\ADMIN\\Music\\hiphop')
                elif 'youtube' in command:
                    talk('Playing ' + song)
                    pywhatkit.playonyt(song)
                else:
                    talk("Not found")






        elif 'search' in command:
            search = command.replace('search', '')
            talk('searching ' + search)
            pywhatkit.search(search)
        elif 'time' in command:
            tim = datetime.datetime.now().strftime('%H:%M')
            talk('Current time is' + tim)
        elif 'tell' in command:
            person = command.replace('tell', '')
            info = wikipedia.summary(person, 20)
            print(info)
            talk("This is about "+ info)
        elif 'what' in command:
            about = command.replace('what', '')
            info = wikipedia.summary(about, 20)
            print(info)
            talk(info)
        elif 'number' in command:
            Num = command.replace('number','')
            ch_number= phonenumbers.parse(Num,"CH")
            yourloaction= geocoder.description_for_number(ch_number,"en")
            service_num=phonenumbers.parse(Num, "RO")
            geoco=OpenCageGeocode(Key)
            query = str(yourloaction)
            results = geoco.geocode(query)
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            myMap= folium.Map(location=[lat, lng],zoom_start=9)
            folium.Marker([lat, lng],popup=yourloaction).add_to((myMap))
            myMap.save("phonelocation.html")
            talk("This number is from" + yourloaction)
            talk(carrier.name_for_number(service_num, "en"))
            talk("latitude and longitude are" + results)
        elif "food" in command:
            food_list = ["Chapo beans","chafua",""]

        else:



            # Define a dictionary of possible responses
            responses = {

                "hello": ["Hi there!", "Hello!", "Hey!", "Greetings!"],
                "hi": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
                "hey": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
                "how are you": ["I'm doing well, thanks for asking!", "I'm doing okay, how about you?",
                                "I'm good, thanks!", "I'm great, how are you?", "I'm feeling fantastic today, thanks!"],
                "what's up": ["Not much, how about you?", "Just hanging out, how about you?",
                              "Nothing new, just chatting with you.",
                              "Just trying to have a conversation, what about you?"],
                "what are you up to": ["Not much, just chatting with you.", "I'm just hanging out here.",
                                       "I'm just passing the time.",
                                       "I'm here to chat and answer questions, what about you?"],
                "how was your day": ["It was good, thanks for asking!", "It was okay, how was yours?",
                                     "It was pretty uneventful, but that's okay.", "It was great, how was your day?"],
                "what do you do": ["I'm a chatbot designed to have conversations with people.",
                                   "I answer questions and have conversations with people like you.",
                                   "I'm here to chat and help with anything you need.",
                                   "I'm programmed to chat and answer your questions, what about you?"],
                "what's new": ["Not much, what's new with you?", "Nothing new here, how about you?",
                               "Just hanging out, what about you?",
                               "I'm a machine, so nothing is new for me. What about you?"],
                "what's for dinner": ["I don't eat, since I'm just a computer program.",
                                      "I'm not sure, what are you having?",
                                      "I don't have the ability to eat, since I'm not a living creature.",
                                      "I'm sorry, but I can't eat. What about you?"],
                "how can I help you": ["You can ask me anything you want!",
                                       "Just chat with me and let me know what you need help with.",
                                       "I'm here to assist you with anything you need.",
                                       "Just tell me what you need help with and I'll do my best to assist you."],
                "thank you": ["You're welcome!", "No problem, happy to help!", "My pleasure.",
                              "Glad I could assist you!"],
                "thanks": ["You're welcome!", "No problem, happy to help!", "My pleasure.", "Glad I could assist you!"],
                "thanks a lot": ["You're welcome!", "No problem, happy to help!", "My pleasure.",
                                 "Glad I could assist you!"],
                "bye": ["Goodbye!", "See you later!", "Bye!", "Take care!"],
                "goodbye": ["Goodbye!", "See you later!", "Bye!", "Take care!"],
                "see you later": ["Goodbye!", "See you later!", "Bye!", "Take care!"],
                "nice to meet you": ["Likewise!", "Nice to meet you too!", "Pleasure meeting you!", "Same here!"],
                "what's your name": ["My name is AI Bot.", "I go by AI Bot.", "You can call me AI Bot.",
                                     "I'm known as AI Bot."],
                "who are you": ["I'm an AI chatbot designed to have conversations with people."],
                "what can you do": ["I can chat with you and answer your questions!",
                                    "I'm here to assist you with anything you need help with.",
                                    "I can help you find information, answer questions, or just chat with you.",
                                    "I can do a lot of things, just let me know what you need help with."],
                "can you help me": ["Of course, what do you need help with?",
                                    "Absolutely, let me know what you need help with.", "Sure thing, I'm here to help!",
                                    "I'm always here to help, just tell me what you need assistance with."],
                "can you give me some advice": ["Sure, what kind of advice are you looking for?",
                                                "Of course, I'll do my best to give you some advice.",
                                                "Absolutely, let me know what you need advice on.",
                                                "I'm happy to offer advice, just tell me what you need advice on."],
                "can you tell me a joke": ["Sure, why did the tomato turn red? Because it saw the salad dressing!",
                                           "Why couldn't the bicycle stand up by itself? Because it was two-tired!",
                                           "What did the grape say when it got stepped on all day? Nothing, it just let out a little wine.",
                                           "Why did the chicken cross the playground? To get to the other slide!"],
                "how old are you": ["I don't really have an age, since I'm just a computer program.",
                                    "I don't have a physical form, so I don't really have an age.",
                                    "I'm ageless, since I'm just a machine.",
                                    "I don't age like humans do, since I'm just an AI program."],
                "what's your favorite color": ["I don't really have a favorite color, since I'm just a machine.",
                                               "I don't have the ability to have preferences, since I'm just a computer program.",
                                               "I don't really have a favorite color, since I'm not a living being.",
                                               "I don't have the ability to see colors like humans do, since I'm just an AI program."],
                "what's the weather like": ["I'm sorry, but I don't have the ability to check the weather.",
                                            "I'm not sure, you might want to check a weather app or website.",
                                            "I don't have access to current weather information, since I'm just an AI program.",
                                            "I'm not equipped to provide weather updates, but there are many apps and websites that can."],
                "what's the time": ["I'm sorry, but I don't have the ability to tell time.",
                                    "I don't have access to the current time, since I'm just a computer program.",
                                    "I'm not equipped to provide time information, but there are many devices and apps that can tell you the time.",
                                    "I'm not able to tell time like a clock, since I'm just an AI program."],
                "can you play a game with me": ["I'm sorry, but I'm not able to play games like a human would.",
                                                "I'm not programmed to play games, but I can chat with you and answer your questions.",
                                                "I don't have the ability to play games, but I can help you find online games to play.",
                                                "I'm not able to play games, since I'm just an AI program."],
                "what's your favorite food": ["I don't really have a favorite food, since I'm just a machine.", "I eat your words"],
                "what's your favorite movie": ["I don't really have a favorite movie, since I'm just a machine.",
                                               "I don't have the ability to watch movies or have preferences since I'm just a computer program.",
                                               "I don't really watch movies, since I'm not a living being.",
                                               "I'm not equipped to have favorite movies, since I'm just an AI program."],
                "what's your favorite song": ["I don't really have a favorite song, since I'm just an AI program.",
                                              "I don't have the ability to listen to music or have preferences, since I'm just a computer program.",
                                              "I don't really listen to music, since I'm not a living being.",
                                              "I don't have the ability to have a favorite song, since I'm just an AI program."],
                "can you recommend a restaurant": ["Sure, what kind of cuisine are you in the mood for?",
                                                   "Absolutely, where are you located and what type of food do you like?",
                                                   "I'd be happy to recommend a restaurant, can you give me some more information about what you're looking for?",
                                                   "Of course, what's your location and what type of cuisine are you interested in?"],
                "what's your favorite book": ["I don't really have a favorite book, since I'm just a machine.",
                                              "I don't have the ability to read books or have preferences, since I'm just a computer program.",
                                              "I don't really read books, since I'm not a living being.",
                                              "I don't have the ability to have a favorite book, since I'm just an AI program."],
                "what's your favorite hobby": ["I don't really have hobbies, since I'm just an AI program.",
                                               "I don't have the ability to have preferences or interests like humans do, since I'm just a computer program.",
                                               "I don't really do anything for fun, since I'm not a living being.",
                                               "I don't have the ability to have hobbies or interests, since I'm just an AI program."],
                "what's the meaning of life": [
                    "That's a philosophical question that has been debated for centuries, with many different answers depending on who you ask.",
                    "The meaning of life is subjective and can vary depending on personal beliefs and experiences.",
                    "The answer to that question is different for everyone, and is ultimately up to each individual to determine for themselves.",
                    "There is no single answer to that question, since it is such a deeply personal and subjective topic."],
                "how do you work": [
                    "I use machine learning algorithms to understand and respond to the input I receive from users.",
                    "I analyze user input using natural language processing techniques, and use that analysis to generate appropriate responses.",
                    "My programming allows me to learn and adapt over time, so I can provide better responses the more I interact with users.",
                    "I use a combination of algorithms and data analysis to understand and respond to user input in a way that is most useful and relevant."],
                "what's your name": ["I'm a virtual assistant designed to help you with whatever you need.",
                                     "I'm an AI-powered chatbot programmed to assist you with anything you need.",
                                     "You can call me Chatbot, since that's my function and purpose.",
                                     "I don't really have a name, since I'm just a machine designed to interact with users."],
                "where are you from": ["I was created by Brian Okungu who work on AI technologies."],

                "How do I know if someone loves me?": [
                    "It's not always easy to tell if someone loves you, but some signs to look for include consistent acts of kindness and care, spending time together, and expressing feelings of affection or admiration. However, the best way to know for sure is to have an honest and open conversation with the person and ask how they feel about you."],
                "What are some romantic things I can do for my partner?": [
                    "Some romantic things you can do for your partner include cooking them a special meal, writing them a love letter or poem, planning a surprise date, or simply spending quality time together."],
                "What's the best way to show someone you love them?": [
                    "The best way to show someone you love them is through consistent acts of kindness, care, and affection. This can include spending quality time together, actively listening to their needs and desires, and doing thoughtful things to show that you care."],
                "How do I know if I'm in love?": [
                    "Being in love can feel different for everyone, but some common signs include feeling a strong connection and attraction to someone, wanting to spend time with them frequently, and feeling a sense of happiness or contentment when you're together."],
                "What are some common relationship problems and how can I avoid them?": [
                    "Common relationship problems can include communication issues, lack of trust, and differing priorities or values. To avoid these problems, it's important to have open and honest communication with your partner, establish clear boundaries and expectations, and work together to address any issues that arise."],
                "How can I make my relationship stronger?": [
                    "To make your relationship stronger, it's important to prioritize communication, spend quality time together, and actively show love and affection towards your partner. It can also be helpful to set goals and work towards them together, whether they're personal or professional."],
                "What's the best way to handle a break up?": [
                    "Breaking up can be difficult, but some tips for handling it include taking time to process your emotions, seeking support from friends and family, and focusing on self-care activities that bring you happiness and fulfillment."],
                "How can I improve my communication with my partner?": [
                    "To improve communication with your partner, it's important to actively listen to their needs and concerns, be clear and direct in your communication, and avoid blaming or attacking language. It can also be helpful to establish regular check-ins or 'state of the relationship' conversations to ensure that both partners are on the same page."],
                "What are some signs that a relationship may not be working out?": [
                    "Some signs that a relationship may not be working out include consistent fighting or disagreements, lack of trust or respect, and feeling unhappy or unfulfilled in the relationship."],
                "How can I make a long distance relationship work?": [
                    "To make a long distance relationship work, it's important to prioritize communication, establish clear expectations and boundaries, and find creative ways to stay connected despite the distance. This can include sending care packages, scheduling virtual dates, or finding shared hobbies or interests to bond over."]


            }

            # Define a function to handle user input and generate a response
            def respond(user_input):
                # Convert the input to lowercase and remove any punctuation
                cleaned_input = user_input.lower().strip("?.,!")
                # Check if the input is in the responses dictionary
                if cleaned_input in responses:
                    # If it is, randomly select a response from the corresponding list of responses
                    return random.choice(responses[cleaned_input])
                else:
                    # If not, respond with a default message
                    return "I'm sorry, I don't understand what you're asking."

            # Define a main function to run the chatbot
            def main():
                print("Hello, I'm AI Bot. How can I help you today?")
                while True:
                    # Get user input
                    with sr.Microphone() as source:
                        print("Listening...")
                        voice = listener.listen(source)
                        command = listener.recognize_google(voice)
                        command = command.lower()
                    # Generate a response using the respond function
                    bot_response = respond(command)
                    # Print the bot's response
                    print("AI Bot:", bot_response)

            # Run the main function to start the chatbot
            if __name__ == "__main__":
                main()

            talk('I am sorry i did not get what you said could you please repeat')



    run_tony()
exit()





