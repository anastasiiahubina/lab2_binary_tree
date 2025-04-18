from collections import deque
import sys

queue = deque()

for line in sys.stdin:
    command = line.strip()
    if command.startswith("push"):
        _, value = command.split()
        queue.append(int(value))
        print("ok")
    elif command == "pop":
        print(queue.popleft())
    elif command == "front":
        print(queue[0])
    elif command == "size":
        print(len(queue))
    elif command == "clear":
        queue.clear()
        print("ok")
    elif command == "exit":
        print("bye")
        break