from Patient import *


class Doctor:
    def __init__(self, time):
        self.time_remaining = 0
        self.current_with_doc = None
        self.rateoftimepatinetwithdoc = time   #10 or 5 -> Age /rateoftimepatinetwithdoc

    def tick(self):
        if self.current_with_doc is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining == 0:
                self.current_with_doc = None


    def busy(self):
        return self.current_with_doc is not None




    def Nextpatient(self, new_patient):
        self.current_with_doc = new_patient
        self.time_remaining = round(new_patient.getage() / self.rateoftimepatinetwithdoc)*60