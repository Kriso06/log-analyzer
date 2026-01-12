import os
from dotenv import load_dotenv
from confluent_kafka import Consumer
import pandas as pd
from log_parser import parse_log_line

load_dotenv()

conf={
    'bootstrap.servers':os.getenv("BOOTSTRAP_SERVER"),
    'security.protocol':'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
    'sasl.username':os.getenv("API_KEY"),
    'sasl.password':os.getenv("API_SECRET"),
    'group.id':'log-analyzer-group',
    'auto.offset.reset':'earliest'
}

consumer=Consumer(conf)
consumer.subscribe(["logs_stream"]) #subscribe to topic
parsed_logs=[]
print("Consumer started. Reading messages...")

try:
    while True:
            msg=consumer.poll(1.0)
            if msg is None:
                  continue
            if msg.error():
                  print(f"Consumer error:{msg.error()}")
                  continue
            line=msg.value().decode("utf-8")
            parsed=parse_log_line(line)
            if parsed:
                  parsed_logs.append(parsed)
            
            #stop after reading some msgs(demo)
            if len(parsed_logs)>=20:
                  break
            
finally:
      consumer.close()

df=pd.DataFrame(parsed_logs)
if not df.empty:
      df["status"]=df["status"].astype(int)
      df["size"]=df["size"].replace("-",0).astype(int)
      print("\nParsed log data:")
      print(df.head())
      print("\nStatus Code Distribution:")
      print(df["status"].value_counts())
else:
      print("No logs were parsed.")