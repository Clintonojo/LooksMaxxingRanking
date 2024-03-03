score = 0

# Score percentage aftewards.ScorePer=Score
# ScorePer=Score/40*100
print("Hello Welcome to looksMaxxing Ranking Game ")
print("ill ask u a few question and u just have to answer them")

# While loop to keep asking the user to enter an input
# While statement will keep going till statement is true
while True:
    try:
        Height = int(input("What height are you in cm: "))
        break
    except ValueError:
        print("Please enter a valid interger for your height")
while True:
    try:
        Weight = int(input("What is your weight in Kg:"))
        break
    except ValueError:
        print("Please enter a vaild interger for your Weight")
if Height >= 190:
    print("This is your Height Score :""10")
    score += 10
elif Height <= 189 and Height >= 184:
    print("This is your Height Score:""9")
    score += 9
elif Height <= 183 and Height >= 175:
    print("This is your Height Score:""8")
    score += 8
elif Height <= 174 and Height >= 170:
    print("This is your height score:""7")
    score += 7

elif Height <= 169 and Height >= 164:
    print("This is your height score:""6")
    score += 6

elif Height <= 163 and Height >= 159:
    print("This is your height score:""5")
    score += 5

elif Height <= 158 and Height >= 153:
    print("This is your height score:""4")
    score += 4

elif Height <= 152 and Height >= 145:
    print("This is your height score:""3")
    score += 3

elif Height <= 144 and Height >= 138:
    print("This is your height score:""2")
    score += 2

elif Height <= 137 and Height >= 130:
    print("This is your height score:""1")
    score += 1

elif Height <= 129:
    print("This is your score:""0")
    score +=0

Heightmeters = Height / 100
bmi = Weight / (Heightmeters * Heightmeters)


gender = input("Enter your if your male of female this is for body fat:")

while True:
    try:
        age = int(input("What age are you:"))
        break
    except ValueError:
        print("Enter interger fot this")
# Ask for age to but like  if age is over 25 then do this maths and if under then do this maths use if then use elif
if gender == "male" and age >= 18:
    MaleBpfA = 1.20 * bmi + 0.23 * age - 16.2

    if MaleBpfA <= 2:
     print("Please rerun application and enter a real weigt or height")
    elif MaleBpfA <= 2 and MaleBpfA <= 5:
     print("This is your bodyFat Score:", "10")
     print("This is your Bodyfat" + (str(MaleBpfA)))
     score += 10
    elif MaleBpfA <= 6 and MaleBpfA <= 13:
     print("This is your bodyFat Score:", "8")
     print("This is your Bodyfat" + (str(MaleBpfA)))
     score += 8
    elif MaleBpfA <= 14 and MaleBpfA <= 17:
     print("This is your bodyfat Score:", "6")
     print("This is your Bodyfat" + (str(MaleBpfA)))
     score += 6
    elif MaleBpfA <= 18 and MaleBpfA <= 24:
     print("This is your bodyfat Score:", "5")
     print("This is your bodyfat" + (str(MaleBpfA)))
     score+=4
    elif MaleBpfA >= 25:
     print("This is your bodyfat Score:", "0")
     print("This is your bodyfat" + (str(MaleBpfA)))
     score += 0



# IF UNDER 18 CODE
if gender == "male" and age <= 18:
    MaleBpfC = 1.51 * bmi - 0.70 * age - 2.2
    if MaleBpfC <= 2:
     print("Please rerun application and enter a real weigt or height")
    elif MaleBpfC <= 2 and MaleBpfC <= 5:
     print("This is your bodyFat Score:", "10")
     print("This is your Bodyfat" + (str(MaleBpfC)))
     score += 10
    elif MaleBpfC <= 6 and MaleBpfC <= 13:
     print("This is your bodyFat Score:", "8")
     print("This is your Bodyfat" + (str(MaleBpfC)))
     score += 8
    elif MaleBpfC <= 14 and MaleBpfC <= 17:
     print("This is your bodyfat Score:", "6")
     print("This is your Bodyfat" + (str(MaleBpfC)))
     score += 6
    elif MaleBpfC <= 18 and MaleBpfC <= 24:
     print("This is your bodyfat Score:", "5")
     print("This is your bodyfat" + (str(MaleBpfC)))
     score += 4
    elif MaleBpfC >= 25:
     print("This is your bodyfat Score:", "0")
     print("This is your bodyfat" + (str(MaleBpfC)))
     score += 0
