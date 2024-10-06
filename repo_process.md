git clone https://github.com/yourusername/old-repo.git
cd old-repo
git remote remove origin
git remote add origin github.com:yourusername/new-repo.git  ------
git push --all origin