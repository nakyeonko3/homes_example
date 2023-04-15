import RPi.GPIO as GPIO
import time
from threading import Event, Thread

def servo_motor_control():
    servo_pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    pwm = GPIO.PWM(servo_pin, 50)  # 50Hz (서보모터 PWM 동작을 위한 주파수)
    pwm.start(3.0) #서보의 0도 위치(0.6ms)이동:값 3.0은 pwm주기인 20ms의 3%를 의미하므로,0.6ms됨.
    pwm.ChangeDutyCycle(3.0)   # 서보모터를 0도로 회전(이동)
    time.sleep(1.0)            # 서보 모터가 이동할 시간을 줌
    pwm.ChangeDutyCycle(9.5)  # 서보 모터를 135도로 회전(이동)
    time.sleep(1.0)            # 서보 모터가 이동할 시간을 줌
    pwm.ChangeDutyCycle(0.0)
    pwm.stop()
    GPIO.cleanup()

def servo_motor_interval(event):
    while True:
        servo_motor_control()
        time.sleep(5)
        # print("servo_motor working...")
        if event.is_set():
            break
    # print("servo_motor break...")

class Auto_Thread():
    def __init__(self, func=servo_motor_interval):
        self.func = func
    
    def start(self):
        self.event = Event()
        self.thread = Thread(target=self.func, args=(self.event,))
        self.thread.start()
    
    def join(self):
        self.thread.join()
    
    def stop(self):
        self.event.set()

if __name__ == "__main__":
    auto_servo_thread=Auto_Thread()
    auto_servo_thread.start()
    time.sleep(15)
    auto_servo_thread.stop()
    auto_servo_thread.join()

    auto_servo_thread.start()
    time.sleep(15)
    auto_servo_thread.stop()
    auto_servo_thread.join()

