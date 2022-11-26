from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})

producer.poll(0)
for i in range(10):
    msg = f"hello python {i}"
    producer.produce('t1', value=msg.encode('utf-8'), key=f'{i}:'.encode('utf-8'))
    producer.flush()

