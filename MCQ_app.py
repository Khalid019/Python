
Q1 = '''Question 1. Name of capital city of Bangladesh
a) Khulna
b) Sylhet
c) Rajshahi
d) Dhaka '''

Q2= '''Question 2. Name of industrial city of Bangladesh
a) Khulna
b) Chittagong
c) Rajshahi
d) Dhaka '''

Q3= '''Question 3. Name of tea industrial city of Bangladesh
a)Sylhet
b) Chittagong
c) Rajshahi
d) Dhaka '''

Q4= '''Question 4. Name of shirimp city of Bangladesh
a) Khulna
b) Chittagong
c) Rajshahi
d) Satkhira '''

Q5= '''Question 5. Name of division city of Bangladesh
a) Khulna
b) Chittagong
c) Rajshahi
d) above all '''

# Creeate dictionary
questions = {Q1:"d", Q2: "b", Q3:"a", Q4:"d", Q5:"d"}


name = input("Enter your Name: ")
print("Hello", name, "Welcome to the quiz")

score = 0
for i in questions:
    print(i)
    skip_question = input("Do you wanna skip this question, please type (Yes/No): ")
    if skip_question == "Yes" or skip_question =="yes":
        continue
    answer = input("Enter the correct answer (a/b/c/d): ")

    if answer == questions[i]:
        print("Correct answer, you got 1 point")
        score = score + 1
        print("Current score is: ", score)

    else:
        print("Wrong answer, you lost 1 point")
        score = score -1  
        print("Current score is: ", score)   

    skip_quiz = input("Do you wanna exit this quiz, please type (Yes/No):")
    if skip_question == "Yes" or skip_question == "yes":
        break     

# Final solution:
print("Final score is: ", score)

