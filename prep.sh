#!/usr/bin/bash

PROJECT=$1
TO=$2

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 PROJECT DEST_PATH"
    exit 1
fi

if [ -e ".git/config" ] && grep -q "python-project" .git/config; then
    echo "In correct git, proceeding..."
else
    echo "Not in correct git repo? Exiting..."
    exit 1
fi

if ! [ -d ${TO} ]; then
    echo "Creating destination directory: ${TO}"
    mkdir -p ${TO}
fi

echo "Copying files to the destination directory"
rsync -ar --verbose --exclude '.git' --exclude '.*swp' * ${TO} 

echo "Removing prep script"
rm -f ${TO}/prep.sh

echo "Replacing \$PROJECT\$ with ${PROJECT}"
files=$(grep -rl '\$PROJECT\$' ${TO})
sed -i "s/\\\$PROJECT\\\$/${PROJECT}/g" ${files}

echo "Changing project dir name to ${PROJECT}"
mv ${TO}/project ${TO}/${PROJECT}
