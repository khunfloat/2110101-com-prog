def no_lowercase(t):
    return not any(char.islower() for char in t)
 
def no_uppercase(t): 
    return not any(char.isupper() for char in t)
 
def no_number(t): 
    return not any(char.isdigit() for char in t)
 
def no_symbol(t): 
    return not any(not char.isalnum() for char in t)
 
def character_repetition(t):
    if len(t) < 4: return False
    for i in range(3, len(t)+1):
        if t[i-3] == t[i-2] == t[i-1] == t[i]:
            return True
    return False

def number_sequence(t): 
    if len(t) < 4: return False
    for i in range(4, len(t)+1):
        a = t[i-4:i]
        if (a in "01234567890987654321") and (a != ''):
            return True
    return False

def letter_sequence(t): 
    if len(t) < 4: return False
    for i in range(4, len(t)+1):
        a = t[i-4:i].lower()
        if (a in "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") and (a != ''):
            return True
    return False

def keyboard_pattern(t):
    if len(t) < 4: return False
    for i in range(4, len(t)+1):
        a = t[i-4:i].lower()
        if ((a in "!@#$%^&*()_+_)(*&^%$#@!)") or (a in "qwertyuiopoiuytrewq") or (a in "asdfghjklkjhgfdsa") or (a in "zxcvbnmnbvcxz")) and (a != ''):
            return True
    return False
#----------------------------- 
passw = input().strip() 
errors = [] 
if len(passw) < 8: 
    errors.append("Less than 8 characters") 
 
if no_lowercase(passw): 
    errors.append("No lowercase letters") 
 
if no_uppercase(passw): 
    errors.append("No uppercase letters")

if no_number(passw): 
    errors.append("No numbers")

if no_symbol(passw): 
    errors.append("No symbols")

if character_repetition(passw):
    errors.append("Character repetition")

if number_sequence(passw):
    errors.append("Number sequence")

if letter_sequence(passw):
    errors.append("Letter sequence")

if keyboard_pattern(passw):
    errors.append("Keyboard pattern")

if len(errors) == 0: 
    print("OK")
else:
    for err in errors:
        print(err)