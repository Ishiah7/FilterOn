ALLOWED_IMAGE_EXTENSIONS = ["JPEG","JPG", "PNG"]
MAX_IMAGE_SIZE = 15 * 1024 * 1024

# Function which checks if file type is in ALLOWED_IMAGE_EXTENSIONS.

def allowed_images(filename):
  if not "." in filename:
    return False
  
  ext = filename.rsplit(".", 1)[1]

  if ext.upper() in ALLOWED_IMAGE_EXTENSIONS:
    return True
     
  else:
    return False


# Function which checks the image file size. Only returns True if file size is less than or equal to MAX_IMAGE_SIZE.

def allowed_images_size(filesize):
  if int(filesize) <= MAX_IMAGE_SIZE:
    return True
  else:
    return False