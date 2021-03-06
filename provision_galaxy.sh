# install prereqs
echo 'installing mercurial...'
sudo apt-get update
sudo apt-get -y install mercurial mercurial-server

# create galaxy user
sudo useradd --home-dir /home/galaxy --create-home galaxy

# edit HOST file

# install galaxy
echo 'installing galaxy...'
export GALAXYPATH='/home/galaxy/galaxy-dist/'
sudo -u galaxy -H sh -c "hg clone https://bitbucket.org/galaxy/galaxy-dist/ $GALAXYPATH"
cd $GALAXYPATH

echo "updating to stable..."
sudo -u galaxy -H sh -c "cd $GALAXYPATH && hg update stable"

# configure galaxy
echo 'configuring galaxy...'
# copy default configurations over
sudo -u galaxy -H sh -c "cp /vagrant/config/* $GALAXYPATH/"

# start galaxy
echo 'running galaxy daemon...'
sudo -u galaxy -H sh -c "cd $GALAXYPATH && sh run.sh --daemon"
