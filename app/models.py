from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    events = db.relationship("Event", backref="user", lazy="dynamic")

    # set table name
    __tablename__ = "user"

    def __repr__(self):
        return "<User #{id}: {username}>".format(
            id=self.id, 
            username=self.username
        )

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(120), index=True)
    start_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # set table name
    __tablename__ = "event"

    def __repr__(self):
        return "<Event #{id}: {desc}>".format(
            id=self.id,
            desc=self.desc,
            start_time=self.start_time,
            end_time=self.end_time
        )