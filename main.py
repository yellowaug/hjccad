from netdisk import MOUNTnetdisk
from startup import STARTUP
import os
class RUN(MOUNTnetdisk):
    def startupfile(self):
        print(self.remotehost,self.username,self.password)
        file=STARTUP()
        file.generatefile(self.commom_connet_use,self.commom_connet_disk,self.shell_connet_disklist)
    def loginsys(self):
        self.login()
        res =self.netdisk()
        return res
    def change_function(self):
        # self.login()
        # res =self.netdisk()
        # if(res==0):
        self.meun()
        step=input("请输入项目编号：")
        if(step=="1" and len(step)==1):
            # self.netdisk()
            self.netporject()
        elif(step=="2"and len(step)==1):
            pass #这个功能还没开放
            # self.netporject()
        elif(step=="9"and len(step)==1):
            self.deldisk()
        elif(step=="0"and len(step)==1):
            # os.system("exit")
            print("系统已退出\n")
            os.system("cls")
            os.system("pause")
            exit(1)
        else:
            print("请输入正确的项目编号")
if __name__=="__main__":
    program = RUN()
    res_num = program.loginsys()
    while(1):
        if(res_num==0):
            program.change_function()
            # program.startupfile()
            program.startupfile()
            os.system("pause")
            os.system("cls")
        else:
            print("请输入正确的用户名及密码")
            res_num = program.loginsys()
            if (res_num == 0):
                program.change_function()
                program.startupfile()
                os.system("pause")
                os.system("cls")