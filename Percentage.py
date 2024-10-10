def calculate_percentage(score, total):
    percentage = (score / total) * 100
    return percentage

score = int(input("Enter the score: "))
total = int(input("Enter the total score: "))
percentage = calculate_percentage(score, total)
print(f"The percentage is: {percentage}%")
