from ctypes import POINTER, c_float, CDLL, Structure, byref
from pathlib import Path
import random

path = Path("dll") / "core.dll"
lib = CDLL(str(path))

# d+定义结构体
class FlightData(Structure):
    _fields_ = [
        ("speed",    c_float),
        ("altitude", c_float),
        ("pitch",    c_float),
        ("roll",     c_float),
        ("fuel",     c_float),
        ("rpm",      c_float),
    ]

# void flight_data_init(FlightData *d)
lib.flight_data_init.argtypes = [POINTER(FlightData)]
lib.flight_data_init.restype  = None

# void update_physics(FlightData *d, float dt, float throttle)
lib.update_physics.argtypes = [POINTER(FlightData), c_float, c_float]
lib.update_physics.restype  = None

# float value_to_angle(float value, float min, float max, float start_angle, float sweep_angle)
lib.value_to_angle.argtypes = [c_float, c_float, c_float, c_float, c_float]
lib.value_to_angle.restype  = c_float

lib.rand_float.argtypes = []
lib.rand_float.restype  = None

# 结构体->指针
aircraft = FlightData()
lib.flight_data_init(byref(aircraft))

throttle_arr = [random.random() for _ in range(60)]
dt = 1.00 / 60.00

for frame in range(600):
    throttle = throttle_arr[(frame // 60) % 60]
    lib.update_physics(byref(aircraft), dt, throttle)
    if frame % 60 == 0:
        # 计算经过时间
        t = frame * dt
        print(f"t={t:4.1f}s | throttle={throttle*100:5.1f}% | "
              f"speed={aircraft.speed:7.2f} | "
              f"rpm={aircraft.rpm:7.1f} | "
              f"fuel={aircraft.fuel:6.1f}")

# angle = lib.value_to_angle(120.0, 0.0, 240.0, 135.0, 270.0)
# print(f"\nvalue_to_angle(120, 0, 240, 135, 270) = {angle:.1f}")