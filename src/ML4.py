from scipy.io import loadmat
mnist_raw = loadmat("mnist-original.mat")
mnist_dat = {
    "data": mnist_raw["data"],
    "target": mnist_raw["label"][0]
}

print(mnist_dat["target"].shape)