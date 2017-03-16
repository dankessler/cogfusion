#!/usr/bin/env bash
set -x
rm -rf cogfusion-0.0
tar -xvzf cogfusion-0.0.tar.gz 
cd cogfusion-0.0

pip install --upgrade pip
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python setup.py develop

cp conf/nginx-redirect.conf /etc/nginx/conf.d/
cp conf/nginx-cogfusion.conf /etc/nginx/sites-available/
cp conf/supervisor-cogfusion.conf /etc/supervisor/conf.d/
ln -fs /etc/nginx/sites-available/nginx-cogfusion.conf /etc/nginx/sites-enabled/
supervisorctl reread
supervisorctl update
supervisorctl restart all
systemctl restart nginx
