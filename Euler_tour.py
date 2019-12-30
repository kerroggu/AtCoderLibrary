def euler_tour(visited,current,graph):
    queue=[current]
    while queue:
        if graph[current]:
            queue.append(current) 
            current=graph[current].pop()
        else:
            visited.append(current)
            current=queue.pop()
    return  
