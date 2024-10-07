import re
import requests
import sys
from datetime import datetime
from translate import Translator
import pyjokes
import wikipediaapi
import os


def main():
    print("Hello!\nWhat can I do for you?")
    i=0
    while True:
        if i>0:
            while True:
                ans = input("Is there anything else that you would like me to do? (Yes/No)\n").lower()
                if re.search(r"\b(?:no)\b", ans, re.IGNORECASE):
                    sys.exit("See you soon!")
                elif re.search(r"\b(?:yes)\b", ans, re.IGNORECASE):
                    print("Whats else would you like?")
                    break
                else:
                    print("Sorry, I didn't understant")
        user_req = input()

        if re.search(r"\b(?:weather|cold|hot)\b", user_req, re.IGNORECASE):
            weather()
            i+=1
        elif re.search(r"\b(?:time)\b", user_req, re.IGNORECASE):
            time()
            i+=1
        elif re.search(r"\b(?:translate)\b", user_req, re.IGNORECASE):
            translate()
            i+=1
        elif re.search(r"\b(?:joke|mood|laugh|funny)\b", user_req, re.IGNORECASE):
            jokes()
            i+=1
        elif re.search(r"\b(?:wikipedia|wiki|information|info|learn|know about)\b", user_req, re.IGNORECASE):
            search_wikipedia()
            i += 1
        elif re.search(r"\b(add|write)\b.*\b(?:notebook|note|notes)\b", user_req, re.IGNORECASE):
            notebook()
            i += 1
        elif re.search(r"\b(read|see)\b.*\b(?:notebook|note|notes)\b", user_req, re.IGNORECASE):
            read_notes()
            i += 1
        else:
            print("Sorry, I didn't understand the assignment...\nPlease repeat.")



def weather():
    city_name = input("Enter the name of the city you want to know the weather: ")
    print("\n\n")
    url = "https://wttr.in/{}".format(city_name)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
        sys.exit()
    print(T)

def time():
    current_time = datetime.now()

    print(f"The current time is: {current_time.strftime('%H:%M:%S')}")

def translate():
    text_to_translate = input("Enter the text you want to translate: ")

    source_language = input("Enter the source language\nen-English,el-Greek,fr-French,de-German etc: ")
    target_language = input("Enter the target language\nen-English,el-Greek,fr-French,de-German etc: ")

    translator = Translator(to_lang=target_language, from_lang=source_language)

    try:
        translation = translator.translate(text_to_translate)
        print(translation)

    except Exception as e:
        print(f"Oops! An error occurred")

def jokes():
    print(f"I will tell you a joke!\n{pyjokes.get_joke()}\nI hope you liked it!")

def search_wikipedia():
    query = input("What do you want to learn about?\n(ex. WW2)\n")
    headers = {"User-Agent": "YourAppName/1.0 (your@email.com)"}
    wiki_wiki = wikipediaapi.Wikipedia("en", headers=headers)

    page_py = wiki_wiki.page(query)

    if page_py.exists():
        summary = page_py.text
        first_paragraph = summary.split("\n\n")[0]
        print("Summary:\n")
        print(first_paragraph)
        print("\n\n")
    else:
        print(f"Sorry, no information found for '{query}' on Wikipedia.")

def notebook():
    try:
        current_date = datetime.now().strftime("%d_%m_%Y")
        file_name = f"note_{current_date}.txt"

        note_content = input("Write your note:\n")


        if os.path.exists(file_name):
            with open(file_name, "a") as file:
                file.write("\n" + note_content)
            print(f"Note saved successfully.")
        else:
            with open(file_name, "w") as file:
                file.write(note_content)
            print(f"Note saved successfully.")

    except Exception as e:
        print(f"An error occurred while interacting with the notebook: {e}")

def read_notes():
    try:
        current_date = datetime.now().strftime("%d_%m_%Y")
        file_name = f"note_{current_date}.txt"

        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                notes = file.read()
                if notes:
                    print("Notes:")
                    print(notes)
                else:
                    print("You don't have any notes for today.")
        else:
            print("You dont have any notes for today.")

    except Exception as e:
        print(f"An error occurred while reading the notes: {e}")



if __name__=="__main__":
    main()
