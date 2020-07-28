import pickle
import random
import smtplib
from email.header import Header
from email.mime.text import MIMEText


class Node:
    def __init__(self, id, name, cate, level, time, desc):
        self.id = id
        self.name = name
        self.cate = cate
        self.level = level
        self.time = time
        self.desc = desc
        self.pre_list = []
        self.aft_list = []

    def addNode(self, node, pre=True):
        if pre:
            self.pre_list.append(node)
        else:
            self.aft_list.append(node)

    def __le__(self, other):
        return self.level <= other.level

    def __lt__(self, other):
        return self.level < other.level

    def setLevel(self, level):
        self.level = level


class User:
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password
        self.learned = []
        self.score = {}

    def add(self, node_id, score):
        self.learned.append(node_id)
        self.score[node_id] = score


def dump2file(filename, Nodes):
    with open(filename, "wb") as f:
        pickle.dump(len(Nodes), f)
        for Node in Nodes:
            pickle.dump(Node, f)


def load2prog(filename):
    with open(filename, "rb") as f:
        num_nodes = pickle.load(f)
        Nodes = []
        for _ in range(num_nodes):
            Nodes.append(pickle.load(f))
    return Nodes


def To_Graph():  # 创建图的邻接矩阵
    Nodes = load2prog('../data.dat')
    length = len(Nodes)
    edgs = [[float('inf')] * length for _ in range(length)]
    for node in Nodes:
        for aft_node in node.aft_list:
            edgs[node.id - 1][aft_node.id - 1] = 1
    return edgs


def email_sender(receiver):
    mail_host = "smtp.qq.com"
    mail_user = "1034618831@qq.com"
    mail_pass = "bllgbumvetbvbfcd"

    sender = '1034618831@qq.com"'
    receivers = [f'{receiver}']

    val_code = random.randint(100000, 999999)

    message = MIMEText(f'Your Verification code is {val_code}', 'plain', 'utf-8')

    message['From'] = Header("Val")
    message['To'] = Header("CODE")

    subject = 'Verification code'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 587)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        return str(val_code)
    except smtplib.SMTPException:
        return "0"
