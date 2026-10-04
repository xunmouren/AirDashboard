#pragma once

// 让C++编译器按C的方式编译函数
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    float speed;        // 空速 km/h
    float altitude;     // 高度 m
    float pitch;        // 俯仰角 °
    float roll;         // 横滚角 °
    float fuel;         // 油量 L
    float rpm;          // 发动机转速 RPM
} FlightData;

// 检查是不是 Windows
#ifdef _WIN32
    //  Windows下,标记这个函数要导出
    #define EXPORT __declspec(dllexport)
#else
    // Linux/macOS下,EXPORT 是空的
    #define EXPORT
#endif

EXPORT void  flight_data_init(FlightData *d);
EXPORT float throttle_to_rpm(float throttle_percent);
EXPORT float value_to_angle(float value, float min, float max, float start_angle, float sweep_angle);
EXPORT float rand_float(void);
EXPORT void update_physics(FlightData *d, float dt, float throttle);

#ifdef __cplusplus
}

#endif