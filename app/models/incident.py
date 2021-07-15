from app import db, login


class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    incname = db.Column(db.String(200), index=True, unique=True)
    fulldesc = db.Column(db.Text, nullable=False)
    incdate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<{} - {}>'.format(self.incdate, self.name)

