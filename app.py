from app import create_app, db
from app.models.user import User
from werkzeug.security import generate_password_hash

app = create_app()

def create_test_user(app):
    with app.app_context():
        db.create_all()   # creates tables if they do not exist

        admin_exists = User.query.filter_by(username="admin").first()
        if not admin_exists:
            hashed_password = generate_password_hash("admin123")
            admin_user = User(username="admin", password=hashed_password, role="admin")
            db.session.add(admin_user)
            db.session.commit()
            print("Admin user created successfully.")

if __name__ == "__main__":
    create_test_user(app)
    app.run(debug=True)