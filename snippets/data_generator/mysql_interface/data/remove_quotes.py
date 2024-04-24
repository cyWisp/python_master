#!/usr/bin/env python
import random

if __name__ == '__main__':

    # file_name = 'comics.csv'
    #
    # with open(file_name) as f:
    #     content = [x.replace('"', '') for x in f.readlines()]
    #
    # numbered_content = [f'{index + 1}, {c}' for index, c in enumerate(content)]
    #
    # with open('comics_updated.csv', 'w') as f:
    #     f.writelines(numbered_content)



    # purchases = []

    # for i in range(60):
    #     purchase_id = i
    #     customer_id = random.randint(1, 35)
    #     order_date = f'{random.randint(2018, 2023)}-{random.randint(1, 12)}-{random.randint(1, 28)}'
    #
    #     year = order_date.split('-')[0]
    #     month = order_date.split('-')[-2]
    #     day = order_date.split('-')[-1]
    #
    #     if int(month) < 10:
    #         month = f'0{month}'
    #
    #     if int(day) < 10:
    #         day = f'0{day}'
    #
    #     order_date = '-'.join([year, month, day])
    #     new_purchase = f'{purchase_id}, {customer_id}, {order_date}\n'
    #
    #     print(new_purchase)
    #     purchases.append(new_purchase)

    purchase_details = []

    for i in range(65):
        purchase_id = random.randint(1, 59)
        comic_id = random.randint(1, 50)
        qty = random.randint(1, 5)

        purchase_details.append(f'{purchase_id}, {comic_id}, {qty}\n')

    with open('purchase_details.csv', 'w') as f:
        f.writelines(purchase_details)
