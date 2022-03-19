from time import sleep
from death import death
import datetime

test_death = death(1, "cliff", "Limgrave")

print(test_death.to_string())

sleep(10)

test_death.update(2, "Sentry", "Stormveil Castle")

print(test_death.to_string())
