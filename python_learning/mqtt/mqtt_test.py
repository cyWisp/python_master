import paho.mqtt.client as mqtt
import logging
import json

HOST = '10.0.0.108'

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

def on_message(client, userdata, message):
    rec = message.payload.decode("utf-8")
    print(f'received: {rec} | type: {type(rec)}')
    rec_dict = json.loads(rec)
    print(rec_dict['person'])

if __name__ == '__main__':
    log.debug('creating client')
    new_client = mqtt.Client('test_client')
    new_client.on_publish = on_publish
    new_client.on_message = on_message

    log.debug('connecting')
    new_client.connect(HOST)

    # log.debug('starting loop')
    # new_client.loop_start()

    log.debug('subscribing')
    new_client.subscribe('/python/test')

    new_client.loop_forever()

    # log.debug('terminating the loop')
    # new_client.loop_stop()

    # log.debug('publishing example json')
    # new_client.publish('/python/test', json.dumps(EXAMPLE_PAYLOAD))















