import random

## Declaring Variables ##

# Name of User
name = "Nemiah"
# Yes or No Question
question = ""
# Magic 8 Balls answer
answer = ""

## Generating Random Number ## 

random_number = random.randint(1, 10)
#print(random_number)

## Control Flow ## 

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Aw hell nah gang"
else:
  answer = "Error"

## Output

# If/else statement in the case that user does not provide a name
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)
# if/else statement in the case that user doesn't give a question
if question == "":
  print("Looks like you didn't ask anything")
else:
  print("Magic 8 Ball's answer: " + answer)