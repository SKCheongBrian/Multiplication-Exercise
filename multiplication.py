import random

def main():
    #get error counter
    count = 0
    #get number of questions from lord brian as well as return error if not valid
    while True:
        try:
            numOfQ = int(input("How many questions shall the young one do today handsome lord sir Brian?: "))
            break
        except ValueError:
            print("Please enter a number Lord Sir handsome sweet smiling Brian.")

    #create loop with number of questions and get random 2 numbers to multiply tgt
    for i in range(numOfQ):
        firstN = random.randint(1,12)
        secondN = random.randint(1,12)

        correctAns = firstN * secondN
        #now get student's response
        while True:
            try:
                stuAns = int(input(f"What is {firstN} multiplied by {secondN}?: "))
                break
            except ValueError:
                print("Bro please enter a number!")

        #initialising random congratulations message
        options = {0 : nice, 1 : goodJob, 2 : awesome}
        #now check students answer if correct
        while True:
            if stuAns == correctAns:
                options[random.randint(0,2)]()
                break
            else:
                count += 1
                print("Wrong!")
                while True:
                    try:
                        stuAns = int(input(f"What is {firstN} multiplied by {secondN}?: "))
                        break
                    except ValueError:
                        print("Bro please enter a number!")
        if count == 0: 
            print(f"Congratulations! You completed all {numOfQ} questions perfectly!")
        elif count == 1:
            print(f"Congratulations! You completed all {numOfQ} questions, you were only wrong {count} time. Nice try!")
        elif count >1:
            print(f"Congratulations! You completed all {numOfQ} questions, you were wrong {count} times. Try harder next time!")


def nice():
    print("Nice!")

def goodJob():
    print("Good job!")

def awesome():
    print("Awesome!")

main()
