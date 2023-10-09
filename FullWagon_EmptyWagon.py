import cv2
from skimage import io
import os
import numpy
import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity


# Video file path
video_path1= 'FULL_WAGONS.MP4'
video_path2= 'EMPTY_WAGONS'
output_path1= 'SEGMENTED_IMAGES/'
output_path2= 'SEGMENTED_IMAGES2'
reference_path='FILTER_IMAGES/'

def preprocess_image(image_path, target_size=(224, 224)):
    image = cv2.resize(image_path, target_size)
    return image.flatten()

if not os.path.exists(output_path1):
    os.makedirs(output_path1)

cap = cv2.VideoCapture(video_path1)

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_filename = os.path.join(output_path1, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)


    frame_count += 1
cap.release()

if not os.path.exists(output_path2):
    os.makedirs(output_path2)

cap = cv2.VideoCapture(video_path2)

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_filename = os.path.join(output_path2, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)


    frame_count += 1
cap.release()

filea= os.listdir(output_path1)
fileb= os.listdir(output_path2)
file2 = os.listdir(reference_path)
print("Comparing images with reference image")
for file in file2:
            filter_path = os.path.join(reference_path, file)
            filter_image = io.imread(filter_path)
            for filenew in filea[199:205]:
                    
                    input_path1= os.path.join(output_path1, filenew)
                    input_image1= io.imread(input_path1)
                    
                    image1_vector = preprocess_image(filter_image)  # Load and preprocess image 1
                    image2_vector= preprocess_image(input_image1)  # Load and preprocess image 2
    
                    # Calculate cosine similarity between the feature vectors
                    similarity_score = cosine_similarity([image1_vector], [image2_vector])
                    
                    similarity_threshold = 0.9

                    if similarity_score[0][0] > similarity_threshold:
                        print("Wagon is full")
                    else:
                        print("Wagon is empty")
for file in file2:
            filter_path = os.path.join(reference_path, file)
            filter_image = io.imread(filter_path)
            for filenew in fileb[199:205]:
                    
                    input_path2= os.path.join(output_path2, filenew)
                    input_image2 = io.imread(input_path2)
                    
                    image1_vector = preprocess_image(filter_image)  # Load and preprocess image 1
                    image2_vector= preprocess_image(input_image2)  # Load and preprocess image 2
    
                    # Calculate cosine similarity between the feature vectors
                    similarity_score = cosine_similarity([image1_vector], [image2_vector])
                    
                    similarity_threshold = 0.9

                    if similarity_score[0][0] > similarity_threshold:
                        print("Wagon is full")
                    else:
                        print("Wagon is empty")
