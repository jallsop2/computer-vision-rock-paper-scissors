import cv2

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from tensorflow import convert_to_tensor as convert


from keras.models import load_model

import numpy as np
import random
import time

model = load_model('keras_model.h5',compile = False)



def get_computer_choice():
    computer_choice = random.choice(range(0,3))
    return computer_choice

def get_user_choice():


    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    tic = time.time()
    print('\n3')
        
    while True:
        toc = time.time()
        if toc - tic >= 1:
            print('\n2')
            break
    while True:
        toc = time.time()
        if toc - tic >= 2:
            print('\n1\n\n')
            break
    while True:
        toc = time.time()
        if toc - tic >= 3:
            break

    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    data_tf = convert(data,np.float32)
    prediction = model.predict(data_tf)
    #cv2.imshow('frame', frame)

    choice = prediction.argmax()
    
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return choice

def get_winner(computer_choice,user_choice):


    if user_choice == 3:
        print("You didn't show anything!" )
        return -1
    
    else:
        choices = ['Rock','Paper','Scissors']
        print(f'\nYou chose: {choices[user_choice]}')
        print(f'\nThe computer chose: {choices[computer_choice]}')

        res = (user_choice - computer_choice)%3
        return res
    

            
def play():

    user_score = 0
    computer_score = 0

    while True:

        print('\n The score is:')
        print(f'\n Player {user_score} : {computer_score} Computer')


        computer_choice = get_computer_choice()

        user_choice = get_user_choice()
        
        res = get_winner(computer_choice,user_choice)

        if res == 1:
            print('\nYou get a point!')
            user_score += 1
        elif res == 0:
            print('\nIt is a tie')
        elif res == 2:
            print('\nThe computer got a point!')
            computer_score += 1
        
        if user_score == 3:
            print('\nCongratulations, you won!')
            break
        
        elif computer_score == 3:
            print('\nSorry, the computer wins.')
            break
        

play()


