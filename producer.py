import os
from dotenv import load_dotenv
from confluent_kafka import Producer

load_dotenv()

conf={
    'bootstrap.servers':os.getenv("BOOTSTRAP_SERVER"),
    'security.protocol':'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
    'sasl.username':os.getenv("API_KEY"),
    'sasl.password':os.getenv("API_SECRET"),
    'linger.ms':5,
    'queue.buffering.max.messages':10000
}

producer=Producer(conf)

def delivery_report(err,msg):
    if err:
        print(f"Delivery failed: {err}")
    
with open("access.log",encoding="utf-8",errors="ignore") as f:
    for line in f:
        while True:
            try:
                producer.produce(
                    topic="logs_stream",
                    value=line.encode("utf-8"),
                    callback=delivery_report
                )
                break
            except BufferError:
                #Queue is full->wait for kafka to catch up
                producer.poll(0.5)
        producer.poll(0)

producer.flush()