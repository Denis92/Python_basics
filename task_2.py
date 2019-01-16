import time


class Microwave:
    """class for working with microwave"""

    def __init__(self, turn_on=True):
        self.turn_on = turn_on
        if not (turn_on):
            print("Микроволновка выключена")
            exit(1)

    def set_timer(self, time_set):
        """method for adjusting the time of work"""
        return time_set

    def start_work(self, time_set, power_set):
        """starting the microwave"""
        temp_time = 0
        start_time = time.time()
        print('Start microwave')
        self._generator_start(power_set)
        while temp_time <= self.set_timer(time_set):
            temp_time = time.time() - start_time
            print(f'Remained {temp_time} second')
        return self.stop_work()

    def stop_work(self):
        """stopping the microwave"""
        self._generator_stop()
        self.set_timer(0)
        print('Stop microwave')
        exit(0)

    def _generator_start(self, power_set):
        """starting the generator"""
        start_config = power_set
        return start_config

    def _generator_stop(self):
        """stopping the generator"""
        stop_config = 0
        return stop_config


mw_1 = Microwave()
start_time = time.time()
mw_1.start_work(10, 600)
