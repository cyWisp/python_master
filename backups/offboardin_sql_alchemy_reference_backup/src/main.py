import logging
from config import cfg


logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - '
           '%(funcName)s - %(levelname)s: %(message)s',
    level=logging.getLevelName(cfg.log_level.upper())
)
log = logging.getLogger(__name__)


if __name__ == '__main__':
    from backups.offboardin_sql_alchemy_reference_backup.src.pdb.pdb import PDB

    with PDB(
        db_name=cfg.db_name,
        db_user=cfg.db_user,
        db_pass=cfg.db_pass,
        db_host=cfg.db_host,
        db_port=cfg.db_port,
    ) as db:
        log.info(f'Initiating offboarding process for DAG: {cfg.data_access_group}')
        db.dag_delete_process(cfg.data_access_group)
