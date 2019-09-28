import spacy
from spacy import displacy
import argparse
import csv

def _main(content):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(content)
    #1
    for chunk in doc.noun_chunks: 
        print("noun phrase : '{}' with root '{}'".format(chunk.text, chunk.root.text))
        print("dependency : {}: {}".format(chunk.root.dep_, spacy.explain(chunk.root.dep_)))
    print("="*10)

    #2 traverse
    root = root_token(doc)
    traverse(root)
    print("="*10)

    #3 subtree
    for token in doc[0].subtree:
        print(token)

    #4 displacy
    displacy.render(doc, style='dep')

def root_token(doc):
    return [token for token in doc if token.head == token][0]

def traverse(root_token):
    """depth first"""
    for child in root_token.children:
        print('head  : {}, ({}: {})'.format(root_token, root_token.pos_, root_token.tag_))
        print('child : {}, ({}: {})'.format(child, child.pos_, child.tag_))
        print('dependency : {}({})'.format(child.dep_, spacy.explain(child.dep_)))
        print('-'*10)
        traverse(child)

def test(filename):
    with open(filename, 'r') as f : 
        test_sets = f.readlines()
    test_sets = [ line.strip() for line in test_sets ]

if __name__ == '__main__':
    #%%
    parser = argparse.ArgumentParser(description='write')
    parser.add_argument(dest='input', type=str)
    args = parser.parse_args()
    
    #%%
    _main(args.input)