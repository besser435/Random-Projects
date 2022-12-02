import random
from tqdm import tqdm
from PIL import Image  


random.seed(10)
width = 500
height =500
img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))


def random_tuple():
    nums = [255,128,0]  # these the color values used
    """    for i in range(255):
    sex_list.append(i)"""

    rng = random.choices(nums, weights=[255,10,1], k=3)
    #print(*sex, sep='')
    #print(sex_list)

    return *rng,
#for i in range(100): print((random_tuple()))


for x in tqdm(range(width)):
    for y in range(height):
        img.putpixel((x, y), random_tuple())
        #print(x, y)

img.show()