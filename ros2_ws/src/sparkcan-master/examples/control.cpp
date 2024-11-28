#include <iostream>
#include <iomanip>
#include <chrono>
#include <ctime>
#include "SparkMax.hpp"
#include "SparkFlex.hpp"

/*
This has been tested with the SPARK MAX while connected to an AndyMark 775 RedLine Motor and
with a Spark Flex connected to a NEO Vortex Brushless Motor.
*/

int main()
{
    try
    {
        // Initialize SparkMax object with CAN interface and CAN ID
        SparkMax motor("can0", 1);

        // Configure and burn parameters for Redline
        motor.SetIdleMode(IdleMode::kBrake);
        motor.SetMotorType(MotorType::kBrushless);
        motor.SetInverted(true);
        motor.BurnFlash();

        // Loop for 10 seconds
        auto start = std::chrono::high_resolution_clock::now();
        while (std::chrono::duration_cast<std::chrono::seconds>(
                   std::chrono::high_resolution_clock::now() - start)
                   .count() < 10)
        {
            // Enable and run motors
            motor.Heartbeat();
            motor.SetDutyCycle(0.05);

            double voltage = 1.0; // Voltage value
            motor.SetVoltage(voltage);

            // Get current time
            auto now = std::chrono::system_clock::now();
            std::time_t now_time = std::chrono::system_clock::to_time_t(now);
            
            // Print timestamp and voltage
            std::cout << std::put_time(std::localtime(&now_time), "%Y-%m-%d %H:%M:%S")
                      << " - Voltage: " << voltage << " V" << std::endl;

            std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Slow output rate
        }
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        return -1;
    }

    return 0;
}
