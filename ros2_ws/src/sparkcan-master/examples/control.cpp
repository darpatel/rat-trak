#include <iostream>
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

        // Configure and burn parmaters for Redline
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
            
            motor.SetVoltage(1);
        }
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        return -1;
    }

    return 0;
}
