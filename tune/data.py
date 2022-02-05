# -*- coding: utf-8 -*-
from pprint import pprint

import MySQLdb

connect = MySQLdb.connect('localhost', 'root', 'I1QEvAR503', 'tune')
cursor = connect.cursor()


def get_category():
    sql = "SELECT * FROM tune_admin_category"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_products(category_id):
    sql = f"SELECT name FROM tune_admin_product WHERE category_id = {category_id} and sell != 1"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_detail_product(name_product):
    sql = f"SELECT * FROM tune_admin_product WHERE name = '{name_product}'"
    cursor.execute(sql)

    return cursor.fetchall()[0]

