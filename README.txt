========================================================
GIT NOTES
========================================================

configuring after GIT install (do always to use github)
git config --global user.name "username"
git config --global user.email "your@email.com"

INITIALIZING FOLDER FOR GIT
git init

ADDING FILES FOR TRACKING PRIOR TO COMMIT
git add <filename>

adding -a to commit adds all files

COMMITING CHANGES
git commit -m "describe changes here"
OR IF YOU NEED TO ADD FILES
git commit -a -m "describe changes here"

PUSHING CHANGES TO BRANCH
git push origin master
OR IF ON A BRANCH
git push origin testbranch

HOW TO MERGE TO MASTER
git checkout master (switch to master)
git merge test
git push origin master (to push merge branch)

CREATING A BRANCH
git checkout -b testbranch 

CHANGING BETWEEN BRANCHES
git checkout master

DELETING A BRANCH (locally)
git branch -D testbranch

DELETING REMOTE BRANCH
git push origin --delete testbranch
CLONING AN ONLINE GIT REPO
git clone [url] 
(only master branch will be copied initally)

ADDING LOCAL REPO TO REMOTE SERVER (push local project to github)
git remote add git@github.com:nsyed1/reponame.git 

CLONING (bringing existing github project to local drive)
git clone username@host:/path/to/repository

CHECKING REMOTE REPO
git remote -v

REMOTE REMOTE URL 
git remote rm remote_name

ADDING REMOTE URL (typically remote_name is 'origin')
git remote add remote_name path_to_server

CHECK WHICH BRANCH YOU'RE ON
git branch (local)
git branch -a (show all branches, remote branches only cloned when switched to)
git status

HARD RESET OF CURRENT BRANCH HEAD USING REMOTE BRANCH
git fetch origin
git reset --hard origin/master

excellent guide (no advanced shit!):
http://rogerdudler.github.io/git-guide/

-----------------------------------------------
IGNORING FILES (e.g. Pycharm .idea folder):
http://stackoverflow.com/questions/11124053/accidentally-committed-idea-directory-files-into-git

  Add .idea directory to the list of ignored files
  First, add it to .gitignore, so it is not accidentally committed by you (or someone else) again:
  
  .idea
  Remove it from repository
  Second, remove the directory only from the repository, but do not delete it locally. To achieve that, do what is listed here:
  
  Git: Remove a file from the repository without deleting it from the local filesystem
  Send the change to others
  Third, commit the .gitignore file and the removal of .idea from the repository. After that push it to the remote(s).
  
  Summary
  The full process would look like this:
  
  $ echo '.idea' >> .gitignore
  $ git rm -r --cached .idea
  $ git add .gitignore
  $ git commit -m '(some message stating you added .idea to ignored entries)'
  $ git push
  
  ---------------------------------------------------
