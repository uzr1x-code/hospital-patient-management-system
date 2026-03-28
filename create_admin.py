from app import create_app, db
from app.models.user import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    admin_exists = User.query.filter_by(username="admin").first()
    if not admin_exists:
        hashed_password = generate_password_hash("admin123", method="sha256")
        admin_user = User(username="admin", password=hashed_password, role="admin")
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully.")
    else:
        print("Admin user already exists.")