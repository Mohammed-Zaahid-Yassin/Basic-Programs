import random

# Dictionary of Indian states and their capitals
capitals = {
    'Andhra Pradesh': 'Amaravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata'
}

for quizNum in range(35):
    # Create quiz and answer key files
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # Write the quiz header
    quizFile.write('Name:\n\nDate:\n\nClass:\n\n')
    quizFile.write((' ' * 20) + f'Indian State Capitals Quiz (Form {quizNum + 1})\n\n')

    # Shuffle state order
    states = list(capitals.keys())
    random.shuffle(states)

    # Create 28 questions for each quiz
    for questionNum in range(28):
        state = states[questionNum]
        correctAnswer = capitals[state]
        wrongAnswers = list(capitals.values())
        wrongAnswers.remove(correctAnswer)
        wrongAnswers = random.sample(wrongAnswers, 3)
        options = wrongAnswers + [correctAnswer]
        random.shuffle(options)

        # Write the question
        quizFile.write(f'{questionNum + 1}. What is the capital of {state}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. {options[i]}\n")
        quizFile.write('\n')

        # Write the answer key
        correctOption = 'ABCD'[options.index(correctAnswer)]
        answerKeyFile.write(f'{questionNum + 1}. {correctOption}\n')

    # Close files
    quizFile.close()
    answerKeyFile.close()
