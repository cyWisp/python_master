from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    Integer,
    String,
    Column,
    ForeignKey,
    DateTime,
    MetaData
)


class Base(DeclarativeBase):
    pass


class Rules(Base):
    __tablename__ = 'rules'
    __metadata__ = MetaData()
    rule_id = Column('rule_id', Integer, primary_key=True)
    organization_contract_id = Column('organization_contract_id', Integer,
                                      ForeignKey('organization_contracts.'
                                                 'organization_contract_id'))


class OrganizationContracts(Base):
    __tablename__ = 'organization_contracts'
    __metadata__ = MetaData()
    organization_contract_id = Column('organization_contract_id',
                                      Integer, primary_key=True)

    data_access_group = Column('data_access_group', String(70))
    date_created = Column('date_created', DateTime)
    deactivated_at = Column('deactivated_at', DateTime)


class OrganizationContractUserRole(Base):
    __tablename__ = 'organization_contract_user_role'
    __metadata__ = MetaData()
    organization_contract_user_role_id = Column('organization_contract_user_role_id',
                                                Integer, primary_key=True)

    organization_contract_id = Column('organization_contract_id', Integer,
                                      ForeignKey('organization_contracts.'
                                                 'organization_contract_id'))


class DataUseAgreementEntries(Base):
    __tablename__ = 'data_use_agreement_entries'
    __metadata__ = MetaData()
    data_use_agreement_entry_id = Column('data_use_agreement_entry_id',
                                         Integer, primary_key=True)
    rule_id = Column('rule_id', Integer, ForeignKey('rules.rule_id'))


class DataUseAgreements(Base):
    __tablename__ = 'data_use_agreements'
    __metadata__ = MetaData()
    data_use_agreement_id = Column('data_use_agreement_id', Integer, primary_key=True)
    organization_contract_id = Column('organization_contract_id', Integer,
                                      ForeignKey('organization_contracts.'
                                                 'organization_contract_id'))
