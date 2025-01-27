from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), unique=True)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    gravity = db.Column(db.Integer)
    terrain = db.Column(db.String(50))
    surface_water = db.Column(db.Integer)
    climate = db.Column(db.String(50))

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "climate": self.climate,
        }


    
class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), unique=True)
    birth_year = db.Column(db.Integer)
    species = db.Column(db.String(50))
    heigth = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    homeworld = db.Column(db.String(50))

class Vehicules(db.Model):
    __tablename__ = 'vehicules'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), unique=True)
    model = db.Column(db.String(50))
    manufacturer = db.Column(db.String(50))
    clase = db.Column(db.String(50))
    cost = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    length = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    mimimum_crew = db.Column(db.Integer)
    passengers= db.Column(db.Integer)

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    personaje_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    vehicules_id = db.Column(db.Integer, db.ForeignKey('vehicules.id'), nullable=False)
    fecha_guardado = db.Column(db.DateTime)

