# SECOND for KITTI object detection
SECOND detector. Based on my unofficial implementation of VoxelNet with some improvements.

ONLY support python 3.6+, pytorch 0.4.1+. Don't support pytorch 0.4.0. Tested in Ubuntu 16.04/18.04.

* Ubuntu 18.04 have speed problem in my environment and may can't build/usr SparseConvNet.


### 1.code

```bash
git clone https://github.com/traveller59/second.pytorch.git
cd ./second.pytorch/second
```

### 2. dependences

It is recommend to use Anaconda package manager.

```bash
shapely
fire 
pybind11 
tensorboardX
protobuf 
scikit-image
numba 
pillow
SparseConvNet
```