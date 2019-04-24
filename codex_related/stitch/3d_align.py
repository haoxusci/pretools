"""3d image stitching test
    references:
    1) https://fly.mpi-cbg.de/~saalfeld/Publications/download/imagejconf2008a.pdf
    2) https://help.codex.bio/codex/cam/pipeline-details/processing-steps#shading-correction

    comment: seems working
"""
from __future__ import division
from skimage.io import imread, imsave
import numpy as np


def test_fft_shift(imagea, imageb):
    '''the detect shift is imagea to imageb
        for example, if shift is x_shift, y_shift, and values are positive
        imageb is overlapping with imagea[x_shift:, y_shift:]
        if negative:
            imageb is overlapping with imagea[:x_shift, :y_shift]
    '''
    #imagea = imread(imagea)
    #imageb = imread(imageb)
    imagea_fft = np.fft.fftn(imagea)
    imageb_fft = np.fft.fftn(imageb)
    imagea_fft_conj = np.conjugate(imagea_fft)
    print(imageb_fft.shape, imagea_fft_conj.shape)
    tt = np.multiply(imageb_fft, imagea_fft_conj)
    b = np.absolute(tt)
    detection_m = (tt) /b
    new_data = np.fft.ifftn(detection_m).real
    the_index = np.unravel_index(np.argmax(new_data), new_data.shape)
    x_shape, y_shape = imagea.shape
    x_index, y_index = the_index
    if x_index > x_shape/2:
        x_index = x_index - x_shape
    if y_index > y_shape/2:
        y_index = y_index - y_shape
    return (np.amax(new_data), x_index, y_index)


def create_images(image):
    image = imread(image)
    a, b = image.shape
    imagea = image[4:, 20:]
    imageb = image[:-4, :-20]
    print(test_fft_shift(imageb, imagea))


def main():
    image = "/Users/hao.xu/Desktop/aa.tif"
    create_images(image)

if __name__=='__main__':
    main()
