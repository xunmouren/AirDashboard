#include <stdio.h>
#include "flight.h"

int main(void) {
    FlightData aircraft;
    flight_data_init(&aircraft);

    float throttle = 50.0f;
    aircraft.rpm = throttle_to_rpm(throttle);

    printf("========== Flight Status ==========\n");
    printf("Speed     : %.1f km/h\n", aircraft.speed);
    printf("Altitude  : %.1f m\n",  aircraft.altitude);
    printf("Pitch     : %.1f deg\n", aircraft.pitch);
    printf("Roll      : %.1f deg\n", aircraft.roll);
    printf("Fuel      : %.1f L\n",   aircraft.fuel);
    printf("RPM       : %.1f\n",     aircraft.rpm);
    printf("==================================\n");

    return 0;
}