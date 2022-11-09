import cv2
from keras.models import load_model
import numpy as np
import random
#import tensorflow as tf


def get_computer_choice():
    computer_choice = random.choice(range(0,3))
    return computer_choice

def get_user_choice():

    #config = tf.ConfigProto()
    #config.gpu_options.allow_growth = True
    #session = tf.Session(config=config)

    model = load_model('keras_model.h5',compile = False)
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    #cv2.imshow('frame', frame)

    choice = prediction.argmax()
    
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return choice

def get_winner(computer_choice,user_choice):
    print(user_choice,computer_choice)
    res = (user_choice - computer_choice)%3
    if res == 1:
        print('You won!')
    elif res == 0:
        print('It is a tie')
    elif res == 2:
        print('You lost')

            
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice,user_choice)

play()


