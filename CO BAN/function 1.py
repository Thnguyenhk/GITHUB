def readinput(txt):
    "read user's answer to given prompt"
    while True:
        answer = input (f'{txt}: ')
        if answer:
            return answer

def greeting (name):
    "return a personalize greeting"
    return f"Nice to meet you, {name}"

print (greeting(readinput('Your name: '))) 