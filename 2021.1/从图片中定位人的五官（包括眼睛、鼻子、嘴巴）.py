#从图片中定位人的五官（包括眼睛、鼻子、嘴巴）
import face_recognition
image = face_recognition.load_image_file("F:\壁纸\4K\nature-girl-model-beautiful-36029.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)


