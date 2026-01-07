import os
from PIL import Image
from flask import current_app

def save_image(image_file):
    """Save and resize uploaded image"""
    if not image_file:
        return None
    
    # Generate unique filename
    import uuid
    from datetime import datetime
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_str = str(uuid.uuid4())[:8]
    ext = image_file.filename.rsplit('.', 1)[1].lower()
    filename = f"{timestamp}_{random_str}.{ext}"
    
    # Save original
    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    image_file.save(upload_path)
    
    # Create thumbnail (optional)
    create_thumbnail(upload_path)
    
    return filename

def create_thumbnail(image_path):
    """Create thumbnail version of image"""
    try:
        with Image.open(image_path) as img:
            # Resize to thumbnail size
            img.thumbnail((300, 200))
            
            # Save thumbnail
            thumb_name = image_path.rsplit('.', 1)[0] + '_thumb.' + image_path.rsplit('.', 1)[1]
            img.save(thumb_name)
    except Exception as e:
        print(f"Error creating thumbnail: {e}")
