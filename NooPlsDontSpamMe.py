## This is the main file, run the script from here

import message
import time
import spam_utils

## Decide how many messages to send. 
## Set it to True if you don't want to have a limit: the program will run until stopped manually. I
# #t is recommended to enter a cooldown value
how_much= True
## Decide how many seconds to wait before sending a new message. If how_much is True it is recommended to set 
## a cooldown to prevent spam detecting from Google forms
cooldown= 0

i=1
while spam_utils.i_feel_like_continuing_spam(i, how_much):
    status= message.message()
    
    if status == 200:
        print('Request', i, 'sent successfully!')
    else:
        print('Request error', i ,':', status)
    
    i= i+1
    
    time.sleep(cooldown)

print('End')