import os
from PIL import Image
path = os.getcwd()
file_path = []
for (root, directories, files) in os.walk(path):
    for file in files:
        if '.webp' in file:
            file_path.append(os.path.join(file))
       
for i in range(len(file_path)):
    im = Image.open(file_path[i]).convert("RGB")
    im.save(str(file_path[i])[:-5]+".png","png",quality=100)
    os.remove(file_path[i])


