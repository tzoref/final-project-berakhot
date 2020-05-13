# Extracting Tractate Berakhot text from JSON in Python

This project uses python code to import a json file containing the Aramaic text of the first tractate of the Babylonian Talmud and to convert the text into a string object that can be manipulated for natural language processing.

# Installation
1. The JSON code for the Aramaic text of tractate Berakhot has been downloaded from the open source website www.sefaria.org, and saved in a file: berakhot_sefaria.json
2. The file berakhot.py imports JSON and opens the berakhot_sefaria.json file.
3. The berakhot.py file creates the text file Berakhot.txt containing the text in a non-nested form.


# Usage
To run the project, run this line in Bash:
python berakhot.py 