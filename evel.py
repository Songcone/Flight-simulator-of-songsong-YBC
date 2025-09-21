from tkinter import messagebox
def evel(a=0,b=1,c=0,d=100):
    m = open('money.txt','w').write(str(a))
    l = open('level.txt','w').write(str(b))
    c = open('count.txt','w').write(str(c))
    g = open('good.txt','w').write(str(d))
messagebox.showinfo('信息','如果您的游戏出现了故障，也许这个疑难解答可以解决您的问题')#金钱  等级  游玩次数   满意度
messagebox.showwarning(f'信息','问题：这个会让我的游戏数据清空吗？\n答：会，但是您可以修改exe文件旁边的四个txt文件，即可恢复数据\n\n问：游戏错误？答：未保存游戏数据！\n问：会启动不出来吗？\n答：不会！(退不出下面有二次确认)')
b = messagebox.askquestion('提问','确定吗？？？')
if b == 'no' or b == False:
    exit()
evel()
messagebox.showinfo('信息','好了！已经恢复正常！重启游戏就可以了，我们会自动退出！')