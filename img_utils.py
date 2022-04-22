from PIL import Image
from pathlib import Path
# from torchvision.


def get_image_paths(f):
    '''f: Path
    returns list of paths of all images in the folder f, or just f if f is a file
    '''
    suffix = ['jpg', 'jpeg', 'png', 'heic']
    if not f.is_file():
        a = []
        for i in suffix:
            a += list(f.glob('*.'+i))
            a += list(f.glob('*.'+i.upper()))
        return a
    else: #if folder is a single file
        return [f]

## load an image:
# im = Image.open(img_path)

## Crop image
# bbox = np.array([x1, y1, x2, y2]).astype(int) #top left - bottom right, must be int
# im = im.crop(bbox)

## resize image: Scale Fill
#--------------------
# Method 1 involves saving/loading the image
# size = 64,64
# im.thumbnail(size, Image.ANTIALIAS)
# im.save('img.jpg')
#--------------------
# Method 2

def scale_fill(im, target_width, target_height):
    '''
    Resize PIL image keeping ratio and adding zero-valued background.
    '''
    target_ratio = target_height / target_width
    im_ratio = im.height / im.width
    if target_ratio > im_ratio:
        # It must be fixed by width
        resize_width = target_width
        resize_height = round(resize_width * im_ratio)
    else:
        # Fixed by height
        resize_height = target_height
        resize_width = round(resize_height / im_ratio)

    image_resize = im.resize((resize_width, resize_height), Image.ANTIALIAS)
    background = Image.new('RGBA', (target_width, target_height), 0)
    offset = (round((target_width - resize_width) / 2), round((target_height - resize_height) / 2))
    background.paste(image_resize, offset)
    return background.convert('RGB')


