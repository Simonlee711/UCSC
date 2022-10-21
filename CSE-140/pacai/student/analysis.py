"""
Analysis question.
Change these default values to obtain the specified policies through value iteration.
If any question is not possible, return just the constant NOT_POSSIBLE:
```
return NOT_POSSIBLE
```
"""

NOT_POSSIBLE = None


def question2():
    """
    With the mitigation of all noise, it appears that it will always go in the right direction
    """

    answerDiscount = 0.9
    answerNoise = 0.0

    return answerDiscount, answerNoise


def question3a():
    """
    Similar to question 2 there is no noise so it should take the shortest path.
    Also reduced the discount and the living reward
    """

    answerDiscount = 0.2
    answerNoise = 0.0
    answerLivingReward = 0.4

    return answerDiscount, answerNoise, answerLivingReward


def question3b():
    """
    I lowered the reward so that the exit was worth more
    """

    answerDiscount = 0.3
    answerNoise = 0.2
    answerLivingReward = 0.2

    return answerDiscount, answerNoise, answerLivingReward


def question3c():
    """
    because we want to avoid cliffs we reduce noise to 0
    """

    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = 0.0

    return answerDiscount, answerNoise, answerLivingReward


def question3d():
    """
    We have a negative reward for answerLivingReward
    which prefers the long distant exit and avoiding the cliff
    conditions
    """

    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = -0.1

    return answerDiscount, answerNoise, answerLivingReward


def question3e():
    """
    If we make the living reward high it will think that is the best option
    therefore we made living reward a big number
    """

    answerDiscount = 0.0
    answerNoise = 0.1
    answerLivingReward = 1.0

    return answerDiscount, answerNoise, answerLivingReward


def question6():
    """
    After experimenting with the epsilon and learning Rate,
    there is no optimal policy that will be learned in 50 iterations
    """

    answerEpsilon = 0.0
    answerLearningRate = 0.0

    return "NOT POSSIBLE"
    return answerEpsilon, answerLearningRate


if __name__ == "__main__":
    questions = [
        question2,
        question3a,
        question3b,
        question3c,
        question3d,
        question3e,
        question6,
    ]

    print("Answers to analysis questions:")
    for question in questions:
        response = question()
        print("    Question %-10s:\t%s" % (question.__name__, str(response)))
