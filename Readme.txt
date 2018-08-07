EX0- SET UP 
EX1 – print statement
EX2 – comments and pound 

the purpose of this setup is so you can do four things very reliably while you work on the exercises: 
1.	Write exercises using your text editor, gedit on Linux, TextWrangler on OSX, or Notepad++ on Windows.  
2.	Run the exercises you wrote.  
3.	Fix them when they are broken.  
4.	Repeat.  


EX0
Windows 
Go to http://notepad-plus-plus.org with your browser, get the Notepad++ text editor, and install it. You do not need to be the administrator to do this.  
1.	Make sure you can get to Notepad++ easily by putting it on your desktop and/or in Quick Launch. Both options are available during setup.  
2.	Run PowerShell from the Start menu. Search for it and you can just hit Enter to run it.  
3.	Make a shortcut to it on your desktop and/or Quick Launch for your convenience.  
4.	Run your Terminal program. It won’t look like much.  
5.	In your Terminal program, run python. You run things in Terminal by just typing the name and hitting Enter. 
6.	If you run python and it’s not there (python is not recognized.), install it from  http://python.org/download.  
7.	Make sure you install Python 3.  
8.	You may be better off with Active State Python, especially if you do not have administrative rights.  
9.	If after you install it python still isn’t recognized, then in PowerShell enter this:  
a.	[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27", "User")  
b.	Close PowerShell and then start it again to make sure Python now runs. If it doesn’t, restart may be required. 
10.	Type quit() and hit Enter to exit python.  


EX0_1
1.	Create a github account 
2.	Create Git Repository
3.	Python101
4.	Install Git on windows 
5.	Clone git on your machine
6.	Create  a readme.txt file and push it.

Install Git on Windows
Git for Windows stand-alone installer
Download the latest Git for Windows installer.
When you've successfully started the installer, you should see the Git Setup wizard screen. Follow the Next and Finish prompts to complete the installation. The default options are pretty sensible for most users.
Open a Command Prompt (or Git Bash if during installation you elected not to use Git from the Windows Command Prompt).
Run the following commands to configure your Git username and email using the following commands, replacing Emma's name with your own. These details will be associated with any commits that you create:
$ git config --global user.name "Emma Paris"  $ git config --global user.email "eparis@atlassian.com"
Optional: Install the Git credential helper on Windows
Bitbucket supports pushing and pulling over HTTP to your remote Git repositories on Bitbucket. Every time you interact with the remote repository, you must supply a username/password combination. You can store these credentials, instead of supplying the combination every time, with the Git Credential Manager for Windows.


