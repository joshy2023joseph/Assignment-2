from PIL import Image
import face_recognition

# Load the jpg file into array
image = face_recognition.load_image_file("/home/joshy/Desktop/Python_Class/Unknown_image/IMG-20200118-WA0025.jpg")

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

print("We found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # Show the actual faces
    face_image = image[top:bottom, left:right]
    crop_image = Image.fromarray(face_image)
    crop_image.show()
    
