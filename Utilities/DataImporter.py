import csv
import pyodbc
import sys
import os

## csv for mapunit
def mapunit(filename, cur):

    SQL = 'SELECT * FROM mapunit;'  # your query goes here
    rows = cur.execute(SQL).fetchall()
    # print rows

    with open(filename, "wb") as csv_file:  # Python 2 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cur.description])  # write headers
        csv_writer.writerows(rows)


## csv for component
def component(filename, cur):

    SQL = 'SELECT * FROM component;'  # your query goes here
    rows = cur.execute(SQL).fetchall()
    # print rows

    with open(filename, "wb") as csv_file:  # Python 2 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cur.description])  # write headers
        csv_writer.writerows(rows)


def test_join(filename, cur):
    SQL = 'SELECT csm.soimoistdept_l, csm.soimoistdept_r, csm.soimoistdept_h, csm.soimoistdepb_l, ' \
          'csm.soimoistdepb_r, csm.soimoistdepb_h, csm.soimoiststat, cm.month, c.runoff, l.areaname ' \
          'FROM ((((cosoilmoist csm INNER JOIN comonth cm ON csm.comonthkey = cm.comonthkey) ' \
          'INNER JOIN component c ON cm.cokey = c.cokey) ' \
          'INNER JOIN mapunit mu ON c.mukey = mu.mukey)' \
          'INNER JOIN legend l ON mu.lkey = l.lkey);'
    rows = cur.execute(SQL).fetchall()
    # print rows

    with open(filename, "a") as csv_file:  # Python 2 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cur.description])  # write headers
        csv_writer.writerows(rows)

def create_crops(filename, cur):
    SQL = 'SELECT legend.areaname, mucropyld.cropname, SUM(mucropyld.irryield_r) FROM ' \
          '(legend INNER JOIN mapunit ON legend.lkey = mapunit.lkey) INNER JOIN ' \
          'mucropyld ON mapunit.mukey = mucropyld.mukey GROUP BY legend.areaname, mucropyld.cropname'

    rows = cur.execute(SQL).fetchall()

    with open(filename, "a") as csv_file:  # Python 2 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cur.description])  # write headers
        csv_writer.writerows(rows)


def creat_non_crops(filename, cur):
    SQL = 'SELECT legend.areaname, mucropyld.cropname, SUM(mucropyld.nonirryield_r) FROM ' \
          '(legend INNER JOIN mapunit ON legend.lkey = mapunit.lkey) INNER JOIN ' \
          'mucropyld ON mapunit.mukey = mucropyld.mukey GROUP BY legend.areaname, mucropyld.cropname'

    rows = cur.execute(SQL).fetchall()

    with open(filename, "a") as csv_file:  # Python 2 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cur.description])  # write headers
        csv_writer.writerows(rows)


def create_windbreak(filename, cur):
    SQL = 'SELECT legend.areaname, copwindbreak.plantcomname, AVG(copwindbreak.wndbrkht_r) FROM ' \
          '((legend INNER JOIN mapunit ON legend.lkey = mapunit.lkey) INNER JOIN component ON mapunit.mukey = component.mukey) ' \
          'INNER JOIN copwindbreak ON component.cokey = copwindbreak.cokey GROUP BY legend.areaname,  copwindbreak.plantcomname'

    rows = cur.execute(SQL).fetchall()

    with open(filename, "a") as csv_file:  # Python 2 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cur.description])  # write headers
        csv_writer.writerows(rows)


def generate_csv(directory):
    csv_dir = "F:\\272\\data\\csvs"
    filename = os.path.join(directory, "soildb_US_2003.mdb")
    con = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+filename+'')
    cur = con.cursor()

    # Map Unit
    prefix = directory.split("\\")[-1]
    output = prefix + "_mapunit.csv"
    csv_file = os.path.join(csv_dir, output)
    mapunit(csv_file, cur)

    # component
    prefix = directory.split("\\")[-1]
    output = prefix + "_component.csv"
    csv_file = os.path.join(csv_dir, output)
    component(csv_file, cur)

    # join
    prefix = directory.split("\\")[-1]
    output = "join.csv"
    csv_file = os.path.join(csv_dir, output)
    test_join(csv_file, cur)

    #crop yield
    prefix = directory.split("\\")[-1]
    output = "crops.csv"
    csv_file = os.path.join(csv_dir, output)
    create_crops(csv_file, cur)

    prefix = directory.split("\\")[-1]
    output = "crops_nonirr.csv"
    csv_file = os.path.join(csv_dir, output)
    create_crops(csv_file, cur)

    prefix =directory.split("\\")[-1]
    output = "windbreak.csv"
    csv_file = os.path.join(csv_dir, output)
    create_windbreak(csv_file, cur)

    cur.close()
    con.close()


if __name__ == "__main__":
    generate_csv(sys.argv[1])