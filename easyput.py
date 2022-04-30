def easyintput(txt):
    if (easyintput == ""):
        raise NameError("TypeError: easyintput("") is empty")
    int(input(txt))   
     
def easyfloatput(txt):
    if (easyfloatput == ""):
        raise NameError("TypeError: easyfloatput("") is empty")
    float(input(txt))
    
def easystrput(txt):
    if (easystrput == ""):
        raise NameError("TypeError: easystrput("") is empty")
    str(input(txt))

def easyput(txt):
    if (easyput == ""):
        raise NameError("TypeError: easyput("") is empty")
    input(txt)