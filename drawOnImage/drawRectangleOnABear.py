import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np



def addRect(imgToRead, imgToSave,x,y,z,w, lw, color, facecolor):
  im = np.array(Image.open(imgToRead), dtype=np.uint8)
  fig,ax = plt.subplots(1)
  ax.imshow(im)
  #rect = patches.Rectangle((50,100),40,30,linewidth=1,edgecolor='r',facecolor='none') 
  rect = patches.Rectangle((x,y),z,w,linewidth=lw,edgecolor=color,facecolor=facecolor) 
  ax.add_patch(rect)
  
  #plt.axis('off')    # Remove axis from image
  
  plt.savefig(imgToSave)
  plt.close()
  return


for i in range(0, 10):
  addRect('bear.jpg', 'imgOut' + str(i)+'.jpg', 340,260,90,70,1,'r','none' )


