import os
from netdisk import MOUNTnetdisk
class STARTUP(MOUNTnetdisk): #这个文件调用有BUG，明天再想办法改掉
    def generatefile(self,shell_connet_user=None,shell_connetlist=None):
        path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
        os.chdir(path)
        cmddshell=[]
        shell="echo off\n"
        shell_1=shell_connet_user
        # shell_2=shell_connet_disk
        cmddshell.append(shell)
        cmddshell.append(shell_1)
        cmddshell.append("\n")
        # cmddshell.append(shell_2)
        file=open("test.bat","w+",encoding="utf-8")
        # print(os.getcwd()+file.name)
        file.writelines(cmddshell)
        file.seek(0,2)
        file.writelines(shell_connetlist)
        # for shell in shellconnect:
        #     file.seek(0,2)
        #     file.write(shell)
        file.flush()
        file.close()