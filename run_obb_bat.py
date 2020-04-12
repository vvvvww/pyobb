from tests.test_obb import sphere
from pyobb.obb import OBB
from data.get_volume import tiff2_stack
import numpy as np
import SimpleITK as sitk
import skimage
from skimage.morphology import dilation

def get_vertices(volume):
    vertices = []
    v_len = len(volume)
    for z in range(v_len):
        for x in range(volume[0].shape[0]):
            for y in range(volume[0].shape[1]):
                if volume[z][x,y] == 255:
                    # print((x,y,z))
                    vertices.append((z,y,x))
    return vertices

def volume_to_numpy(volume):
    num_slices = len(volume)
    np_vol = np.zeros([num_slices, volume[0].shape[0], volume[0].shape[1]])
    for z in range(num_slices):
        np_vol[z] = volume[z]
    return np_vol


def write_nii(volume, out_path):
    img_sitk = sitk.GetImageFromArray(volume)
    sitk.WriteImage(img_sitk, out_path)


if __name__ == '__main__':
    sh = sphere(1, (0, 0, 0), 30)
    obb = OBB.build_from_points(sh['vertices'])
    img_file_path = './data/bat-cochlea-volume.tif'
    volume = tiff2_stack(img_file_path)
    skel_path = './data/bat-cochlea-volume_skeleton.tif'
    skel = tiff2_stack(skel_path)
    np_vol = volume_to_numpy(skel)
    kernel = skimage.morphology.disk(5)
    skel_dila = dilation(np_vol)
    out_path = './data/skeleton.nii.gz'
    write_nii(skel_dila, out_path)
    vertices = get_vertices(volume)
    obb = OBB.build_from_points(vertices)
    print(obb.points)
