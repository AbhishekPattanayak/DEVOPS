# Commands for git 

1. git init -> Initialises the repo in the current working directory
2. git status -> shows you the status of the files e.g untracked files, modified files etc 

# Untracked files -> when pushed to the staging area ahnd committed it returnms back to the unmodified state . This indicates that the snapshot has been taken for the file. 

3. git add -> add the files to the staging area
     3.1 git add . -> adds all the files inside the parent folder
     3.2 git add <file-name> -> adds the file which is specified.
     3.3 git add -A -> Adds all the files

4. git status -> checks for the status of the file, if it is modified etc etc. 

5. git commit -m "Message" -> Commits the files with a message. 

6. git checkout <file-name>/<branch-name> -> matches the file with the last commit 
     6.1 git checkout -f -> all the files will be restored according to the last commit you made.

7. git log -> shows you the commit that you have made basically logs. 
       7.1 git log -p -1 -> Filtering how many commits you want to check, also shows you the changes that you have made. Shows the output of the git diff. 
 
8. git diff -> Compares the working file with the staging area file and shows the difference. 

9. git diff --staged -> Compares the staged area with the last commit

10. git commit -a -m "<Message>"->  -a -> adds, -m -> message

11. git rm -> removes from working directory and staging area.
    11.1 git rm --cached <file-name> -> only removes the file from the staging area.

12. git status -s -> shows the shorter version of the status (First M shows that the file has entered the staging area, the second space shows that the file has been modified in the working tree)

13. git ignore -> Youy cant make this directly in your folder, make this from the bash terminal, Some of the files you will want to ignore. You dont want to track these files. syntax -> touch .gitignore 
       - Add the files in the .gitignore which you want to ignore and dont want to push to the staging area. Can be some logs file etc. 
       - You can ignore whole folders, you will have to add the <folder-name>/

14. Main branch -> Master, so you dont want to make any changes on the master branch. Instead you want to create a separate branch. 

15. git branch <branch-name> -> This command will create a new branch. 

16. git branch -> Shows you the branches present. 

17. git checkout feature1 -> switches to the feature1 branch

18. git checkout master -> checkout to the master branch.

19. git merge <branch-name> -> If you want to merge your changes to the master branch. Switch to master branch and run git merge <branch-name>

20. To merge master branch and the other branch first, fisrt commit your changes in the other branch then switch to the master branch and run the "git merge <branch-name>" command

21. git checkout -b <branch-name>  -> creates the branch and takes you to the branch "-b" is the branch flag. 

22. Github is a service which hosts GIT. This is sort of a online repository where you can store your codes. 

23. git remote add origin <repo-link> - adding the repository and naming as remote. 

24. git remote remove origin - removing the origin. 

25. git push origin master - Pushing the changes to the master branch

26. Do the SSH setup to connect the local repo with the remote repo. 

25. git remote set-url origin "<SSH-URL>"
