import random
import smtplib
import time

# This function sends emails to the participants with their names and gifts.
# It uses the smtplib library to send emails.
# The function takes three parameters: name, gift and email.
# The function logs in to the email account and sends the message.
def send_email(name:str, gift:str, email:str) -> None:
    myEmail = "noreplyabdo@gmail.com"
    password = "grryseyqqpgyhszh"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(user=myEmail, password=password)
    message = f'Hi {name},\n\nYou have been assigned {gift} for this year\'s Secret Santa. Please keep this a secret until the 25th of December.\n\nMerry Christmas!\n\nSecret Santa Bot'
    s.sendmail("your email", email, message)
    s.quit()
    
# create a dictionary of names and public keys
def takeNames(a: str) -> dict:
    namesKeys = {}
    for i in a.split(","):
        namesKeys[i.split(":")[0].strip()] = int(i.split(":")[1].strip())
    return namesKeys

# take the names from the dictionary and put them in a list
def getNames(dic: dict[str, int]) -> list[str]:
    return list(dic.keys())

# from the list of names we shuffle them and assign them to each other
def assignSecretSanta(dictionary: dict[str, str]) -> dict[str, str]:
    names = list(dictionary.keys())
    random.shuffle(names)
    secret = {}
    for i in range(len(names)):
        if i == len(names) - 1:
            secret[names[i]] = names[0]
        else:
            secret[names[i]] = names[i + 1]
    return secret

# loop through the dictionary and assign gifts to each person
def assignGifts(gifts:list[str],choice:str,name:str,email:str):
    if choice.lower()  in gifts:
        gift =  gifts[choice.lower()]
        send_email(name,gift,email)

# this function is used to clear the terminal
def clearTerminal():
    print("\033c", end="")

# function to check if the private key is correct by calling the findPrivateKey function
def checkKey(name,privateKey,dictionary):
    return privateKey == findPrivateKey(dictionary[name] )

# calculate the coprime of a number
def findCoprime(a = 120):
    coprime = []
    for i in range(1,a):
        if gcd(i,a) == 1:
            coprime.append(i)
    return coprime

# calculate the gcd of two numbers
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)



# function to find the private key given the public key
# This code will find the private key in RSA algorithm
# The private key will be used to decrypt the cipher text
# The public key, p, q, n, and phi are known
def findPrivateKey(publicKey):
    p,q,n,phi = 11,13,143,120
    for i in range(1,phi):
        if (publicKey*i) % phi == 1:
            return i

def checkGift(gift):
    gifts = ['hat','bag','socks','shoes','jacket','gloves','scarf','glasses','watch','wallet','belt','tie','shirts','pants','shorts']
    if gift.lower() in gifts:
        return True
    return False

# function that takes a gift string and checks if its a valid gift


if __name__ == "__main__":
    # to get a map of public keys and private keys
    # public = findCoprime()
    # private = findPrivateKeys(public)
    # publicPrivate = {private[num]: public[num] for num in range(len(public))}
    # print(publicPrivate)


    print('''  ██████ ▓█████  ▄████▄   ██▀███  ▓█████▄▄▄█████▓     ██████  ▄▄▄       ███▄    █ ▄▄▄█████▓ ▄▄▄      
▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▓  ██▒ ▓▒   ▒██    ▒ ▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▒████▄    
░ ▓██▄   ▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒ ▓██░ ▒░   ░ ▓██▄   ▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██  ▀█▄  
  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░ ▓██▓ ░      ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ░██▄▄▄▄██ 
▒██████▒▒░▒████▒▒ ▓███▀ ░░██▓ ▒██▒░▒████▒ ▒██▒ ░    ▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░  ▓█   ▓██▒
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░░      ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░    ▒▒   ▓▒█░
░ ░▒  ░ ░ ░ ░  ░  ░  ▒     ░▒ ░ ▒░ ░ ░  ░   ░       ░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░    ░      ▒   ▒▒ ░
░  ░  ░     ░   ░          ░░   ░    ░    ░         ░  ░  ░    ░   ▒      ░   ░ ░   ░        ░   ▒   
      ░     ░  ░░ ░         ░        ░  ░                 ░        ░  ░         ░                ░  ░
                ░                                                                                    ''')
    print()
    print()
    print()
    a = input("Enter each name and its public key separated by a comma. Ex; email:key,email:key ... : ")
    time.sleep(4)
    namesDict = takeNames(a)
    namesArray = getNames(namesDict)
    if len(namesArray) < 3:
        print("You need at least 3 people to play this game")
        exit()
    s = assignSecretSanta(namesDict)
    print("Now we will call each name out and when you see your name you provide your private key to revel who will you get and send the gift after that the console will be cleared and the next name will be called")
    for i in namesArray:
        print(i)
        private = input("enter your private key to continue:")
        if findPrivateKey((namesDict[i])) == int(private):
            print("You have been assigned to: ", s[i])
            checker = True
            while checkKey:
                g = input(f"send a gift to {s[i]} which will be deliver through email: ")
                if checkGift(g):
                    checker = False
                    break
                else:
                    print("Invalid gift")
                    continue
            send_email(s[i],g,namesDict[s[i]])
            input("Press enter to continue and move to the next person")
            clearTerminal()
            time.sleep(3)
        clearTerminal()
    print("All the names have been called and the secret santa has been assigned to each one")
