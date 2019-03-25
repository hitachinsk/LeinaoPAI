# py37-pytorch1.0.1-cu90-ctc

## Feature

* CUDA 9.0 
* CUDNN 7.1.2
* python 3.7.1
* pytorch 1.0.1
* tensorboardx
* ctcdecode
<!-- * warpctc-pytorch -->
* ffmpeg 4.1
* gym 0.12.0
* opencv-contrib-python 4.0.0.21

+ ipython
+ lmdb
+ h5py

## Build

```bash
docker build -t py37-pytorch1.0.1-cu90-ctc ./images/py37-pytorch1.0.1-cu90-ctc/
```

## Note
最后一步编译会出现processing ctcdecode，后面比较慢，请耐心等待15分钟左右，谢谢