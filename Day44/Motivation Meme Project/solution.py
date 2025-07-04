from collections import deque

def open_lock(deadends, target):
    dead = set(deadends)
    if "0000" in dead:
        return -1
    visited = set("0000")
    queue = deque([("0000", 0)])  # (current_code, steps)

    while queue:
        code, steps = queue.popleft()
        if code == target:
            return steps

        for i in range(4):  # for each wheel
            digit = int(code[i])
            print(digit)
            for move in [-1, 1]:  # turn wheel forward or backward
                new_digit = (digit + move) % 10
                print("New Digit")
                print(new_digit)
                new_code = code[:i] + str(new_digit) + code[i+1:]
                print("New code")
                print(new_code)
                if new_code not in visited and new_code not in dead:
                    visited.add(new_code)
                    print("Visited")
                    print(visited)
                    queue.append((new_code, steps + 1))
                    print("queue")
                    print(queue)
    return -1  # target not reachable

# Main Input Handling
T = int(input())
for _ in range(T):
    N = int(input())
    deadends = input().split()
    target = input().strip()
    print(open_lock(deadends, target))