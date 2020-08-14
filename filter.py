from PIL import Image, ImageFilter, ImageOps


# Function that takes user image and filters it. It saves the filtered image to the filesystem / server.

def imageFilter(image, filter):

  image = Image.open(image)
  image_name = image.filename
  image_type = image_name.rsplit(".", 1)[1]

  if filter == "grayscale":
    filtered_image = ImageOps.grayscale(image)
    filtered_image.save(f'filtered_image.{image_type}')


  elif filter == "BLUR":
    filtered_image = image.filter(getattr(ImageFilter, filter)(8))
    filtered_image.save(f'filtered_image.{image_type}')

  else:
    filtered_image = image.filter(getattr(ImageFilter, filter)())
    filtered_image.save(f'filtered_image.{image_type}')