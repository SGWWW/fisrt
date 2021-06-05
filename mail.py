import yagmail
#链接邮箱服务器
yag=yagmail.SMTP(user="gry1417@163.com",password="JEMARBMOYZONOUXM",host="smtp.163.com")
#邮箱正文
email_name=["2369282540@qq.com"]
contents=["打卡成功"]
subject=["打卡成功"]
#发送邮件
yag.send(email_name,subject,contents)
print('成功')
