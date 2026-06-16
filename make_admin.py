from database import SessionLocal
import models

db = SessionLocal()

user = db.query(models.User).filter(
    models.User.username == "Samyak"
).first()

if user:
    user.role = "admin"
    db.commit()
    print("User promoted to admin!")
else:
    print("User not found!")

db.close()