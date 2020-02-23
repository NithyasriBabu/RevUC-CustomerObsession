"""Import json data from CSV file to Datababse"""
# importing the data using this could take a really really long time 
# Dont Use

import os
import csv
from apis.models import Products, Households, Transactions
from django.core.management.base import BaseCommand
from datetime import datetime
from customer.settings import BASE_DIR

class Command(BaseCommand):
    def import_products(self):
        file_path = os.path.join(BASE_DIR, 'processed_data','5000_products_prosessed.csv')
        print(file_path, 'data_folder')
        with open(file_path, encoding='utf-8') as data_file:
            data = csv.reader(data_file)
            i=0
            for product_data in data:
                product_id = product_data[0]
                department = product_data[1]
                commodity = product_data[2]
                brand_type = product_data[3]
                organic = product_data[4]

                try:
                    product, created = Products.objects.get_or_create(
                        product_id= product_id,
                        department=department,
                        commodity=commodity,
                        brand_type=brand_type,
                        organic=organic)
                    
                    if created:
                        product.save()
                        display_format = "{} Product, {}, has been saved."
                        print(display_format.format(i, product))
                    else:
                        display_format = "{} Product, {}, already in DB."
                        print(display_format.format(i, product))

                except Exception as ex:
                    print(str(ex))
                    msg = "\n\nSomething went wrong saving this product: {}\n{}".format(product_id, str(ex))
                    print(msg)
                finally:
                    i += 1

        
    def import_households(self):
        file_path = os.path.join(BASE_DIR, 'processed_data','5000_households_prosessed.csv')
        print(file_path, 'data_folder')
        with open(file_path, encoding='utf-8') as data_file:
            data = csv.reader(data_file)
            i=0
            for household_data in data:
                hshd_id = household_data[0]
                loyalty = household_data[1]
                age_range = household_data[2]
                marital_status = household_data[3]
                income_range = household_data[4]
                homeowner = household_data[5]
                hshd_comp = household_data[6]
                hh_size = household_data[7]
                children = household_data[8]

                try:
                    household, created = Households.objects.get_or_create(
                        hshd_id=hshd_id,
                        loyalty=loyalty,
                        age_range=age_range,
                        marital_status=marital_status,
                        income_range=income_range,
                        homeowner=homeowner,
                        hshd_comp=hshd_comp,
                        hh_size=hh_size,
                        children=children)
                            
                    if created:
                        household.save()
                        display_format = "{} Household, {}, has been saved."
                        print(display_format.format(i, household))
                    else:
                        display_format = "{} Household, {}, already in DB."
                        print(display_format.format(i, household))

                except Exception as ex:
                    print(str(ex))
                    msg = "\n\nSomething went wrong saving this product: {}\n{}".format(hshd_id, str(ex))
                    print(msg)
                finally:
                    i += 1

    def import_transactions(self):
        file_path = os.path.join(BASE_DIR, 'processed_data','5000_transactions_prosessed.csv')
        print(file_path, 'data_folder')
        with open(file_path, encoding='utf-8') as data_file:
            data = csv.reader(data_file)
            i=0
            for transactions_data in data:
                hshd_id = transactions_data[0]
                bskt_id = transactions_data[1]
                trans_date = transactions_data[2]
                product_id = transactions_data[3]
                spend = transactions_data[4]
                units = transactions_data[5]
                store_region = transactions_data[6]
                week_num = transactions_data[7]
                year = transactions_data[8]

                try:
                    transaction, created = Transactions.objects.get_or_create(
                        hshd_id=hshd_id,
                        bskt_id=bskt_id,
                        trans_date=trans_date,
                        product_id=product_id,
                        spend=spend,
                        units=units,
                        store_region=store_region,
                        week_num=week_num,
                        year=year)
                            
                    if created:
                        transaction.save()
                        display_format = "{} Transaction, {}, has been saved."
                        print(display_format.format(i, transaction))
                    else:
                        display_format = "{} Transaction, {}, already in DB."
                        print(display_format.format(i, transaction))
                except Exception as ex:
                    print(str(ex))
                    msg = "\n\nSomething went wrong saving this product: {}\n{}".format(bskt_id, str(ex))
                    print(msg)
                finally:
                    i += 1

    def handle(self, *args, **options):
        """Call the function to import data"""
        self.import_products()
        self.import_households()
        self.import_transactions()