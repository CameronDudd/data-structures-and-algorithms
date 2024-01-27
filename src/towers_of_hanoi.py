"""TOWERS OF HANOI"""

from typing import List

from utils.stack import HanoiStack


def user_select_stack(stacks: List[HanoiStack]) -> HanoiStack:
    """stay in loop until use has selected a stack"""
    choices = {_.name[0] for _ in stacks}  # first letter of each stack name
    while True:
        for stk in stacks:
            print(f"Enter {stk.name[0]} for {stk.name}")
        user_input = input("Choice: ")
        if user_input in choices:
            for stk in stacks:
                if user_input == stk.name[0]:
                    return stk


def main() -> None:
    """
    main
    todo:
        - better handling of empty stacks
        - UI improvements
        - DRY out code
    """
    left_stack = HanoiStack("Left")
    middle_stack = HanoiStack("Middle")
    right_stack = HanoiStack("Right")
    stacks = [left_stack, middle_stack, right_stack]

    num_disks = 0
    while num_disks < 3:
        num_disks_input = input("Disks (>=3):")
        if num_disks_input.isnumeric():
            num_disks = int(num_disks_input)

    for disk_num in range(num_disks, 0, -1):
        left_stack.push(disk_num)

    optimal_moves = (2**num_disks) - 1
    print(f"{optimal_moves=}")

    num_user_moves = 0
    while right_stack.size != num_disks:
        print("==========================")
        print("......Current Stacks......")
        for stack in stacks:
            print(stack)
        print("==========================")
        while True:
            print("choose stack to take from")
            from_stack = user_select_stack(stacks)
            if from_stack.is_empty:
                print("cannot take from empty stack")
                continue
            from_stack_disk = from_stack.peek()
            assert from_stack_disk is not None, ""
            print("chooes stack to move to")
            to_stack = user_select_stack(stacks)
            to_stack_disk = to_stack.peek()
            if to_stack_disk is None or from_stack_disk < to_stack_disk:
                disk = from_stack.pop()
                to_stack.push(disk)
                num_user_moves += 1
                break
            print("invalid move")
    print("\n\n\n...Current Stacks...")
    print("==========================")
    for stack in stacks:
        print(stack)
    print("==========================")
    print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {optimal_moves}")


if __name__ == "__main__":
    main()
