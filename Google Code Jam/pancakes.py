# solution to problem B. Revenge of the Pancakes

T = int(input()) # number of test cases

for case in range(1, T + 1):
    stack = input()
    stack_length = len(stack)
    completed = "+" * stack_length
    count = 0

    while stack != completed:
        print("Stack:", stack)
        flag = False
        for place, pancake in enumerate(stack):
            if pancake == "-":
                flag = True
            elif flag:
                ending = stack[place:]
                start = ''.join(["+" if p == "-" else "-" for p in stack[place - 1::-1]])
                print("Start:", start, "end:", ending)  # comment or delete later
                stack = start + ending
                count += 1
                print("flipped middle")  # comment or delete later
                break
        else:
            print("flipped ending")  # comment or delete later
            if flag:
                stack = ''.join(["+" if p == "-" else "-" for p in stack[::-1]])
                count += 1
    print("Case #{}: {}".format(case, count))
