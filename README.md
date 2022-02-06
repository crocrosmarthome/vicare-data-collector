##How to


```
docker run -it \
 -e VICARE_CLIENT_ID=<yourviessmannclientid> \
 -e VICARE_EMAIL=<youremail> \
 -e VICARE_PASSWORD=<yourpassword> \
 -e INFLUXDB_URL=<influxdburl> \
 -e INFLUXDB_BUCKET=<influxdbtoken> \
 -e INFLUXDB_TOKEN=<influxdbsecret> \
 -e INFLUXDB_ORG=<influxdborg> \
vicare-data-collector:latest
```