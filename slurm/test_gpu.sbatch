#!/bin/bash
#SBATCH --job-name=orchid_gpu_test
#SBATCH --output=slurm/orchid_gpu_test_%j.out
#SBATCH --time=00:05:00

# ORCHID GPU settings
#SBATCH --account=orchid
#SBATCH --qos=orchid
#SBATCH --partition=orchid
#SBATCH --gres=gpu:1

# Resources
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

# Load conda
source ~/miniconda3/etc/profile.d/conda.sh
conda activate predicts

echo "Running on:"
hostname

echo "GPU Info:"
nvidia-smi

echo "Testing PyTorch CUDA:"
python - << 'EOF'
import torch
print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
EOF
