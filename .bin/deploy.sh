#!/bin/sh

set -u

THIS_DIR=$(cd $(dirname $0); pwd)

cd $THIS_DIR
git submodule init
git submodule update

for f in .??*; do
   [ "$f" = ".git" ] && continue
   [ "$f" = ".gitconfig.local.template" ] && continue
   [ "$f" = ".gitmodules" ] && continue

   ln -snfv ~/dotfiles/"$f" ~/
done

[ -e ~/.gitconfig.local ] || cp ~/dotfiles/.gitconfig.local.template ~/.gitconfig.local
