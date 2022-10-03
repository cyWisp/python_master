#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

if __name__ == '__main__':
    import hr
    import disgruntled

    payroll_system = hr.PayrollSystem()

    payroll_system.calculate_payroll([
        hr.SalaryEmployee(1, 'John Smith', 1500),
        hr.HourlyEmployee(2, 'Bill Murray', 40, 15),
        hr.CommissionEmployee(3, 'Sam Houston', 1000, 250),
        disgruntled.DisgruntledEmployee(4, 'Bob')
    ])
