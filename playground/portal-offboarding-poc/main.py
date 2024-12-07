import json
import logging

from config import cfg
from psycopg2 import OperationalError, Error


logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - '
           '%(funcName)s - %(levelname)s: %(message)s',
    level=logging.getLevelName(cfg.log_level.upper())
)
log = logging.getLogger(__name__)


if __name__ == '__main__':

    log.debug(f'Configuration:\n{json.dumps(vars(cfg), indent=4)}')

    from pdb.pdb import PDB
    from pdb.queries import PortalOffBoarding

    log.info(cfg.data_access_group)

    queries = PortalOffBoarding()

    with PDB(
        db_name=cfg.db_name,
        db_user=cfg.db_user,
        db_pass=cfg.db_pass,
        db_host=cfg.db_host,
        db_port=cfg.db_port,
    ) as db:

        org_contract_id = db.read(queries.get_org_contract_id(cfg.data_access_group))[0][0]
        log.info(f'Running offboarding process for {cfg.data_access_group} | {org_contract_id}')

        for name, op in queries.ops.items():
            try:
                log.info(f'Executing {name} | Organization Contract ID: {org_contract_id}.')
                db.run_query(queries.ops[name](org_contract_id))

            except (OperationalError, Error) as e:
                log.error(f'Database operation failed:\n{e}')

        log.info(f'Executing {name} | Data Access Group: {org_contract_id}.')
        db.run_query(queries.delete_dag(cfg.data_access_group))

        if not db.read(queries.validate(cfg.data_access_group)):
            log.info('Offboarding process completed successfully.')
        else:
            log.info('Offboarding process failed.')





