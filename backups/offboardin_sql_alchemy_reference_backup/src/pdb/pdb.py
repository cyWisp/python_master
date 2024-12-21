import logging
from sys import exit
from datetime import datetime

from .models import (
    Rules,
    OrganizationContracts,
    OrganizationContractUserRole,
    DataUseAgreementEntries,
    DataUseAgreements
)

from sqlalchemy import select, update, delete, create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import (
    DatabaseError,
    DisconnectionError
)


log = logging.getLogger(__name__)


class PDB:
    def __init__(self, db_name: str, db_user: str, db_pass: str,
                 db_host: str, db_port: int = 5432):

        self.db_session, self.db_engine = self._connect(
            db_name=db_name,
            db_user=db_user,
            db_pass=db_pass,
            db_host=db_host,
            db_port=db_port,
        )

        self.rules = Rules
        self.organization_contracts = OrganizationContracts
        self.organization_contract_user_role = OrganizationContractUserRole
        self.data_use_agreement_entries = DataUseAgreementEntries
        self.data_use_agreements = DataUseAgreements

    def _connect(self, db_name: str, db_user: str, db_pass: str,
                 db_host: str, db_port: int = 5432):
        url = URL.create(
            drivername='postgresql',
            username=db_user,
            host=db_host,
            password=db_pass,
            database=db_name,
            port=db_port
        )

        new_engine = create_engine(url).connect()
        new_session = sessionmaker(bind=new_engine)
        return new_session(), new_engine

    def dag_delete_process(self, dag):
        try:
            # org_contract_id = self.get_org_contract_id(dag)

            # self.dag_in_db(dag)
            self.deactivate_dag(dag)
            self.verify_deactivated(dag)

            # self.delete_organization_contract_user_role(org_contract_id)
            # self.delete_data_use_agreement_entries(org_contract_id)
            #
            # self.delete_rules(org_contract_id)
            # self.delete_duas(org_contract_id)
            # self.delete_dag(dag)
            # self.dag_in_db(dag)

        except (
            ValueError,
            DatabaseError,
            DisconnectionError
        ) as e:
            log.error(e)
            exit(1)

    def deactivate_dag(self, dag: str):
        try:
            log.info(f'Deactivating {dag}.')

            stmt = (update(self.organization_contracts)
                    .where(self.organization_contracts.data_access_group == dag)
                    .values(deactivated_at=str(datetime.now())))

            self.db_session.execute(stmt)
            self.db_engine.commit()

        except (DatabaseError, DisconnectionError):
            raise

    def verify_deactivated(self, dag: str):
        try:
            log.info(f'Deactivating {dag}.')

            stmt = (select(self.organization_contracts)
                    .where(self.organization_contracts.data_access_group == dag))

            result = self.db_session.execute(stmt).fetchone()

            if result[0].__dict__['deactivated_at']:
                log.info('DAG successfully deactivated.')
            else:
                log.info('DAG still active')

        except (DatabaseError, DisconnectionError):
            raise

    def dag_in_db(self, dag: str) -> None:
        try:
            log.debug(f'Verifying DAG {dag} no longer exists in the database.')

            stmt = (select(self.organization_contracts)
                    .where(self.organization_contracts.data_access_group
                           == dag.lower()))

            result = self.db_session.execute(stmt).fetchone()

            if not result:
                log.info('DAG successfully removed from the database.')
            else:
                raise ValueError('Operation did not complete successfully.')

        except ValueError as e:
            log.error(e)
            raise

        except (DatabaseError, DisconnectionError):
            raise

    def get_org_contract_id(self, dag: str) -> int:
        try:
            log.debug(f'Querying organization contract ID for {dag}.')

            stmt = (select(self.organization_contracts)
                    .where(self.organization_contracts.data_access_group
                           == dag.lower()))

            result = self.db_session.execute(stmt).fetchone()

            if not result:
                raise ValueError('Organization contract ID not found.')

            else:
                org_contract_id = result[0].__dict__['organization_contract_id']
                log.debug(f'Organization contract ID found: {org_contract_id}.')

                return org_contract_id

        except ValueError:
            raise

        except (DatabaseError, DisconnectionError):
            raise

    def delete_organization_contract_user_role(self, org_contract_id: int) -> None:
        try:
            log.debug(f'Deleting organization contract '
                      f'user role for OCID: {org_contract_id}.')

            stmt = (delete(self.organization_contract_user_role)
                    .where(self.organization_contract_user_role.organization_contract_id
                           == org_contract_id))

            self.db_engine.execute(stmt)
            self.db_engine.commit()

        except (DatabaseError, DisconnectionError):
            raise

    def delete_data_use_agreement_entries(self, org_contract_id: int) -> None:
        try:
            log.debug(f'Deleting data use agreement '
                      f'entries for OCID: {org_contract_id}.')

            stmt = ((delete(self.data_use_agreement_entries)
                    .where(self.data_use_agreement_entries.rule_id
                           == self.rules.rule_id))
                    .where(self.rules.organization_contract_id
                           == org_contract_id))

            self.db_engine.execute(stmt)
            self.db_engine.commit()

        except (DatabaseError, DisconnectionError):
            raise

    def delete_rules(self, org_contract_id: int) -> None:
        try:
            log.debug(f'Deleting rules for OCID: {org_contract_id}.')

            stmt = (delete(self.rules)
                    .where(self.rules.organization_contract_id
                           == org_contract_id))

            self.db_engine.execute(stmt)
            self.db_engine.commit()

        except (DatabaseError, DisconnectionError):
            raise

    def delete_duas(self, org_contract_id: int) -> None:
        try:
            log.debug(f'Deleting organization '
                      f'contract user role for OCID: {org_contract_id}.')

            stmt = (delete(self.data_use_agreements)
                    .where(self.data_use_agreements.organization_contract_id
                           == org_contract_id))

            self.db_engine.execute(stmt)
            self.db_engine.commit()

        except (DatabaseError, DisconnectionError):
            raise

    def delete_dag(self, dag: str) -> None:
        try:
            log.debug(f'Deleting DAG: {dag}.')

            stmt = (delete(self.organization_contracts)
                    .where(self.organization_contracts.data_access_group
                           == dag.lower()))

            self.db_engine.execute(stmt)
            self.db_engine.commit()

        except (DatabaseError, DisconnectionError):
            raise

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
