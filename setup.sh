#Script for installing matplotlib for python
sudo apt-get install python-pip
sudo apt-get install python-pip libfreetype6-dev libpng-dev libxft-dev python-numpy
sudo -E pip install tabulate
curl https://pypi.python.org/packages/source/s/setuptools/setuptools-18.2.zip > setuptools-18.2.zip
unzip setuptools-18.2.zip
cd setuptools-18.2
sudo python ez_setup.py
cd ..
rm -rf setuptools-18.2
rm setuptools-18.2.zip
sudo -E pip install matplotlib