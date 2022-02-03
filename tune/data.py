# -*- coding: utf-8 -*-
import MySQLdb


connect = MySQLdb.connect('localhost', 'root', 'I1QEvAR503', 'tune')
cursor = connect.cursor()


def get_category():
    sql = ("SELECT name FROM tune_admin_product")
    cursor.execute(sql)
    res = cursor.fetchall()
    return res