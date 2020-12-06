
import pandas as pd
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# df = pd.read_csv('data.csv', index_col='tag')
df = pd.read_csv('data.csv')

def get_quote(tag):
  '''
  '''
  filter_df = df
  try:
    if tag:
      filter_df = df[df['tag'].str.contains(tag)]
    return filter_df.sample()
  except:
    return filter_df.sample()

@app.route('/quote/')
@app.route('/quote/<tag>')
def index(tag=None):
  quote = get_quote(tag)
  return quote.to_json()

if __name__ == '__main__':
    app.run()