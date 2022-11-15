import cv2
import sys

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from tensorflow import convert_to_tensor as convert


from keras.models import load_model

import numpy as np
import random
import time

model = load_model('keras_model.h5',compile = False)

cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

class rps():
    def __init__(self, play_to = 3):
        self.user_score = 0
        self.computer_score = 0

        self.user_choice = -2
        self.computer_choice = -2

        self.prev_winner = 3

        self.play_to = play_to


            
    def get_choices(self):


        self.computer_choice = random.choice(range(0,3))
      

        tic = time.time()
            
        while True:
            ret, frame = cap.read()
            frame_border = cv2.copyMakeBorder(src =frame,top = 150,bottom = 0,left = 0,right = 0,borderType = cv2.BORDER_CONSTANT)
            cv2.putText(frame_border,'Player',(100,40),font,1,(255,255,255),2,2)
            cv2.putText(frame_border,f'{self.user_score}',(280,40),font,1,(255,255,255),2,2)

            cv2.putText(frame_border,f': {self.computer_score}',(318,40),font,1,(255,255,255),2,2)
            cv2.putText(frame_border,'Computer',(440,40),font,1,(255,255,255),2,2)

            toc = time.time() - tic
            if 0 < toc < 1:
                cv2.putText(frame_border,'3',(292,130),font,3,(255,255,255),5,2)
            elif 1 <= toc < 2:
                cv2.putText(frame_border,'2',(292,130),font,3,(255,255,255),5,2)
            elif 2 <= toc < 3:
                cv2.putText(frame_border,'1',(292,130),font,3,(255,255,255),5,2)
            elif 3.5 < toc:
                cv2.imshow('frame', frame_border)
                cv2.waitKey(1)
                break

            cv2.imshow('frame', frame_border)
            cv2.waitKey(1)
    
        
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        ret, frame = cap.read()

        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
        data[0] = normalized_image
        data_tf = convert(data,np.float32)
        prediction = model.predict(data_tf)
        

        self.user_choice = prediction.argmax()
    
        
        
        

    def get_result(self):
        
        if self.user_choice == 3:
            self.prev_winner = 2
            
        else:
            
            res = (self.user_choice - self.computer_choice)%3
            
            if res == 1:
                self.user_score += 1
                self.prev_winner = 1
            elif res == 0:
                self.prev_winner = 0
            elif res == 2:
                self.computer_score += 1
                self.prev_winner = -1

        

    def show_result(self):

        choices = ['Rock','Paper','Scissors']
        colours = ((255,255,255),(0,255,0),(0,0,255))
        #answers = (('It is a tie'),('You get a point!'),("You didn't show anything!"),('The computer got a point'))
        #answers_pos = ((260,130),(230,130),(180,130),(150,130))


        if self.prev_winner == 3:
            while True:
        
                ret, frame = cap.read()

                frame_border = cv2.copyMakeBorder(src =frame,top = 150,bottom = 0,left = 0,right = 0,borderType = cv2.BORDER_CONSTANT)
                cv2.putText(frame_border,'Player',(100,40),font,1,(255,255,255),2,2)
                cv2.putText(frame_border,f'{self.user_score}',(280,40),font,1,(255,255,255),2,2)

                cv2.putText(frame_border,f': {self.computer_score}',(318,40),font,1,(255,255,255),2,2)
                cv2.putText(frame_border,'Computer',(440,40),font,1,(255,255,255),2,2)
               
                cv2.putText(frame_border,"Press c to start the game, or q to quit.",(100,130),font,0.75,(255,255,255),2,2)

                cv2.imshow('frame', frame_border)

                k = cv2.waitKey(1) & 0xFF

                if k == ord('c'):
                    self.user_score = 0
                    self.computer_score = 0
                    break
                
                elif k == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    sys.exit()

        elif self.user_score == self.play_to:

            while True:
        
                ret, frame = cap.read()

                frame_border = cv2.copyMakeBorder(src =frame,top = 150,bottom = 0,left = 0,right = 0,borderType = cv2.BORDER_CONSTANT)
                cv2.putText(frame_border,'Player',(100,40),font,1,(255,255,255),2,2)
                cv2.putText(frame_border,f'{self.user_score}',(280,40),font,1,(255,255,255),2,2)

                cv2.putText(frame_border,f': {self.computer_score}',(318,40),font,1,(255,255,255),2,2)
                cv2.putText(frame_border,'Computer',(440,40),font,1,(255,255,255),2,2)


                cv2.putText(frame_border,"Congratulations, you won!",(170,90),font,0.75,(255,255,255),2,2)
  
                
                cv2.putText(frame_border,"Press c to play again, or q to quit.",(120,130),font,0.75,(255,255,255),1,2)

                cv2.imshow('frame', frame_border)

                k = cv2.waitKey(1) & 0xFF

                if k == ord('c'):
                    self.user_score = 0
                    self.computer_score = 0
                    break
                
                elif k == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    sys.exit()
                
        
        elif self.computer_score == self.play_to:
            while True:
        
                ret, frame = cap.read()

                frame_border = cv2.copyMakeBorder(src =frame,top = 150,bottom = 0,left = 0,right = 0,borderType = cv2.BORDER_CONSTANT)
                cv2.putText(frame_border,'Player',(100,40),font,1,(255,255,255),2,2)
                cv2.putText(frame_border,f'{self.user_score}',(280,40),font,1,(255,255,255),2,2)

                cv2.putText(frame_border,f': {self.computer_score}',(318,40),font,1,(255,255,255),2,2)
                cv2.putText(frame_border,'Computer',(440,40),font,1,(255,255,255),2,2)


                cv2.putText(frame_border,"Sorry, the computer won",(190,90),font,0.75,(255,255,255),2,2)
  
                
                cv2.putText(frame_border,"Press c to play again, or q to quit.",(120,130),font,0.75,(255,255,255),1,2)

                cv2.imshow('frame', frame_border)

                k = cv2.waitKey(1) & 0xFF

                if k == ord('c'):
                    self.user_score = 0
                    self.computer_score = 0
                    break
                
                elif k == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    sys.exit()

        else:
            while True:
        
                ret, frame = cap.read()

                frame_border = cv2.copyMakeBorder(src =frame,top = 150,bottom = 0,left = 0,right = 0,borderType = cv2.BORDER_CONSTANT)
                cv2.putText(frame_border,'Player',(100,40),font,1,(255,255,255),2,2)
                cv2.putText(frame_border,f'{self.user_score}',(280,40),font,1,(255,255,255),2,2)

                cv2.putText(frame_border,f': {self.computer_score}',(318,40),font,1,(255,255,255),2,2)
                cv2.putText(frame_border,'Computer',(440,40),font,1,(255,255,255),2,2)

                if self.prev_winner != 2:
                    cv2.putText(frame_border,f'{choices[self.user_choice]}',(100,90),font,0.75,colours[self.prev_winner],1,2)
                    cv2.putText(frame_border,f'{choices[self.computer_choice]}',(440,90),font,0.75,colours[-self.prev_winner],1,2)
                else:
                    cv2.putText(frame_border,"You didn't show anything!",(180,90),font,0.75,(255,255,255),2,2)
                #cv2.putText(frame_border,answers[self.prev_winner],answers_pos[self.prev_winner],font,0.75,(255,255,255),2,2)
                
                cv2.putText(frame_border,"Press c to continue, or q to quit.",(130,130),font,0.75,(255,255,255),1,2)

                cv2.imshow('frame', frame_border)

                k = cv2.waitKey(1) & 0xFF

                if k == ord('c'):
                    break
                
                elif k == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    sys.exit()

            
            

            
def play(play_to):

    game = rps(play_to)

    while True:

        game.show_result()

        game.get_choices()
        
        game.get_result()
       
        


    
play(2)

cap.release()
# Destroy all the windows
cv2.destroyAllWindows()