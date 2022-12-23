"""extract the vocal.wav from the output file path and rename it to the filename.wav and move it to the database file path"""

import os
import shutil


# get database file path
file_path = os.path.join(os.path.dirname(__file__),'output')

# get all file name in output file path
filenames = os.listdir(file_path)

# look through all file name in output file path
output_filepath = os.path.join(os.path.dirname(__file__),'database')

cnt = 0

# look all file name in output file path
for f in filenames:
    cnt+=1
    # get the vocal.wav in output file path
    tar =  os.path.join(file_path,f,f,'vocals.wav')
    # rename tar to filename.wav
    if os.path.exists(tar) :
        new_tar = os.path.join(file_path,f,f,f+'.wav')
        if len(new_tar) > 255:
            print('File name too long: ',f)
            continue
        os.rename(tar,new_tar)

        # if not exist in database file path
        if not os.path.exists(os.path.join(output_filepath,f+'.wav')):
            # move filename.wav to database file path
            shutil.move(new_tar,output_filepath)
    