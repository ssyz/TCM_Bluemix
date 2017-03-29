# import necessary libraries
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

# te    st picture of a woman, accessed through a URL
test_url = 'https://www.ibm.com/ibm/ginni/images' \
           '/ginni_bio_780x981_v4_03162016.jpg'

# test picture of a fruit bowl
pic_fruit = '/home/jsyz/Desktop/TCM_IBM/images/fruitbowl.jpg'

# initialize IBM Watson Visual Recognition
visual_recognition = VisualRecognitionV3('2016-05-20', api_key='3698607dce8f1afbb97fba77e23ba33eab3ca2a8')

'''
Functions below get data from a URL
'''

# classifier for image from URL
print(json.dumps(visual_recognition.classify(images_url=test_url), indent=2))

# analyze faces in an image from URL and get data about them
print(json.dumps(visual_recognition.detect_faces(images_url=test_url), indent=2))


'''
Functions below get data from file
'''

# classifier for image from file using an id
with open(pic_fruit, 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(images_file=image_file), indent=2))

# ???
with open(pic_fruit, 'rb')\
        as image_file:
    print(json.dumps(visual_recognition.recognize_text(images_file=image_file), indent=2))

# analyze faces in an image from file and get data about them
with open(pic_fruit, 'rb')\
        as image_file:
    print(json.dumps(visual_recognition.detect_faces(images_file=image_file), indent=2))
