import pymysql
import requests
import json

def get_conn():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        database="views",
        password="root",
        charset="utf8",
        port=3306
    )

    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql, *args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res



def bigdata_toplist():
    sql = "select * from basic_info"
    res = query(sql)
    data = []
    for i in res:
        for j in i:
            data.append(j)
    return res

def bigdata_company():
    sql = "SELECT * from package_rank ORDER BY package DESC"
    res = query(sql)
    data = []
    for i in res:
        data.append({'name': i[0], 'value': float(i[1])})
    # print(data)
    return data

def bigdata_chart3():
    sql = "SELECT * from chart3"
    res = query(sql)
    data = []
    for i in res:
        data.append({'name': i[0], 'value': int(i[1])})
    return data

def bigdata_sales_rank():
    sql = "select * from goods_sales_rank"
    res = query(sql)
    data = []
    for i in res:
        data.append(i)
    return data

def bigdata_chart2_data():
    sql = "select * from chart2"
    res = query(sql)
    ydata = []
    xdata = []
    for i in res:
        ydata.append({'name': i[0], 'value': int(i[1])})
        xdata.append(i[0])
    return ydata, xdata

def bigdata_ceshi5_data():
    res1 = query("select name,value from ceshis5 where id=1 ORDER BY value DESC")
    res2 = query("select name,value from ceshis5 where id=2 ORDER BY value DESC")
    res3 = query("select name,value from ceshis5 where id=3 ORDER BY value DESC")
    res4 = query("select name,value from ceshis5 where id=4 ORDER BY value DESC")
    res5 = query("select name,value from ceshis5 where id=5 ORDER BY value DESC")
    res6 = query("select name,value from ceshis5 where id=6 ORDER BY value DESC")
    data1 = {}
    data2 = {}
    data3 = {}
    data4 = {}
    data5 = {}
    data6 = {}
    for i in res1:
        data1[i[0]] = int(i[1])
    for i in res2:
        data2[i[0]] = int(i[1])
    for i in res3:
        data3[i[0]] = int(i[1])
    for i in res4:
        data4[i[0]] = int(i[1])
    for i in res5:
        data5[i[0]] = int(i[1])
    for i in res6:
        data6[i[0]] = int(i[1])
    return data1,data2,data3,data4,data5,data6


def bigdata_chart4_data():
    res = query("SELECT * from bigdata_chart4")
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    for i in res:
        data1.append(i[0])
        data2.append(i[1])
        data3.append(i[2])
        data4.append(i[3])
    return data1,data2,data3,data4

def bigdata_chart5_data():
    res = query("SELECT * from bigdata_chart5")
    data1 = []
    data2 = []
    for i in res:
        data1.append(i[0])
        data2.append(i[1])
    return data1,data2

def survey_basic_info_data():
    res = query("SELECT * from survery_basic_info")
    data = []
    for i in res:
        for r in i:
            data.append(r)
    return data

def survey_shop_info_data():
    res = query("select * from survey_shop_info")
    data = []
    for i in res:
        data.append(i)
    return data

def survey_shop_basic_data():
    res = query("SELECT * from survey_shop_basic")
    data = []
    for i in res:
        for r in i:
            data.append(r)
    return data

def survey_chart3():
    sql = "SELECT * from survey_chart3"
    res = query(sql)
    data = []
    for i in res:
        data.append({'name': i[0], 'value': int(i[1])})
    return data

def survey_chart2_data():
    sql = "select * from survey_chart2"
    res = query(sql)
    ydata = []
    xdata = []
    for i in res:
        ydata.append({'name': i[0], 'value': int(i[1])})
        xdata.append(i[0])
    return ydata, xdata

def survey_chart5_data():
    res = query("SELECT * from survey_chart5")
    data1 = []
    data2 = []
    for i in res:
        data1.append(i[0])
        data2.append(i[1])
    return data1, data2

def survey_shuiipin_data():
    sql = "select * from survey_shuiipin"
    res = query(sql)
    data = []
    for i in res:
        data.append({'name': i[0], 'value': int(i[1])})
    return data

def survey_diqu_data():
    sql = "select * from survey_diqu"
    res = query(sql)
    data = []
    for i in res:
        data.append({'name': i[0], 'value': int(i[1])/2})
    return data

def survey_chart4_data():
    res = query("SELECT * from survey_chart4")
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    for i in res:
        data1.append(i[0])
        data2.append(i[1])
        data3.append(i[2])
        data4.append(i[3])
        data5.append(i[4])
    return data1,data2,data3,data4,data5

def index2_toplist():
    sql = "select * from index2_top"
    res = query(sql)
    data = []
    for i in res:
        data.append(i)
    return data

def index2_chart_data():
    res = query("select * from index2_chart order by value desc")
    data = []
    for i in res:
        data.append({'name': i[0], 'value': i[1]})
    return data

def index2_toptitle():
    sql = "select * from index2_top_title"
    res = query(sql)
    data = []
    for i in res:
        for r in i:
            data.append(r)
    return data

def index3_char1_2_data():
    res1 = query("select name,value from index3_char1_2 a order by a.`value` limit 6")
    res2 = query("select name,value from index3_char1_2 a order by a.`value` limit 6,10")
    name1 = []
    name2 = []
    value1 = []
    value2 = []
    for i in res1:
        name1.append(i[0])
        value1.append(i[1])
    for i in res2:
        name2.append(i[0])
        value2.append(i[1])
    return name1,value1,name2,value2

def index3_char3_data():
    res = query("select * from index3_char3")
    province = []
    damaged = []
    lost = []
    reject = []
    not_signed = []
    for i in res:
        province.append(i[0])
        damaged.append(i[1])
        lost.append(i[2])
        reject.append(i[3])
        not_signed.append(i[4])
    return province, damaged, lost, reject, not_signed

def index3_maps_data():
    sql = "select * from index3_maps"
    res = query(sql)
    data = []
    for i in res:
        data.append([{'name': i[0], 'value': int(i[1])}])
    return data

def index3_chart5_data():
    res1 = query("select old, value1 from index3_chart_5")
    line_old = []
    line_value = []
    for i in res1:
        line_old.append(i[0])
        line_value.append(i[1])
    res2 = query("select sex, sum(value3) from index3_chart_5 group by sex")
    sex_data = []
    for i in res2:
        sex_data.append({"value":int(i[1]), "name":i[0]})
    res3 = query("select education,value2 from index3_chart_5")
    edu_data = []
    for i in res3:
        edu_data.append({"value": int(i[1]), "name": i[0]})
    return sex_data,line_old,line_value,edu_data

def index3_chart6_data():
    sql = "select * from index3_chart_6"
    res = query(sql)
    data1 = []
    data2 = []
    for i in res:
        data1.append({'date': i[0], 'value': int(i[1])})
    for i in res:
        data2.append({'date': i[0], 'value': int(i[2])})
    return data1,data2

def index3_chart8_data():
    sql = "select * from index3_chart8"
    res = query(sql)
    data = []
    for i in res:
        data.append({'value': int(i[1]), 'name': i[0]})
    return data

if __name__ == '__main__':
    print(index3_chart8_data())