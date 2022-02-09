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


def get_products(category_name):

    sql = f"SELECT tune_admin_seriescategory.id, tune_admin_product.name" \
          f" FROM tune_admin_seriescategory, tune_admin_product" \
          f" WHERE tune_admin_seriescategory.category = '{category_name}'" \
          f" AND tune_admin_product.series_id = tune_admin_seriescategory.id" \
          f" AND sell != 1"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_current_product():
    sql = f"SELECT tune_admin_product.series_id, tune_admin_seriescategory.category " \
          f" FROM tune_admin_product, tune_admin_seriescategory " \
          f"WHERE tune_admin_product.series_id = tune_admin_seriescategory.id AND sell != 1;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_series(name_series):
    sql = f"SELECT category FROM tune_admin_seriescategory WHERE category LIKE '%{name_series}%';"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_detail_product(name_product):
    sql = f"SELECT * FROM tune_admin_product WHERE name = '{name_product}'"
    cursor.execute(sql)

    return cursor.fetchall()[0]


def get_all_products():
    sql = f"SELECT name FROM tune_admin_product WHERE sell != 1"
    cursor.execute(sql)

    return cursor.fetchall()


def get_re_messages():
    import datetime

    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)
    """
    Возвращает все посты к пересылке
    :return:
    """
    sql = f"SELECT image_1, image_2, image_3, text " \
          f" FROM tune_admin_product WHERE sell != 1" \
          f" and next_edition < '{today}' and next_edition < '{tomorrow}'"
    cursor.execute(sql)

    return cursor.fetchall()