import heapq

def min_cost(items):
    heapq.heapify(items)
    total_cost = 0
    
    while len(items) > 1:
        x = heapq.heappop(items)
        y = heapq.heappop(items)
        
        cost = x + y
        
        total_cost += cost
        
        heapq.heappush(cables, cost)
    
    return total_cost


if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    result = min_cost(cables)
    print("Connecting cables minimal cost:", result)
