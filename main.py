

import cv2
import matplotlib.pyplot as plt
def cv_Show(name,img):
    cv2.imshow(name,img)

    cv2.waitKey(10000)
    # waiting 10 seconds or if the user press one key,
    # return the value of that key immediately and execute the nextline code
    cv2.destroyAllWindows()


# video=cv2.VideoCapture('test2.mp4')
# if video.isOpened:
#     open,frame=video.read()
# else:
#     open=False
# while video.isOpened:
#     ret,frame=video.read()
#     if not ret:
#         break
#
#     # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     # # convert frame from BGR to gray
#     gray=frame.copy()
#     gray[:,:,0]=0
#     gray[:,:,1]=0
#     # set b and g to zero, only red color left
#     cv2.imshow('result',gray)
#
#
#
#
#
#     if ord('q') == (cv2.waitKey(1)&0xFF):
#             # why do we use &0xFF?
#             # answer:
#             # 1.Compatibility Across Platforms: Different operating
#             # systems and environments may handle key codes differently.
#             # On some systems, the higher bits of the key code might contain
#             # additional information, and using & 0xFF ensures that
#             # only the lower 8 bits (which represent the actual key value) are considered.
#             # 2. Consistency: This approach guarantees
#             # that the comparison is consistent with the expected
#             # ASCII values, ensuring the correct detection of key presses.
#             break
# video.release()

picture=cv2.imread('test.jpg')
picture2=picture[0:200,0:200]
cv_Show("pary",picture2)
# cv_show is a function created above


print(picture2)
picture3=picture2.copy()
picture3[:,0:100,1]+=100
cv2.imshow("before_adding",picture2)
cv2.waitKey(10000)
cv2.imshow("after_adding",picture3)
cv2.waitKey(10000)

# the under code shows the difference between operator_+ and cv2.add(p1,p2)
picture2+=200
picture4=picture2+picture3
cv2.imshow("directly_adding",picture4)
cv2.waitKey(10000)
picture5=cv2.add(picture2,picture3)
cv2.imshow("cv2_add_function",picture5)
cv2.waitKey(10000)
print("compare the difference")
print(picture4[0:8,0:2,0])
print(picture5[0:8,0:2,0])
print(picture2[0:8,0:2,0])



#  The under code shows how to merge two pictures with diffierent size
picture=cv2.imread('test.jpg')
merged_picture=cv2.imread("picture_used_merge.jpg")
merged_picture=cv2.resize(merged_picture,(picture.shape[1],picture.shape[0]))
print("new size  "+ str(merged_picture.shape)+str(picture.shape))
After_Merged=cv2.addWeighted(picture,0.5,merged_picture,0.5,0)
cv2.imshow("After_merged",After_Merged)
cv2.waitKey(6000)





