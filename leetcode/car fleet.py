class Solution:
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:
        cars, time = [], []
        for p, s in zip(position, speed):
            cars.append([p, s])

        for p, s in sorted(zip(position, speed)):
            time.append((target-p)/s)

        result, temp = 0, 0
        for t in reversed(time):
            if t > temp:
                result += 1
                temp = t

        return result

