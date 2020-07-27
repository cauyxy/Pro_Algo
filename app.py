from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

Nodes = load2prog("data.dat")


def get_Node(id):
    for node in Nodes:
        if id == node.id:
            return node


@app.route('/')
def hello_world():
    return render_template("index.html", nodes_part1=Nodes[:10], nodes_part2=Nodes[10:])


@app.route('/details', methods=["get", "post"])
def details():
    node_id = request.values.get("id")
    node = get_Node(eval(node_id))

    # TODO: 完成sim_node的计算
    sim_nodes = 0

    return render_template("single.html", node=node)


if __name__ == '__main__':
    app.run(port=8887)
