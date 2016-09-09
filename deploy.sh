git pull
env/bin/python setup.py develop
pkill cogfusion
env/bin/cogfusion serve &
