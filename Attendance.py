x=input('Input did you have any medical issues in your football season resulting with you not playing. Please answer yes or no.\n')
if x=='yes':
    print('You are still okay to be on the team because a medical issue is unpredictable.')
elif x=='no':
    y=int(input('What is your number of attendences out of 20 matches?\n'))
    if y>17:
        print('You have played for the team for enough matches and you are stil okay to stay on the team.')
    else:
        print('Sorry, you are not there for the team and we no longer need you.')
else:
    print('Invalid Input')