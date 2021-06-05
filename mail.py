import yagmail
#链接邮箱服务器
yag=yagmail.SMTP(user="Gry1417@163.com",password="shi123...",host="smtp.163.com")
#邮箱正文
contents="打卡成功"
subject="打卡成功"
#发送邮件
yag.send=('2369282540@qq.com',subject,contents)
