import paho.mqtt.client as mqtt


TOPIC = ""
HOSTNAME = "nakyeonko3.local"


def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    make_csvfile()


def make_csvfile(sensor_value):
    print("hello, world")


def mqtt_init():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOSTNAME)  # 접속할 호스트명
    client.loop_start()


mqtt_init()
