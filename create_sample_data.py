from app import create_app, db
from app.models import Vehicle
from datetime import datetime

def create_sample_data():
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Sample vehicles
        vehicles = [
            Vehicle(
                make='Tesla',
                model='Model S',
                year=2023,
                price=89990.00,
                mileage=1500,
                fuel_type='Electric',
                transmission='Automatic',
                color='Red',
                description='Luxury electric sedan with autopilot',
                is_available=True
            ),
            Vehicle(
                make='BMW',
                model='X5',
                year=2022,
                price=68990.00,
                mileage=12000,
                fuel_type='Petrol',
                transmission='Automatic',
                color='Black',
                description='Premium SUV with M Sport package',
                is_available=True
            ),
            Vehicle(
                make='Mercedes-Benz',
                model='E-Class',
                year=2023,
                price=74900.00,
                mileage=5000,
                fuel_type='Hybrid',
                transmission='Automatic',
                color='Silver',
                description='Executive luxury sedan',
                is_available=True
            ),
            Vehicle(
                make='Audi',
                model='Q7',
                year=2021,
                price=55900.00,
                mileage=25000,
                fuel_type='Diesel',
                transmission='Automatic',
                color='White',
                description='Spacious luxury SUV',
                is_available=True
            ),
            Vehicle(
                make='Porsche',
                model='911 Carrera',
                year=2023,
                price=115000.00,
                mileage=800,
                fuel_type='Petrol',
                transmission='Automatic',
                color='Yellow',
                description='Iconic sports car',
                is_available=True
            ),
            Vehicle(
                make='Ford',
                model='F-150',
                year=2022,
                price=48900.00,
                mileage=18000,
                fuel_type='Petrol',
                transmission='Automatic',
                color='Blue',
                description='Best-selling truck with eco-boost engine',
                is_available=True
            )
        ]
        
        # Add vehicles to database
        for vehicle in vehicles:
            db.session.add(vehicle)
        
        db.session.commit()
        print('Sample data created successfully!')

if __name__ == '__main__':
    create_sample_data()
