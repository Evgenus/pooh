#### In the memory of awesome things this site wil be hosted [HERE](http://evgenus.github.io/pooh/).

1. Download and install Git (TortoiseGit is good)
2. Clone my repository from path you can fing above at this page
3. Download and install somewhere nginx for windows
4. At <nginx instalation path>/conf copy file nginx.conf with name pooh.conf

Inside this file change

    root   html;
    
into

    root   <path where repository clonned>/output;
    
Change

    listen 80;
    
into

    listen 8000;
    
5. At <nginx instalation path> create file run_pooh.cmd and write inside


    nginx.exe -c conf\pooh.conf
    
6. Run this file and you can access site inside browser http://localhost:8000/pooh
7. At <path where repository clonned> look at gen.py to read pretty comments))))
8. Install Python 2.6 from http://python.org (maybe 2.7 works too but I've not tried)
9. Install Mako Templates Engine from http://pypi.python.org/pypi/Mako/0.3.6/
10. Now you can freely edit source pages, then run gen.py and see changes inside browser
11. To download edited things into FTP I used TotalCommander (MainMenu/Commands/Synchronize directories)
That is the way to copy only changed files.

