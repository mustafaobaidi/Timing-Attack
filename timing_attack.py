from time import perf_counter
from string import ascii_lowercase
from pprint import pprint
from time import time_ns

#the vulnerable function that compares the real password with the guessed one
def verify_password(stored_pwd, entered_pwd):
    if len(stored_pwd) != len(entered_pwd):
        return False
    
    for i in range(len(stored_pwd)):
        if stored_pwd[i] != entered_pwd[i]:
            return False
    return True

# timing attack occurs in this function where we can map the letter to time and check which on took the longest so we can say that this is the
# guessed charchter
def cracked(cracked_letter,padding,real_password):
    result = {char:0 for char in ascii_lowercase} 
    for _ in range (10001):
        for letter in ascii_lowercase: #loop thorugh the letters a..z
            str1 = cracked_letter + letter + '_' * padding
            start= time_ns()
            answer = verify_password(real_password,str1)  
            stop= time_ns()
            result[letter] += stop - start

    return sorted(result,key = result.get,reverse= True)[0]

def FinalGuess(cracked_letters,real_password):
    for letter in ascii_lowercase:
        guess = cracked_letters + letter
        answer = verify_password(real_password,guess)  
        if(answer):
            print(guess)

# check if the string contains any numbers
def contains_numbers(str):
    for char in str:
        if char.isdigit():
            return True
    return False

# check if the string contains any upper case

def contains_upper(str):
    for char in str:
        if char.isupper():
            return True
    return False


with open('password.txt', 'r') as file:
    data = file.read().rstrip()

if(contains_numbers(data)):
    print('the password contains a number, outside of the program\'s scope')

elif(contains_upper(data)):
    print('the password contains an upper case, outside of the program\'s scope')



else:
    cracked_letters = ''
    padding = len(data) -1
    for _ in range(padding):
        next_letter = cracked(cracked_letters,padding,data)
        cracked_letters += next_letter
        padding -=1
        print(cracked_letters)
    FinalGuess(cracked_letters,data)