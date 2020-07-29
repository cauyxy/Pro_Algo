from flask import Flask, render_template, request
from models import *
from Zy.Sort_by_similarity import Sort_by_similarity
from Search.search import Search
from FindPreAft.FindPre import FindPre
from FindPreAft.FindAft import FindAft
from Recommend.recommend import Recommend

app = Flask(__name__)

Nodes = load2prog("data.dat")
try:
    Users = load2prog("user.dat")
except:
    Users = []
next_id = len(Users) + 100

ver_code = {}


def get_Node(id):
    for node in Nodes:
        if id == node.id:
            return node


def get_User(user_id):
    for user in Users:
        if user_id == user.id:
            return user


def user_match(email):
    for user in Users:
        if email == user.email:
            return True
    return False


def login_match(email, password):
    for user in Users:
        if email == user.email and password == user.password:
            return user
    return False


@app.route('/')
@app.route('/login', methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")

        user = login_match(email, password)

        for node in Nodes:
            node.tmp_score = user.score[node.id]

        if user:
            return render_template("index.html", user_id=user.id, nodes_part1=Nodes[:10],
                                   nodes_part2=Nodes[10:])
        else:
            return render_template("login.html", err="Illegal Login")


@app.route('/register', methods=["get", "post"])
def register(next_id=next_id):
    if request.method == "GET":
        return render_template("register.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")

        if user_match(email):
            return render_template("register.html", err="This email have registered")

        code = request.form.get("code")
        if code != ver_code[email]:
            return render_template("register.html", email=email, err="Verification Code is Wrong!")

        u = User(next_id, email, password)
        Users.append(u)
        dump2file("user.dat", Users)
        next_id += 1
        ver_code.pop(email)

        return render_template("login.html")


@app.route('/details', methods=["get", "post"])
def details():
    user_id = request.values.get("user_id")
    node_id = request.values.get("id")
    node = get_Node(eval(node_id))

    nodes = Sort_by_similarity(node)

    '''
    time,result_nodes = function(node)
    '''

    return render_template("details.html", node=node, sim_nodes=nodes[1:6])


@app.route('/updatescore', methods=["get"])
def updatescore():
    user_id = request.values.get("user_id")
    node_id = request.values.get("id")
    score = request.values.get("score")
    user = get_User(eval(user_id))
    user.add(eval(node_id), score)
    dump2file("user.dat", Users)

    return "Ok"


@app.route('/verification', methods=["get"])
def verification():
    email_addr = request.values.get("email")

    code = email_sender(email_addr)

    if code != "0":
        ver_code[email_addr] = code
        return "Ok"
    else:
        return "ERR"


@app.route('/artlist', methods=["get"])
def artlist():
    mode = request.values.get("mode")

    # TODO: 更改到排序的知识点
    if mode=="0":
        # Sort By Time
        result_nodes = Nodes
    else:
        # Sort By Level
        result_nodes = Nodes

    return render_template("node_list.html", nodes=result_nodes)


@app.route("/search", methods=["post", "get"])
def search():
    request_str = request.values.get("s")

    # TODO: 完成定义 ---字符串搜索
    result_nodes = Search(request_str)

    return render_template("node_list.html", msg="字符串搜索", nodes=result_nodes)


@app.route("/search_1", methods=["post", "get"])
def search_1():
    mode = request.values.get("mode")
    node_id = request.values.get("id")
    node = get_Node(eval(node_id))


    if mode == "0":
        # TODO: 完成定义 -------前后续节点

        result_nodes = Nodes
        return render_template("node_list.html", msg=f"{node.name}的前后续节点", nodes=result_nodes)
    else:
        score = get_User(eval(node_id)).score

        # TODO: 完成定义  -------给我推荐
        result_nodes = Recommend(node_id,score)
        return render_template("node_list.html", msg="给我推荐", nodes=result_nodes)


if __name__ == '__main__':
    app.run(port=8887)
