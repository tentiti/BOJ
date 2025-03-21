from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    current_weight = 0
    current_bridge= deque([0]*bridge_length)
    
    while current_bridge:
        answer += 1
        
        exited_truck = current_bridge.pop()
        current_weight -= exited_truck
        
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.pop(0)
                current_bridge.appendleft(new_truck)
                current_weight += new_truck
            else:
                current_bridge.appendleft(0)
        
    return answer