#! /usr/bin/env bash

# Current directory
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# Set up environment
source $DIR/config.sh

# Run aggregator
python $DIR/github_reminder.py
