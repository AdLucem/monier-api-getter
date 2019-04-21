# Get Word Meanings From Monier-Williams Dictionary

Clone the script and install requirements like so, from the linux terminal command line: 

```
git clone https://github.com/AdLucem/monier-api-getter.git 
pip install -r requirements.txt
```

To get the meaning of a sanskrit word from the monier-williams dictionary, run the script like so:

```
python3 get.py <sanskrit_word_in_slp1>
```

The output will be displayed on the terminal like so:

```
headword 1
-----------------------------------
-> meaning 1
-> meaning 2
===================================
headword 2
-----------------------------------
-> meaning 1
-> meaning 2
===================================
```

It also can read words from a file, given that the file has one word per line in the SLP1 format. Here's the command to do so:

```
$ python3 get_from_file.py <filename>
```

It prints the word no. (as given in the file), the word and the meanings in the above format, to terminal.

If there's any issue with the script, please raise an issue.

