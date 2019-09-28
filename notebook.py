#%% settings
from spacy import displacy
import spacy
from collections import defaultdict
import highlight

#%% read testsets, and nlp settins
test_filename = 'test_sets.txt'
with open(test_filename, 'r') as f:
    lines = f.read().splitlines()
nlp = spacy.load("en_core_web_sm")

#%% first, save pos, tag, and dependency, and containing sentences
examples_for_dep = defaultdict(lambda: defaultdict(list))
examples_for_tag = defaultdict(lambda: defaultdict(list))
examples_for_pos = defaultdict(lambda: defaultdict(list))
for line in lines:
    doc = nlp(line)
    for i, token in enumerate(doc):
        examples_for_dep[token.dep_][doc].append((i, token.head.i))
        examples_for_tag[token.tag_][doc].append(i)
        examples_for_pos[token.pos_][doc].append(i)

#%%
# tag and explanation and examples 
# print(examples_for_pos)
def print_examples(examples_for):
    for tag, doc_and_index in examples_for.items():
        print('tag :: {}\nexplanation :: {}'.format(tag, spacy.explain(tag)))
        print('----example-----')
        for doc, indices in doc_and_index.items():
            print(highlight.by_token(indices, doc))
        print('================\n\n')
print_examples(examples_for_pos)
print_examples(examples_for_tag)

for dep, doc_and_index in examples_for_dep.items():
    print('dep :: {}\nexplanation :: {}'.format(dep, spacy.explain(dep)))
    print('----example-----')
    for doc, index_and_headindex in doc_and_index.items():
        indices = []
        head_indices = []
        for ih in index_and_headindex:
            print("{0:10}->{1:10}".format(doc[ih[0]].text, doc[ih[1]].text))
            indices.append(ih[0])
            head_indices.append(ih[1])
        print(highlight.by_token_two_color(indices, head_indices, doc))
    print('================\n\n')