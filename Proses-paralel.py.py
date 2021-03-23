import platform as p
import subprocess as sub
import time
import multiprocessing

time1 = time.perf_counter()

def checkping(host):
    systemOs = '-n' if p.system().lower() == 'windows' else '-c'
    pinging = ['ping', systemOs, '1', host]
    status = ''
    time.sleep(1)

    if sub.call(pinging) == 0:
        status = 'UP'
    else:
        status = 'DOWN'

    output = '\nHost {} is {}'.format(host, status)

    print(output)

hosts = ['192.168.1.1','192.168.1.2','192.168.1.3','8.8.8.8','8.8.4.4']
hosts2 = []

for i in hosts:
    P = multiprocessing.Process(target=checkping, args=[i])
    P.start()
    hosts2.append(P)

for j in hosts2:
    j.join()

time2 = time.perf_counter()

print('')

print('Selesai dalam waktu {} detik'.format(time2-time1,2))

