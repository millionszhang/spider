import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
#sender 是邮件发送人邮箱。password是服务器授权码，mail—host是服务器地址(这里是qqstmp服务器)
sender = 'zyw1819787473@163.com'
passWord = '0224zhangyw'
mail_host = 'smtp.163.com'
#receivers 是邮件接收人，用列表保存，可添加多个
receivers = ['1819787473@qq.com']

#设置email信息
msg = MIMEMultipart()
#邮件主题
msg['Subject'] = input(f"{'请输入邮件主题：'}")
#发送方信息
msg['From'] = sender
#邮件正文是MIMEText：
msg_content = input(f"{'请输入邮件内容：'}")
msg.attach(MIMEText(msg_content,'plain','utf-8'))
#添加附件就是加上一个MIMEBase,从本地读取一个图片
with open('C:\\Users\\Administrator\\Desktop\\python\\课表.xlsx','rb') as f:
    #设置附件的mime和文件名，这里是jpg类型，可以换png或其他类型：
    mime = MIMEBase('image ','xlsx',filename='lyon.xlsx')
    #加上必要的头信息：
    mime.add_header('Content-Disposition','attachment',filename='lyon.xlsx')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    #把附件的内容读进来：
    mime.set_payload(f.read())
    #用Base64编码
    encoders.encode_base64(mime)
    #添加到MIMEMultipart：
    msg.attach(mime)

#登陆并发送邮件
try:
    #qqstmp服务器的端口号为465或587
    s = smtplib.SMTP_SSL("smtp.163.com",994)
    s.set_debuglevel(1)
    s.login(sender,passWord)
    #给receivers列表中的联系人逐个发送邮件
    for i in range(len(receivers)):
        to = receivers[i]
        msg['To'] = to
        s.sendmail(sender,to,msg.as_string())
        print('sucess!')
    s.quit()
    print("all emails have been sent over!")
except smtplib.SMTPException as e:
    print("Falied,%s",e)



