class AppointmentScheduling:
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, student, faculty, datetime):
        self.appointments.append({"student": student, "faculty": faculty, "datetime": datetime})
        print(f"Appointment scheduled between {student} and {faculty} at {datetime}")

    def get_appointments(self, user):
        return [appt for appt in self.appointments if appt["student"] == user or appt["faculty"] == user]
