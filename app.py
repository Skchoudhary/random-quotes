import pandas as pd

df = pd.read_csv('data.csv', index_col='tag')


def get_quote(tag):
  '''
  '''
  try:
    if tag:
      return df[df['tag'].str.contains(tag)][0]
    else:
      return df.sample()
  except:
    return df.sample()

def application(env, start_response):
  '''
  '''
  tag = get_query('tag')
  quote = get_quote(tag)
  start_response('200 OK', [('Content-Type','application/json')])
  return to_json(quote)