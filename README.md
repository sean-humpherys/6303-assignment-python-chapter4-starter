In VS Code, press Ctrl+Shift+V to preview this README.md file or Cmd+Shift+V on a Mac.
# 6303-assignment-python-chapter4
The instructions for this assignment can be found at   
(https://docs.google.com/document/d/1QZuGPhN9vr-SsXKNwSeBI-Wo-ppTRoVkxU-kZwhWqqk/edit)  
 

## How to run Python apps
Open a terminal in VS Code from Terminal Menu, New Terminal. Type one of the following commands. 
```
  python app.py
  python payroll.py
  python testpayroll.py
```

## Useful GIT Commands:  
Use the terminal or command line to issue git commands. 
  
**Typically, only configure your settings one time per computer**, unless you want to edit your name or email address in the future or change computers. Git saves this info on your computer. Substitute your name and email address. This info will be used to log who made what changes to code.
```
 git config --global user.name "Sean Humpherys" 
 git config --global user.email shumpherys@wtamu.edu
```

**To clone an assignment the first time, follow these commands.** Do this command for each assignment. Or, if you use multiple computers (work, home, school) do this once per computer per assignment. The URL to your assignment respository is found under the [Code] button and "Clone with HTTPS" on github.com. 
```bash
 git clone https://github.com/username/something  #use the URL to your specific assignment repository on github.com
 ```

**At the start of your coding session each day**, you should issue the following command to verify you have the latest changes to the online-repository or to pull down any changes/comments made by the professor:     
```bash
 git pull  
 git status 
```
You should see "Your branch is up to date with the 'origin/master', and "nothing to commit"    
 
**At the end of each day (or after your class) you should run these commands** to upload your changes to your online repository. The professor can see your changes:     
```bash
 git add -A
 git status    
 git commit -m "Type a message here in quotes that briefly describing your changes"
 git status    
 git push
 git status   
```
The first status should report that files have changed or been added and needs to be committed. The second status should say "nothing to commit." The third status should report "Your branch is up to date with the 'origin/master', and "nothing to commit"  

**When you are done with the assignemnt and ready for the professor to grade**, issue the following command with the commit message **"Ready for grading"**. The professor will see your comment and grade the assignment. 
```bash
 git add -A  
 git commit -m "Ready for grading" 
 git push
 git status   
```
After you are familiar with git workflow, you can skip the 'git status' commands, but they are useful for beginnners to see what is happening at each command. 
