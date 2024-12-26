import pyinputplus as pyip
import random,time

numberOfQuestions,correctAnswers = 10,0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1,num2 = random.randint(0,10),random.randint(0,10)

    prompt = f'#Q{questionNumber+1}: {num1} x {num2}='
    try:
        pyip.inputStr(prompt,allowRegexes=[f'^{num1*num2}$'],blockRegexes=[('.*','Incorrect!')],
                      limit=2,timeout=3)
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    else:
        print("Correct!")
        correctAnswers += 1

    time.sleep(1)

print(f"Score:{correctAnswers}")
print(f"Accuracy rate:{correctAnswers/numberOfQuestions*100:.2f}%")