# import necessary libraries
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

# initialize IBM Watson Natural Language Understanding
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='30591802-9044-40d8-9f35-1ad35d5be377',
    password='eo00agimrNqe')

# analyze text
response = natural_language_understanding.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
         'Superman fears not Banner, but Wayne.',
    features=[features.Entities(), features.Keywords()])

# print results
print(json.dumps(response["keywords"][0]["text"], indent=2))
