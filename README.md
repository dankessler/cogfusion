cogfusion
=========
Work on the cogfusion toolbox started at Neurohackweek 2016

[![Build](https://travis-ci.org/dankessler/cogfusion.svg?branch=master)](https://travis-ci.org/dankessler/cogfusion)
[![Coverage](https://img.shields.io/coveralls/dankessler/cogfusion.svg)](https://coveralls.io/r/dankessler/cogfusion)

Run tests:

```shell
python setup.py test
```

Start web app server:
```shell
cogfusion serve
```

Deploy to production server:
```shell
python setup.py sdist   # Create build artifact
./deploy.sh             # Send build artifact to server and install it there
```
(Assumes the server has the packages listed in system-requirements.txt and you have
ssh access to the server)


