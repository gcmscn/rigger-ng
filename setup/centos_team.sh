DST=/usr/local/rigger-ng
PKG=${HOME}/devspace/rigger-ng/src
if test -d $DST 
  sudo rm -rf $DST 
fi
sudo cp -r  $DST $PKG
cd $DST ;
./setup.sh centos.py