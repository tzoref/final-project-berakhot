This project is a first step towards a long-term ambition of creating a digital resource for the analysis of the corpus of the Babylonian Talmud.  

* *LONG-TERM GOAL*
to create a database with information about the 13 traditional "hermeneutical principles" used in the Talmud and related rabbinic writings. 

* *MID-RANGE GOAL*
to catalogue and compare Talmudic occurrences of the "a fortiori" argument, a form of analogical reasoning, arguing from a mild case to a more severe case.  These instances are marked by technical terms, such as "qal va'chomer", "eino din", and "al achat kama ve'chama" (conventionally translated into English as: "a fortiori", "is it not clear from comparison", "all the more so".)

* *COURSE PROJECT GOAL*
initial (overly-ambitious) goal: to search for instances of this argument by means of the expressions "qal va'chomer" and "eino din" and "al achat kama ve'chama" in the first "tractate" of the Babylonian Talmud-- "Berakhot" (English: "Blessings").
# ADJUSTED GOAL:
1. to use python to extract the text of the tractate Berakhot from a JSON file containing the text, downloaded from the open source website www.sefaria.org.
2. to use python to convert the text into manipulable strings, in a non-nested form.
3. to create a text file containing the non-nested form of the text.

The documentation in berakhot.py lays out the steps in my thinking, once I grasped the conceptualization of identifying the values and types of the keys in the json data.
I struggled a lot with the reversal of text, due to the right-to-left feature of Aramaic/Hebrew.  
I have not yet resolved this issue. 
I also remain confused by the differences in sequence and direction in Bash as compared to the berakhot.txt file. (I've also gotten varying results when I've tried to copy and paste from bash into a Word document, including Word freezing)

# NEXT GOALS FOR FUTURE:
to resolve the problems of the direction of the text, at the level of strings and larger chunks (what I've called "elements").
to use NLP to SEARCH for the desired terms and print out the occurrences.
to find ways to mark the occurences: (1) by means of surrounding words (2) correlating the text with conventional notation of page and "side" number. 