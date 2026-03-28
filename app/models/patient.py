from app import db

class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    address = db.Column(db.String(200))
    blood_type = db.Column(db.String(20))
    allergies = db.Column(db.String(200))
    emergency_contact_name = db.Column(db.String(100))
    emergency_contact_phone = db.Column(db.String(20))
    medical_notes = db.Column(db.String(200))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=True)
    status = db.Column(db.String(20), default="active")

    doctor = db.relationship('Doctor', backref=db.backref('patients', lazy=True))

    def __repr__(self):
        return f"<Patient {self.first_name} {self.last_name}>"