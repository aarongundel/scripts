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
