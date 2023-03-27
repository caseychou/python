import time
from urllib.parse import unquote, quote

# declares a list, replace the URL placeholders with the URLs to encode or decode
url_list = [
        'url1',
        'url2',
        'url3'
        ]

# global error status for error handler
err = int(0)

# decodes the list of urls and outputs the decoded string
def decode_this_url (url_list):
    for item in url_list:
        url = unquote(item)
        print(url)
    return url

# encodes the list of urls and outputs the decoded string
def encode_this_url (url_list):
    for item in url_list:
        url = quote(item)
        print(url)
    return url

# prompts the user to indicate which function to use, or sets an error code equal to 1, failing the error handler, 
# which loops this function until err = 0
def menu_function ():
    encode_or_decode = input('(e)ncode or (e)ecode URL list? (Respond with the letter corresponding with the operation you need)')
    global err
    if encode_or_decode == "e" :
        encode_this_url(url_list)
        time.sleep(1.5)
        err = 0
    elif encode_or_decode == "d":
        decode_this_url(url_list)
        time.sleep(1.5)
        err = 0
    else:
        err = 1

#  loops menu_function() unless err = 0
def err_handler():
    if err == '1':
        menu_function()
    else:
        return
    
# triggers the menu 
menu_function()

# checks error status and loops menu_function if the user inputs a(an) invalid character(s)
err_handler()