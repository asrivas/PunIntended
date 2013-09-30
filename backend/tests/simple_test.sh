#! /bin/bash

pwd
cd src
# with no args run a few tests
python dispatch.py 

python dispatch.py prime 3
python dispatch.py gcd 3 5
python dispatch.py pun
python dispatch.py text like fire

