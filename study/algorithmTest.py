def binarySearch(attr, vaule):
    start = 0
    end = len(attr)
    while start <= end:
        middle = int((start + end) / 2)
        guessValue = attr[middle]
        if guessValue == vaule:
            return middle
        elif guessValue > vaule:
            end = middle
        else:
            start = middle
    return None


def selectSort(attr):
    for i in range(len(attr)):
        selectSmall(i, attr)


def selectSmall(start, attr):
    small = attr[start]
    smallIndex = start
    for i in range(start + 1, len(attr)):
        if attr[i] < small:
            small = attr[i]
            smallIndex = i
    attr[smallIndex] = attr[start]
    attr[start] = small


def look_for_key(main_box):
    pile = main_box.make_a_


# def selectSort(attr):
#     newArray = []
#     for i in range(len(attr)):
#         smallIndex = selectSmall(attr)
#         newArray.append(attr.pop(smallIndex))
#     return newArray
#
#
# def selectSmall(attr):
#     small = attr[0]
#     smallIndex = 0
#     for i in range(1, len(attr)):
#         if attr[i] < small:
#             small = attr[i]
#             smallIndex = i
#     return smallIndex
# 使用递归求数组的和
def recursionSum(attr):
    if len(attr) < 2:
        return attr[0]
    else:
        return attr[0] + recursionSum(attr[1:])


def fastSort(attr):
    if len(attr) < 2:
        return attr
    else:
        mi = attr[0]
        left = [i for i in attr[1:] if i <= mi]
        right = [i for i in attr[1:] if i > mi]
        return fastSort(left) + [mi] + fastSort(right)


# ------------------------ 迪克斯特拉算法 -------------------------
graph = {}  # 权重图
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

infinity = float("inf")
costs = {}  # 开销表
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}  # 存储父节点
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []  # 处理过的点


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node,cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    neighbor_nodes = graph[node]  # 获取处理节点邻居节点
    cost = costs[node]  # 获取该节点到起点的距离
    for n in neighbor_nodes:  # 循环邻居节点
        new_cost = cost + neighbor_nodes[n]  # 获取经过处理该节点到邻居节点的距离
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
lujing = "fin"
fin_ = parents["fin"]
lujing += "<-%s" % fin_
while fin_ != "start":
    fin_ = parents[fin_]
    lujing += "<-%s" % fin_
print(lujing)
print(costs["fin"])

# ------------------------ 迪克斯特拉算法 -------------------------
if __name__ == '__main__':
    # attr = (1, 3, 6, 9, 12, 18, 19, 20, 34, 39, 40, 41, 41, 55, 56, 60, 61, 62, 63, 64, 65, 70)
    attr = [11, 30, 16, 29, 2, 13, 19, 24, 314, 39, 80, 101, 41, 55, 56, 60, 61, 62, 673, 14, 6, 7]
    # selectSort(attr)

    print(fastSort(attr))
