# Ask user to enter their first name, last name and age and accept input
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))

# Create username in lowercase for user
username = first_name[0].lower() + last_name.lower() + str(age)

# Output username
print('Hello', first_name, 'your username is', username)

# Accept 3 bowling scores & test for validity for scores between 0-300
# Ask for first score
first_score = int(input('Enter your first score: '))
if (first_score >= 0) and (first_score <= 300):
    # If first score is valid, ask for second score
    second_score = int(input('Enter second score: '))
    if (second_score >= 0) and (second_score <= 300):
        # If second score is valid, ask for third score
        third_score = int(input('Enter third score: '))
        if (third_score >= 0) and (third_score <= 300):
            # Output scores
            print('Your scores are:', '\nFirst score:', first_score,
                  '\nSecond Score:', second_score, '\nThird score:', third_score)
        else:
            print('Invalid score. Valid bowling scores are between 0 - 300.')
            exit()
    else:
        print('Invalid score. Valid bowling scores are between 0 - 300.')
        exit()
else:
    print('Invalid score. Valid bowling scores are between 0 - 300.')
    exit()

# Store scores in a list
scores = [first_score, second_score, third_score]
# Calculate average score
average_score = round(sum(scores) / len(scores))

# Determine if skill level is beginner (0-90)
if (average_score >= 0) and (average_score <= 90):
    print(username, 'your average score of', average_score, 'indicates you are beginner!')
# Determine if skill level is intermediate (91-180)
elif (average_score >= 91) and (average_score <= 180):
    print(username, 'your average score of', average_score, 'indicates your skill level is intermediate!')
# Determine if skill level is advance (181 - 300)
elif (average_score >= 181) and (average_score <= 300):
    print(username, 'your average score of', average_score, 'indicates your skill level is advance!')
else:
    print('Invalid scores, try again.')
