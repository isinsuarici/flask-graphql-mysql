from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    description = db.Column(db.String(45))
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description        }