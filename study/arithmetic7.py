# 迪克斯特拉算法

# 1.建立图
graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}

# 定义无穷大
infinity = float("inf")

# 2.建立开销表 即从起始位置到节点的开销
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

# 3.建立父节点表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

# 4.处理过的点
processed = []


# 5.找出未处理过最短路程的点
def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 6.找出起点到终点最短路程
node = find_lowest_cost_node(costs)
while node is not None:
    neighbor_nodes = graph[node]  # 获取邻居点
    cost = costs[node]  # 处理点到起点的位置
    for n, c in neighbor_nodes.items():
        new_cost = cost + c  # 从起点经过处理点的路程
        if new_cost < costs[n]:  # 如果经过处理点的路径 比之前的路径短 则更新开销表和父节点表
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

result = "fin"
parent = parents["fin"]
while parent != "start":
    result = "%s-->%s" % (parent, result)
    parent = parents[parent]
result = "start-->%s" % result
print("最短路径:%s,最短距离:%s" % (result, costs["fin"]))

# ------------------------ 迪克斯特拉算法 -------------------------
# graph = {}  # 权重图
# graph["start"] = {}
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2
#
# graph["a"] = {}
# graph["a"]["fin"] = 1
#
# graph["b"] = {}
# graph["b"]["a"] = 3
# graph["b"]["fin"] = 5
#
# graph["fin"] = {}
#
# infinity = float("inf")
# costs = {}  # 开销表
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity
#
# parents = {}  # 存储父节点
# parents["a"] = "start"
# parents["b"] = "start"
# parents["fin"] = None
#
# processed = []  # 处理过的点
#
#
# def find_lowest_cost_node(costs):
#     lowest_cost = float("inf")
#     lowest_cost_node = None
#     for node,cost in costs.items():
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node
#
#
# node = find_lowest_cost_node(costs)
# while node is not None:
#     neighbor_nodes = graph[node]  # 获取处理节点邻居节点
#     cost = costs[node]  # 获取该节点到起点的距离
#     for n in neighbor_nodes:  # 循环邻居节点
#         new_cost = cost + neighbor_nodes[n]  # 获取经过处理该节点到邻居节点的距离
#         if costs[n] > new_cost:
#             costs[n] = new_cost
#             parents[n] = node
#     processed.append(node)
#     node = find_lowest_cost_node(costs)
# lujing = "fin"
# fin_ = parents["fin"]
# lujing += "<-%s" % fin_
# while fin_ != "start":
#     fin_ = parents[fin_]
#     lujing += "<-%s" % fin_
# print(lujing)
# print(costs["fin"])

# ------------------------ 迪克斯特拉算法 -------------------------
