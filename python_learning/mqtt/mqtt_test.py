import paho.mqtt.client as mqtt
import logging
import json

HOST_NAME = '10.0.0.108'

EXAMPLE_PAYLOAD = {
    'person': {
        'name': 'rob',
        'age': 36
    },
    'car': {
        'make': 'ford',
        'model': 'mustang'
    }
}

logging.basicConfig(
    format='%(process)d - %(asctime)s- %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()

def on_publish(client, userdata, mid):
    log.debug('Message Published')

if __name__ == '__main__':
    log.debug('creating client')
    new_client = mqtt.Client('test_client')
    new_client.on_publish = on_publish

    log.debug('connecting')
    new_client.connect(HOST_NAME)

    log.debug('subscribing')
    new_client.subscribe('test_topic')

    log.debug('publishing example json')
    new_client.publish('test_topic', json.dumps(EXAMPLE_PAYLOAD))













