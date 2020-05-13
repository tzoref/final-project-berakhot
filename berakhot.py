# Create a text file of the textual material in the json Berakhot file that will be usable for text analysis

import json

with open('Berakhot_sefaria.json') as f:
    data = json.load(f)

# print type of data.  Output is: class 'dict'
print("Type of data = " + str(type(data)))

# print the keys of the dictionary, data
print(data.keys())
print("")
# output is: dict_keys(['language', 'title', 'versionSource', 'versionTitle', 'status', 'priority', 'license', 'licenseVetted', 'versionNotes', 'versionTitleInHebrew', 'versionNotesInHebrew', 'heTitle', 'categories', 'text', 'sectionNames'])

# set a variable for the contents of the 'text' key
text_list = data['text']
print(len(text_list))
print(type(text_list))

# print(text_list).  comment out this code to reduce output volume

string_text = ""

text_list.reverse()

for element in text_list:
    for string in element:
        for letter in string:
            # print(letter)
            string_text = letter + string_text
print(string_text)
print(type(string_text))
print(len(string_text))

file = open('Berakhot.txt', 'w')
file.write(string_text)