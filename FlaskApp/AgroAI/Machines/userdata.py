import traceback
import csv
import os


def write_to_csv(jsonstr):
    if not os.path.exists(os.path.dirname(__file__) + '/Data/userdata.csv'):
        with open(os.path.dirname(__file__) + '/Data/userdata.csv', 'a') as fp:
            writer = csv.DictWriter(fp, jsonstr.keys())
            writer.writeheader()
            writer.writerow(jsonstr)
    else:
        with open(os.path.dirname(__file__) + '/Data/userdata.csv', 'a') as fp:
            writer = csv.DictWriter(fp, jsonstr.keys())
            writer.writerow(jsonstr)


def import_userdata(jsonstr):
    print jsonstr
    print type(jsonstr)
    try:
        write_to_csv(jsonstr=jsonstr)
    except Exception:
        print traceback.format_exc()
        # Here exception  occured for some reason as file already is use by other user,
        # then try again to write into the file.
        write_to_csv(jsonstr=jsonstr)
