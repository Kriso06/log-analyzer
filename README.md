# Scalable Log Analytics System (Kafka-based Ingestion)
This project implements a Kafka-based log analytics pipeline using Python.
In Phase 2, server logs are streamed into Kafka using a producer and consumed
by a Python consumer, where they are parsed and converted into structured data
for analysis.

## Architecture (Phase 2)
access.log  
→ Kafka Producer (Python)  
→ Kafka Topic (logs-stream)  
→ Kafka Consumer (Python)  
→ Regex-based Log Parser  
→ Structured Data (Pandas DataFrame)

## Technologies Used
- Apache Kafka (Confluent Cloud)
- Python
- confluent-kafka
- pandas
- python-dotenv
- Regular Expressions (Regex)

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Set environment variables
Create a .env file with the following:
BOOTSTRAP_SERVER=...
API_KEY=...
API_SECRET=...

### 3. Run the producer
python producer.py

### 4. Run the consumer
python consumer.py

## Phase 1 Features

- Kafka-based log ingestion using a Python producer
- Kafka consumer for reading streamed log data
- Regex-based parsing of unstructured server logs
- Conversion of logs into structured Pandas DataFrame
- Basic analytical insights such as HTTP status code distribution

## Future Enhancements

- Integrate Spark Structured Streaming for large-scale processing
- Increase Kafka partitions for parallel consumption
- Add real-time monitoring and alerting
- Apply ML-based anomaly detection on logs
