import random
import keyword

Mclin_responses = [ #more responses are being added
    "Somebody helps this child", # response 0
    "You think you cute?", # response 1
    "Step out of line!", # response 2
    "Get a precious child!", # response 3
    "Did you talk to your study buddy?", # response 4
    "You need to fire your study buddy", # response 5
    "I shouldnt hear your mouth all the way over here.", # response 6
    "Do yall leave yall doors open at home", # response 7
    "You shouldnt be talking while someone else is giving their journal", # response 8
    "Are you gonna take that chair across that chair stage with you", # response 9
    "Dont take my laptop" # response 10
]

keyWords = [
    "Book", # Key word 0
    "Journal", # key word 1
    "Laptop", # Key word 2
    "Can", # Key word 3
    "i", # Key word 4
    "?", # Key word 5
    "Move" # Key word 6
]

mclinDoubleResponse = [
    "Did you talk to your study buddy?",
    "You need to fire your study buddy"
]

userInput = input("ask Mclin a question:")
keyword_found = False
mclinDoubleResponse1 = random.randint(0,1)

for keyword in keyWords:
    # If the keyword is in the user's input
    if keyword.lower() in userInput.lower(): 
        keyword_found = True
        # Respond based on the specific keyword
        if keyword == "Book":
            print(mclinDoubleResponse[mclinDoubleResponse1])  #Choses between two functions  (Did you talk to your study buddy?) or "You need to fire your study buddy"
        elif keyword == "Journal":
            print(Mclin_responses[8])  # prints ("You shouldnt be talking while someone else is giving their journal")
        elif keyword == "Laptop":
            print(Mclin_responses[10]) #prints ("Dont take my laptop")
        elif keyword == "?":
            print
        else:
            print(Mclin_responses[0])  # Default response if other keywords found
        break  # Exit loop if a keyword is found
# Goes directly into another function
if not keyword_found:
    print("I didn't understand your question.")

# old code without keyword feature
# playerName = input("whats your name?:")
# randQuestions = random.randint(0,9) 
# userOutput = input(playerName + " ask Mclin a question:")
# response = Mclin_responses[randQuestions]


# ## these are all of Mclin Responses
# while True:  ## While keeps the Statement running
#     randQuestions = random.randint(0,9) 
#     userOutput = input(playerName + " ask Mclin a question:")
#     response = Mclin_responses[randQuestions]
#     print(response)
#     break

