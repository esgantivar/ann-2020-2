import h5py
import shutil
import os
from fuel.datasets import H5PYDataset
import numpy as np
from tqdm import tqdm
from keras.preprocessing.image import load_img, img_to_array

def get_paths(name):
    paths = []
    names = []
    with open(f"{name}.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            paths.append(stripped_line)
            names.append(stripped_line.split('/')[-1])
    return paths, names

def build_subset(x):
    if not os.path.exists('storage/breakhis'):
        os.makedirs('storage/breakhis')
       
    if not os.path.exists(f'storage/breakhis/{x}PX'):
        os.makedirs(f'storage/breakhis/{x}PX')
        
    labels = {}
    paths, names = get_paths(f"BENIGN_{x}PX")
    for path in tqdm(paths):
        shutil.copy(path, f"storage/breakhis/{x}PX")
    for name in names:
        labels[name] = 0
    paths, names = get_paths(f"MALIGNANT_{x}PX")
    for path in tqdm(paths):
        shutil.copy(path, f"storage/breakhis/{x}PX")
    for name in names:
        labels[name] = 1
    return labels


def generate_h5(labels, name='breakhis_40PX', path='storage/breakhis/40PX', target_size=(256, 256), img_size=[256, 256]):
    n_samples = len(labels)
    n_test, n_dev = int(len(labels) * .3), int(len(labels) * .2)
    n_train = n_samples - n_test - n_dev

    f = h5py.File(f'{name}.hdf5', mode='w')

    _images = f.create_dataset('images', [len(labels)] + img_size + [3], dtype='int32')
    _labels = f.create_dataset('labels', [len(labels)], dtype='int32')

    _images.dims[0].label = 'batch'
    _images.dims[1].label = 'width'
    _images.dims[2].label = 'height'
    _images.dims[3].label = 'channel'

    _labels.dims[0].label = 'batch'

    B = np.copy(np.array(list(labels.keys())))
    rng = np.random.RandomState()
    perm = rng.permutation(B)

    for i in tqdm(range(perm.shape[0])):
        name = perm[i]
        image_path = f"{path}/{name}"
        img = load_img(image_path, target_size=target_size)
        _images[i] = img_to_array(img)
        _labels[i] = labels[name]

    split_dict = {
        'train': {
            'images': (0, n_train),
            'labels': (0, n_train)
        },
        'dev': {
            'images': (n_train, n_train + n_dev),
            'labels': (n_train, n_train + n_dev)
        },
        'test': {
            'images': (n_train + n_dev, n_samples),
            'labels': (n_train + n_dev, n_samples)
        }
    }

    f.attrs['split'] = H5PYDataset.create_split_array(split_dict)
    f.flush()
    f.close()