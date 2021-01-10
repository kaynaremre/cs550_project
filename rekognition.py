#!/usr/bin/env python3

import boto3
import sys

def detect_labels_local_file(photo):

    client=boto3.client('rekognition')

    with open(photo, 'rb+') as image:
        response = client.detect_protective_equipment(Image={'Bytes': image.read()},
            SummarizationAttributes={'MinConfidence':80, 'RequiredEquipmentTypes':['FACE_COVER']})

    #print('Person ID Summary\n----------------')
    #display_summary('With required equipment',response['Summary']['PersonsWithRequiredEquipment'] )
    display_summary('Without required equipment',response['Summary']['PersonsWithoutRequiredEquipment'], response['Persons'])
    #display_summary('Indeterminate',response['Summary']['PersonsIndeterminate'] )
    #print(response['Summary'])
    #print(response)
    #for person in response['Persons']:
    #    print(person)
    return (len(response['Persons']))

#Display summary information for supplied summary.
def display_summary(summary_type, summary, resp):
    #print (summary_type + '\n\tIDs: ',end='')
    if (len(summary)==0):
        print('No person identificated without face mask')
    else:
        #print('There are',len(summary),'people without mask !')
        
        for i in summary:
            print(resp[i]['BoundingBox'])

def main():

    photo = sys.argv[1]
    detect_labels_local_file(photo)

if __name__ == "__main__":
    main()
    