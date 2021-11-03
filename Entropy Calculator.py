import math

def entropy(a, b):
    if (a == 0 or b == 0) and a + b >= 0:
        return 0
    elif a == b:
        return 1
    else:
        return (- (a / (a + b)) * math.log(a / (a + b), 2) - (b / (a + b)) * math.log(b / (a + b), 2))
    #  - probability_a * log base 2 of probability_a - probability_b * log base 2 of probability_b



print(entropy(2,1))