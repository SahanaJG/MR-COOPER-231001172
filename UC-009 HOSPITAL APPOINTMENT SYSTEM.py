from datetime import datetime

# DOCTOR CLASS
class Doctor:
    MAX_APPOINTMENTS= 20
    def __init__(self, doctorId, name, speciality):
        self.doctorId= doctorId
        self.name= name
        self.speciality= speciality
        self.schedule= []
        self.availableSlot= []
        self.is_available= True


    def __str__(self):
        status= "Available" if self.is_available else "Busy"
        return f"{self.doctorId} | Dr.{self.name} | {self.speciality} | {status}"

# PATIENT CLASS
class Patient:
    def __init__(self, patientId, name,age,phone):
        self.patientId= patientId
        self.name= name
        self.age= age
        self.phone= phone
        self.medicalHistory= []
        self.appointments= []

    def bookAppointment(self, doctor):
        if not doctor.is_available:
            print("Doctor not available")
            return

        doctor.is_available = False
        self.appointments.append(doctor)
        print(f"{self.name} booked appointment with Dr.{doctor.name}")


    def cancelAppointment(self, doctor):
        if doctor in self.appointments:
            doctor.is_available = True
            self.appointments.remove(doctor)
            print(f"Appointment cancelled with Dr.{doctor.name}")
        else:
            print("No such appointment found")    

class Admin:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name
    # def add_slot(self, hospital,doctor,slot):

    # DOCTOR MANAGEMENT
    def add_doctor(self, hospital, doctor):
        hospital.add_doctor(doctor)

    def update_doctor(self, hospital, doctorId, name=None, speciality=None):
        hospital.update_doctor(doctorId, name, speciality)

    def remove_doctor(self, hospital, doctorId):
        hospital.remove_doctor(doctorId)

    def view_doctors(self, hospital):
        hospital.display_doctors()

    # PATIENT MANAGEMENT
    def add_patient(self, hospital, patient):
        hospital.register_patient(patient)

    def update_patient(self, hospital, patient_id, name=None):
        hospital.update_patient(patient_id, name)

    def remove_patient(self, hospital, patient_id):
        hospital.remove_patient(patient_id)

    def view_patients(self, hospital):
        hospital.display_patients()


# APPOINTMENT CLASS
class Appointment:
    def __init__(self, appointmentId, patientId, doctorId, date, slot, status,notes):
        self.appointmentId= appointmentId
        self.patientId= patientId
        self.doctorId= doctorId
        self.date= date
        self.slot= slot
        self.status= status
        self.notes= notes
    def confirm(self, appointmentId, patientId, doctorId):
        if patientId in self.patients and doctorId in self.doctors:
            patient = self.patients[patientId]
            doctor = self.doctors[doctorId]
            patient.confirm(doctor)
        else:
            print("Invalid patient or doctor ID")


# HOSPITAL CLASS 
class Hospital:
    def __init__(self):
        self.doctors = {}
        self.patients = {}

    # DOCTOR FUNCTIONS 
    def add_doctor(self, doctor):
        if doctor.doctorId in self.doctors:
            print("Doctor ID already exists")
        else:
            self.doctors[doctor.doctorId] = doctor
            print("Doctor added")

    def update_doctor(self, doctorId, name=None, specialty=None):
        if doctorId in self.doctors:
            d = self.doctors[doctorId]
            if name:
                d.name = name
            if specialty:
                d.specialty = specialty
            print("Doctor updated")
        else:
            print("Doctor not found")

    def remove_doctor(self, doctorId):
        if doctorId in self.doctors:
            del self.doctors[doctorId]
            print("Doctor removed")
        else:
            print("Doctor not found")

    # PATIENT FUNCTIONS 
    def register_patient(self, patient):
        if patient.patientId in self.patients:
            print("Patient ID exists")
        else:
            self.patients[patient.patientId] = patient
            print("Patient registered")

    def update_patient(self, patientId, name=None):
        if patientId in self.patients:
            if name:
                self.patients[patientId].name = name
            print("Patient updated")
        else:
            print("Patient not found")

    def remove_patient(self, patientId):
        if patientId in self.patients:
            del self.patients[patientId]
            print("Patient removed")
        else:
            print("Patient not found")

    # APPOINTMENT FUNCTIONS 
    def bookAppointment(self, patientId, doctorId):
        if patientId in self.patients and doctorId in self.doctors:
            patient = self.patients[patientId]
            doctor = self.doctors[doctorId]
            patient.bookAppointment(doctor)
        else:
            print("Invalid patient or doctor ID")

    def cancelAppointmentointment(self, patientId, doctorId):
        if patientId in self.patients and doctorId in self.doctors:
            patient = self.patients[patientId]
            doctor = self.doctors[doctorId]
            patient.cancelAppointmentointment(doctor)
        else:
            print("Invalid IDs")

    # SEARCH 
    def search_doctors(self, keyword):
        keyword = keyword.lower()
        results = []

        for d in self.doctors.values():
            if keyword in d.name.lower() or keyword in d.specialty.lower():
                results.append(d)

        if results:
            print("\nDoctors Found:")
            for d in results:
                print(d)
        else:
            print("No doctors found")

    # DISPLAY 
    def display_doctors(self):
        print("\nDoctors List:")
        for d in self.doctors.values():
            print(d)

    def display_patients(self):
        print("\nPatients List:")
        for p in self.patients.values():
            print(f"{p.patientId} | {p.name} | Appointments: {len(p.appointments)}")


