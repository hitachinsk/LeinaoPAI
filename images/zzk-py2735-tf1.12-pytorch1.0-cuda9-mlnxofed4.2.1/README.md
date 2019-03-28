# zzk-py2735-tf1.12-pytorch1.0-cuda9-mlnxofed4.2.1

## Feature

- Python 2.7.12 (apt)
- Python 3.5.2 (apt)
- Tensorflow 1.12.0 (pip/pip3)
- PyTorch 1.0.0 (pip/pip3)
- Cuda 9.0 
- Cudnn 7.4.1.5-1
- NCCL 2.4.1-1
- OpenMPI 3.1.2
- MLNX_OFED 4.2-1



## Build

~~~sh
docker build -t zzk-py2735-tf1.12-pytorch1.0-cuda9-mlnxofed4.2.1:latest .
~~~



## Reference

[1] https://github.com/horovod/horovod/blob/master/Dockerfile

[2] https://community.mellanox.com/s/article/how-to-create-a-docker-container-with-rdma-accelerated-applications-over-100gb-infiniband-network

