from payloads.payloads import Payloads
import paho.mqtt.client as mqtt

import json
import logging
import random
import time

logging.basicConfig(
    format='%(process)d - %(asctime)s- %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()

MQTT_MESSAGE = json.dumps({
    'test': 'value',
    'another': 'test'
})

MQTT_TOPIC = 'test_topic'

def on_publish(client, userdata, mid):
    log.debug('Message published')

def on_connect(client):
    client.subscribe(MQTT_TOPIC)
#
# def on_message(client, userdata, msg):
#     log.debug(msg.topic)
#     log.debug(msg.payload)
#     client.disconnect()


if __name__ == '__main__':
    mqtt_client = mqtt.Client('test_client')

    # Register callback functions
    mqtt_client.on_publish = on_publish
    mqtt_client.on_connect = on_connect

    # connect with MQTT Broker
    mqtt_client.connect('10.0.0.108')

    mqtt_client.subscribe('test_topic')

    max_payloads = 5
    counter = 0

    while True:
        if counter == max_payloads: break
        p = random.choice(list(Payloads.ALL_PAYLOADS.value))

        log.debug(f'sending {p}')
        mqtt_client.publish('test_topic', Payloads.ALL_PAYLOADS.value[p])
        counter += 1

        time.sleep(2)




