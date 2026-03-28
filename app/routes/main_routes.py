


from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required
from app import db
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.appointment import Appointment
from datetime import datetime
main = Blueprint('main', __name__)
# For home page
@main.route("/")
def home():
    return render_template("landing.html")

# View Patients Route
@main.route("/patients")
@login_required
def view_patients():
    patients = Patient.query.all()
    return render_template("patients.html", patients=patients)

# Add Patient Route
@main.route("/add-patient", methods=["GET", "POST"])
@login_required
def add_patient():
    if request.method == "POST":
        patient = Patient(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            date_of_birth=request.form["date_of_birth"],
            gender=request.form["gender"],
            phone=request.form["phone"],
            email=request.form["email"],
            address=request.form["address"],
            blood_type=request.form["blood_type"],
            allergies=request.form["allergies"],
            emergency_contact_name=request.form["emergency_contact_name"],
            emergency_contact_phone=request.form["emergency_contact_phone"],
            medical_notes=request.form["medical_notes"],
            status="active",
            doctor_id=request.form["doctor_id"]  # Assign doctor from form
        )
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for("main.view_patients"))
    
    doctors = Doctor.query.all()  # Fetch all doctors
    return render_template("add_patient.html", doctors=doctors)

# Add Doctor Route
@main.route("/add-doctor", methods=["GET", "POST"])
@login_required
def add_doctor():
    if request.method == "POST":
        doctor = Doctor(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            specialty=request.form["specialty"],
            phone=request.form["phone"],
            email=request.form["email"],
            address=request.form["address"],
            office_hours=request.form["office_hours"]
        )
        db.session.add(doctor)
        db.session.commit()
        return redirect(url_for("main.view_doctors"))
    return render_template("add_doctor.html")

# View Doctors Route
@main.route("/doctors")
@login_required
def view_doctors():
    doctors = Doctor.query.all()
    return render_template("doctors.html", doctors=doctors)

# View Appointments Route
@main.route("/appointments")
@login_required
def view_appointments():
    appointments = Appointment.query.all()
    return render_template("appointments.html", appointments=appointments)

# Add Appointment Route
@main.route("/add-appointment", methods=["GET", "POST"])
@login_required
def add_appointment():
    if request.method == "POST":
        appointment_date = datetime.strptime(
            request.form["appointment_date"],
            "%Y-%m-%dT%H:%M"
        )

        appointment = Appointment(
            patient_id=request.form["patient_id"],
            doctor_id=request.form["doctor_id"],
            appointment_date=appointment_date
        )
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for("main.view_appointments"))

    patients = Patient.query.all()
    doctors = Doctor.query.all()
    return render_template("add_appointment.html", patients=patients, doctors=doctors)
    
    patients = Patient.query.all()  # Get all patients
    doctors = Doctor.query.all()    # Get all doctors
    return render_template("add_appointment.html", patients=patients, doctors=doctors)