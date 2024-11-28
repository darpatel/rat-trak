import lgpio
import time

# Define configuration
PWM_PIN = 18  # GPIO pin connected to the motor controller
FREQ = 100     # PWM frequency in Hz (typical for servo signals)

# Open GPIO chip
h = lgpio.gpiochip_open(0)

try:
    while True:
        # Prompt the user for pulse width input
        pulse_width = float(input("Enter pulse width (1000 to 2000 μs): "))
        
        if 1000 <= pulse_width <= 2000:
            lgpio.tx_servo(h, PWM_PIN, int(pulse_width))
            print(f"Pulse width set to {pulse_width} μs")
        else:
            print("Invalid input. Enter a value between 1000 and 2000.")
except KeyboardInterrupt:
    print("Exiting gracefully...")
    # Stop sending PWM signal by setting pulse width to 0
    lgpio.tx_servo(h, PWM_PIN, 0)
finally:
    lgpio.gpiochip_close(h)
    print("GPIO cleaned up.")



