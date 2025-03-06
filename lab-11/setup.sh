#!/bin/bash

set -e  # Exit if any command fails to execute

# Install dependencies
sudo apt update
sudo apt install -y git curl build-essential

# Clone the micro repository from GitHub
git clone https://github.com/zyedidia/micro.git
cd micro

# Build and install the utility
make build
sudo mv micro /usr/local/bin/micro

# Clean up
cd ..
rm -rf micro

echo "Installation of micro complete! Run 'micro' to start using it."