import cv2

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from tensorflow import convert_to_tensor as convert


from keras.models import load_model

import numpy as np
import random
import time

model = load_model('keras_model.h5',compile = False)



class rps():
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

        self.user_choice = -2
        self.computer_choice = -2

            
    def get_choices(self):

        self.computer_choice = random.choice(range(0,3))
      
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

        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        data_tf = convert(data,np.float32)
        prediction = model.predict(data_tf)
        #cv2.imshow('frame', frame)

        self.user_choice = prediction.argmax()
        
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    def get_result(self):


        if self.user_choice == 3:
            print("\nYou didn't show anything!" )
            return
        
        else:
            choices = ['Rock','Paper','Scissors']
            print(f'\nYou chose: {choices[self.user_choice]}')
            print(f'\nThe computer chose: {choices[self.computer_choice]}')

            res = (self.user_choice - self.computer_choice)%3
            
            if res == 1:
                print('\nYou get a point!')
                self.user_score += 1
            elif res == 0:
                print('\nIt is a tie')
            elif res == 2:
                print('\nThe computer got a point!')
                self.computer_score += 1
            
            print('\nThe score is:')
            print(f'\n   Player {self.user_score} : {self.computer_score} Computer')

            
            

            
def play():

    game = rps()

    while True:

        game.get_choices()
        
        game.get_result()
       
        if game.user_score == 3:
            print('\nCongratulations, you won!')
            break
        
        elif game.computer_score == 3:
            print('\nSorry, the computer wins.')
            break

        go = input('\nDo you want to continue? (y/n):  ')

        if go == 'n':
            return

play()


