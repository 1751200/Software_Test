state_diagram = {
    'nodes': [
        '空闲',
        '等待输入密码',
        '进入账户',
        '等待二次输入密码',
        '吞卡',
        '等待三次输入密码',
        '退卡'
    ],
    'edges': [
        (0, 1, '插入银行卡'),
        (1, 2, '输入密码正确'),
        (1, 3, '等待第二次输入密码'),
        (1, 4, '超过2分钟未操作'),
        (2, 6, '结束操作'),
        (3, 2, '输入密码正确'),
        (3, 4, '超过2分钟未操作'),
        (3, 5, '输入密码错误'),
        (5, 2, '输入密码正确'),
        (5, 4, '超过2分钟未操作'),
        (5, 6, '输入密码错误'),
        (6, 0, '取卡')
    ]
}


def tran_tree(graph):
    tree = {'nodes': [graph['nodes'][0]], 'edges': []}
    nodes = [0]
    init = True
    map = [0 for _ in range(len(graph['nodes']))]
    while len(nodes):
        node = nodes.pop()
        for edge in graph['edges']:
            if edge[0] == node and (edge[0] != 0 or init):
                init = False
                tree['nodes'].append(graph['nodes'][edge[1]])
                nodes.append(edge[1])
                map[edge[1]] = len(tree['nodes']) - 1
                tree['edges'].append((map[edge[0]], map[edge[1]], edge[2]))
    return tree


code = r'''def tran_tree(graph):
    tree = {'nodes': [graph['nodes'][0]], 'edges': []}
    nodes = [0]
    init = True
    map = [0 for _ in range(len(graph['nodes']))]
    while len(nodes):
        node = nodes.pop()
        for edge in graph['edges']:
            if edge[0] == node and (edge[0] != 0 or init):
                init = False
                tree['nodes'].append(graph['nodes'][edge[1]])
                nodes.append(edge[1])
                map[edge[1]] = len(tree['nodes']) - 1
                tree['edges'].append((map[edge[0]], map[edge[1]], edge[2]))
    return tree'''


if __name__ == '__main__':
    # end_points = [i for i in range(len(graph['nodes'])) if i not in [e[0] for e in graph['edges']]]
    print(len(tran_tree((state_diagram))['nodes']))
