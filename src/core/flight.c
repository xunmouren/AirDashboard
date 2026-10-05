#include <stdlib.h>
#include "flight.h"

#define MAX_SPEED 1000.0f  // 速度上限
#define MAX_ACCEL 200.0f   // 最大加速度
#define MAX_FUEL_RATE 5.0f // 满油门油耗

// 初始化飞行数据
EXPORT void flight_data_init(FlightData *d) {
    d->speed    = 0.0f;
    d->altitude = 0.0f;
    d->pitch    = 0.0f;
    d->roll     = 0.0f;
    d->fuel     = 500.0f;
    d->rpm      = 0.0f;
}

// 油门百分比(0~100)→转速 RPM
EXPORT float throttle_to_rpm(float throttle_percent) {
    if (throttle_percent < 0.0f)   throttle_percent = 0.0f;
    if (throttle_percent > 100.0f) throttle_percent = 100.0f;
    return throttle_percent * 40.0f;
}

// 数值→仪表盘指针角度
EXPORT float value_to_angle(float value, float min, float max,
                            float start_angle, float sweep_angle) {
    if (max <= min) return start_angle;
    float ratio = (value - min) / (max - min);
    if (ratio < 0.0f) ratio = 0.0f;
    if (ratio > 1.0f) ratio = 1.0f;
    return start_angle + ratio * sweep_angle;
}

// 伪随机浮点数
EXPORT float rand_float(void) {
    return (float)rand() / (float)RAND_MAX;
}

// 状态更新
EXPORT void update_physics(FlightData *d, float dt, float throttle) {
    if (d == NULL || dt <= 0.0f) return;

    // 油门0~1
    if (throttle < 0.0f) throttle = 0.0f;
    if (throttle > 1.0f) throttle = 1.0f;

    // 油门→转速
    d->rpm = throttle_to_rpm(throttle * 100.0f);

    // 油门→速度
    d->speed += throttle * MAX_ACCEL * dt;
    if (d->speed > MAX_SPEED) d->speed = MAX_SPEED;
    if (d->speed < 0.0f) d->speed = 0.0f;

    // 油门→油耗
    d->fuel -= throttle * MAX_FUEL_RATE * dt;
    if (d->fuel < 0.0f) d->fuel = 0.0f;
}