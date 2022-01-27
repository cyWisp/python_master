import paho.mqtt.client as mqtt
import logging

logging.basicConfig(
    format='%(process)d - %(asctime)s- %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()




class MQTTClient(mqtt.Client):
    def __init__(self, name, host, topic):
        self.name = name
        self.host = host
        self.topic = topic

        super().__init__(name)
        self.on_publish = self.on_publish
        self.on_connect = self.on_connect

        self.mqtt_connect()
        # self.on_connect = self.on_connect

    def mqtt_connect(self):
        log.debug(f'Connecting to {self.host}')

        try:
            self.connect(self.host)
            log.debug(f'Successfully connected to {self.host}')
        except Exception as e:
            log.exception(f'Unable to connect:\n{e}')

    def publish_message(self, message):
        log.debug(f'Publishing {message[:32]}...')
        try:
            self.publish(self.topic, message)
        except Exception as e:
            log.exception(f'Unable to publish:\n{e}')

    def on_publish(self, client, userdata, mid):
        log.debug('Message published!')

    def on_connect(self, userdata, flags, rc):
        log.debug(f'Subscribing to {self.topic}')

        try:
            self.subscribe(self.topic)
            log.debug(f'Successfully subscribed to {self.topic}')
        except Exception as e:
            log.exception(f'Something went wrong:\n{e}')

    def on_message(self, client, userdata, msg):
        log.debug(msg.topic)
        log.debug(msg.payload)
        self.disconnect()










