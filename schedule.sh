#!/bin/bash

#PBS -l select=1:ncpus=1:mem=20gb
#PBS -l walltime=18:00:00
#PBS -N test
#PBS -q long_cpuQ
#PBS -o ../output/out
#PBS -e ../output/err

module load python-3.8.13
python3 -m venv bioinsp

source ./bioinsp/bin/activate

cd ./bioinspired/Bio-Inspired-AI-Project

python3 -m pip install --upgrade pip
python3 -m pip install -r ./requirements.txt 
python3 ./main.py

deactivate

# qsub -q short_gpuQ -l walltime=3:00:00 -o ../output/out -e ../output/err ./schedule.sh