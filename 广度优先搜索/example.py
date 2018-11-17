from collections import  deque

# 创建字典
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] =[]


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    # 创建一个双端队列
    search_queue = deque()
    # 将你的邻居都加入到这个搜索队列中
    search_queue += graph['you']
    # 记录被搜索过的人
    searched = []
    # 只要队列不为空
    while search_queue:
        person = search_queue.popleft()
        # 当这个人没被检查过时才进行检查
        if person not in searched:
            if person_is_seller(person):
                print(person+' is the one')
                return True
            else:
                # 将被检查人的邻居加入检查队列中
                search_queue += graph[person]
                # 将此人标记为已检查
                searched.append(person)
    print('nobody is seller')
    return False


search('you')