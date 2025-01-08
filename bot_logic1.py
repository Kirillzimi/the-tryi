import random
import requests
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
    return password

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
    

def get_duck_image_url():    
        url = 'https://random.dog/db7ea879-376a-4e00-b4e0-ee5b413be84d.jpg'
        res = requests.get(url)
        data = res.json()
        return data['url']

