from netdisk import MOUNTnetdisk
from startup import STARTUP
import os
class RUN(MOUNTnetdisk):
    def startupfile(self):  #写入连接项目盘启动文件的方法
        # print(self.remotehost,self.username,self.password)
        file=STARTUP()
    #     file.generatefile("start_netdisk",self.shell_connet_disklist)
        file.generatefile("start_disk",self.shell_connet_disklist)
    def checkdatadisk(self):
        s_password=input("请输入登录资料盘的二级密码：")
        if(s_password=="123456"):
            return 0
        else:
            return 1
    def loginsys(self):
        self.login()
        res =self.netdisk()
        file=STARTUP()
        file.generatefile("start_login",self.shellconnetlist)
        return res
    def checknetdisk(self): #检查项目路径是否挂载
        resultlist=[]
        checkpath=[r"W:\\",r"X:\\",r"Y:\\",r"Z:\\"]
        for path in checkpath:
            diskres=os.path.isdir(path)
            resultlist.append(diskres)
        return resultlist
    def change_function(self):
        # self.login()
        # res =self.netdisk()
        # if(res==0):
        os.system("cls")
        self.meun()
        step=input("请输入项目编号：")
        # self.deldisk()
        # self.netporject(step)
        if(step=="1" and len(step)==1):
            n=0
            disklist = self.checknetdisk()
            for res in disklist:
                if (res == True):
                    n = n + 1
                else:
                    pass
            if(n==0):
                self.netporject(step)
            else:
                self.deldisk()
                self.netporject(step)
            # pass
        elif(step!="9"and  step!="1"and step!='0' and step!= "8" ):
            self.deldisk()
            self.netporject(step)
        elif(step=="8"):
            s_password = input("请输入登录资料盘的二级密码：")
            if (s_password == "123456"):
                self.netdatadisk()
                self.change_function()
            else:
                print("请输入正确的二级密码")
                self.change_function()
            # logdata = self.checknetdisk()
            # if (logdata==0):
            #     self.netdatadisk()
            # else:
            #     self.checknetdisk()
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

    n=0
    program = RUN()
    reslist=program.checknetdisk()
    for res in reslist:
        if(res==True):
            n=n+1
        else:
            pass

    if(n!=4):
        res_num = program.loginsys()
        while(1):
            if(res_num==0):
                program.change_function()
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
    elif(n==4):
        # program.deldisk()
        while (1):
            program.change_function()
            # program.startupfile()
            program.startupfile()
            os.system("pause")
            os.system("cls")
    else:
        print("未知错误，请联系管理员，程序作者已经跑路了，当你看到这个错误的时候！")