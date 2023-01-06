from Queue import Queue
from Doctor import *
from Patient import *
import random


def simulation(total_time, rate_time_patient):
    total_time *= 3600
    patinet_Queue = Queue()
    waiting_time = []
    clinic_DOC = Doctor(rate_time_patient)
    new_patient = Patient(rate_time_patient)

    for currentSecond in range(total_time):
        if random.randrange(1, 361) == 360:
            new_patient = Patient(currentSecond)
            patinet_Queue.enqueue(new_patient)

        if (not clinic_DOC.busy()) and (not patinet_Queue.isEmpty()):
            next_Patient = patinet_Queue.dequeue()
            clinic_DOC.Nextpatient(next_Patient)

            waiting_time.append(next_Patient.wait_time(currentSecond))

        clinic_DOC.tick()
    averageWaitTime = sum(waiting_time)/len(waiting_time)/60
    print("Average Waiting Time : ", " {:.2f}".format(averageWaitTime), "mins \t , unrated Patient :", patinet_Queue.Size())


for i in range(10):
    simulation(4, 5)

print("="*100)

for i in range(10):
    simulation(4, 10)







