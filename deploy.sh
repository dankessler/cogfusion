git pull
env/bin/pip -e .
pkill cogfusion
env/bin/cogfusion serve &
