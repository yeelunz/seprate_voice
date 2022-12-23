import os
from spleeter.separator import Separator

def separate_voice(input_file, output_file):
    # get input file path and output file path
    file_path = os.path.join(os.path.dirname(__file__))
    input_file_path = os.path.join(file_path, 'input',input_file)
    output_file_path = os.path.join(file_path, 'output',output_file.split('.')[0])

    # check if the file is already separated or not a wav file
    if output_file.split('.')[0] in output_filenames or not input_file_path.endswith('.wav')  :
        print(output_file_path, "Failed")
        return

    # separate the voice and compress it to 128k
    separator = Separator('spleeter:2stems',multiprocess=False)
    separator.separate_to_file(input_file_path,output_file_path,bitrate='128k',codec='mp3')

    # compress the output file
    # os.system('ffmpeg -i ' + output_file_path + '/vocals.wav -c:a libmp3lame -b:a 128k ' + output_file_path + '/vocals.mp3')


# get all file in input folder
filenames = os.listdir(os.path.join(os.path.dirname(__file__), 'input'))
# get file in output folder
output_filenames = os.listdir(os.path.join(os.path.dirname(__file__), 'output'))

for i,f in enumerate(filenames):
    print(i, '/', len(filenames))
    separate_voice(f, f)



