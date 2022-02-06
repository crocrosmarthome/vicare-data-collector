from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import os

_url = os.environ['INFLUXDB_URL']
_bucket = os.environ['INFLUXDB_BUCKET']
_org = os.environ['INFLUXDB_ORG']
_token = os.environ['INFLUXDB_TOKEN']

_influxdb_client = InfluxDBClient(url=_url, token=_token, org=_org)

write_api = _influxdb_client.write_api(write_options=SYNCHRONOUS)


def writeMeasure(time, measurement_name, fieldname, fieldvalue):
    if not isinstance(fieldvalue, str):
        fieldvalue = float(fieldvalue)
    _p = Point(measurement_name).time(time).field(fieldname, fieldvalue)
    write_api.write(bucket=_bucket, org=_org, record=_p)
