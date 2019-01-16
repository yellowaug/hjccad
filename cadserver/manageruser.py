import os
import wmi

class ManagerServer(object):
    def __init__(self):
        print("="*50)
        print("\n")
        print("CAD\t协\t同\t管\t理\t端")
        print("\n")
        print("=" * 50)
    def creatuser(self):
        usr=input("请输入用户名：")
        pwd=input("请输入密码：")
        deletegroup="net localgroup Users {name} /delete".format(name=usr)
        addusershell="net user {name} {password} /add".format(name=usr,password=pwd)
        addgroup="net localgroup Administrators {name} /add".format(name=usr)
        os.system(addusershell)
        os.system(deletegroup)
        os.system(addgroup)
    def createshare(self):
        # sharename=input("请输入共享名：")
        # sharepath=input("请将要共享的文件夹拖入运行程序框中：")
        # createshareshell="net share {s_name}={path} /grant:test1,full"
        user=wmi.WMI()
        userlist = user.Win32_GroupUser()
        print(user.Win32_GroupUser)
        for users in userlist:
            # if(user.PartComponent.SIDType):
            # print(user.PartComponent.SID)

            userinfos=users.PartComponent
            print(userinfos)
            # for userinfo in userinfos:
            #     print(userinfo)
        u_list = user.Win32_SystemAccount
        print(u_list)
        # for i in u_list:
        #     print(i)
    def deleteuser(self):
        pass
    def deleteshare(self):
        pass

ctr=ManagerServer()
# ctr.creatuser()
ctr.createshare()