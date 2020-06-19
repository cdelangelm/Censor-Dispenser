# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in,
# and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_one(text, word):
    replacement = ''
    if word in text:
        for letter in word:
            replacement += '#'
        email_one_censored = text.replace(word, replacement)
    return email_one_censored

print(censor_one(email_one, 'learning algorithms'))