
class PortalOffBoarding():
    def __init__(self):
        self.ops = {
            'delete_org_user_role': self.delete_org_user_role,
            'delete_data_use_agreement_entries': self.delete_data_use_agreement_entries,
            'delete_rules': self.delete_rules,
            'delete_duas': self.delete_duas,
        }

    def validate(self, data_access_group: str) -> str:
        return f'''
            SELECT *
            FROM organization_contracts
            WHERE data_access_group ILIKE \'{data_access_group}\'
        '''

    def get_org_contract_id(self, data_access_group: str) -> str:
        return f'''
            SELECT organization_contract_id
            FROM organization_contracts
            WHERE data_access_group ILIKE \'{data_access_group}\'
        '''

    def delete_org_user_role(self, org_contract_id: int) -> str:
        return f'''
            DELETE FROM organization_contract_user_roles
            WHERE organization_contract_id = {str(org_contract_id)}
        '''

    def delete_data_use_agreement_entries(self, org_contract_id: int) -> str:
        return f'''
            DELETE FROM data_use_agreement_entries
            USING rules
            WHERE rules.organization_contract_id = {str(org_contract_id)}
        '''

    def delete_rules(self, org_contract_id: int) -> str:
        return f'''
            DELETE FROM rules
            WHERE organization_contract_id = {str(org_contract_id)}
        '''

    def delete_duas(self, org_contract_id: int) -> str:
        return f'''
            DELETE FROM data_use_agreements
            WHERE organization_contract_id = {str(org_contract_id)}
        '''

    def delete_dag(self, data_access_group: str) -> str:
        return f'''
            DELETE FROM organization_contracts
            WHERE data_access_group ILIKE \'{data_access_group}\'
        '''
