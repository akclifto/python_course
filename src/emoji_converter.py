msg = input("")
words = msg.split(" ") # separate string by word

# on windows to get the emojis, press "WINDOWS_Key" + "period",
# the unicode version list can be found here: https://www.unicode.org/emoji/charts/full-emoji-list.html
emojis = {
    ":)": "\U0001F600",
    ">:(": "😠" 
}

result = ""
for word in words:
    result += emojis.get(word, word) + " "

print(result)