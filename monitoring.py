import subprocess

import concurrent.futures

import time

from datetime import datetime

import csv



# read file host

with open('host.cfg') as file:
    
readFile = file.read().splitlines()



# fungsi check host

def check_host(ip):
    
status, result = subprocess.getstatusoutput("ping -c1 " + ip)
    
csvFile = open('output.csv', 'a')
    
csvWriter = csv.writer(csvFile, delimiter=";")
   
if (status == 0):
        
csvWriter.writerow([datetime.now(), ip, 'UP'])
        
return f"{datetime.now()} : Host {ip} is UP"
    
else:
       
csvWriter.writerow([datetime.now(), ip, 'DOWN'])
        
return f'{datetime.now()} : Host {ip} is DOWN'





while(True):
    
# waktu awal
    
T1 = time.perf_counter()

    
# proses multithreading
    
with concurrent.futures.ThreadPoolExecutor() as executor:
        
print("Mulai monitor......")
        
results = executor.map(check_host, readFile)
        
for result in results:
            
print(result)

    

# waktu akhir
    
T2 = time.perf_counter()

    

# cetak total waktu
    
print(f"selesai dalam : {round(T2 - T1, 2)} detik \n")

    

# waktu jeda
    
time.sleep(5)