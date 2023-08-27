from time import sleep


new = 1
old = 1

def maincode():
    print("maincode")

while True:
    sleep(2.0)
    
    print(".")
    
    if new == old:
        continue
    else:
        print("new request")
        old = new
        maincode()