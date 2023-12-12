# bayes theorem

def bayes(x,y,a):
    return float((x*y) / a)

n = float(1 / 50000)
v = bayes(0.7, n, 0.01)
print("Bayes Value : ",bayes(0.7, n, 0.01))
print("Percentage : ",v*100,"%")

print()

# Dice

dice = [1,2,3,4,5,6]
even_number = [2,4,6]
even=0
odd=0
for i in range(6):
    if i % 2 == 0 :
        even+=1
    else :
        odd+=1

probabilityOfEvenNumber = even/6
probabilityOfOddNumber = odd/6
print("Probability of Even number : ",probabilityOfEvenNumber)
print("Percentage : ",probabilityOfEvenNumber*100)
print("Probability of Odd number : ",probabilityOfOddNumber)
print("Percentage : ",probabilityOfOddNumber*100,"%")


print()

# Marie's wedding'

prob_A1 = 0.014
prob_B_A1 = 0.9
prob_A2 = 0.986
prob_B_A2 = 0.1

Prob_A1_B = (prob_A1*prob_B_A1) / ((prob_A1 * prob_B_A1)+(prob_A2*prob_B_A2))
print("Prob",Prob_A1_B)
print("Percentage : ",Prob_A1_B * 100,"%")

# Conditional Probability

import pandas as pd
import numpy as np

df = pd.DataFrame({'gender': np.repeat(np.array(['Male', 'Female']), 150),
                   'sport': np.repeat(np.array(['Football', 'Badminton', 'Football',
                                                'Soccer', 'Cricket', 'Basketball',
                                                'Football', 'Soccer']),
                                    (34, 40, 58, 18, 34, 52, 20, 44))})


survey_data = pd.crosstab(index=df['gender'], columns=df['sport'], margins=True)

print(survey_data)


