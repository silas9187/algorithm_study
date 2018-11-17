"""
狄克斯特拉算法用于在加权图中查找最短路径，
仅当权重为正时狄克斯特拉算法才有效。
"""
# 解决此问题需要三个散列表
graph = {}
# 储存邻居和前往邻居的节点开销
# 1.起点的邻居
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
# 2.A点的邻居
graph['a'] = {}
graph['a']['fin'] = 1
# 2.B点的邻居
graph['b'] = {}
graph['b']['fin'] = 5
graph['b']['a'] = 3
# 3.终点的邻居
graph['fin'] = {}
# 存储每个节点开销的散列表（节点的开销是指从起点出发到达该点需要的时间）
infinity = float("inf")  # 表示无穷大
costs = {}
costs['a'] = 6
costs['b'] =2
costs['fin'] = infinity
# 储存父节点的散列表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
# 记录下处理过的节点
processed = []
# 第一步：找出未处理中最便宜的节点，即可在最短时间内前往的节点
# 定义找出最便宜节点的函数
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # 遍历所有节点的开销
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 如果当前节点开销更低并且未被处理过
            lowest_cost = cost
            lowest_cost_node = node
    return  lowest_cost_node


node = find_lowest_cost_node(costs)
# 第二步，对于该节点的邻居，检查是否有前往他们更短的开销，如果有，则更新其开销
while node is not None:  # 处理过所有节点后结束
    cost = costs[node]
    neighbors = graph[node]  # 获取该节点的邻居
    for n in neighbors.keys():  # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]  # 更新最便宜的点的邻居节点的开销
        if costs[n] > new_cost:  # 如果经当前节点前往该邻居更近
            costs[n] = new_cost  # 就更新该邻居的开销
            parents[n] = node  # 同时更新该邻居的父节点为当前节点
    processed.append(node)  # 将当前节点标为处理过
# 重复第二步
    node = find_lowest_cost_node(costs)
print(costs['fin'])
