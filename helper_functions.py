import uuid
import os
import urllib.parse
from bs4 import BeautifulSoup, Comment
import pandas as pd

# Define the path for data files
graphs_path = ''

# Read TSV files
def read_tsv(file_name, names=None):
    file_path = os.path.join(graphs_path, f'{file_name}.tsv')
    
    # Extract column name from the file
    if not names:
        with open(file_path, 'r') as file:
            for line in file:
                if 'FORMAT' in line:
                    format_line = line
                    break
        names = format_line.split()[2:]
    
    return pd.read_csv(file_path,
                      delimiter='\t', comment='#', header=0, names=names)

# Generate a unique string with the same length from a given input string
def gen_uniq_str(str_):
    return uuid.uuid4().hex[:len(str_) + 1]

# Find the HTML position of a list of link targets in a source article
def find_html_position(source, targets):
    article_quote = source
    file_path = os.path.join('plaintext_articles/', article_quote[0].lower(), f'{article_quote}.htm')
    
    try:
        with open(file_path) as f:
            art_html = f.read()
    except Exception as e:
        print(f"Error reading HTML file for source: {source}")
        return -1

    soup = BeautifulSoup(art_html, features="html.parser")
    
    # Remove unnecessary elements from the HTML
    for element in soup(["script", "style", "head"]):
        element.extract()

    comments = soup.findAll(string=lambda string: isinstance(string, Comment))
    for comment in comments:
        comment.extract()  # Remove HTML comments

    locators = []
    
    for tgt in targets:
        try:
            locator = gen_uniq_str(urllib.parse.unquote_plus(tgt))
            locators.append(locator)
            # Replace the anchor tag with the locator
            soup.select_one(f'a[href*="/{urllib.parse.quote_plus(tgt)}.htm"]').replace_with(locator)
        except Exception as e:
            k = f'a[href*="{urllib.parse.quote_plus(tgt)}.htm"]'
            print(k)
            print(source, tgt)
            pass
    
    # Clean and concatenate the text from the HTML
    text = " ".join(soup.text.split())
    
    # Calculate the relative positions of targets in the text
    pos = {}
    for iloc, loc in enumerate(locators):
        pos[targets[iloc]] = text.find(loc) / len(text)
        
    return pos

def filter_rows_by_values(df, col, values):
    return df[~df[col].isin(values)]