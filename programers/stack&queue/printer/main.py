
from collections import deque

def solution(priorities, location):
    answer = 0
    
    priorities_idx = deque([priority,idx] for idx,priority in enumerate(priorities))

    while True:
        item = priorities_idx.popleft()
        if priorities_idx and item[0] < max(priorities_idx)[0]:
            priorities_idx.append(item)

        else:
            answer += 1
            if item[1] == location:
                break

    return answer