import os
import cv2
path = r"D:\mohanteja\major project data set\bowling"
a = os.listdir(path)
for i in a:
    path1 = os.path.join(path,i)
    # print("path1")
    path2 = os.listdir(path1)
    for j in path2:
        path3 = os.path.join(path1,j)
        print("path3",path3)
        im = cv2.imread(path3)
        im = cv2.resize(im,(600,600))
        cv2.imwrite(path3,im)
print("successfully completed")       

        
   