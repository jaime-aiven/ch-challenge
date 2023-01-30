from clickhouse_driver import Client
client = Client('clickhouse-jaime-test-dev-sandbox.aivencloud.com',
                user='avnadmin',
                password='AVNS_HousDm5C838sDM9WMjd',
                secure=True,
                port='12691',
                )

## docker run -it  --rm clickhouse/clickhouse-client --user avnadmin --password AVNS_HousDm5C838sDM9WMjd --host clickhouse-jaime-test-dev-sandbox.aivencloud.com --port 12691 --secure

#to confirm its all wowrking
client.execute('SHOW DATABASES')