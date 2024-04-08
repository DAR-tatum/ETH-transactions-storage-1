from google.cloud import bigquery

client = bigquery.Client()

try:
  # Attempt a simple operation that requires a connection (e.g., list datasets)
  datasets = list(client.list_datasets())
  print("The client is connected.")
except Exception as e:
  print(f"An error occurred: {e}")