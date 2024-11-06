# # import subprocess
# # from ibm_watson import SpeechToTextV1
# # from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



# # apikey = 'g0DqEZMpri1cvbksy-kirYcK2EM1I1CqPa3sspZB80OL'
# # url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/b45f69c1-732c-41d2-98bb-3987a66f4baa'

# # authenticator = IAMAuthenticator(apikey)
# # stt = SpeechToTextV1(authenticator=authenticator)
# # stt.set_service_url(url)


# # try:
# #     with open('audio.wav', 'rb') as f:
# #         res = stt.recognize(audio=f, content_type='audio/wav', model='en-AU_NarrowbandModel').get_result()
# #     print(res)

# # except Exception as e:
# #     print("An error occurred:", e)


# # from pydub import AudioSegment
# # from ibm_watson import SpeechToTextV1
# # from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# # # Load the large audio file
# # audio = AudioSegment.from_wav('audio.wav')

# # # Split the audio into 10-minute segments
# # segment_length = 10 * 60 * 1000  # 10 minutes in milliseconds
# # segment_files = []

# # for i in range(0, len(audio), segment_length):
# #     segment = audio[i:i + segment_length]
# #     segment_filename = f'segment_{i // segment_length}.wav'
# #     segment.export(segment_filename, format='wav')
# #     segment_files.append(segment_filename)

# # # IBM Watson Speech to Text setup
# # apikey = 'g0DqEZMpri1cvbksy-kirYcK2EM1I1CqPa3sspZB80OL'
# # url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/b45f69c1-732c-41d2-98bb-3987a66f4baa'

# # authenticator = IAMAuthenticator(apikey)
# # stt = SpeechToTextV1(authenticator=authenticator)
# # stt.set_service_url(url)

# # # Transcribe each segment and print the results
# # for segment_file in segment_files:
# #     try:
# #         with open(segment_file, 'rb') as f:
# #             res = stt.recognize(audio=f, content_type='audio/wav', model='en-AU_NarrowbandModel').get_result()
# #             print(f"Transcription for {segment_file}:")
# #             print(res)
# #             res['results']
# #             print(len(res['results']))
# #             text = [result['alternatives'][0]['transcript'].rstrip() + '.\n' for result in res['results']]
# #             text =[para[0].title() + para[1:] for para in text]
# #             transcript =''.join(text)
# #             with open ('output.txt','w') as out:
# #                 out.writelines(transcript)




        

# #     except Exception as e:
# #         print(f"An error occurred while transcribing {segment_file}: {e}")


# import subprocess
# from ibm_watson import SpeechToTextV1
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# # Load the large audio file (change the input file format if necessary)
# audio = AudioSegment.from_file('input.wmv', format='wmv')  # Specify the format if not .wav

# # Split the audio into 10-minute segments
# segment_length = 10 * 60 * 1000  # 10 minutes in milliseconds
# segment_files = []

# for i in range(0, len(audio), segment_length):
#     segment = audio[i:i + segment_length]
#     segment_filename = f'segment_{i // segment_length}.wav'
#     segment.export(segment_filename, format='wav')
#     segment_files.append(segment_filename)

# # IBM Watson Speech to Text setup
# apikey = 'g0DqEZMpri1cvbksy-kirYcK2EM1I1CqPa3sspZB80OL'
# url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/b45f69c1-732c-41d2-98bb-3987a66f4baa'

# authenticator = IAMAuthenticator(apikey)
# stt = SpeechToTextV1(authenticator=authenticator)
# stt.set_service_url(url)

# # Prepare to write the final transcript
# with open('output.txt', 'w') as out:
#     # Transcribe each segment and write the results
#     for segment_file in segment_files:
#         try:
#             with open(segment_file, 'rb') as f:
#                 res = stt.recognize(audio=f, content_type='audio/wav', model='en-AU_NarrowbandModel').get_result()
#                 print(f"Transcription for {segment_file}:")
                
