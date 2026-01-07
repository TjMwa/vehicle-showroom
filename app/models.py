from datetime import datetime
from app import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    mileage = db.Column(db.Integer)
    fuel_type = db.Column(db.String(20))  # Petrol, Diesel, Electric, Hybrid
    transmission = db.Column(db.String(20))  # Manual, Automatic
    color = db.Column(db.String(30))
    description = db.Column(db.Text)
    image_filename = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_available = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Vehicle {self.year} {self.make} {self.model}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'price': self.price,
            'mileage': self.mileage,
            'fuel_type': self.fuel_type,
            'transmission': self.transmission,
            'color': self.color,
            'description': self.description,
            'image_url': f'/static/uploads/{self.image_filename}' if self.image_filename else None,
            'is_available': self.is_available
        }

class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    vehicle = db.relationship('Vehicle', backref=db.backref('inquiries', lazy=True))
