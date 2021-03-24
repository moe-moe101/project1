from . import db

class Property(db.Model):
    __tablename__="properties"

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(150))
    dscription =db.Column(db.String(500))
    no_rooms =db.Column(db.String(15))
    no_bathrooms = db.Column(db.String(15))
    price = db.Column(db.String(150))
    location = db.Column(db.String(255))
    Type = db.Column(db.String(80))
    photo = db.Column(db.String(80))

    def __init__(self,title,description,no_rooms,no_bathrooms,price,location,Type,photo):
        self.title = title
        self.description = description
        self.no_rooms = no_rooms
        self.no_bathrooms = no_bathrooms
        self.price = price
        self.location = location
        self.Type = Type
        self.photo = photo
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' %self.title