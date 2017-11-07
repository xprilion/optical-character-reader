import numpy as np
import matplotlib.pylab as plt

im = plt.imread("image.jpg")

print im.shape

def normalize(f):
	lmin = float(f.min())
	lmax = float(f.max())
	return np.floor((f-lmin)/(lmax-lmin)*255.)


def plti(im, h=8, **kwargs):
    """
    Helper function to plot an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('off')
    plt.show()
    
def to_grayscale(im, weights = np.c_[0.5, 0.5, 1]):
    """
    Transforms a colour image to a greyscale image by
    taking the mean of the RGB values, weighted
    by the matrix weights
    """
    tile = np.tile(weights, reps=(im.shape[0],im.shape[1],1))
    return np.sum(tile * im, axis=2)

#plti(im)

#im = im[100:500,:2000,:]    

im = normalize(im)

#im = to_grayscale(im)

plti(im, cmap='Greys')
