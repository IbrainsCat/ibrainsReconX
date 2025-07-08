#!/bin/bash
pkg install -y git python nmap figlet toilet
pip install requests fpdf

git clone https://github.com/ibrainsCat/IbrainsReconX.git
cd IbrainsReconX
python core.py
