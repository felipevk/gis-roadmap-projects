#!/bin/bash

# Create virtual environment
python3 -m venv geocli

# Activate it
source geocli/bin/activate

# Install essential packages
pip install --upgrade pip
pip install shapely matplotlib jupyter

# Optional: Add Jupyter kernel for this environment
python -m ipykernel install --user --name=geocli --display-name "Python (geocli)"

echo "✅ Environment created and ready: 'geocli'"