#!/bin/bash
#SBATCH --account=no-project
#SBATCH --qos=debug
#SBATCH --partition=debug
#SBATCH --job-name=cpu_test
#SBATCH --output=slurm/cpu_test_%j.out
#SBATCH --time=00:01:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G

# Initialize conda
source ~/miniconda3/etc/profile.d/conda.sh
conda activate predicts

echo "Running on:"
hostname

echo "Python version:"
python --version

echo "Python path:"
which python
