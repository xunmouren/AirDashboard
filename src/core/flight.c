#include "flight.h"

// EXPORT 让函数在DLL里可以被外部(Python)看到
EXPORT void flight_data_init(FlightData *d) {
    d->speed    = 0.0f;
    d->altitude = 0.0f;
    d->pitch    = 0.0f;
    d->roll     = 0.0f;
    d->fuel     = 500.0f;
    d->rpm      = 0.0f;
}

// 把油门百分比(0~100)换算成发动机转速(RPM)
EXPORT float throttle_to_rpm(float throttle_percent) {
    if (throttle_percent < 0.0f)   throttle_percent = 0.0f;
    if (throttle_percent > 100.0f) throttle_percent = 100.0f;
    return throttle_percent * 40.0f;
}

// 把任意数值映射成仪表盘指针的角度,仪表盘最核心的换算函数
EXPORT float value_to_angle(float value, float min, float max,
                            float start_angle, float sweep_angle) {
    if (max <= min) return start_angle;
    float ratio = (value - min) / (max - min);
    if (ratio < 0.0f) ratio = 0.0f;
    if (ratio > 1.0f) ratio = 1.0f;
    return start_angle + ratio * sweep_angle;
}