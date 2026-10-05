from ctypes import POINTER, c_float, CDLL, Structure, byref
from pathlib import Path

# DLL路径
_dll_path = Path(__file__).parent.parent.parent / "dll" / "core.dll"
lib = CDLL(str(_dll_path))


class FlightData(Structure):
    _fields_ = [
        ("speed",    c_float),
        ("altitude", c_float),
        ("pitch",    c_float),
        ("roll",     c_float),
        ("fuel",     c_float),
        ("rpm",      c_float),
    ]


# 函数签名
lib.flight_data_init.argtypes = [POINTER(FlightData)]
lib.flight_data_init.restype  = None

lib.update_physics.argtypes = [POINTER(FlightData), c_float, c_float]
lib.update_physics.restype  = None

lib.value_to_angle.argtypes = [c_float, c_float, c_float, c_float, c_float]
lib.value_to_angle.restype  = c_float

lib.rand_float.argtypes = []
lib.rand_float.restype  = c_float


def init_flight_data():
    """创建并初始化一个 FlightData 实例"""
    data = FlightData()
    lib.flight_data_init(byref(data))
    return data


def update_flight(data, dt, throttle):
    """更新速度、转速、油量"""
    lib.update_physics(byref(data), dt, throttle)


def value_to_angle(value, min_val, max_val, start_angle, sweep_angle):
    """数值 → 仪表盘指针角度"""
    return lib.value_to_angle(value, min_val, max_val, start_angle, sweep_angle)


def speed_to_angle(speed):
    """空速专用：0~1000 km/h → 135° 起，扫 270°"""
    return value_to_angle(speed, 0.0, 1000.0, 135.0, 270.0)