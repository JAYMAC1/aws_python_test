import boto3
from boto3 import  client
from io import StringIO
from playsound import playsound
from contextlib import closing

polly = client("polly", 'eu-west-1' )
response = polly.synthesize_speech(
    Text="Good Morning. My Name is James. I am Testing Polly AWS Service For Voice Application.",
    OutputFormat="mp3",
    VoiceId="Raveena")

print(response)

if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        data = stream.read()
        fo = open("c:\\temp\\pollytest.mp3", "wb")
        fo.write( data )
        fo.close()

playsound('c:\\temp\\pollytest.mp3')
