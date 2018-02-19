import boto3
import json

from boto3 import  client
from io import StringIO
from playsound import playsound
from contextlib import closing

if __name__ == "__main__":

    def checkPicture(service,fileName,bucket,region):
        fileName=fileName
        bucket=bucket
        region = region
        client=boto3.client(service,region)

        response = client.detect_faces(
            Image={
                'S3Object': {
                    'Bucket':bucket,
                    'Name':fileName 
                }
            },
            Attributes=['ALL'])

        #print('Detected faces for ' + fileName)
        for faceDetail in response['FaceDetails']:
            Text = 'The detected face is between {0} and {1} years old'.format(str(faceDetail['AgeRange']['Low']), str(faceDetail['AgeRange']['High']))
            Text = Text + 'The person appears to be ' + str(faceDetail['Emotions'][0]['Type'])
            return Text 
            #print('The detected face is between {0} and {1} years old'.format(str(faceDetail['AgeRange']['Low']), str(faceDetail['AgeRange']['High'])))
            #print('The person appears to be ' + str(faceDetail['Emotions'][0]['Type']))
            #print('Here are the other attributes:')
            #print(json.dumps(faceDetail, indent=4, sort_keys=True))

polly = client("polly", "eu-west-1" )
response = polly.synthesize_speech(
    Text=checkPicture("rekognition","20180215_194003.jpg","s3-jm-photos","eu-west-1"),
    OutputFormat="mp3",
    VoiceId="Emma")

if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        data = stream.read()
        fo = open("c:\\temp\\pollytest.mp3", "wb")
        fo.write( data )
        fo.close()

playsound('c:\\temp\\pollytest.mp3')