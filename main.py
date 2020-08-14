from flask import Flask, url_for, redirect, render_template, request, send_file
from PIL import Image, ImageFilter, ImageOps
from imageFunctions import allowed_images, allowed_images_size
import os
from filter import imageFilter
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['IMAGE_UPLOADS'] = "C:/Users/User/Desktop/PROJECTS/Hobby Projects/Python/FilterOn"


@app.route('/', methods=['POST', 'GET'])
def home():

  # Checks if there is a POST request.

  if request.method == 'POST':

    # Checks if the request files are being sent.

    if request.files:

      # Checks if the cookies contain "filesize", javascript function returning file size.

      if "filesize" in request.cookies:

        # Checks if the image sent is equal to or lower than allowed image size set.

        if not allowed_images_size(request.cookies["filesize"]):
          return render_template('home.html', message="Image Size Too Large")

        # Gets image and filter type sent by user.

        user_image = request.files["image"]
        filter_type = request.form["filters_box"]

        # Checks if user chose a image file.

        if user_image.filename == "":

          return render_template('home.html', message="No File Selected!")

        # Checks if the file type is allowed, only image types are allowed.
        
        if allowed_images(user_image.filename):

          # secure_filename used to safely store file to filesystem / server.

          filename = secure_filename(user_image.filename)

          # Saving image file to filesystem / server.

          user_image.save(os.path.join(app.config['IMAGE_UPLOADS'], filename))

          # Calling imageFilter function. Takes care of filtering the image.

          imageFilter(filename, filter_type)

          # Removes the user image from the file system / server. Did this to keep server clean

          os.remove(f"C:/Users/User/Desktop/PROJECTS/Hobby Projects/Python/FilterOn/{filename}")

          # Sends back filtered image as download.

          return send_file('C:/Users/User/Desktop/PROJECTS/Hobby Projects/Python/FilterOn/filtered_image.jpg', attachment_filename='filtered_image.jpg', as_attachment=True)

        else:
          return render_template('home.html', message="Invalid File Type!")
      else:
        return render_template('home.html', )
    else:
      return render_template('home.html')
  else:  
    return render_template('home.html')



@app.route('/features') 
def features():
  return render_template('features.html')


if __name__ == '__main__':
  app.run(debug=True)






  

  