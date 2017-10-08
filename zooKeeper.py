# Create zoo
import pandas as pd
import random


#All animals have the following tuple structure: torso_height, torso_width, head_height, head_width, ear_length

def capybara(n):
    keys = ["Capybara_"+str(i) for i in range(1,n+1)]
    capybaraDict = {key: None for key in keys}
    
    for capy in capybaraDict:
        baseValue = float(random.randrange(10, 50, 1))
        torso_height = baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        torso_width = 0.5*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        head_height = 0.2*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        head_width = 0.1*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        ear_length = 0.01*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        capybaraDict[capy] = (torso_height, torso_width, head_height, head_width, ear_length)
    
    return(capybaraDict)

def bigCapybara(n):
    keys = ["Big_Capybara_"+str(i) for i in range(1,n+1)]
    bigCapybaraDict = {key: None for key in keys}
    
    for capy in bigCapybaraDict:
        baseValue = float(random.randrange(50, 80, 1))
        torso_height = baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        torso_width = 0.5*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        head_height = 0.2*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        head_width = 0.1*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        ear_length = 0.01*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        bigCapybaraDict[capy] = (torso_height, torso_width, head_height, head_width, ear_length)
    
    return(bigCapybaraDict)

def puppy(n):
    keys = ["Puppy_"+str(i) for i in range(1,n+1)]
    puppyDict = {key: None for key in keys}
    
    for puppy in puppyDict:
        baseValue = float(random.randrange(10, 20, 1))
        torso_height = baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        torso_width = 0.3*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        head_height = 0.2*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        head_width = 0.1*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        ear_length = 0.3*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        puppyDict[puppy] = (torso_height, torso_width, head_height, head_width, ear_length)
    
    return(puppyDict)

def elephant(n):
    keys = ["Elephant_"+str(i) for i in range(1,n+1)]
    elephantDict = {key: None for key in keys}
    
    for elephant in elephantDict:
        baseValue = float(random.randrange(80, 150, 1))
        torso_height = baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        torso_width = 0.5*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        head_height = 0.3*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        head_width = 0.3*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        ear_length = 0.5*baseValue*(1.00+(float(random.randrange(-10, 10, 1))/100))
        elephantDict[elephant] = (torso_height, torso_width, head_height, head_width, ear_length)
    
    return(elephantDict)

def makeZoo(n):
    if type(n) != int and type(n) != float:
        print("You must enter an integer.")
	return("You must enter an integer.")
    elif int(n) < 1:
        print("Only happy, positive animals, please!")
	return("Only happy, positive animals, please!")
    else:
        nFloat = float(n)
        nInt = int(n)
        
        # Create 55% capybaras, 20% really big capybaras, 15% puppies, 10% elephants
        bigCapybaraN = int(0.10*nFloat)
        puppyN = int(0.05*nFloat)
        elephantN = int(0.01*nFloat)
        capybaraN = nInt - (bigCapybaraN + puppyN + elephantN)
        
        myCapybaras = capybara(capybaraN)
        myBigCapybaras = bigCapybara(bigCapybaraN)
        myPuppies = puppy(puppyN)
        myElephants = elephant(elephantN)
        
        myZoo = {}
        myZoo.update(myCapybaras)
        myZoo.update(myBigCapybaras)
        myZoo.update(myPuppies)
        myZoo.update(myElephants)
        
        allAnimals = pd.DataFrame.from_dict(myZoo).transpose()
        allAnimals.columns = ['torso_height', 'torso_width', 'head_height', 'head_width', 'ear_length']
        
        return(allAnimals)