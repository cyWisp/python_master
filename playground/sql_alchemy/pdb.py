import os
import logging

from sqlalchemy import create_engine, Table, select, delete
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, DeclarativeBase, session


logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)


def get_db_session(db_name: str, db_user: str, db_pass: str,
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


db_session, db_engine = get_db_session(
    db_name='portal-dev',
    db_user='postgres',
    db_pass='password',
    db_host='localhost',
    db_port=5432
)


class Base(DeclarativeBase):
    pass

class Rules(Base):
    __table__ = Table('rules', Base.metadata,
                      autoload_with=db_engine)

class OrganizationContracts(Base):
    __table__ = Table('organization_contracts', Base.metadata,
                      autoload_with=db_engine)

class OrganizationContractUserRole(Base):
    __table__ = Table('organization_contract_user_role', Base.metadata,
                      autoload_with=db_engine)

class DataUseAgreementEntries(Base):
    __table__ = Table('data_use_agreement_entries', Base.metadata,
                      autoload_with=db_engine)

class DataUseAgreements(Base):
    __table__ = Table('data_use_agreements', Base.metadata,
                      autoload_with=db_engine)

class PDB:
    RETRIES = 3

    def __init__(self, alchemy_session: session):
        self.db_session = alchemy_session
        self.ops = {
            'delete_org_user_role': self.delete_org_user_role,
            'delete_data_use_agreement_entries': self.delete_data_use_agreement_entries,
            'delete_rules': self.delete_rules,
            'delete_duas': self.delete_duas,
        }

        self.rules = Rules
        self.organization_contracts = OrganizationContracts
        self.organization_contract_user_role = OrganizationContractUserRole
        self.data_use_agreement_entries = DataUseAgreementEntries
        self.data_use_agreements = DataUseAgreementEntries



    def dag_in_db(self, data_access_group):
        stmt = (select(self.organization_contracts)
                .where(self.organization_contracts.data_access_group
                       == data_access_group.lower()))

        if len(self.db_session.execute(stmt).fetchall()) == 0:
            log.info('not in there')
        else:
            log.info('in there')


    def get_org_contract_id(self, data_access_group: str):
        stmt = (select(self.organization_contracts)
                .where(self.organization_contracts.data_access_group
                       == data_access_group.lower()))

        log.info(stmt)

        result = self.db_session.execute(stmt).fetchall()

        log.info(result[0][0].organization_contract_id)

    def delete_org_user_role(self, org_contract_id: int):
        self.db_session.query(
            self.organization_contract_user_role).filter(
            self.organization_contract_user_role.organization_contract_id
            == org_contract_id).delete()

    def delete_data_use_agreement_entries(self, org_contract_id: int):
        stmt = (delete(self.data_use_agreement_entries)
                .where(self.data_use_agreement_entries.organization_contract_id == self.rules.organization_contract_id)
                .where(self.rules.organization_contract_id == org_contract_id))

        self.db_session.execute(stmt)

    def delete_rules(self, org_contract_id: int):
        self.db_session.query(
            self.rules).filter(
            self.rules.organization_contract_id
            == org_contract_id).delete()

    def delete_duas(self, org_contract_id: int):
        self.db_session.query(
            self.data_use_agreements).filter(
            self.data_use_agreements.organization_contract_id
            == org_contract_id).delete()

    def delete_dag(self, data_access_group: str):
        self.db_session.query(
            self.organization_contracts).filter(
            self.organization_contracts.data_access_group
            == data_access_group).delete()


if __name__ == '__main__':

    db = PDB(db_session)

    # db.dag_in_db('cdr-pda-qdas')
    # db.get_org_contract_id('cdr-pda-qdas')
    db.delete_org_user_role(105)
    # db.dag_in_db('not-in-there')


