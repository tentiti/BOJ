emoticon_dict = { "CU": "see you", ":-)": "I’m happy", ":-( ": "I’m unhappy", ";-)": "wink", ":-P": "stick out my tongue", "(~.~)": "sleepy", "TA": "totally awesome", "CCC": "Canadian Computing Competition", "CUZ": "because", "TY": "thank-you", "YW": "you’re welcome", "TTYL": "talk to you later" }
while True:
    x = input()
    print(emoticon_dict.get(x, x))
    if x=='TTYL':
        break