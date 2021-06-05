import yagmail
#链接邮箱服务器
yag=yagmail.SMTP("2369282540@qq.com","xgukgqroswdzeaic",host="smtp.qq.com")
#邮箱正文
contents="打卡成功"
subject="打卡成功"
#发送邮件
yag.send=('Gry1417@163.com',subject,contents)
