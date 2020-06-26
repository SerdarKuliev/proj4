import time

while True:

    class TrafficLight:

        def __init__(self, _modes):
            self._modes = "color"

        def _red(self):
            self._modes = "red"
            return(f"Red, wait, {time.sleep(15)} ")   # Думал обратный отсчет получится.


        def _yellow(self):
            self._modes = "yellow"
            return(f"Yellow, wait, {time.sleep(7)} ")


        def _green(self):
            self._modes = "green"
            return(f"Green, go-go-go, {time.sleep(2)} ")



    r = TrafficLight('red')
    print(r._red())
    y = TrafficLight('yellow')
    print(y._yellow())
    g = TrafficLight('green')
    print(g._green())

else:
    pass




