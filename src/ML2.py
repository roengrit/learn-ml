from sklearn import datasets

digit_dat = datasets.load_digits()

print(digit_dat["DESCR"])
print(digit_dat.keys())

#first image size 8x8
print(digit_dat["images"][0])