# -*- coding: utf-8 -*-
# Author    : kaizen
# Datetime  : 2020/5/29 18:12
# User      : closed
# File      : testing.py
# explain   : 文件说明
import os
import sys


class processAllBidSpider(object):
    @staticmethod
    def createSettingFile():
        path = os.getcwd() + os.sep + 'bid_setting'
        filepath = os.getcwd() + os.sep + 'bid_file'
        for file in os.listdir(path):
            if 'common_template' in file:
                with open(path + os.sep + file, 'r', encoding='utf-8') as f, open(path + os.sep + 'common_settings.py',
                                                                                  'w', encoding='utf-8') as f2:
                    filepath = "EXCEL_FILE_PATH = \'" + filepath + "\'"
                    if 'win' in sys.platform:
                        filepath = filepath.replace('\\', '\\\\')
                    f2.writelines(f.read() + filepath)

    @staticmethod
    def processBidSpider():
        """
        取当前路径下的所有文件和文件夹
        :return:
        """
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if 'main.py' in file:
                    os.chdir(root)
                    os.system('python main.py')


# class sendEmail():
#     def __init__(self):
#         self.today = str(date.today())
#     def createZipFile(self, dirpath):
#         current_filepath = os.path.join(dirpath, self.today)
#         filename = os.path.join(current_filepath, '合同文件(' + self.today + ').zip')
#         with zipfile.ZipFile(filename, 'w', zipfile.ZIP_STORED) as f:
#             files = [os.path.join(current_filepath, file) for file in os.listdir(current_filepath) if '.xlsx' in file]
#             [f.write(file) for file in files]
#         return filename
#
#     def send(self, filepath):
#         sender = 'zhangpan@rietergroup.com'
#         # sender = 'zhzwx9@163.com'
#         receivers = EMAIL_TO  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
#         # 创建一个带附件的实例
#         message = MIMEMultipart()
#         message['From'] = Header(EMAIL_TO[1], 'utf-8')
#         message['To'] = Header(EMAIL_TO[0], 'utf-8')
#         # message['Cc'] = Header(sender, 'utf-8')
#         subject = """今日合同数据...."""
#         message['Subject'] = Header(subject, 'utf-8')
#
#         # 邮件正文内容
#         message.attach(MIMEText('这是合同数据新邮件，5点之后发送......', 'plain', 'utf-8'))
#
#
#         att = MIMEBase('application', 'octet-stream')
#         att.set_payload(open(filepath, 'rb').read())
#         att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '合同数据.zip'))
#         encoders.encode_base64(att)
#         message.attach(att)
#         try:
#             smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com')
#
#             smtpObj.connect('smtp.exmail.qq.com',465)
#             smtpObj.login(sender, '123456Aa')
#             smtpObj.sendmail(sender, receivers, message.as_string())
#             print("邮件发送成功")
#
#         except smtplib.SMTPException as e:
#             print(e)
#             print("Error: 无法发送邮件")


if __name__ == '__main__':
    processAllBidSpider.createSettingFile()
    processAllBidSpider.processBidSpider()
    # dirpath = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../../..")), 'bid_file')
    # # dirpath = os.path.join(os.getcwd(), 'bid_file')
    # email = sendEmail()
    # filepath = email.createZipFile(dirpath)
    # email.send(filepath)
