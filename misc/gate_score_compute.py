total_score = 0

print("::General Aptitude::")
for q in range(10):
    response = input(f'Is the answers same? {q+1} :: ')
    # my_response = input(f'Enter your response for question {q+1} :: ')
    # correct_response = input(f'Enter correct response for question {q+1} :: ')
    # if my_response == correct_response:
    if response == 'y':
        if q < 5:
            total_score += 1
        else:
            total_score += 2
    elif response == 'n':
        if q < 5:
            total_score -= 0.33
        else:
            total_score -= 0.66

print(f'Score for GA: {total_score}')

print("::CS::")
for q in range(55):
    response = input(f'Is the answers same? {q+1} :: ')
#     my_response = input(f'Enter your response for question {q+1} :: ')
#     correct_response = input(f'Enter correct response for question {q+1} :: ')
#     if my_response == correct_response:
    if response == 'y':
        if q < 25:
            total_score += 1
        else:
            total_score += 2
    elif response == 'n':
        if q < 25:
            total_score -= 0.33
        else:
            total_score -= 0.66

print(f'Final score: {total_score}')

# ::General Aptitude::
# Is the answers same? 1 :: y
# Is the answers same? 2 :: y
# Is the answers same? 3 :: y
# Is the answers same? 4 :: y
# Is the answers same? 5 :: y
# Is the answers same? 6 :: n
# Is the answers same? 7 :: y
# Is the answers same? 8 :: y
# Is the answers same? 9 :: n
# Is the answers same? 10 :: y
# Score for GA: 9.68
# ::CS::
# Is the answers same? 1 :: y
# Is the answers same? 2 :: y
# Is the answers same? 3 :: y
# Is the answers same? 4 :: t
# Is the answers same? 5 :: t
# Is the answers same? 6 :: y
# Is the answers same? 7 :: t
# Is the answers same? 8 :: t
# Is the answers same? 9 :: t
# Is the answers same? 10 :: y
# Is the answers same? 11 :: t
# Is the answers same? 12 :: y
# Is the answers same? 13 :: t
# Is the answers same? 14 :: t
# Is the answers same? 15 :: t
# Is the answers same? 16 :: t
# Is the answers same? 17 :: y
# Is the answers same? 18 :: t
# Is the answers same? 19 :: t
# Is the answers same? 20 :: y
# Is the answers same? 21 :: y
# Is the answers same? 22 :: n
# Is the answers same? 23 :: t
# Is the answers same? 24 :: t
# Is the answers same? 25 :: t
# Is the answers same? 26 :: t
# Is the answers same? 27 :: t
# Is the answers same? 28 :: t
# Is the answers same? 29 :: t
# Is the answers same? 30 :: t
# Is the answers same? 31 :: t
# Is the answers same? 32 :: t
# Is the answers same? 33 :: t
# Is the answers same? 34 :: t
# Is the answers same? 35 :: t
# Is the answers same? 36 :: t
# Is the answers same? 37 :: y
# Is the answers same? 38 :: t
# Is the answers same? 39 :: t
# Is the answers same? 40 :: t
# Is the answers same? 41 :: t
# Is the answers same? 42 :: t
# Is the answers same? 43 :: n
# Is the answers same? 44 :: t
# Is the answers same? 45 :: n
# Is the answers same? 46 :: n
# Is the answers same? 47 :: t
# Is the answers same? 48 :: y
# Is the answers same? 49 :: y
# Is the answers same? 50 :: t
# Is the answers same? 51 :: t
# Is the answers same? 52 :: t
# Is the answers same? 53 :: y
# Is the answers same? 54 :: t
# Is the answers same? 55 :: t
# Final score: 24.37