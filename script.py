import random
import pyautogui
import string

chars = "abcdefghijklmnopqrstuvwxyz0123456789*!@#$%^&()<>?/:;\|{[}]"
# chars = string.printable 

chars_list = list(chars)

password = pyautogui.password("Enter a password : ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("<_=_=_=_=_=_=_=_=_=_>"+ str(guess_password)+ "<_=_=_=_=_=_=_=_=_=_>")

    if(guess_password == list(password)):
        print("Your password is : "+ "".join(guess_password))
        break