# CONSULTATION CLASS
class Consultation:
    def __init__(self, consultationId, appointmentId, notes, prescription, date):
        self.consultationId= consultationId
        self.appointmentId= appointmentId
        self.notes= notes
        self.prescription= prescription
        self.date= date

# SLOT CLASS
class Slot:
    def __init__(self, startTime, endTime,doctorId):
        self.startTime= startTime
        self.endTime= endTime
        self.isBooked= False


    

# ---------------- MAIN ----------------
def main():
    hospital = Hospital()
    admin = Admin(1, "Admin")

    while True:
        print("\n===== HOSPITAL SYSTEM =====")
        print("1. Admin")
        print("2. Patient")
        print("3. Exit")

        choice = input("Enter choice: ")

        # -------- ADMIN MENU --------
        if choice == "1":
            while True:
                print("\n--- ADMIN MENU ---")
                print("1. Add Doctor")
                print("2. Update Doctor")
                print("3. Remove Doctor")
                print("4. View Doctors")
                print("5. Add Patient")
                print("6. Update Patient")
                print("7. Remove Patient")
                print("8. View Patients")
                print("9. Back")

                ch = input("Enter choice: ")

                if ch == "1":
                    did = int(input("Doctor ID: "))
                    name = input("Name: ")
                    spec = input("speciality: ")
                    admin.add_doctor(hospital, Doctor(did, name, spec))

                elif ch == "2":
                    did = int(input("Doctor ID: "))
                    name = input("New Name: ")
                    spec = input("New speciality: ")
                    admin.update_doctor(hospital, did, name, spec)

                elif ch == "3":
                    did = int(input("Doctor ID: "))
                    admin.remove_doctor(hospital, did)

                elif ch == "4":
                    admin.view_doctors(hospital)

                elif ch == "5":
                    pid = int(input("Patient ID: "))
                    name = input("Name: ")
                    admin.add_patient(hospital, Patient(pid, name))

                elif ch == "6":
                    pid = int(input("Patient ID: "))
                    name = input("New Name: ")
                    admin.update_patient(hospital, pid, name)

                elif ch == "7":
                    pid = int(input("Patient ID: "))
                    admin.remove_patient(hospital, pid)

                elif ch == "8":
                    admin.view_patients(hospital)

                elif ch == "9":
                    break

                else:
                    print("Invalid choice")

        # -------- PATIENT MENU --------
        elif choice == "2":
            while True:
                print("\n--- PATIENT MENU ---")
                print("1. Register")
                print("2. Book Appointment")
                print("3. Cancel Appointment")
                print("4. Search Doctor")
                print("5. View Doctors")
                print("6. Back")

                ch = input("Enter choice: ")

                if ch == "1":
                    pid = int(input("Patient ID: "))
                    name = input("Name: ")
                    age=int(input("Patient Age:"))
                    phone=input("Phone: ")
                    hospital.register_patient(Patient(pid, name, age, phone))

                elif ch == "2":
                    pid = int(input("Patient ID: "))
                    did = int(input("Doctor ID: "))
                    hospital.bookAppointment(pid, did)

                elif ch == "3":
                    pid = int(input("Patient ID: "))
                    did = int(input("Doctor ID: "))
                    hospital.cancelAppointmentointment(pid, did)

                elif ch == "4":
                    keyword = input("Enter keyword: ")
                    hospital.search_doctors(keyword)

                elif ch == "5":
                    hospital.display_doctors()

                elif ch == "6":
                    break

                else:
                    print("Invalid choice")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()