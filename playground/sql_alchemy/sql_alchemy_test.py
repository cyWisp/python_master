import os
import logging
from xmlrpc.client import DateTime

from sqlalchemy import (
    create_engine,
    Table,
    Integer,
    Column,
    String,
    select,
    ForeignKey,
    MetaData,
    DateTime
)

from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, DeclarativeBase

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)




if __name__ == '__main__':

    url = URL.create(
        drivername='postgresql',
        username='test',
        host='portal-db-postgres-dev.cluster-cwsrmf1yp1co.us-east-1.rds.amazonaws.com',
        password='EqOvgXiR6f',
        database='test',
        port=5432
    )

    engine = None

    try:
        engine = create_engine(url)
        connection = engine.connect()

    except Exception as e:
        log.error(e)

    session = None

    if engine:
        Session = sessionmaker(bind=engine)
        session = Session()

    # meta = MetaData()

    class Base(DeclarativeBase):
        pass


    class Rules(Base):
        __tablename__ = 'rules'
        __metadata__ = MetaData()
        rule_id = Column('rule_id', Integer, primary_key=True)
        organization_contract_id = Column('organization_contract_id', Integer, ForeignKey('organization_contracts.organization_contract_id'))

    class OrganizationContracts(Base):
        # __table__ = Table('rules', Base.metadata,
        #                   autoload_with=engine)
        __tablename__ = 'organization_contracts'
        __metadata__ = MetaData()
        organization_contract_id = Column('organization_contract_id', Integer, primary_key=True)
        data_access_group = Column('data_access_group', String(70))
        date_created = Column('date_created', DateTime)

    class OrganizationContractUserRole(Base):
        __tablename__ = 'organization_contract_user_role'
        __metadata__ = MetaData()
        organization_contract_user_role_id = Column('organization_contract_user_role_id', Integer, primary_key=True)
        organization_contract_id = Column('organization_contract_id', Integer, ForeignKey('organization_contracts.organization_contract_id'))

    class DataUseAgreementEntries(Base):
        __tablename__ = 'data_use_agreement_entries'
        __metadata__ = MetaData()
        data_use_agreement_entry_id = Column('data_use_agreement_entry_id', Integer, primary_key=True)
        rule_id = Column('rule_id', Integer, ForeignKey('rules.rule_id'))

    class DataUseAgreements(Base):
        __tablename__ = 'data_use_agreements'
        __metadata__ = MetaData()
        data_use_agreement_id = Column('data_use_agreement_id', Integer, primary_key=True)
        organization_contract_id = Column('organization_contract_id', Integer, ForeignKey('organization_contracts.organization_contract_id'))


    # rules = session.query(Rules).all()
    #
    # for rule in rules:
    #     log.info(rule.__dict__['rule_id'])

    stmt = select(Rules).where(Rules.rule_id == 1)
    result = session.execute(stmt).fetchone()
    log.info(result[0].__dict__['rule_id'])

    stmt = select(OrganizationContracts).where(OrganizationContracts.data_access_group == 'test-org-new')
    result = session.execute(stmt).fetchone()
    log.info(result[0].__dict__['organization_contract_id'])

    stmt = select(OrganizationContractUserRole).where(OrganizationContractUserRole.organization_contract_id == 10)

    result = session.execute(stmt).fetchone()
    log.info(result[0].__dict__['organization_contract_id'])

    stmt = select(DataUseAgreementEntries).where(DataUseAgreementEntries.data_use_agreement_entry_id == 125)

    result = session.execute(stmt).fetchone()
    log.info(result[0].__dict__['data_use_agreement_entry_id'])

    stmt = select(DataUseAgreements).where(DataUseAgreements.data_use_agreement_id == 3)
    result = session.execute(stmt).fetchone()
    log.info(result[0].__dict__['data_use_agreement__id'])



