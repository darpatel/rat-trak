import pigpio
import time

# Initialize pigpio
pi = pigpio.pi()
pwm_pin = 18  # Replace with the GPIO pin connected to motor control

# Set PWM frequency and duty cycle
pi.set_mode(pwm_pin, pigpio.OUTPUT)
pi.set_PWM_frequency(pwm_pin, 1000)  # 1 kHz frequency
pi.set_PWM_dutycycle(pwm_pin, 128)   # 50% duty cycle (range is 0-255)

try:
    while True:
        # Motor control logic can be added here
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    pi.set_PWM_dutycycle(pwm_pin, 0)
    pi.stop()
