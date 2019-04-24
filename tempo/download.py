"""Use this script
    1) to download dapi channel from the lung dataset.
    2) did the imagestack for it."""
from shutil import copyfile
import os
from fnmatch import fnmatch
from skimage.io import imread, imsave
import numpy as np


def list_file(folder, outpath):
    for file in os.listdir(folder):
        if fnmatch(file, 'TileScan 2*C00.tif'):
            src_file = os.path.join(folder, file)
            des_file = os.path.join(outpath, file)
            print(file)
            copyfile(src_file, des_file)


def main1():
    folder = "/mnt/external"
    outpath = "/Users/hao.xu/Desktop/basic_test"
    list_file(folder, outpath)


def stack_image(folder, outfolder):
    file_list = os.listdir(folder)
    file_list.sort()
    file_list.append('over')
    subset=[]
    for i, item in enumerate(file_list):
        #print(i//13)
        if not i%13:
            if i // 13:
                dataset = np.empty((13, 2048, 2048))
                for t, file in enumerate(subset):
                    filedata = imread(os.path.join(folder, file))
                    dataset[t,:,:]=filedata
                if i//13 < 10:
                    savename = '0' + str(i//13) + '.tif'
                else:
                    savename = str(i//13) + '.tif'
                imsave(os.path.join(outfolder, savename), np.asarray(dataset,\
                dtype=np.uint16))
            subset = []
        subset.append(item)

def main():
    folder = "/Users/hao.xu/Desktop/test/basic_test"
    outfolder = "/Users/hao.xu/Desktop/test/stack"
    stack_image(folder, outfolder)


if __name__=='__main__':
    main()
