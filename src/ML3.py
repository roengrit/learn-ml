from sklearn import datasets
import pylab

digit_dat = datasets.load_digits()

print(digit_dat["DESCR"])
print(digit_dat.keys())

#first image size 8x8
print(digit_dat["images"][0])

#show image
pylab.imshow(digit_dat["images"][0],cmap=pylab.cm.gray_r)
pylab.show()