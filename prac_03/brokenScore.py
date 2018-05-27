"""
CP1404 Practical
Broken program to determine score status
"""

def scoreCheck(score):
    if score < 0:
        print("Invalid score")
    elif score > 100:
        print("Invalid score")
    elif 50 < score < 90:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")
    return score

def main():
    score = float(input("Enter score: "))
    scoreCheck(score)

main()