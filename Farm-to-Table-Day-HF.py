print("Farm to Table Triva Board Game Code \nby HF '23 \nBe sure to get the game board that goes with this game!")

#food trivia game
import random

class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers
#these are the questions you are asked and then the answer is after that and then after the true answer are the "distration answers"
qaList = [QA("What is the largest type of olive tree called?", "donkey olive", ["ancient olive", "bullet", "horse olive"]),
QA("How many types of apples are there around the world?", "7,000", ["2,000", "9,000", "5,500"]),
QA("Besides vanilla, what spice is the most expensive?", "saffron", ["ginger", "cinnamon", "cardamom"]),
QA("What does the name for pomegranate mean?", "apple with many seeds", ["big red fruit", "round strawberry","red peach with a crown"]),
QA("Cranberrys that are good and ripe will bounce. So, a common nickname for them is what?", "Bounceberry", ["floatberry", "boingfruit", "bouncefruit"]),
QA("The science of apple growing is called what?", "pomology", ["apple chemistry", "applelogy", "blossom science"]),
QA("Vanilla is the only fruit-bearing member of what family?", "orchid family", ["pod family", "blossom family", "bean family"]),
QA("How long can pomegranate trees live up to?", "200 years", ["300 years", "100 years", "50 years"]),
QA("How many liters of olives does it take to make one liter of olive oil?", "7 liters", ["8 liters", "10 liters", "3 liters"]),
QA("An apple floats, because what percentage of it's volume is air?", "25%", ["50%", "75%", "35%"]),
QA("What percentage of cranberries are almost all water?", "90%", ["50%", "40%", "70%"]),
QA("Only one type of bee can pollinate vanilla in Central America. What is that bee?", "melipona bee", ["bumble bee", "carpenter bee", "honey bee"]),
QA("The flower that produces the vanilla bean lasts how many days?", "one day", ["three days", "one week", "two days"]),
QA("Pomegranates grown in the United States are typically grown in what months?", "September to Decemeber", ["Febuary to April", "June to September", "Septemeber to October"]),
QA("Apples are apart of what family?", "rose family", ["branch family", "red family", "seed family"]),
QA("Americans consume how many gallons of jellied cranberry sauce every holiday season?", "5,062,500", ["6,062,500", "3,062,500", "2,050,120"]),
QA("How many cranberries does it take to make one can of cranberry jelly?", "200", ["300", "450", "100"]),
QA("What type of climates are pomegranates typically grown in?", "hot and dry", ["cold and wet", "humid", "dry and cold"]),
QA("In ancient Greece, tossing an apple to a girl was a traditional proposal of what? Catching it was her acceptance.", "marriage", ["forgiveness", "to go on a trip", "that we only eat apples for the rest of our lives"]),
QA("Nearly what percentage of Americans choose vanilla as their No. 1 ice cream flavor?", "30%", ["40%", "25%", "10%"])]
#code to help them make sure they pick an answer and dont make a typo 
#tells them is answer is correct or incorrect
corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
  print(qaItem.question)
  print("Possible answers are:")
  possible = qaItem.otherAnsw + [qaItem.corrAnsw] 
  random.shuffle(possible)
  count = 0 
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")
  userAnsw = input()
  while not userAnsw.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnsw = input()
  if possible[userAnsw-1] == qaItem.corrAnsw:
    print("Your answer was correct.")
    corrCount += 1
  else:
    print("Your answer was wrong.")
    print("Correct answer was: " + qaItem.corrAnsw)
  print("")

print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")
