#!/bin/bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

## Sync Timewarrior data so it's saved in Git

if [ -d $HOME/.timewarrior ]; then
  rsync -avz $HOME/.timewarrior/data $THIS_DIR/dot_timewarrior
fi