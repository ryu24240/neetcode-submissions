class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       
        cars = sorted(
                zip(position, speed),
                key=lambda car: car[0],
                reverse=True
                )

        fleet = 0
        previous_time = 0

        for current_position, current_speed in cars:
            arrival_time = (target - current_position) / current_speed
            if arrival_time > previous_time:
                fleet += 1
                previous_time = arrival_time

        return fleet



        