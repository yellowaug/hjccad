import os
from netdisk import MOUNTnetdisk
class STARTUP(MOUNTnetdisk): #这个文件调用有BUG，明天再想办法改掉
    def generatefile(self,f_name=None,shell_connetlist=None):
        path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
        os.chdir(path)
        cmddshell=[]
        shell="@echo off"
        shell_msg="@echo off connetting to project disk,don't close the window,it will auto close in end !!!"
        # shell_1=shell_connet_user
        cmddshell.append(shell)
        # cmddshell.append(shell_1)
        cmddshell.append("\n")
        cmddshell.append(shell_msg+"\n")
        name="{filename}.bat".format(filename=f_name)
        file=open(name,"w+",encoding="utf-8")
        file.writelines(cmddshell)
        file.seek(0,2)
        file.writelines(shell_connetlist)
        file.flush()
        file.close()