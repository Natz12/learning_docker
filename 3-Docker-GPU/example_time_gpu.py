from datetime import datetime
import time
import pandas # We dont use this library in the code but we still import it to check the env is correct
import torch

for i in range(5):
    print(datetime.now())
    
    print(torch.cuda.device_count(), torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    time.sleep(5)
print('end')
