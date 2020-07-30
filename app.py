from flask import Flask, render_template, request
from models import *

from Zy.Sort import *

from Search.search import Search
from Recommend.recommend import Recommend

from FindPreAft.FindPre import FindPre
from FindPreAft.FindAft import FindAft

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
            return render_template("index.html", user_id=user.id, nodes_part1=Nodes[:int(len(Nodes) / 2)],
                                   nodes_part2=Nodes[int(len(Nodes) / 2):])
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

    time, result_nodes = Top_Sort(node)

    return render_template("details.html", node=node, sim_nodes=nodes[1:6], nodes=result_nodes, time=time)


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

    if mode == "0":
        # Sort By Time
        result_nodes = Sort_by_time()
        msg = "Sort By Time"
    else:
        # Sort By Level
        result_nodes = Sort_by_level()
        msg = "Sort By Level"

    return render_template("node_list.html", msg=msg, nodes=result_nodes)


@app.route("/search", methods=["post", "get"])
def search():
    request_str = request.values.get("s")
    result_nodes = Search(request_str)
    return render_template("node_list.html", msg="字符串搜索", nodes=result_nodes)


@app.route("/search_1", methods=["post", "get"])
def search_1():
    mode = request.values.get("mode")
    node_id = request.values.get("id")
    node = get_Node(eval(node_id))

    if mode == "0":
        nodes_pre = FindPre(node)
        nodes_aft = FindAft(node)
        return render_template("node_list.html", msg=f"{node.name}的前后续节点", nodes_pre=nodes_pre, nodes_aft=nodes_aft,
                               fenlan=True)
    else:
        score = get_User(eval(node_id)).score
        LearntNodes_id = [i for i in score.keys()]
        Grades = [i for i in score.values()]
        result_nodes = Recommend(LearntNodes_id, Grades)
        return render_template("node_list.html", msg="给我推荐", nodes=result_nodes)


@app.route("/add_node", methods=["post", "get"])
def add_node():
    user_id = request.values.get("user_id")
    if request.method == "GET":
        return render_template("add_node.html", user_id=user_id, Nodes=Nodes)


    else:
        id = len(Nodes) + 1
        name = request.form.get("name")
        level = eval(request.form.get("level"))
        cate = eval(request.form.get("cate"))
        time = eval(request.form.get("time"))
        desc = request.form.get("desc")
        pre_list = request.form.getlist("pre_list")
        aft_list = request.form.getlist("aft_list")
        pre_list = [eval(_) for _ in pre_list]
        aft_list = [eval(_) for _ in aft_list]
        pre_list = [get_Node(n_id) for n_id in pre_list]
        aft_list = [get_Node(n_id) for n_id in aft_list]

        tmp_node = Node(id, name, cate, level, time, desc)
        tmp_node.pre_list = pre_list
        tmp_node.aft_list = aft_list

        for node in tmp_node.pre_list:
            node.aft_list.append(tmp_node)
        for node in tmp_node.aft_list:
            node.pre_list.append(tmp_node)

        Nodes.append(tmp_node)

        dump2file("data.dat", Nodes)

        return render_template("index.html", user_id=user_id, nodes_part1=Nodes[:int(len(Nodes) / 2)],
                               nodes_part2=Nodes[int(len(Nodes) / 2):])


if __name__ == '__main__':
    app.run(port=8887)
