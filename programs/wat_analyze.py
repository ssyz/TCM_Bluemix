'''
This program utilizes some Watson services from IBM Bluemix:
(1) Natural Language Understanding
(2) Visual Recognition

Intended for educational purposes. Written by: Jay Syz
'''

# import necessary libraries
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features
import os.path
from os.path import join, dirname, isfile
from os import environ, listdir
from watson_developer_cloud import VisualRecognitionV3
import time
from os.path import basename

# initialize IBM Watson Natural Language Understanding
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='30591802-9044-40d8-9f35-1ad35d5be377',
    password='eo00agimrNqe')
# initialize IBM Watson Visual Recognition
visual_recognition = VisualRecognitionV3('2016-05-20', api_key='3698607dce8f1afbb97fba77e23ba33eab3ca2a8')

# path to list pictures
pic_path = '/home/jsyz/Desktop/TCM_IBM/images/'

# analyze text
def analyze_text():
    full_text = 'Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne.'
    response = natural_language_understanding.analyze(
        text = full_text,
        features=[features.Keywords()])

    # response is a dict
    keyWord_1 = response["keywords"][0]["text"]
    keyWeight_1 = response["keywords"][0]["relevance"]

    # return results
    return(full_text, keyWord_1, keyWeight_1)

# analyze picture
def analyze_pic(ch):
    # analyze faces in an image from file and get data about them
    nf = False
    with open(pic_path+ch, 'rb')\
            as image_file:
        pic_analysis = visual_recognition.detect_faces(images_file=image_file)
        pic_name = basename(pic_analysis["images"][0]["image"])

        # error handler for image with no face
        try:
            pic_id = pic_analysis["images"][0]["faces"][0]["identity"]["name"]
            pic_score = pic_analysis["images"][0]["faces"][0]["identity"]["score"]
        except:
            print "Oh no! No person found in this image..."
            nf = True
        if nf == True:
            pic_id = "[N/A]"
            pic_score = "[N/A]"

        # return findings
        return(pic_name, pic_id, pic_score)

# main method
def main():
    print "Hi! I'm Wat, I can help you understand text and pictures because I'm smarter than you"
    time.sleep(1)

    # main loop
    play = True
    while play == True:
        choice = raw_input("Do you need help with text or a picture?\n")

        # text analysis
        if 'text' in choice:
            # call Watson Natural Language Understanding
            print "\n---Start of text analysis---\n"
            (t, kW, kWe) = analyze_text()
            print "For this text:  " + t + "\n"
            print "The most relevant keyword is " + kW + ", with a relevance score of " + str(kWe)
            print "\n---End of text analysis---\n"

        # picture analysis
        elif 'pic' in choice:
            # print file options from the images directory
            onlyFiles = [f for f in listdir(pic_path) if isfile(join(pic_path, f))]
            print "\n"
            print onlyFiles
            print "\n"

            pic_c = raw_input("Which of these pictures would you like to analyze? (Please type the full filename)\n")
            print("\nYou chose to analyze " + pic_path + pic_c + "...\n")

            # error handler for invalid file name
            if os.path.isfile(pic_path + pic_c) == False:
                print("You have entered an invalid file name.")
                print("Now you get to start back from the beginning.\n")
                continue

            # call Watson Visual Recognition
            if play == True:
                print "\n---Start of picture analysis---\n"
                (p_n, p_id, p_s) = analyze_pic(pic_c)
                print "For this image:  " + p_n + "\n"
                print "The person is " + p_id + ", with a relevance score of " + str(p_s)
                print "\n---End of picture analysis---\n"

        # typing exit quits the program
        elif 'exit' in choice:
            print "\nBye!\n"
            play = False

        # for all other cases
        else:
            exit = raw_input("Sorry, I didn't understand your request, do you want to quit the program?\n")
            if 'yes' in exit:
                print "\nBye!\n"
                play = False
            else:
                continue

# call main method
if __name__ == '__main__':
    main()
