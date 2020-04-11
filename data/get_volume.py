from libtiff import TIFF

def tiff2_stack(filePath):
    tif = TIFF.open(filePath,mode='r')
    stack = []
    for img in list(tif.iter_images()):
        stack.append(img)
    return stack

if __name__ == '__main__':
    img = tiff2_stack("bat-cochlea-volume.tif")
    print(img[0].shape)