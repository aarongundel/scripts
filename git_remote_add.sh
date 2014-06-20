#!/usr/bin/env bash

# This script initializes the git repository, creates the README, opens it for editing, 
# allows for initial commit before prompting for the git repository (which you should have
# already created) and pushing the repository to the new remote.  

git init
touch README.md
echo "Opening README in vi for editing.  (i to edit; :q to exit)" 
read
vi README.md
git add .
echo "Enter a commit message" 
read commit_message
git commit -m "$commit_message"
echo "Enter a git repository URL"
read repository
git remote add origin $repository
git remote -v
git push origin master
