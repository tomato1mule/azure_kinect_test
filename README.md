# azure_kinect

## Azure Kinect Installation
See https://github.com/microsoft/Azure-Kinect-Sensor-SDK/issues/1790

```bash
# https://github.com/microsoft/Azure-Kinect-Sensor-SDK/issues/1790
sudo apt-add-repository -y -n 'deb http://archive.ubuntu.com/ubuntu focal main'          # Add ubuntu 20.04 repo
sudo apt-add-repository -y 'deb http://archive.ubuntu.com/ubuntu focal universe'         # Add ubuntu 20.04 repo 
sudo apt-get install -y libsoundio1
sudo apt-add-repository -r -y -n 'deb http://archive.ubuntu.com/ubuntu focal universe'   # Remove ubuntu 20.04 repo
sudo apt-add-repository -r -y 'deb http://archive.ubuntu.com/ubuntu focal main'          # Remove ubuntu 20.04 repo


# ------------------------------------------------------------------------------ # 
# libk4a 1.3
# ------------------------------------------------------------------------------ # 

# curl -sSL https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/libk/libk4a1.3/libk4a1.3_1.3.0_amd64.deb > /tmp/libk4a1.3_1.3.0_amd64.deb
# echo 'libk4a1.3 libk4a1.3/accepted-eula-hash string 0f5d5c5de396e4fee4c0753a21fee0c1ed726cf0316204edda484f08cb266d76' | sudo debconf-set-selections
# sudo dpkg -i /tmp/libk4a1.3_1.3.0_amd64.deb

# curl -sSL https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/libk/libk4a1.3-dev/libk4a1.3-dev_1.3.0_amd64.deb > /tmp/libk4a1.3-dev_1.3.0_amd64.deb
# sudo dpkg -i /tmp/libk4a1.3-dev_1.3.0_amd64.deb

# curl -sSL https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/libk/libk4abt1.0/libk4abt1.0_1.0.0_amd64.deb > /tmp/libk4abt1.0_1.0.0_amd64.deb
# echo 'libk4abt1.0	libk4abt1.0/accepted-eula-hash	string	03a13b63730639eeb6626d24fd45cf25131ee8e8e0df3f1b63f552269b176e38' | sudo debconf-set-selections
# sudo dpkg -i /tmp/libk4abt1.0_1.0.0_amd64.deb

# curl -sSL https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/libk/libk4abt1.0-dev/libk4abt1.0-dev_1.0.0_amd64.deb > /tmp/libk4abt1.0-dev_1.0.0_amd64.deb
# sudo dpkg -i /tmp/libk4abt1.0-dev_1.0.0_amd64.deb

# curl -sSL https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/k/k4a-tools/k4a-tools_1.3.0_amd64.deb > /tmp/k4a-tools_1.3.0_amd64.deb
# sudo dpkg -i /tmp/k4a-tools_1.3.0_amd64.deb


# ------------------------------------------------------------------------------ # 
# libk4a 1.4
# ------------------------------------------------------------------------------ # 

curl -sSL https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/libk/libk4a1.4/libk4a1.4_1.4.1_amd64.deb > /tmp/libk4a1.4_1.4.1_amd64.deb
sudo dpkg -i /tmp/libk4a1.4_1.4.1_amd64.deb

curl -sSL https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/libk/libk4a1.4-dev/libk4a1.4-dev_1.4.1_amd64.deb > /tmp/libk4a1.4-dev_1.4.1_amd64.deb
sudo dpkg -i /tmp/libk4a1.4-dev_1.4.1_amd64.deb

curl -sSL https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/k/k4a-tools/k4a-tools_1.4.1_amd64.deb > /tmp/k4a-tools_1.4.1_amd64.deb
sudo dpkg -i /tmp/k4a-tools_1.4.1_amd64.deb



# ------------------------------------------------------------------------------ # 
# Udev rules
# ------------------------------------------------------------------------------ # 

sudo cp k4a/99-k4a.rules /etc/udev/rules.d/99-k4a.rules
```



```bash
conda create -n kinect python=3.8
conda activate kinect
mamba install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 -c pytorch
pip3 install open3d==0.17.0
pip install jupyter
```