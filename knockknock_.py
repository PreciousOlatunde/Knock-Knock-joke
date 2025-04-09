#Ask the user for their name and store in a name variable

name = input("Hello, What's your name? ")

#Repeat their name in a greeting

print("Hi {}, here's a joke for you: ".format(name))

#Fist knock knock line

print("Knock knock")

#Ask for input

input1 = input("(Now you say something): ")

#Next knock knock line

print("Cow says.")

#Ask for more input

input2 = input("(Now you say something): ")

#Last knock knock line

print("No, a cow says moooo!")

#define function newJoke() that tells a second joke.

def newJoke():
    #first knock knock line
    print("Knock knock")
    #ask for input
    input1 = input("(Now you say something): ")
    #next knock knock line
    print("Snow.")
    #ask for more input
    input2 = input("(Now you say something): ")
    #last knock knock line
    print("Snow use now. The joke's over.")


#define function checkResponse() that asks if they would like another joke then checks the user's response and reacts accordingly

def checkResponse():
    #ask if they would like another joke

    response = input("Would you like another joke? ")

    #change all the characters in their response to lowercase

    response = response.lower()

    #if-else statement to check if they said yes, no or something else

    if "no" in response:
        #print a goodbye message
        print("Alright! Goodbye!")
    #check is the word yes is in the response
    elif "yes" in response:
        #call the function that tells a new joke
        newJoke()
    #handle is user input is not yes or no
    else:
        #instruct the user to respond with yes or no
        print("I dont understand. Please respond with yes or no. ")
        #call the function again to check their new response
        checkResponse()

#call checkResponse() to ask the user if they would like a new joke

checkResponse()
