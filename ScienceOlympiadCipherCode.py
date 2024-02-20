import random
import math
import numpy as np
import sys
import os
# Variables Initializing
alphaBetList = ["A","B","C","D","E",'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',"Z"]
alphaBetListWithoutJ = ["A","B","C","D","E",'F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',"Z"]

def stringtoList(x):
    y = []
    for i in range(0,len(x)):
        y= y + [x[i]]
    return(y)
def alphabetGenerator():
    outPut = []
    for item in random.sample(alphaBetList,26):
        outPut.append(item)
    return(outPut)
def alphabetGeneratorWithoutJ():
    outPut = []
    for item in random.sample(alphaBetListWithoutJ,25):
        outPut.append(item)
    return(outPut)
def alphabetGeneratorFromKeyword(keyword):
    try:
        if not isinstance(keyword, str):
            keyword = str(keyword).upper()
        alphabetstring = ''
        for item in keyword:
            if item not in alphabetstring and item in alphaBetList:
                alphabetstring = alphabetstring + item
        for word in alphaBetList:
            if word not in alphabetstring:
                alphabetstring = alphabetstring + word
        return(alphabetstring)
    except Error as ErrMsg:
        print('Error in the Keyeord based Alphabet Generator: ', ErrMsg)
def alphabetGeneratorHumanRadable():
    resultingText = ''
    Start = alphabetGenerator()
    for item in Start:
        resultingText = resultingText + item
    return(resultingText)
def polybusSquareGenerator():
    x = input('USe your own alphabet? Y/n ')
    if x == 'Y':
        startingAlphabet = input('Please type your alphabet.')
    else:
        startingAlphabet = alphabetGeneratorWithoutJ()
    polybusSquare = np.zeros((5,5))
    newAlphabet = []
    # Note to self: Rember to add I/J checing to code for encryption
    for item in startingAlphabet: 
        newAlphabet.append(alphaBetListWithoutJ.index(item))

    polybusSquare[0] = newAlphabet[0:5]
    polybusSquare[1] = newAlphabet[5:10]
    polybusSquare[2] = newAlphabet[10:15]
    polybusSquare[3] = newAlphabet[15:20]
    polybusSquare[4] = newAlphabet[20:25]

    return(polybusSquare)
def listToString(targetList):
    newString = ''
    for item in targetList:
        newString = newString + item + ' '
    return newString
def userReadablePolybusSquare():
    inputSart = polybusSquareGenerator()
    intermediateList = []
    for item in inputSart:
        for x in item:
            intermediateList.append(alphaBetListWithoutJ[int(x)])
    print('')
    print('Remember that I and J are equivalent.')
    print('')
    print('  1 2 3 4 5')
    print('1' , listToString(intermediateList[0:5]))
    print('2' , listToString(intermediateList[5:10]))
    print('3' , listToString(intermediateList[10:15]))
    print('4' , listToString(intermediateList[15:20]))
    print('5' , listToString(intermediateList[20:25]))
def generateRandomText():
    randomText = ''
    lengthTarget = int(input('Length? '))
    for i in range(lengthTarget):
        randomText = randomText + alphaBetList[random.randint(0,25)]
    return(randomText)
def generateRandomTextTesting():
    randomText = ''
    lengthTarget = int(input('Length? '))
    for i in range(lengthTarget):
        randomText = randomText + alphaBetList[random.randint(0,25)]
        if i % (lengthTarget/10) == 0:
            print(str(int(str(int(i/int(str(lengthTarget)[0])))[0]))+'0%')
    return(randomText)
def atbashEncryption(plainText):
    cipherText=''
    CipherAlphabet = alphaBetList[::-1]
    for letter in plainText:
        if letter in alphaBetList:
            cipherText = cipherText + CipherAlphabet[alphaBetList.index(letter)]
        if letter == ' ':
            cipherText = cipherText + ' '
    return cipherText

def main():
    print("Starting Science Olympiad Cryptology Assistance System")
    print("Type 1 for Ceasar")
    print("Type 2 for Alphabet Scrambler Tool")
    print("Type 3 for the Block Splitter Tool")
    print("Type 4 for MonoAlphabetic Substitution")
    print("Type 5 for Polybus Square Generator")
    print("Type 6 for Random Text Generator")
    print("Type 7 for Atbash Cipher")
    print("Type 'Quit' to Quit")

    target = str(input("Cipher Number? "))
    
    outPut = ""
    if target == "1": 
        plainText = str(input("Type the message to encrypt ")).upper()
        key = int(input("Key (If applicable) "))
        for item in plainText:
            if item in alphaBetList:
                mynum = alphaBetList.index(item)
                mynum = (mynum + key) % 26
                outPut = outPut + alphaBetList[mynum]
        print(str(outPut))
   
    if target == '2':
        answer = input('Generate from keyword? Y/n ')
        if answer == 'Y':
            keyforAlphabet = input('Keyword')
            newAlphabet = alphabetGeneratorFromKeyword(keyforAlphabet)
            print(newAlphabet)
        if answer == 'n':
            print('Generating random alphabet . . . ')
            print(alphabetGeneratorHumanRadable())

    if target == '3':
        blockLength = int(input('block length? '))
        c = 0
        for item in input("input text "):
            if item != ' ':
                outPut = outPut + item
                c = c + 1
                if c % blockLength == 0 and c != 0:
                    outPut = outPut + ' '
        outPut = outPut
        print(outPut)
    if target =='4':
        cipherText = ''
        x = input("Use your own Alphabet? Y/n ")
        if x == 'Y':
            InitialCipherAlphabet = input("Please Type in an alphabet with no spaces. ")
            CipherAlphabet = stringtoList(str(InitialCipherAlphabet))
        else:
            CipherAlphabet = alphabetGenerator()
        plainText = input("Please type the plaintext. ").upper()
        for letter in plainText:
            if letter in alphaBetList:
                cipherText = cipherText + CipherAlphabet[alphaBetList.index(letter)]
            if letter == ' ':
                cipherText = cipherText + ' '
        print(cipherText)

    if target =='5':
        userReadablePolybusSquare()
    if target =='6':
        answer = input('Save to File or command line? Y/n ')
        if answer == 'n':
            print(generateRandomText())
        if answer == 'T':
            print(generateRandomTextTesting())
        if answer == 'Y':
            print('This feature is not yet implemented.')
            #os
    if target =='7':
        answer = str(input('Please Type the plain text of your message. '))
        print(str(atbashEncryption(answer)))
    if target == '8':
        None
        #Place holder

        
    if target =='Quit':
        sys.exit()

    # remember to update the below 7 to include the current number of ciphers
    for i in range(8):
        if target == str(i):
            print('')
            FinalQuestion = input('Quit?? Y/n ')
            if FinalQuestion == 'Y':
                print('Quiting . . . .')
                sys.exit()
    else:
        print("That wasn't an option. Restarting. . . . ")
        main()
    

#Seems to return an error when run in debug mode.
#if __name__ == '__main__':
  #  main()

main()