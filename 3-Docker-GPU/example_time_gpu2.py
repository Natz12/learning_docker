from datetime import datetime
import time
import pandas # We dont use this library in the code but we still import it to check the env is correct
import torch

text_path = "time_running.txt"
for i in range(5):
    now = datetime.now()
    print(now, " yay")
    with open(text_path, "a") as text_file:
        text_file.write(str(now)+'\n')
        text_file.write(str(torch.cuda.device_count())+str(torch.device('cuda' if torch.cuda.is_available() else 'cpu')))
    time.sleep(5)
    
print('END')
