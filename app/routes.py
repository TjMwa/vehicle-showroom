import os
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app import db
from app.models import Vehicle, Inquiry
from app.forms import VehicleForm, InquiryForm
from config import Config

bp = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@bp.route('/')
def index():
    vehicles = Vehicle.query.filter_by(is_available=True).order_by(Vehicle.created_at.desc()).limit(6).all()
    return render_template('index.html', vehicles=vehicles)

@bp.route('/vehicles')
def vehicles():
    page = request.args.get('page', 1, type=int)
    per_page = 9
    
    # Filtering
    make = request.args.get('make')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    
    query = Vehicle.query.filter_by(is_available=True)
    
    if make:
        query = query.filter(Vehicle.make.ilike(f'%{make}%'))
    if min_price:
        query = query.filter(Vehicle.price >= min_price)
    if max_price:
        query = query.filter(Vehicle.price <= max_price)
    
    vehicles = query.order_by(Vehicle.created_at.desc()).paginate(page=page, per_page=per_page)
    
    # Get unique makes for filter dropdown
    makes = db.session.query(Vehicle.make).distinct().all()
    
    return render_template('vehicles.html', vehicles=vehicles, makes=makes)

@bp.route('/vehicle/<int:id>')
def view_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    form = InquiryForm()
    return render_template('view_vehicle.html', vehicle=vehicle, form=form)

@bp.route('/vehicle/<int:id>/inquiry', methods=['POST'])
def vehicle_inquiry(id):
    vehicle = Vehicle.query.get_or_404(id)
    form = InquiryForm()
    
    if form.validate_on_submit():
        inquiry = Inquiry(
            vehicle_id=vehicle.id,
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            message=form.message.data
        )
        db.session.add(inquiry)
        db.session.commit()
        flash('Your inquiry has been submitted successfully!', 'success')
        return redirect(url_for('main.view_vehicle', id=vehicle.id))
    
    return render_template('view_vehicle.html', vehicle=vehicle, form=form)

@bp.route('/admin/vehicles')
def admin_vehicles():
    vehicles = Vehicle.query.order_by(Vehicle.created_at.desc()).all()
    return render_template('admin/vehicles.html', vehicles=vehicles)

@bp.route('/admin/vehicle/add', methods=['GET', 'POST'])
def add_vehicle():
    form = VehicleForm()
    
    if form.validate_on_submit():
        vehicle = Vehicle(
            make=form.make.data,
            model=form.model.data,
            year=form.year.data,
            price=form.price.data,
            mileage=form.mileage.data,
            fuel_type=form.fuel_type.data,
            transmission=form.transmission.data,
            color=form.color.data,
            description=form.description.data,
            is_available=form.is_available.data
        )
        
        # Handle image upload
        if form.image.data:
            file = form.image.data
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Add timestamp to avoid filename conflicts
                from datetime import datetime
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"{timestamp}_{filename}"
                file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                vehicle.image_filename = filename
        
        db.session.add(vehicle)
        db.session.commit()
        
        flash('Vehicle added successfully!', 'success')
        return redirect(url_for('main.admin_vehicles'))
    
    return render_template('admin/add_vehicle.html', form=form)

@bp.route('/admin/vehicle/<int:id>/edit', methods=['GET', 'POST'])
def edit_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    form = VehicleForm(obj=vehicle)
    
    if form.validate_on_submit():
        vehicle.make = form.make.data
        vehicle.model = form.model.data
        vehicle.year = form.year.data
        vehicle.price = form.price.data
        vehicle.mileage = form.mileage.data
        vehicle.fuel_type = form.fuel_type.data
        vehicle.transmission = form.transmission.data
        vehicle.color = form.color.data
        vehicle.description = form.description.data
        vehicle.is_available = form.is_available.data
        
        # Handle image upload
        if form.image.data:
            file = form.image.data
            if file and allowed_file(file.filename):
                # Delete old image if exists
                if vehicle.image_filename:
                    old_image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], vehicle.image_filename)
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
                
                filename = secure_filename(file.filename)
                from datetime import datetime
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"{timestamp}_{filename}"
                file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                vehicle.image_filename = filename
        
        db.session.commit()
        flash('Vehicle updated successfully!', 'success')
        return redirect(url_for('main.admin_vehicles'))
    
    return render_template('admin/edit_vehicle.html', form=form, vehicle=vehicle)

@bp.route('/admin/vehicle/<int:id>/delete', methods=['POST'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    
    # Delete image if exists
    if vehicle.image_filename:
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], vehicle.image_filename)
        if os.path.exists(image_path):
            os.remove(image_path)
    
    db.session.delete(vehicle)
    db.session.commit()
    
    flash('Vehicle deleted successfully!', 'success')
    return redirect(url_for('main.admin_vehicles'))

@bp.route('/api/vehicles')
def api_vehicles():
    vehicles = Vehicle.query.filter_by(is_available=True).all()
    return jsonify([vehicle.to_dict() for vehicle in vehicles])

@bp.route('/api/vehicle/<int:id>')
def api_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    return jsonify(vehicle.to_dict())
