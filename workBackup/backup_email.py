import os
import datetime
import shutil
import subprocess
from subprocess import PIPE

today = datetime.date.today() 
todaystr = today.strftime("%Y%m%d")


def copy2_verbose(src, dst):
    print('Copying {0}'.format(src))
    shutil.copy2(src,dst)
       

if __name__ =='__main__':
    print("Starting backup process")
    print("Starting backup e-mail")

    #copy folder to backup
    mail_folder = 'D:\\Users\\derekwai\\thunderbird.mail'
    #work_folder = 'D:\\Users\\derekwai\\derek\\Winnington_Work'
    mail_target_folder = 'W:\\user.backup\\derekwai\\'+ todaystr + '\\thunderbird.mail\\'   
    #work_target_folder = 'W:\\user.backup\\derekwai\\'+ todaystr + '\\Winnington_Work\\' 
    try:
        shutil.copytree(mail_folder,mail_target_folder, copy_function=copy2_verbose)
    except (Error, OSError) as e:
        print ("Attempt to copy failed: %s" % e)
    print ("Finished backup E-mail")
    print ("Starting backup Derek's Work folder")

    #try:
    #   shutil.copytree(work_folder,work_target_folder, copy_function=copy2_verbose)
    #except (Error, OSError) as e:
    #    print ("Attempt to copy failed: %s" % e)
    
    #print("Finished backup Derek's Work folder")
    print("Backup Finished!!")


