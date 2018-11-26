"""贪婪算法：每步都选择局部最优解，最终得到的就是全局最优解或者得到非常接近的解"""
# 包含要覆盖的州
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}# 传入一个数组，它被转换为集合
# 可供选择的广播台清单
stations = {}
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}
# 存储最终选择的广播电台
final_stations = set()
while states_needed:
    best_station = None
    states_covered =set()  # 包含该广播电台覆盖的所以未覆盖的州
    for station ,states_for_station in stations.items():
        convered = states_needed & states_for_station  # 集合求交集
        print(convered)
        if len(convered) > len(states_covered):
            best_station = station
            states_covered = convered
    states_needed -= states_covered
    final_stations.add(best_station)


print(final_stations)