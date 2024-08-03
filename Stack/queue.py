from collections import deque
s=[]
dq=deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(dq)