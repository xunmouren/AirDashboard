#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include "flight.h"

int main(void) {
    FlightData aircraft;
    srand((unsigned int)time(NULL));
    // 初始化飞行数据
    flight_data_init(&aircraft);

    /* 输出测试
    printf("========== Flight Status ==========\n");
    printf("Speed     : %.1f km/h\n", aircraft.speed);
    printf("Altitude  : %.1f m\n",  aircraft.altitude);
    printf("Pitch     : %.1f deg\n", aircraft.pitch);
    printf("Roll      : %.1f deg\n", aircraft.roll);
    printf("Fuel      : %.1f L\n",   aircraft.fuel);
    printf("RPM       : %.1f\n",     aircraft.rpm);
    printf("==================================\n");
    */

    // 时间步长
    float dt = 1.0f / 60.0f;
    // 预生成油门表
    float throttle_arr[60];
    for (int i = 0; i < 60; i++) {
        throttle_arr[i] = rand_float();
    }

    for (int frame = 0; frame < 600; frame++) {
        float throttle = throttle_arr[(frame / 60) % 60];
        update_physics(&aircraft, dt, throttle);

        if (frame % 60 == 0) {
            printf("t=%4.1fs | throttle=%5.1f%% | speed=%7.2f | rpm=%7.1f | fuel=%6.1f\n",
                   frame * dt,
                   throttle * 100.0f,
                   aircraft.speed,
                   aircraft.rpm,
                   aircraft.fuel);
        }
    }
    return 0;
}