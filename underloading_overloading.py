import cv2
from skimage import io
from skimage.metrics import structural_similarity as ssim
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

#Intialising Dummy variables
num = 0
temp = 0


#Configuring Time details for email
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

# Configuring Email details
smtp_server = 'smtp.gmail.com'
smtp_port = 587 
sender_email = 'yourgmail@gmail.com' #replace with original id and password
sender_password = 'passcode'
receivers= ['dummy@gmail.com','dummy@gmail.com']
subject = 'Enter subject here'
body= ' '

message = MIMEMultipart()
message['From'] = sender_email

message['Subject'] = subject

def compare_ssim_emp(ssim_score, wagon_num):
    threshold = 0.9
    if ssim_score> threshold:
         print("The wagon "+str(wagon_num)+" is completely empty")
         print("____________________________________")
         global num 
         num = 1
         
         
    else:
            print("The wagon "+str(wagon_num)+" is not empty")
            print("____________________________________")
            num =2
            
            
            


def compare_ssim_full(ssim_score, wagon_num):
    threshold = 0.9
    if ssim_score> threshold:
         print("The wagon "+str(wagon_num)+" is completely full")
         print("____________________________________")
         global temp 
         temp = 1
         
         
         
         
    else:
            print("The wagon "+str(wagon_num)+" is not full")
            print("____________________________________")
            temp = 2
            
            
            
            
    
print("Comparing images of various Wagons ")

#Input images are given manually
#Replace your images
input_image1 = io.imread('Empty_Input1.PNG')
input_image2 = io.imread('Empty_Input2.PNG')
input_image3 = io.imread('Filled_Input1.PNG')
input_image4 = io.imread('Filled_Input2.PNG')

# A filter image is given which is used for reference
filter_image1 = io.imread('Empty_Filter.PNG')
filter_image1 = io.imread('Filled_Filter.PNG')

input_image_gray1 = cv2.cvtColor(input_image1, cv2.COLOR_BGR2GRAY)
input_image_gray2 = cv2.cvtColor(input_image2, cv2.COLOR_BGR2GRAY)
input_image_gray3 = cv2.cvtColor(input_image3, cv2.COLOR_BGR2GRAY)
input_image_gray4 = cv2.cvtColor(input_image4, cv2.COLOR_BGR2GRAY)
filter_image_gray1 = cv2.cvtColor(filter_image1, cv2.COLOR_BGR2GRAY)
filter_image_gray2 = cv2.cvtColor(filter_image1, cv2.COLOR_BGR2GRAY)

target_size1 = (1024, 1024)
target_size2 = (1024, 1024)

#Resizing images
input_image_gray1_resized = cv2.resize(input_image_gray1, target_size1)
input_image_gray2_resized = cv2.resize(input_image_gray2, target_size1)
input_image_gray3_resized = cv2.resize(input_image_gray3, target_size2)
input_image_gray4_resized = cv2.resize(input_image_gray4, target_size2)

filter_image_gray1_resized = cv2.resize(filter_image_gray1, target_size1)
filter_image_gray2_resized = cv2.resize(filter_image_gray2, target_size2)

# Structural Similarity is compared between input image and filter image
ssim_score1 = ssim(input_image_gray1_resized, filter_image_gray1_resized)
ssim_score2 = ssim(input_image_gray2_resized, filter_image_gray1_resized)
ssim_score3 = ssim(input_image_gray3_resized, filter_image_gray2_resized)
ssim_score4 = ssim(input_image_gray4_resized, filter_image_gray2_resized)


print("WAGON 1:")
wagon_num = 1
compare_ssim_emp(ssim_score1,wagon_num)
if num ==1:
     body = f"Time is: {current_time}, WAGON "+wagon_num+" is Empty "
     message.attach(MIMEText(body, 'plain'))
     
elif num == 2:
     body = f"Time is: {current_time}, WAGON "+str(wagon_num)+" is not Empty "
     message.attach(MIMEText(body, 'plain'))
     



print("WAGON 2:")
wagon_num = 2
compare_ssim_emp(ssim_score2, wagon_num)
if num == 1:
     body = f"\n Time is: {current_time}, WAGON "+wagon_num+" is Empty "
     message.attach(MIMEText(body, 'plain'))
     
elif num == 2:
     body = f"\n Time is: {current_time}, WAGON "+str(wagon_num)+" is not Empty " 
     message.attach(MIMEText(body, 'plain'))



print("WAGON 3:")
wagon_num = 3
compare_ssim_full(ssim_score3, wagon_num)
if temp == 1:
     body = f"\n Time is: {current_time}, WAGON "+str(wagon_num)+" is Full "
     message.attach(MIMEText(body, 'plain'))

elif temp ==2:
     body = f"\n Time is: {current_time}, WAGON "+str(wagon_num)+" is not Full "
     message.attach(MIMEText(body, 'plain'))



print("WAGON 4:")
wagon_num = 4
compare_ssim_full(ssim_score4, wagon_num)
if temp == 1:
     body = f"\n Time is: {current_time}, WAGON "+str(wagon_num)+" is Full "
     message.attach(MIMEText(body, 'plain'))

elif temp ==2:
     body = f"\n Time is: {current_time}, WAGON "+str(wagon_num)+" is not Full "
     message.attach(MIMEText(body, 'plain'))

#Sending Email
     
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Use TLS for secure connection
    server.login(sender_email, sender_password)

    # Send the email
    for receiver in receivers:
         server.sendmail(sender_email, receiver, message.as_string())
    

    print("Email sent")

except Exception as e:
    print(f'Error: {e}')

finally:
    server.quit()
