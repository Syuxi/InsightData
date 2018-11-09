#!/bin/bash
#MSUB -q buyin
#MSUB -l walltime=01:00:00
#MSUB -M yuxisuo2018@u.northwestern.edu
#MSUB -j oe
#MSUB -m abe
#MSUB -N BC
#MSUB -l nodes=6:ppn=6

# add a project directory to your PATH (if needed)
#export PATH=/projects/b1045/anaconda2/bin:$PATH
#export PATH=$PATH:/projects/b1045/yuxisuo/test/test1.py
# export NCARG_ROOT=/home/deh224/software/ncl_6.3.0_nodap

# To start pynio_pyngl environment
#source activate pynio_pyngl

#pip install netCDF4
#pip install csvkit
# load modules you need to use
#module use /projects/b1045/modules
# Set your working directory
#cd $PBS_O_WORKDIR

# A command you actually want to execute:
python ./input/h1b_DataTesting.py
#exit this virtual environment please issue the command:
#source deactivate pynio_pyngl
