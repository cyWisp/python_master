import configargparse
import json
import logging
import sys
import paramiko

parser = configargparse.get_argument_parser(
    description='Update and restart script configuration.'
)

parser.add_argument('-l', '--log-level', type=str, required=False, default='info',
                    help='The log level')

parser.add_argument('-h', '--hosts-file', type=str, required=False, default='hosts.txt',
                    help='A list of hosts to connect to.')

parser.add_argument('-s', '--single-host', type=str, required=False, default='127.0.0.1',
                    help='A single host to connect to.')

cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s',
    level=logging.getLevelName(cfg.log_level.upper())
)

log = logging.getLogger(__name__)

log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')


class SSHCommander:
    def __init__(
        self,
        host: str = None,
        hosts_file: str = None,
        user: str = None,
        password: str = None
    ):

        try:
            if not host and not hosts_file:
                raise ValueError('Please provide either a single host or list of hosts.')
            self.hosts = self.read_hosts_file(hosts_file) if hosts_file else [host]

        except ValueError as e:
            log.error(e)
            sys.exit(1)

        log.info('Creating SSH client.')
        self.ssh_client = paramiko.SSHClient()
        self.user, self.password = user, password

        self.results = {}

    def store_results(self, hostname, command, status):
        self.results[hostname] = {command: status}

    def run_single_command(self, command: str) -> None:
        log.info('Setting missing host key policy.')
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        for host in self.hosts:
            self.authenticate(
                host,
                self.user,
                self.password
            )

            try:
                log.info(f'Running {command} on {host}.')

                channel = self.ssh_client.get_transport().open_session()
                channel.exec_command(command)
                exit_code = channel.recv_exit_status()

                log.info(f'Command result status code: {exit_code}')
                result = 'Success' if exit_code == 0 else 'Failed'
                self.store_results(host, command, result)

            except Exception as e:
                log.error(e)
                continue

    @staticmethod
    def read_hosts_file(hosts_list: str) -> list:
        try:
            log.info(f'Reading hosts file: {hosts_list}')

            with open(hosts_list) as hosts:
                return [x.replace('\n', '') for x in hosts.readlines()]

        except Exception as e:
            log.error(e)

    def authenticate(self, host_ip: str, user_name: str, pw: str) -> None:
        try:
            log.info(f'Connecting to {host_ip}')

            self.ssh_client.connect(
                host_ip,
                username=user_name,
                password=pw,
            )

        except Exception as e:
            log.error(e)

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # try:
        #     if self.results:
        #         log.info(f'Command run results: {json.dumps(self.results, indent=4)}')
        #
        #     log.info('Closing SSH client.')
        #     self.ssh_client.close()
        #
        # except Exception as e:
        #     log.error(e)


if __name__ == '__main__':
    with SSHCommander(
        hosts_file='hosts.txt',
        user='wisp',
        password='ADMINforJUSTICE1220!'
    ) as com:
        com.run_single_command('ls')
        com.ssh_client.close()

        log.info(json.dumps(com.results, indent=4))