#                 # Check if there are results
#                 if 'results' in res and res['results']:
#                     text = [result['alternatives'][0]['transcript'].rstrip() + '.\n' for result in res['results']]
#                     text = [para[0].title() + para[1:] for para in text]  # Capitalize the first letter of each sentence
#                     transcript = ''.join(text)

#                     # Write the transcript of the current segment to the output file
#                     out.write(transcript)
#                 else:
#                     print(f"No transcriptions found for {segment_file}.")

#         except Exception as e:
#             print(f"An error occurred while transcribing {segment_file}: {e}")

# # print("Transcription completed. Check 'output.txt' for results.")
import subprocess
from ibm_watson import SpeechToTextV1 # type: ignore
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator # type: ignore
from pydub import AudioSegment

# Load the audio file and specify format if not .wav
audio = AudioSegment.from_file('input.wav', format='wav')

# Split the audio into 10-minute segments
segment_length = 10 * 60 * 1000  # 10 minutes in milliseconds
segment_files = []

for i in range(0, len(audio), segment_length):
    segment = audio[i:i + segment_length]
    segment_filename = f'segment_{i // segment_length}.wav'
    segment.export(segment_filename, format='wav')
    segment_files.append(segment_filename)

# IBM Watson Speech to Text setup
apikey = 'g0DqEZMpri1cvbksy-kirYcK2EM1I1CqPa3sspZB80OL'
url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/b45f69c1-732c-41d2-98bb-3987a66f4baa'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

# Prepare the output file for the transcript
with open('output.txt', 'w') as out:
    for segment_file in segment_files:
        try:
            with open(segment_file, 'rb') as f:
                res = stt.recognize(audio=f, content_type='audio/wav', model='en-AU_NarrowbandModel').get_result()
                
                # Check if there are results and process them
                if 'results' in res and res['results']:
                    text = [result['alternatives'][0]['transcript'].strip() + '.\n' for result in res['results']]
                    text = [para.capitalize() for para in text]  # Capitalize first letter of each sentence
                    transcript = ''.join(text)
                    out.write(transcript)
                    print(f"Transcription for {segment_file} added.")
                else:
                    print(f"No transcription results for {segment_file}.")

        except Exception as e:
            print(f"An error occurred while transcribing {segment_file}: {e}")

print("Transcription completed. Check 'output.txt' for results.")



# from ibm_watson import SpeechToTextV1
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from pydub import AudioSegment

# # Load the audio file
# audio = AudioSegment.from_file('input.wav', format='wav')

# # Export the entire audio to WAV format for compatibility with IBM Watson
# audio.export('temp_audio.wav', format='wav')

# # IBM Watson Speech to Text setup
# apikey = 'g0DqEZMpri1cvbksy-kirYcK2EM1I1CqPa3sspZB80OL'
# url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/b45f69c1-732c-41d2-98bb-3987a66f4baa'

# authenticator = IAMAuthenticator(apikey)
# stt = SpeechToTextV1(authenticator=authenticator)
# stt.set_service_url(url)

# # Open the temporary WAV file and transcribe it at once
# try:
#     with open('temp_audio.wav', 'rb') as audio_file:
#         res = stt.recognize(audio=audio_file, content_type='audio/wav', model='en-AU_NarrowbandModel').get_result()

#         # Check if there are transcription results and process them
#         if 'results' in res and res['results']:
#             text = [result['alternatives'][0]['transcript'].strip() + '.\n' for result in res['results']]
#             text = [para.capitalize() for para in text]  # Capitalize first letter of each sentence
#             transcript = ''.join(text)

#             # Write the final transcript to the output file
#             with open('output.txt', 'w') as out:
#                 out.write(transcript)
#             print("Transcription completed successfully. Check 'output.txt' for results.")
#         else:
#             print("No transcription results found.")

# except Exception as e:
#     print(f"An error occurred during transcription: {e}")
