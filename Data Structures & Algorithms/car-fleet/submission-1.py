class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for car in cars:
            pos, sp = car
            time = (target - pos) / sp
            if not(stack and time <= stack[-1]):
                stack.append(time)
        return len(stack)
        