from tests.test_obb import sphere
from pyobb.obb import OBB
from data.get_volume import tiff2_stack

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


if __name__ == '__main__':
    sh = sphere(1, (0, 0, 0), 30)
    obb = OBB.build_from_points(sh['vertices'])
    img_file_path = './data/bat-cochlea-volume.tif'
    volume = tiff2_stack(img_file_path)
    vertices = get_vertices(volume)
    obb = OBB.build_from_points(vertices)
    print(obb)
