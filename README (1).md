# My Assistant

## Video URL: https://youtu.be/53-4OWWmNz4

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Testing](#testing)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Introduction

Welcome to the Assistant project! This project is a simple Python-based assistant that can perform various every-day tasks, including providing weather information, translating text, searching Wikipedia, managing a notebook, telling jokes and more..

## Features

- **Weather information**: Get the current weather for a specific city of your choice.
- **Time**: Display the current time.
- **Translation**: Translate text from one language to another.
- **Jokes**: Enjoy a good laugh with random jokes.
- **Wikipedia search**: Retrieve information from Wikipedia based on user queries.
- **Notebook**: Write and read notes for each day.

## Prerequisites

The libraries used are in requirements.txt file.

- translate 3.6.1
- pyjokes 0.6.0
- requests 2.31.0
- Wikipedia-API 0.6.0

You can install them using the following pip command:

` pip install -r requirements.txt `

## Usage

Run the script
` python project.py `

```
Hello!
What can I do for you?
```

After that, you can request for several functions listed [above](#Features) or you can terminate the program at any time using CTRL + C.

## Time

You can ask the current time.

```
What time is it?
The current time is: 17:55:32
Is there anything else that you would like me to do? (Yes/No)
```
"Tell me the time", "Can you please tell me the time", or just "time" etc will work as well.

By typing "no" (case insensitive) you can terminate the program

```python
Is there anything else that you would like me to do? (Yes/No)
no
See you soon!
```

Else, by typing "yes" (case insensitive) you can continue with another request

## Weather

You can ask for the weather of the city that you input.

```
Whats else would you like?
Can you give me information about the weather?
Enter the name of the city you want to know the weather: Thessaloniki



Weather report: Thessaloniki

     \  /       Partly cloudy
   _ /"".-.     19 °C
     \_(   ).   ↖ 22 km/h
     /(___(__)  10 km
                0.3 mm
                                                       ┌─────────────┐
┌──────────────────────────────┬───────────────────────┤  Mon 04 Mar ├───────────────────────┬──────────────────────────────┐
│            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│               Overcast       │  _`/"".-.     Light rain sho…│  _`/"".-.     Patchy rain ne…│  _`/"".-.     Patchy rain ne…│
│      .--.     11 °C          │   ,\_(   ).   14 °C          │   ,\_(   ).   +13(12) °C     │   ,\_(   ).   +11(10) °C     │
│   .-(    ).   ↙ 7-9 km/h     │    /(___(__)  ↖ 7-9 km/h     │    /(___(__)  ← 14-22 km/h   │    /(___(__)  ↙ 13-20 km/h   │
│  (___.__)__)  10 km          │      ‘ ‘ ‘ ‘  10 km          │      ‘ ‘ ‘ ‘  10 km          │      ‘ ‘ ‘ ‘  10 km          │
│               0.0 mm | 0%    │     ‘ ‘ ‘ ‘   0.3 mm | 100%  │     ‘ ‘ ‘ ‘   0.0 mm | 73%   │     ‘ ‘ ‘ ‘   0.0 mm | 65%   │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                       ┌─────────────┐
┌──────────────────────────────┬───────────────────────┤  Tue 05 Mar ├───────────────────────┬──────────────────────────────┐
│            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│      .-.      Moderate rain  │      .-.      Light drizzle  │  _`/"".-.     Patchy rain ne…│     \   /     Clear          │
│     (   ).    +8(7) °C       │     (   ).    +9(7) °C       │   ,\_(   ).   +11(10) °C     │      .-.      9 °C           │
│    (___(__)   → 9-12 km/h    │    (___(__)   ↘ 12-17 km/h   │    /(___(__)  → 10-16 km/h   │   ― (   ) ―   ↘ 5-10 km/h    │
│   ‚‘‚‘‚‘‚‘    7 km           │     ‘ ‘ ‘ ‘   2 km           │      ‘ ‘ ‘ ‘  10 km          │      `-’      10 km          │
│   ‚’‚’‚’‚’    3.1 mm | 100%  │    ‘ ‘ ‘ ‘    0.5 mm | 100%  │     ‘ ‘ ‘ ‘   0.0 mm | 82%   │     /   \     0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                       ┌─────────────┐
┌──────────────────────────────┬───────────────────────┤  Wed 06 Mar ├───────────────────────┬──────────────────────────────┐
│            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│    \  /       Partly Cloudy  │  _`/"".-.     Patchy rain ne…│     \   /     Sunny          │    \  /       Partly Cloudy  │
│  _ /"".-.     10 °C          │   ,\_(   ).   13 °C          │      .-.      +12(11) °C     │  _ /"".-.     +10(9) °C      │
│    \_(   ).   ↓ 1 km/h       │    /(___(__)  ↑ 6-7 km/h     │   ― (   ) ―   ↑ 10-16 km/h   │    \_(   ).   ↖ 9-15 km/h    │
│    /(___(__)  10 km          │      ‘ ‘ ‘ ‘  10 km          │      `-’      10 km          │    /(___(__)  10 km          │
│               0.0 mm | 0%    │     ‘ ‘ ‘ ‘   0.1 mm | 100%  │     /   \     0.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
Location: Θεσσαλονίκη, Δήμος Θεσσαλονίκης, Περιφερειακή Ενότητα Θεσσαλονίκης, Περιφέρεια Κεντρικής Μακεδονίας, Αποκεντρωμένη Διοίκηση Μακεδονίας - Θράκης, Ελλάδα [40.6403167,22.9352716]

Follow @igor_chubin for wttr.in updates

Is there anything else that you would like me to do? (Yes/No)
```
## Translate

You can ask for a translation of words/sentences from any language to another.

```
Whats else would you like?
I want to translate a sentence
Enter the text you want to translate: Hello, how are you?
Enter the source language
en-English,el-Greek,fr-French,de-German etc: en
Enter the target language
en-English,el-Greek,fr-French,de-German etc: el
Γεια τι κάνεις;
Is there anything else that you would like me to do? (Yes/No)
```
## Jokes

You can ask the program to improve your mood by telling you a joke.
```
Whats else would you like?
Can you tell me a joke?
I will tell you a joke!
Why did the programmer quit his job? Because he didn't get arrays.
I hope you liked it!
Is there anything else that you would like me to do? (Yes/No)
```

## Wikipedia Search

You can ask the program for information about a subject and it return you the first paragraph of wikipedia.

```
Whats else would you like?
I would like some information
What do you want to learn about?
(ex. WW2)
Greece
Summary:

Greece, officially the Hellenic Republic, is a country in Southeast Europe on the southern tip of the Balkan peninsula. Greece shares land borders with Albania to the northwest, North Macedonia and Bulgaria to the north, and Turkey to the east. The Aegean Sea lies to the east of the mainland, the Ionian Sea to the west, and the Mediterranean Sea to the south. Greece has the longest coastline on the Mediterranean Basin, featuring thousands of islands. It has a population of nearly 10.3 million. Athens is the nation's capital and largest city, followed by Thessaloniki and Patras.
Greece is considered the cradle of Western civilization and the birthplace of democracy, Western philosophy, Western literature, historiography, political science, major scientific and mathematical principles, theatre, and the Olympic Games. From the eighth century BC, the Greeks were organised into various independent city-states known as poleis (singular polis) that spanned the Mediterranean and Black seas. Philip II of Macedon united most of present-day Greece in the fourth century BC, with his son Alexander the Great rapidly conquering much of the known ancient world from the eastern Mediterranean to northwestern India. The subsequent Hellenistic period saw the height of Greek culture and influence in antiquity. Greece was annexed by Rome in the second century BC, becoming an integral part of the Roman Empire and its continuation, the Byzantine Empire, which was predominately Greek in culture and language. Modern Greek identity began taking shape with the emergence of the Greek Orthodox Church in the first century AD, which transmitted Greek traditions to the wider Orthodox world. Following the gradual decline and fragmentation of the Byzantine Empire, Greece came under Ottoman rule in the mid-15th century.
Greece emerged as a modern nation state in 1830 following a protracted war of independence. The Kingdom of Greece embarked on an ambitious nationalist project that vastly expanded its territory over the next century. Persistent social division, civil strife, and political instability were exacerbated by the Balkan Wars, World War I, and the Greco-Turkish War. A short-lived republic was established in 1924 but fell to a royalist dictatorship in 1936, which collapsed after Italy and German invaded during World War II. The subsequent military occupation gave way to civil war and military dictatorship. Greece nonetheless achieved record economic growth from 1950 through the 1970s, and democracy was restored in 1975, leading to the current parliamentary republic.
Greece is a democratic and developed country with an advanced high-income economy, the second largest in the Balkans, where it is an important regional investor. A founding member of the United Nations, Greece was the tenth member to join what is today European Union and has been part of the eurozone since 2001. It is also a member of numerous other international institutions, including the Council of Europe, NATO, the OECD, the WTO, and the OSCE. Greece has a unique cultural heritage, large tourism industry, and prominent shipping sector. The country's rich historical legacy is reflected in part by its 19 UNESCO World Heritage Sites.



Is there anything else that you would like me to do? (Yes/No)
```

## Notebook

The program gives you the ability to have a notebook for your daily tasks. You can read and write new notes, and they are stored in a .txt file with the name of the current date.

If you want to write a note:
```
Whats else would you like?
I would like to write a note in my notebook.
Write your note:
6:00 PM GYM
Note saved successfully.
Is there anything else that you would like me to do? (Yes/No)
```
A file named note_05_03_2024.txt is created.

If you want to read the notes:
```
Whats else would you like?
I would like to read my notes
Notes:
6:00 PM GYM
Is there anything else that you would like me to do? (Yes/No)
```

In case there aren't any notes:
```
Whats else would you like?
I would like to read my notes
You dont have any notes for today.
Is there anything else that you would like me to do? (Yes/No)
```

## Testing

To run tests, use the following command:
```
python tests.py
```

## Acknowledgments

* Thanks to the contributors of the external libraries used in this project.
* Special thanks to [translate](https://translate-python.readthedocs.io/en/latest/), [pyjokes](https://pypi.org/project/pyjokes/), and [wikipedia-api](https://pypi.org/project/Wikipedia-API/).


> [!NOTE]
> The program is case-insensitive.


> [!NOTE]
> The program can accept different inputs to perform a certain task.

## Contact

* Name: Vagelis Zarkadoulas
* Email: vagzarkadoulasdh@gmail.com
* GitHub: vagzark

[Return to the top](#my-assistant)
