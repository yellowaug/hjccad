import os
class MOUNTnetdisk(object):
    def __init__(self):
        print("="*30)
        print("华\t景\t城\tCAD\t协\t同\t测\t试\t版")
        print("="*30)
        # self.step = input()
    def meun(self):
        print("="*30)
        print("\n")
        # print("1:连\t接\t网\t盘")
        # print("\n" )
        print("1:连\t接\t测\t试\t项\t目")
        print("\n" )
        print("2:连\t接\t资\t料\t盘")
        print("\n" )
        print("9:退\t出\t项\t目")
        print("\n" )
        print("0:退\t出\t程\t序")
        print("\n")
        print("=" * 30)
    def login(self):
        self.remotehost = '192.168.13.167'
        self.username = input("请输入用户名：")
        self.password = input("请输入密码：")
    def netdisk(self):
        # self.shellconnetlist=[]
        # step=input("请选择项目：")
        # if(step=="1" and len(step)==1):
        localpath = 'R:'
        remotepath = "project"
        # self.username = input("请输入用户名：")
        # self.password = input("请输入密码：")
        self.commom_connet_use=r"net use \\{remotehost} {pwd} /user:{u_name}".format(remotehost=self.remotehost,pwd=self.password,u_name=self.username)
        # commom2=r"net use {localpath} \\{remotehost}\{remotepath} {pwd} /user:{u_name}".\
        #     format(localpath=localpath,remotehost=self.remotehost,remotepath=remotepath,u_name=self.username,pwd=self.password)
        self.commom_connet_disk = r"net use {localpath} \\{remotehost}\{remotepath}". \
            format(localpath=localpath, remotehost=self.remotehost, remotepath=remotepath)
        # self.shellconnetlist.append(commom_connet_use)
        # self.shellconnetlist.append(commom_connet_disk)
        res1=os.system(self.commom_connet_use)
        if (res1==0):
            os.system(self.commom_connet_disk)
            # if (res==0):
            #     print("项目文件添加成功")
            #     res2 = os.system("net use /PERSISTENT:yes")
            #     print(res2)
            # else:
            #     print("项目文件添加失败")
        else:
            print("账号和密码错误")
            print(res1)

        return res1
        # elif(step=="2" and len(step)==1):
        #     disk = MOUNTnetdisk()
        #     disk.netporject()
        # elif(step=="9"and len(step)==1):
        #     disk = MOUNTnetdisk()
        #     disk.deldisk()
        # else:
        #     print("请输入正确的项目编号：")
        # os.system("pause")
        # os.system("cls")
        # disk = MOUNTnetdisk()
        # disk.netdisk()
    def netporject(self):
        self.shell_connet_disklist=[]
        localpath = ["W:","X:","Y:","Z:"]
        # remotehost = '192.168.13.167'
        remotepath = ["test1","test2","test3","test4"]
        # username = self.username
        # password = self.password
        for i in range(4):
            # commome = r"net use {localpath} \\{remotehost}\{remotepath} {pwd} /user:{u_name}". \
            # format(localpath=localpath[i], remotehost=remotehost, remotepath=remotepath[i], u_name=username, pwd=password)
            commome = r"net use {localpath} \\{remotehost}\{remotepath}". \
            format(localpath=localpath[i], remotehost=self.remotehost, remotepath=remotepath[i])
            res =os.system(commome)
            if (res==0):
                self.shell_connet_disklist.append("\n")
                self.shell_connet_disklist.append(commome)
                print("项目文件添加成功")
            else:
                print("项目文件添加失败")
    def deldisk(self):
        res =os.system("net use * /delete ")
        input(res)

# disk = MOUNTnetdisk()
# disk.netdisk()
# disk.deldisk()
# disk.netporject()
