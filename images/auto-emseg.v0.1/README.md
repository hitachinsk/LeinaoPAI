# auto-emseg
### version 0.1
### created by ngchc &lt;changc@mail.ustc.edu.cn&gt;

## basic image
### nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04

## added packages
### anaconda3 python2.7 libboost-dev build-essential autotools-dev rsync curl wget jqopenssh-server openssh-client sudo vim nano git

### for python2: cython h5py numpy scipy munkres mahotas tqdm Pillow
### for python3: pytorch torchvision opencv SimpleITK tqdm libtiff joblib

## build command
### docker build ./images/auto-emseg.v0.1 -t auto-emseg:v0.1
