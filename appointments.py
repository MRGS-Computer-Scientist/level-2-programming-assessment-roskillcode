class AppointmentScheduling:
    def __init__(self):
        #Initialize the AppointmentScheduling class with an empty list of appointments.
        self.appointments = []

    def schedule_appointment(self, student, faculty, datetime):
        #Add a new appointment to the list and print a confirmation message.
        self.appointments.append({"student": student, "faculty": faculty, "datetime": datetime})
        print(f"Appointment scheduled between {student} and {faculty} at {datetime}")

    def get_appointments(self, user):
        #Return a list of appointments for a specific user (as a student or faculty).
        return [appt for appt in self.appointments if appt["student"] == user or appt["faculty"] == user]
