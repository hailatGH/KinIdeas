#!/bin/bash

echo "Enter a commit for the push: "
read COMMIT
git add .
git commit -m "$COMMIT"
git push
echo "SUCCESS"