#!/usr/bin/sh

echo '################################'
echo '#   Creating wheel files ...####'
echo '################################'

pip3 wheel -w . .

echo '################################'
echo '#   Creating pex files   ...####'
echo '################################'

pex --python=python3 --disable-cache -f $PWD <project_name>  -e src.webapp -o <project_name>

echo '################################'
echo '#   Deleting wheel files ...####'
echo '################################'

rm *.whl
rm progress.pickle
