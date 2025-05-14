from extensions import db

class CamUsers(db.Model):
    __tablename__ = 'cam_users'
    users_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    def __repr__(self):
        return f"<CamUsers(id={self.users_id}, username='{self.user_name}', email='{self.email}')>"