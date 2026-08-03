class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for car in cars:
            pos, sp = car
            if not(stack and (target - pos) / sp <= stack[-1]):
                stack.append((target - pos) / sp)
        return len(stack)
        