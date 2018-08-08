import click
from google.cloud import bigquery




def testquery(client):
  job = client.query("""SELECT count(*) as count, 1 as a FROM `w4111-columbia.graph.tweets` """)

  # waits for query to execute and return
  results = job.result()
  return list(results)


def q1(client):
  return []

def q2(client):
  return []

def q3(client):
  return []

def q4(client):
  return []

def q5(client):
  return []


@click.command()
@click.argument("PATHTOCRED", type=click.Path(exists=True))
def main(pathtocred):
  client = bigquery.Client.from_service_account_json(pathtocred)

  funcs_to_test = [testquery, q1, q2, q3, q4, q5]
  for func in funcs_to_test:
    rows = func(client)
    print "\n====%s====" % func.__name__
    for r in rows:
      print r


if __name__ == "__main__":
  main()
