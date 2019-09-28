```python
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
```


```python
test_filename = 'test_sets.txt'
with open(test_filename, 'r') as f:
    lines = f.read().splitlines()
```


```python
pos_index = []
tag_index = []
dep_index = []
```


```python
for line in lines:
    print('sentence : ', line)
    doc = nlp(line)
    for token in doc:
        pos_index.append(token.pos_) if token.pos_ not in pos_index else pos_index
        tag_index.append(token.tag_) if token.tag_ not in tag_index else tag_index
        dep_index.append(token.dep_) if token.dep_ not in dep_index else dep_index
        print('{0:20} | {1:20} | {2:20} | {3:20}'.format(token.text, token.pos_, token.tag_, token.dep_))
    displacy.render(doc, style='dep')
    print('--------------------------'*2)

```

    sentence :  Life isn't about finding yourself. Life is about creating yourself.
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    n't                  | ADV                  | RB                   | neg                 
    about                | ADP                  | IN                   | prep                
    finding              | VERB                 | VBG                  | pcomp               
    yourself             | PRON                 | PRP                  | dobj                
    .                    | PUNCT                | .                    | punct               
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    about                | ADP                  | IN                   | prep                
    creating             | VERB                 | VBG                  | pcomp               
    yourself             | PRON                 | PRP                  | dobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="fd75989cc4bf4684b5447ac919d11f8b-0" class="displacy" width="1975" height="312.0" direction="ltr" style="max-width: none; height: 312.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="400">n't</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="575">about</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="750">finding</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="925">yourself.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">about</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">creating</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">yourself.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">PRON</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fd75989cc4bf4684b5447ac919d11f8b-0-0" stroke-width="2px" d="M70,177.0 C70,89.5 220.0,89.5 220.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fd75989cc4bf4684b5447ac919d11f8b-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,179.0 L62,167.0 78,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fd75989cc4bf4684b5447ac919d11f8b-0-1" stroke-width="2px" d="M245,177.0 C245,89.5 395.0,89.5 395.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fd75989cc4bf4684b5447ac919d11f8b-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M395.0,179.0 L403.0,167.0 387.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fd75989cc4bf4684b5447ac919d11f8b-0-2" stroke-width="2px" d="M245,177.0 C245,2.0 575.0,2.0 575.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fd75989cc4bf4684b5447ac919d11f8b-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M575.0,179.0 L583.0,167.0 567.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fd75989cc4bf4684b5447ac919d11f8b-0-3" stroke-width="2px" d="M595,177.0 C595,89.5 745.0,89.5 745.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fd75989cc4bf4684b5447ac919d11f8b-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M745.0,179.0 L753.0,167.0 737.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fd75989cc4bf4684b5447ac919d11f8b-0-4" stroke-width="2px" d="M770,177.0 C770,89.5 920.0,89.5 920.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fd75989cc4bf4684b5447ac919d11f8b-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M920.0,179.0 L928.0,167.0 912.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fd75989cc4bf4684b5447ac919d11f8b-0-5" stroke-width="2px" d="M1120,177.0 C1120,89.5 1270.0,89.5 1270.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fd75989cc4bf4684b5447ac919d11f8b-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,179.0 L1112,167.0 1128,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fd75989cc4bf4684b5447ac919d11f8b-0-6" stroke-width="2px" d="M1295,177.0 C1295,89.5 1445.0,89.5 1445.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fd75989cc4bf4684b5447ac919d11f8b-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1445.0,179.0 L1453.0,167.0 1437.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fd75989cc4bf4684b5447ac919d11f8b-0-7" stroke-width="2px" d="M1470,177.0 C1470,89.5 1620.0,89.5 1620.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fd75989cc4bf4684b5447ac919d11f8b-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1620.0,179.0 L1628.0,167.0 1612.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fd75989cc4bf4684b5447ac919d11f8b-0-8" stroke-width="2px" d="M1645,177.0 C1645,89.5 1795.0,89.5 1795.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fd75989cc4bf4684b5447ac919d11f8b-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1795.0,179.0 L1803.0,167.0 1787.0,167.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  The most important thing is to enjoy your life - to be happy - it's all that matters.
    The                  | DET                  | DT                   | det                 
    most                 | ADV                  | RBS                  | advmod              
    important            | ADJ                  | JJ                   | amod                
    thing                | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ccomp               
    to                   | PART                 | TO                   | aux                 
    enjoy                | VERB                 | VB                   | xcomp               
    your                 | DET                  | PRP$                 | poss                
    life                 | NOUN                 | NN                   | dobj                
    -                    | PUNCT                | :                    | punct               
    to                   | PART                 | TO                   | aux                 
    be                   | VERB                 | VB                   | conj                
    happy                | ADJ                  | JJ                   | acomp               
    -                    | PUNCT                | :                    | punct               
    it                   | PRON                 | PRP                  | nsubj               
    's                   | VERB                 | VBZ                  | ROOT                
    all                  | DET                  | DT                   | attr                
    that                 | DET                  | WDT                  | nsubj               
    matters              | VERB                 | VBZ                  | relcl               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="e2c35133a69b4b30b9f5c37d85b1ea60-0" class="displacy" width="3025" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">The</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">most</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">important</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">thing</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">enjoy</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">your</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">life -</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">be</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">happy -</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">'s</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">all</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2675">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2850">matters.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">VERB</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-0" stroke-width="2px" d="M70,439.5 C70,177.0 565.0,177.0 565.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-1" stroke-width="2px" d="M245,439.5 C245,352.0 380.0,352.0 380.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,441.5 L237,429.5 253,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-2" stroke-width="2px" d="M420,439.5 C420,352.0 555.0,352.0 555.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,441.5 L412,429.5 428,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-3" stroke-width="2px" d="M595,439.5 C595,352.0 730.0,352.0 730.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,441.5 L587,429.5 603,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-4" stroke-width="2px" d="M770,439.5 C770,2.0 2325.0,2.0 2325.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,441.5 L762,429.5 778,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-5" stroke-width="2px" d="M945,439.5 C945,352.0 1080.0,352.0 1080.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,441.5 L937,429.5 953,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-6" stroke-width="2px" d="M770,439.5 C770,264.5 1085.0,264.5 1085.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1085.0,441.5 L1093.0,429.5 1077.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-7" stroke-width="2px" d="M1295,439.5 C1295,352.0 1430.0,352.0 1430.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,441.5 L1287,429.5 1303,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-8" stroke-width="2px" d="M1120,439.5 C1120,264.5 1435.0,264.5 1435.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1435.0,441.5 L1443.0,429.5 1427.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-9" stroke-width="2px" d="M1645,439.5 C1645,352.0 1780.0,352.0 1780.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,441.5 L1637,429.5 1653,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-10" stroke-width="2px" d="M1120,439.5 C1120,89.5 1795.0,89.5 1795.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1795.0,441.5 L1803.0,429.5 1787.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-11" stroke-width="2px" d="M1820,439.5 C1820,352.0 1955.0,352.0 1955.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1955.0,441.5 L1963.0,429.5 1947.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-12" stroke-width="2px" d="M2170,439.5 C2170,352.0 2305.0,352.0 2305.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,441.5 L2162,429.5 2178,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-13" stroke-width="2px" d="M2345,439.5 C2345,352.0 2480.0,352.0 2480.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2480.0,441.5 L2488.0,429.5 2472.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-14" stroke-width="2px" d="M2695,439.5 C2695,352.0 2830.0,352.0 2830.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,441.5 L2687,429.5 2703,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-15" stroke-width="2px" d="M2520,439.5 C2520,264.5 2835.0,264.5 2835.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e2c35133a69b4b30b9f5c37d85b1ea60-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2835.0,441.5 L2843.0,429.5 2827.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  I have found that if you love life, life will love you back.
    I                    | PRON                 | PRP                  | nsubj               
    have                 | VERB                 | VBP                  | aux                 
    found                | VERB                 | VBN                  | ROOT                
    that                 | ADP                  | IN                   | mark                
    if                   | ADP                  | IN                   | mark                
    you                  | PRON                 | PRP                  | nsubj               
    love                 | VERB                 | VBP                  | advcl               
    life                 | NOUN                 | NN                   | dobj                
    ,                    | PUNCT                | ,                    | punct               
    life                 | NOUN                 | NN                   | nsubj               
    will                 | VERB                 | MD                   | aux                 
    love                 | VERB                 | VB                   | ccomp               
    you                  | PRON                 | PRP                  | dobj                
    back                 | ADV                  | RB                   | advmod              
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="61bdbc770663454f9d90f001fe57cff3-0" class="displacy" width="2325" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">I</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">have</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">found</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">if</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">love</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">life,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">will</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">love</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">back.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">ADV</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-0" stroke-width="2px" d="M70,439.5 C70,264.5 385.0,264.5 385.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-1" stroke-width="2px" d="M245,439.5 C245,352.0 380.0,352.0 380.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,441.5 L237,429.5 253,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-2" stroke-width="2px" d="M595,439.5 C595,89.5 1795.0,89.5 1795.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,441.5 L587,429.5 603,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-3" stroke-width="2px" d="M770,439.5 C770,264.5 1085.0,264.5 1085.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,441.5 L762,429.5 778,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-4" stroke-width="2px" d="M945,439.5 C945,352.0 1080.0,352.0 1080.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,441.5 L937,429.5 953,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-5" stroke-width="2px" d="M1120,439.5 C1120,177.0 1790.0,177.0 1790.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,441.5 L1112,429.5 1128,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-6" stroke-width="2px" d="M1120,439.5 C1120,352.0 1255.0,352.0 1255.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1255.0,441.5 L1263.0,429.5 1247.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-7" stroke-width="2px" d="M1470,439.5 C1470,264.5 1785.0,264.5 1785.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1470,441.5 L1462,429.5 1478,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-8" stroke-width="2px" d="M1645,439.5 C1645,352.0 1780.0,352.0 1780.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,441.5 L1637,429.5 1653,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-9" stroke-width="2px" d="M420,439.5 C420,2.0 1800.0,2.0 1800.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1800.0,441.5 L1808.0,429.5 1792.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-10" stroke-width="2px" d="M1820,439.5 C1820,352.0 1955.0,352.0 1955.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1955.0,441.5 L1963.0,429.5 1947.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-61bdbc770663454f9d90f001fe57cff3-0-11" stroke-width="2px" d="M1820,439.5 C1820,264.5 2135.0,264.5 2135.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-61bdbc770663454f9d90f001fe57cff3-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2135.0,441.5 L2143.0,429.5 2127.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is really simple, but we insist on making it complicated.
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    really               | ADV                  | RB                   | advmod              
    simple               | ADJ                  | JJ                   | acomp               
    ,                    | PUNCT                | ,                    | punct               
    but                  | CCONJ                | CC                   | cc                  
    we                   | PRON                 | PRP                  | nsubj               
    insist               | VERB                 | VBP                  | conj                
    on                   | ADP                  | IN                   | prep                
    making               | VERB                 | VBG                  | pcomp               
    it                   | PRON                 | PRP                  | nsubj               
    complicated          | VERB                 | VBN                  | ccomp               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="0e4c20117ac248e68a738d560d5dc56b-0" class="displacy" width="1975" height="487.0" direction="ltr" style="max-width: none; height: 487.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="400">really</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="575">simple,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="750">but</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="925">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">insist</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">on</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">making</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">complicated.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e4c20117ac248e68a738d560d5dc56b-0-0" stroke-width="2px" d="M70,352.0 C70,264.5 210.0,264.5 210.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e4c20117ac248e68a738d560d5dc56b-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,354.0 L62,342.0 78,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e4c20117ac248e68a738d560d5dc56b-0-1" stroke-width="2px" d="M420,352.0 C420,264.5 560.0,264.5 560.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e4c20117ac248e68a738d560d5dc56b-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,354.0 L412,342.0 428,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e4c20117ac248e68a738d560d5dc56b-0-2" stroke-width="2px" d="M245,352.0 C245,177.0 565.0,177.0 565.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e4c20117ac248e68a738d560d5dc56b-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M565.0,354.0 L573.0,342.0 557.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e4c20117ac248e68a738d560d5dc56b-0-3" stroke-width="2px" d="M245,352.0 C245,89.5 745.0,89.5 745.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e4c20117ac248e68a738d560d5dc56b-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M745.0,354.0 L753.0,342.0 737.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e4c20117ac248e68a738d560d5dc56b-0-4" stroke-width="2px" d="M945,352.0 C945,264.5 1085.0,264.5 1085.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e4c20117ac248e68a738d560d5dc56b-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,354.0 L937,342.0 953,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e4c20117ac248e68a738d560d5dc56b-0-5" stroke-width="2px" d="M245,352.0 C245,2.0 1100.0,2.0 1100.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e4c20117ac248e68a738d560d5dc56b-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1100.0,354.0 L1108.0,342.0 1092.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e4c20117ac248e68a738d560d5dc56b-0-6" stroke-width="2px" d="M1120,352.0 C1120,264.5 1260.0,264.5 1260.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e4c20117ac248e68a738d560d5dc56b-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1260.0,354.0 L1268.0,342.0 1252.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e4c20117ac248e68a738d560d5dc56b-0-7" stroke-width="2px" d="M1295,352.0 C1295,264.5 1435.0,264.5 1435.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e4c20117ac248e68a738d560d5dc56b-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1435.0,354.0 L1443.0,342.0 1427.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e4c20117ac248e68a738d560d5dc56b-0-8" stroke-width="2px" d="M1645,352.0 C1645,264.5 1785.0,264.5 1785.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e4c20117ac248e68a738d560d5dc56b-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,354.0 L1637,342.0 1653,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e4c20117ac248e68a738d560d5dc56b-0-9" stroke-width="2px" d="M1470,352.0 C1470,177.0 1790.0,177.0 1790.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e4c20117ac248e68a738d560d5dc56b-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1790.0,354.0 L1798.0,342.0 1782.0,342.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  In the end, it's not the years in your life that count. It's the life in your years.
    In                   | ADP                  | IN                   | prep                
    the                  | DET                  | DT                   | det                 
    end                  | NOUN                 | NN                   | pobj                
    ,                    | PUNCT                | ,                    | punct               
    it                   | PRON                 | PRP                  | nsubj               
    's                   | VERB                 | VBZ                  | ROOT                
    not                  | ADV                  | RB                   | neg                 
    the                  | DET                  | DT                   | det                 
    years                | NOUN                 | NNS                  | attr                
    in                   | ADP                  | IN                   | prep                
    your                 | DET                  | PRP$                 | poss                
    life                 | NOUN                 | NN                   | pobj                
    that                 | DET                  | WDT                  | nsubj               
    count                | VERB                 | VBP                  | relcl               
    .                    | PUNCT                | .                    | punct               
    It                   | PRON                 | PRP                  | nsubj               
    's                   | VERB                 | VBZ                  | ROOT                
    the                  | DET                  | DT                   | det                 
    life                 | NOUN                 | NN                   | attr                
    in                   | ADP                  | IN                   | prep                
    your                 | DET                  | PRP$                 | poss                
    years                | NOUN                 | NNS                  | pobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="fa16be53af4642a7ac058e3c7119845c-0" class="displacy" width="3550" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">In</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">end,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">'s</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">years</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">your</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">count.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">It</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">'s</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2675">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2850">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3025">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3200">your</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3375">years.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-0" stroke-width="2px" d="M70,439.5 C70,89.5 745.0,89.5 745.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-1" stroke-width="2px" d="M245,439.5 C245,352.0 380.0,352.0 380.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,441.5 L237,429.5 253,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-2" stroke-width="2px" d="M70,439.5 C70,264.5 385.0,264.5 385.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M385.0,441.5 L393.0,429.5 377.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-3" stroke-width="2px" d="M595,439.5 C595,352.0 730.0,352.0 730.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,441.5 L587,429.5 603,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-4" stroke-width="2px" d="M770,439.5 C770,352.0 905.0,352.0 905.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M905.0,441.5 L913.0,429.5 897.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-5" stroke-width="2px" d="M1120,439.5 C1120,352.0 1255.0,352.0 1255.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,441.5 L1112,429.5 1128,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-6" stroke-width="2px" d="M770,439.5 C770,177.0 1265.0,177.0 1265.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1265.0,441.5 L1273.0,429.5 1257.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-7" stroke-width="2px" d="M1295,439.5 C1295,352.0 1430.0,352.0 1430.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1430.0,441.5 L1438.0,429.5 1422.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-8" stroke-width="2px" d="M1645,439.5 C1645,352.0 1780.0,352.0 1780.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,441.5 L1637,429.5 1653,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-9" stroke-width="2px" d="M1470,439.5 C1470,264.5 1785.0,264.5 1785.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1785.0,441.5 L1793.0,429.5 1777.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-10" stroke-width="2px" d="M1995,439.5 C1995,352.0 2130.0,352.0 2130.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,441.5 L1987,429.5 2003,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-11" stroke-width="2px" d="M1295,439.5 C1295,2.0 2150.0,2.0 2150.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2150.0,441.5 L2158.0,429.5 2142.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-12" stroke-width="2px" d="M2345,439.5 C2345,352.0 2480.0,352.0 2480.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,441.5 L2337,429.5 2353,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-13" stroke-width="2px" d="M2695,439.5 C2695,352.0 2830.0,352.0 2830.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,441.5 L2687,429.5 2703,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-14" stroke-width="2px" d="M2520,439.5 C2520,264.5 2835.0,264.5 2835.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2835.0,441.5 L2843.0,429.5 2827.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-15" stroke-width="2px" d="M2870,439.5 C2870,352.0 3005.0,352.0 3005.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3005.0,441.5 L3013.0,429.5 2997.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-16" stroke-width="2px" d="M3220,439.5 C3220,352.0 3355.0,352.0 3355.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3220,441.5 L3212,429.5 3228,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa16be53af4642a7ac058e3c7119845c-0-17" stroke-width="2px" d="M3045,439.5 C3045,264.5 3360.0,264.5 3360.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa16be53af4642a7ac058e3c7119845c-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3360.0,441.5 L3368.0,429.5 3352.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is inherently risky. There is only one big risk you should avoid at all costs, and that is the risk of doing nothing.
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    inherently           | ADV                  | RB                   | advmod              
    risky                | ADJ                  | JJ                   | acomp               
    .                    | PUNCT                | .                    | punct               
    There                | ADV                  | EX                   | expl                
    is                   | VERB                 | VBZ                  | ROOT                
    only                 | ADV                  | RB                   | advmod              
    one                  | NUM                  | CD                   | nummod              
    big                  | ADJ                  | JJ                   | amod                
    risk                 | NOUN                 | NN                   | attr                
    you                  | PRON                 | PRP                  | nsubj               
    should               | VERB                 | MD                   | aux                 
    avoid                | VERB                 | VB                   | relcl               
    at                   | ADP                  | IN                   | prep                
    all                  | DET                  | DT                   | det                 
    costs                | NOUN                 | NNS                  | pobj                
    ,                    | PUNCT                | ,                    | punct               
    and                  | CCONJ                | CC                   | cc                  
    that                 | DET                  | DT                   | nsubj               
    is                   | VERB                 | VBZ                  | conj                
    the                  | DET                  | DT                   | det                 
    risk                 | NOUN                 | NN                   | attr                
    of                   | ADP                  | IN                   | prep                
    doing                | VERB                 | VBG                  | pcomp               
    nothing              | NOUN                 | NN                   | dobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="efeb7a48c4c04fed9e2c885ff25adccb-0" class="displacy" width="4250" height="662.0" direction="ltr" style="max-width: none; height: 662.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="400">inherently</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="575">risky.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="750">There</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="925">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">only</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">one</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">big</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">risk</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">should</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">avoid</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">at</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">all</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">costs,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3375">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3550">risk</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3725">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3725">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3900">doing</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3900">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="4075">nothing.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4075">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-0" stroke-width="2px" d="M70,527.0 C70,439.5 200.0,439.5 200.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,529.0 L62,517.0 78,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-1" stroke-width="2px" d="M245,527.0 C245,439.5 375.0,439.5 375.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M375.0,529.0 L383.0,517.0 367.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-2" stroke-width="2px" d="M245,527.0 C245,352.0 555.0,352.0 555.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M555.0,529.0 L563.0,517.0 547.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-3" stroke-width="2px" d="M770,527.0 C770,439.5 900.0,439.5 900.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">expl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,529.0 L762,517.0 778,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-4" stroke-width="2px" d="M1120,527.0 C1120,439.5 1250.0,439.5 1250.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,529.0 L1112,517.0 1128,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-5" stroke-width="2px" d="M1295,527.0 C1295,352.0 1605.0,352.0 1605.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nummod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,529.0 L1287,517.0 1303,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-6" stroke-width="2px" d="M1470,527.0 C1470,439.5 1600.0,439.5 1600.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1470,529.0 L1462,517.0 1478,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-7" stroke-width="2px" d="M945,527.0 C945,177.0 1615.0,177.0 1615.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1615.0,529.0 L1623.0,517.0 1607.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-8" stroke-width="2px" d="M1820,527.0 C1820,352.0 2130.0,352.0 2130.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,529.0 L1812,517.0 1828,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-9" stroke-width="2px" d="M1995,527.0 C1995,439.5 2125.0,439.5 2125.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,529.0 L1987,517.0 2003,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-10" stroke-width="2px" d="M1645,527.0 C1645,264.5 2135.0,264.5 2135.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2135.0,529.0 L2143.0,517.0 2127.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-11" stroke-width="2px" d="M2170,527.0 C2170,439.5 2300.0,439.5 2300.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2300.0,529.0 L2308.0,517.0 2292.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-12" stroke-width="2px" d="M2520,527.0 C2520,439.5 2650.0,439.5 2650.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2520,529.0 L2512,517.0 2528,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-13" stroke-width="2px" d="M2345,527.0 C2345,352.0 2655.0,352.0 2655.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2655.0,529.0 L2663.0,517.0 2647.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-14" stroke-width="2px" d="M945,527.0 C945,89.5 2845.0,89.5 2845.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2845.0,529.0 L2853.0,517.0 2837.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-15" stroke-width="2px" d="M3045,527.0 C3045,439.5 3175.0,439.5 3175.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3045,529.0 L3037,517.0 3053,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-16" stroke-width="2px" d="M945,527.0 C945,2.0 3200.0,2.0 3200.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3200.0,529.0 L3208.0,517.0 3192.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-17" stroke-width="2px" d="M3395,527.0 C3395,439.5 3525.0,439.5 3525.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3395,529.0 L3387,517.0 3403,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-18" stroke-width="2px" d="M3220,527.0 C3220,352.0 3530.0,352.0 3530.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3530.0,529.0 L3538.0,517.0 3522.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-19" stroke-width="2px" d="M3570,527.0 C3570,439.5 3700.0,439.5 3700.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3700.0,529.0 L3708.0,517.0 3692.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-20" stroke-width="2px" d="M3745,527.0 C3745,439.5 3875.0,439.5 3875.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-20" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3875.0,529.0 L3883.0,517.0 3867.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-21" stroke-width="2px" d="M3920,527.0 C3920,439.5 4050.0,439.5 4050.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-efeb7a48c4c04fed9e2c885ff25adccb-0-21" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4050.0,529.0 L4058.0,517.0 4042.0,517.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  We all have two lives. The second one starts when we realize we only have one.
    We                   | PRON                 | PRP                  | nsubj               
    all                  | DET                  | DT                   | appos               
    have                 | VERB                 | VBP                  | ROOT                
    two                  | NUM                  | CD                   | nummod              
    lives                | NOUN                 | NNS                  | dobj                
    .                    | PUNCT                | .                    | punct               
    The                  | DET                  | DT                   | det                 
    second               | ADJ                  | JJ                   | amod                
    one                  | NOUN                 | NN                   | nsubj               
    starts               | VERB                 | VBZ                  | ROOT                
    when                 | ADV                  | WRB                  | advmod              
    we                   | PRON                 | PRP                  | nsubj               
    realize              | VERB                 | VBP                  | advcl               
    we                   | PRON                 | PRP                  | nsubj               
    only                 | ADV                  | RB                   | advmod              
    have                 | VERB                 | VBP                  | ccomp               
    one                  | NUM                  | CD                   | dobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="a89a6aefd5b14be2adce57167909113f-0" class="displacy" width="2850" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">We</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">all</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">have</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">two</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">lives.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">The</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">second</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">one</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">starts</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">when</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">realize</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">only</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">have</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2675">one.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">NUM</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-0" stroke-width="2px" d="M70,264.5 C70,89.5 395.0,89.5 395.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-1" stroke-width="2px" d="M70,264.5 C70,177.0 215.0,177.0 215.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">appos</textPath>
    </text>
    <path class="displacy-arrowhead" d="M215.0,266.5 L223.0,254.5 207.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-2" stroke-width="2px" d="M595,264.5 C595,177.0 740.0,177.0 740.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nummod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,266.5 L587,254.5 603,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-3" stroke-width="2px" d="M420,264.5 C420,89.5 745.0,89.5 745.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M745.0,266.5 L753.0,254.5 737.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-4" stroke-width="2px" d="M945,264.5 C945,89.5 1270.0,89.5 1270.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,266.5 L937,254.5 953,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-5" stroke-width="2px" d="M1120,264.5 C1120,177.0 1265.0,177.0 1265.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,266.5 L1112,254.5 1128,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-6" stroke-width="2px" d="M1295,264.5 C1295,177.0 1440.0,177.0 1440.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,266.5 L1287,254.5 1303,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-7" stroke-width="2px" d="M1645,264.5 C1645,89.5 1970.0,89.5 1970.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,266.5 L1637,254.5 1653,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-8" stroke-width="2px" d="M1820,264.5 C1820,177.0 1965.0,177.0 1965.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,266.5 L1812,254.5 1828,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-9" stroke-width="2px" d="M1470,264.5 C1470,2.0 1975.0,2.0 1975.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1975.0,266.5 L1983.0,254.5 1967.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-10" stroke-width="2px" d="M2170,264.5 C2170,89.5 2495.0,89.5 2495.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,266.5 L2162,254.5 2178,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-11" stroke-width="2px" d="M2345,264.5 C2345,177.0 2490.0,177.0 2490.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,266.5 L2337,254.5 2353,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-12" stroke-width="2px" d="M1995,264.5 C1995,2.0 2500.0,2.0 2500.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2500.0,266.5 L2508.0,254.5 2492.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-a89a6aefd5b14be2adce57167909113f-0-13" stroke-width="2px" d="M2520,264.5 C2520,177.0 2665.0,177.0 2665.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-a89a6aefd5b14be2adce57167909113f-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2665.0,266.5 L2673.0,254.5 2657.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  You get in life what you have the courage to ask for.
    You                  | PRON                 | PRP                  | nsubj               
    get                  | VERB                 | VBP                  | ROOT                
    in                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    what                 | PRON                 | WP                   | dobj                
    you                  | PRON                 | PRP                  | nsubj               
    have                 | VERB                 | VBP                  | ccomp               
    the                  | DET                  | DT                   | det                 
    courage              | NOUN                 | NN                   | dobj                
    to                   | PART                 | TO                   | aux                 
    ask                  | VERB                 | VB                   | relcl               
    for                  | ADP                  | IN                   | prep                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="757a693357a84013a3dece4d01716e84-0" class="displacy" width="2150" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">You</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">get</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">what</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">have</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">courage</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">ask</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">for.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADP</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-0" stroke-width="2px" d="M70,264.5 C70,177.0 215.0,177.0 215.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-1" stroke-width="2px" d="M245,264.5 C245,177.0 390.0,177.0 390.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M390.0,266.5 L398.0,254.5 382.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-2" stroke-width="2px" d="M420,264.5 C420,177.0 565.0,177.0 565.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M565.0,266.5 L573.0,254.5 557.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-3" stroke-width="2px" d="M770,264.5 C770,89.5 1095.0,89.5 1095.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,266.5 L762,254.5 778,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-4" stroke-width="2px" d="M945,264.5 C945,177.0 1090.0,177.0 1090.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,266.5 L937,254.5 953,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-5" stroke-width="2px" d="M245,264.5 C245,2.0 1100.0,2.0 1100.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1100.0,266.5 L1108.0,254.5 1092.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-6" stroke-width="2px" d="M1295,264.5 C1295,177.0 1440.0,177.0 1440.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,266.5 L1287,254.5 1303,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-7" stroke-width="2px" d="M1120,264.5 C1120,89.5 1445.0,89.5 1445.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1445.0,266.5 L1453.0,254.5 1437.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-8" stroke-width="2px" d="M1645,264.5 C1645,177.0 1790.0,177.0 1790.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,266.5 L1637,254.5 1653,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-9" stroke-width="2px" d="M1470,264.5 C1470,89.5 1795.0,89.5 1795.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1795.0,266.5 L1803.0,254.5 1787.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-757a693357a84013a3dece4d01716e84-0-10" stroke-width="2px" d="M1820,264.5 C1820,177.0 1965.0,177.0 1965.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-757a693357a84013a3dece4d01716e84-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1965.0,266.5 L1973.0,254.5 1957.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  People have different reasons for the way they live their lives. You cannot put everyone's reasons in the same box.
    People               | NOUN                 | NNS                  | nsubj               
    have                 | VERB                 | VBP                  | ROOT                
    different            | ADJ                  | JJ                   | amod                
    reasons              | NOUN                 | NNS                  | dobj                
    for                  | ADP                  | IN                   | prep                
    the                  | DET                  | DT                   | det                 
    way                  | NOUN                 | NN                   | pobj                
    they                 | PRON                 | PRP                  | nsubj               
    live                 | VERB                 | VBP                  | relcl               
    their                | DET                  | PRP$                 | poss                
    lives                | NOUN                 | NNS                  | dobj                
    .                    | PUNCT                | .                    | punct               
    You                  | PRON                 | PRP                  | nsubj               
    can                  | AUX                  | MD                   | aux                 
    not                  | ADV                  | RB                   | neg                 
    put                  | VERB                 | VB                   | ROOT                
    everyone             | NOUN                 | NN                   | poss                
    's                   | PART                 | POS                  | case                
    reasons              | NOUN                 | NNS                  | dobj                
    in                   | ADP                  | IN                   | prep                
    the                  | DET                  | DT                   | det                 
    same                 | ADJ                  | JJ                   | amod                
    box                  | NOUN                 | NN                   | pobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="896d835c014b435ebe3940f183dd56b0-0" class="displacy" width="3900" height="487.0" direction="ltr" style="max-width: none; height: 487.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="50">People</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="225">have</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="400">different</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="575">reasons</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="750">for</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="925">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">way</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">they</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">live</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">their</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">lives.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">You</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">can</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">put</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">everyone</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">'s</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">reasons</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3375">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3550">same</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3725">box.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3725">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-0" stroke-width="2px" d="M70,352.0 C70,264.5 210.0,264.5 210.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,354.0 L62,342.0 78,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-1" stroke-width="2px" d="M420,352.0 C420,264.5 560.0,264.5 560.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,354.0 L412,342.0 428,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-2" stroke-width="2px" d="M245,352.0 C245,177.0 565.0,177.0 565.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M565.0,354.0 L573.0,342.0 557.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-3" stroke-width="2px" d="M595,352.0 C595,264.5 735.0,264.5 735.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M735.0,354.0 L743.0,342.0 727.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-4" stroke-width="2px" d="M945,352.0 C945,264.5 1085.0,264.5 1085.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,354.0 L937,342.0 953,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-5" stroke-width="2px" d="M770,352.0 C770,177.0 1090.0,177.0 1090.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1090.0,354.0 L1098.0,342.0 1082.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-6" stroke-width="2px" d="M1295,352.0 C1295,264.5 1435.0,264.5 1435.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,354.0 L1287,342.0 1303,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-7" stroke-width="2px" d="M1120,352.0 C1120,177.0 1440.0,177.0 1440.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1440.0,354.0 L1448.0,342.0 1432.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-8" stroke-width="2px" d="M1645,352.0 C1645,264.5 1785.0,264.5 1785.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,354.0 L1637,342.0 1653,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-9" stroke-width="2px" d="M1470,352.0 C1470,177.0 1790.0,177.0 1790.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1790.0,354.0 L1798.0,342.0 1782.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-10" stroke-width="2px" d="M1995,352.0 C1995,89.5 2495.0,89.5 2495.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,354.0 L1987,342.0 2003,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-11" stroke-width="2px" d="M2170,352.0 C2170,177.0 2490.0,177.0 2490.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,354.0 L2162,342.0 2178,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-12" stroke-width="2px" d="M2345,352.0 C2345,264.5 2485.0,264.5 2485.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,354.0 L2337,342.0 2353,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-13" stroke-width="2px" d="M2695,352.0 C2695,177.0 3015.0,177.0 3015.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,354.0 L2687,342.0 2703,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-14" stroke-width="2px" d="M2695,352.0 C2695,264.5 2835.0,264.5 2835.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">case</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2835.0,354.0 L2843.0,342.0 2827.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-15" stroke-width="2px" d="M2520,352.0 C2520,89.5 3020.0,89.5 3020.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3020.0,354.0 L3028.0,342.0 3012.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-16" stroke-width="2px" d="M2520,352.0 C2520,2.0 3200.0,2.0 3200.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3200.0,354.0 L3208.0,342.0 3192.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-17" stroke-width="2px" d="M3395,352.0 C3395,177.0 3715.0,177.0 3715.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3395,354.0 L3387,342.0 3403,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-18" stroke-width="2px" d="M3570,352.0 C3570,264.5 3710.0,264.5 3710.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3570,354.0 L3562,342.0 3578,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-896d835c014b435ebe3940f183dd56b0-0-19" stroke-width="2px" d="M3220,352.0 C3220,89.5 3720.0,89.5 3720.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-896d835c014b435ebe3940f183dd56b0-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3720.0,354.0 L3728.0,342.0 3712.0,342.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Mellow doesn't always make for a good story, but it makes for a good life.
    Mellow               | PROPN                | NNP                  | nsubj               
    does                 | VERB                 | VBZ                  | aux                 
    n't                  | ADV                  | RB                   | neg                 
    always               | ADV                  | RB                   | advmod              
    make                 | VERB                 | VB                   | ROOT                
    for                  | ADP                  | IN                   | prep                
    a                    | DET                  | DT                   | det                 
    good                 | ADJ                  | JJ                   | amod                
    story                | NOUN                 | NN                   | pobj                
    ,                    | PUNCT                | ,                    | punct               
    but                  | CCONJ                | CC                   | cc                  
    it                   | PRON                 | PRP                  | nsubj               
    makes                | VERB                 | VBZ                  | conj                
    for                  | ADP                  | IN                   | prep                
    a                    | DET                  | DT                   | det                 
    good                 | ADJ                  | JJ                   | amod                
    life                 | NOUN                 | NN                   | pobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="d5a97af2d5964f488c81b89ab0ec8392-0" class="displacy" width="2850" height="662.0" direction="ltr" style="max-width: none; height: 662.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Mellow</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">PROPN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="225">does</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="400">n't</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="575">always</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="750">make</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="925">for</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">good</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">story,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">but</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">makes</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">for</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">good</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">life.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-0" stroke-width="2px" d="M70,527.0 C70,177.0 740.0,177.0 740.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,529.0 L62,517.0 78,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-1" stroke-width="2px" d="M245,527.0 C245,264.5 735.0,264.5 735.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,529.0 L237,517.0 253,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-2" stroke-width="2px" d="M420,527.0 C420,352.0 730.0,352.0 730.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,529.0 L412,517.0 428,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-3" stroke-width="2px" d="M595,527.0 C595,439.5 725.0,439.5 725.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,529.0 L587,517.0 603,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-4" stroke-width="2px" d="M770,527.0 C770,439.5 900.0,439.5 900.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M900.0,529.0 L908.0,517.0 892.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-5" stroke-width="2px" d="M1120,527.0 C1120,352.0 1430.0,352.0 1430.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,529.0 L1112,517.0 1128,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-6" stroke-width="2px" d="M1295,527.0 C1295,439.5 1425.0,439.5 1425.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,529.0 L1287,517.0 1303,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-7" stroke-width="2px" d="M945,527.0 C945,264.5 1435.0,264.5 1435.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1435.0,529.0 L1443.0,517.0 1427.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-8" stroke-width="2px" d="M770,527.0 C770,89.5 1620.0,89.5 1620.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1620.0,529.0 L1628.0,517.0 1612.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-9" stroke-width="2px" d="M1820,527.0 C1820,439.5 1950.0,439.5 1950.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,529.0 L1812,517.0 1828,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-10" stroke-width="2px" d="M770,527.0 C770,2.0 1975.0,2.0 1975.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1975.0,529.0 L1983.0,517.0 1967.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-11" stroke-width="2px" d="M1995,527.0 C1995,439.5 2125.0,439.5 2125.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2125.0,529.0 L2133.0,517.0 2117.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-12" stroke-width="2px" d="M2345,527.0 C2345,352.0 2655.0,352.0 2655.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,529.0 L2337,517.0 2353,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-13" stroke-width="2px" d="M2520,527.0 C2520,439.5 2650.0,439.5 2650.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2520,529.0 L2512,517.0 2528,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d5a97af2d5964f488c81b89ab0ec8392-0-14" stroke-width="2px" d="M2170,527.0 C2170,264.5 2660.0,264.5 2660.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d5a97af2d5964f488c81b89ab0ec8392-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2660.0,529.0 L2668.0,517.0 2652.0,517.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Work like you don't need the money, love like you've never been hurt and dance like no one is watching.
    Work                 | VERB                 | VB                   | nsubjpass           
    like                 | ADP                  | IN                   | mark                
    you                  | PRON                 | PRP                  | nsubj               
    do                   | VERB                 | VBP                  | aux                 
    n't                  | ADV                  | RB                   | neg                 
    need                 | VERB                 | VB                   | advcl               
    the                  | DET                  | DT                   | det                 
    money                | NOUN                 | NN                   | dobj                
    ,                    | PUNCT                | ,                    | punct               
    love                 | VERB                 | VBP                  | dep                 
    like                 | ADP                  | IN                   | intj                
    you                  | PRON                 | PRP                  | nsubjpass           
    've                  | VERB                 | VB                   | aux                 
    never                | ADV                  | RB                   | neg                 
    been                 | VERB                 | VBN                  | auxpass             
    hurt                 | VERB                 | VBN                  | ROOT                
    and                  | CCONJ                | CC                   | cc                  
    dance                | VERB                 | VB                   | conj                
    like                 | ADP                  | IN                   | mark                
    no                   | DET                  | DT                   | det                 
    one                  | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | aux                 
    watching             | VERB                 | VBG                  | advcl               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="35f762fcd56842e28ff28deba1505777-0" class="displacy" width="3900" height="749.5" direction="ltr" style="max-width: none; height: 749.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Work</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="225">like</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="400">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="575">do</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="750">n't</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="925">need</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">money,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">love</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">like</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">'ve</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">never</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">been</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">hurt</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="2675">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="2850">dance</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="3025">like</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="3200">no</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="3375">one</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="3550">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="3725">watching.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3725">VERB</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-0" stroke-width="2px" d="M70,614.5 C70,2.0 2500.0,2.0 2500.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubjpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,616.5 L62,604.5 78,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-1" stroke-width="2px" d="M245,614.5 C245,264.5 910.0,264.5 910.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,616.5 L237,604.5 253,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-2" stroke-width="2px" d="M420,614.5 C420,352.0 905.0,352.0 905.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,616.5 L412,604.5 428,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-3" stroke-width="2px" d="M595,614.5 C595,439.5 900.0,439.5 900.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,616.5 L587,604.5 603,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-4" stroke-width="2px" d="M770,614.5 C770,527.0 895.0,527.0 895.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,616.5 L762,604.5 778,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-5" stroke-width="2px" d="M70,614.5 C70,177.0 915.0,177.0 915.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M915.0,616.5 L923.0,604.5 907.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-6" stroke-width="2px" d="M1120,614.5 C1120,527.0 1245.0,527.0 1245.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,616.5 L1112,604.5 1128,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-7" stroke-width="2px" d="M945,614.5 C945,439.5 1250.0,439.5 1250.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1250.0,616.5 L1258.0,604.5 1242.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-8" stroke-width="2px" d="M70,614.5 C70,89.5 1445.0,89.5 1445.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1445.0,616.5 L1453.0,604.5 1437.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-9" stroke-width="2px" d="M1470,614.5 C1470,527.0 1595.0,527.0 1595.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">intj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1595.0,616.5 L1603.0,604.5 1587.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-10" stroke-width="2px" d="M1820,614.5 C1820,264.5 2485.0,264.5 2485.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubjpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,616.5 L1812,604.5 1828,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-11" stroke-width="2px" d="M1995,614.5 C1995,352.0 2480.0,352.0 2480.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,616.5 L1987,604.5 2003,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-12" stroke-width="2px" d="M2170,614.5 C2170,439.5 2475.0,439.5 2475.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,616.5 L2162,604.5 2178,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-13" stroke-width="2px" d="M2345,614.5 C2345,527.0 2470.0,527.0 2470.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">auxpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,616.5 L2337,604.5 2353,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-14" stroke-width="2px" d="M2520,614.5 C2520,527.0 2645.0,527.0 2645.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2645.0,616.5 L2653.0,604.5 2637.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-15" stroke-width="2px" d="M2520,614.5 C2520,439.5 2825.0,439.5 2825.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2825.0,616.5 L2833.0,604.5 2817.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-16" stroke-width="2px" d="M3045,614.5 C3045,264.5 3710.0,264.5 3710.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3045,616.5 L3037,604.5 3053,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-17" stroke-width="2px" d="M3220,614.5 C3220,527.0 3345.0,527.0 3345.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3220,616.5 L3212,604.5 3228,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-18" stroke-width="2px" d="M3395,614.5 C3395,439.5 3700.0,439.5 3700.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3395,616.5 L3387,604.5 3403,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-19" stroke-width="2px" d="M3570,614.5 C3570,527.0 3695.0,527.0 3695.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3570,616.5 L3562,604.5 3578,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-35f762fcd56842e28ff28deba1505777-0-20" stroke-width="2px" d="M2870,614.5 C2870,177.0 3715.0,177.0 3715.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-35f762fcd56842e28ff28deba1505777-0-20" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3715.0,616.5 L3723.0,604.5 3707.0,604.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  When one door closes, another opens; but we often look so long and so regretfully upon the closed door that we do not see the one that has opened for us.
    When                 | ADV                  | WRB                  | advmod              
    one                  | NUM                  | CD                   | nummod              
    door                 | NOUN                 | NN                   | nsubj               
    closes               | VERB                 | VBZ                  | advcl               
    ,                    | PUNCT                | ,                    | punct               
    another              | DET                  | DT                   | nsubj               
    opens                | VERB                 | VBZ                  | ROOT                
    ;                    | PUNCT                | :                    | punct               
    but                  | CCONJ                | CC                   | cc                  
    we                   | PRON                 | PRP                  | nsubj               
    often                | ADV                  | RB                   | advmod              
    look                 | VERB                 | VBP                  | conj                
    so                   | ADV                  | RB                   | advmod              
    long                 | ADV                  | RB                   | advmod              
    and                  | CCONJ                | CC                   | cc                  
    so                   | ADV                  | RB                   | advmod              
    regretfully          | ADV                  | RB                   | conj                
    upon                 | ADP                  | IN                   | prep                
    the                  | DET                  | DT                   | det                 
    closed               | ADJ                  | JJ                   | amod                
    door                 | NOUN                 | NN                   | pobj                
    that                 | DET                  | WDT                  | mark                
    we                   | PRON                 | PRP                  | nsubj               
    do                   | VERB                 | VBP                  | aux                 
    not                  | ADV                  | RB                   | neg                 
    see                  | VERB                 | VB                   | ccomp               
    the                  | DET                  | DT                   | det                 
    one                  | NOUN                 | NN                   | dobj                
    that                 | DET                  | WDT                  | nsubj               
    has                  | VERB                 | VBZ                  | aux                 
    opened               | VERB                 | VBN                  | relcl               
    for                  | ADP                  | IN                   | dative              
    us                   | PRON                 | PRP                  | pobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="e7e2bdcb60eb4d35a08ed715d2f23581-0" class="displacy" width="5475" height="662.0" direction="ltr" style="max-width: none; height: 662.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="50">When</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="225">one</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="400">door</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="575">closes,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="750">another</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="925">opens;</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">but</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">often</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">look</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">so</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">long</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">so</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">regretfully</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">upon</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">closed</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">door</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3375">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3550">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3725">do</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3725">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3900">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3900">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="4075">see</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4075">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="4250">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4250">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="4425">one</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4425">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="4600">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4600">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="4775">has</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4775">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="4950">opened</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4950">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="5125">for</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5125">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="5300">us.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5300">PRON</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-0" stroke-width="2px" d="M70,527.0 C70,264.5 560.0,264.5 560.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,529.0 L62,517.0 78,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-1" stroke-width="2px" d="M245,527.0 C245,439.5 375.0,439.5 375.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nummod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,529.0 L237,517.0 253,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-2" stroke-width="2px" d="M420,527.0 C420,439.5 550.0,439.5 550.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,529.0 L412,517.0 428,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-3" stroke-width="2px" d="M595,527.0 C595,352.0 905.0,352.0 905.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,529.0 L587,517.0 603,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-4" stroke-width="2px" d="M770,527.0 C770,439.5 900.0,439.5 900.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,529.0 L762,517.0 778,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-5" stroke-width="2px" d="M945,527.0 C945,439.5 1075.0,439.5 1075.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1075.0,529.0 L1083.0,517.0 1067.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-6" stroke-width="2px" d="M1295,527.0 C1295,352.0 1605.0,352.0 1605.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,529.0 L1287,517.0 1303,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-7" stroke-width="2px" d="M1470,527.0 C1470,439.5 1600.0,439.5 1600.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1470,529.0 L1462,517.0 1478,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-8" stroke-width="2px" d="M945,527.0 C945,177.0 1615.0,177.0 1615.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1615.0,529.0 L1623.0,517.0 1607.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-9" stroke-width="2px" d="M1820,527.0 C1820,439.5 1950.0,439.5 1950.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,529.0 L1812,517.0 1828,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-10" stroke-width="2px" d="M1645,527.0 C1645,352.0 1955.0,352.0 1955.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1955.0,529.0 L1963.0,517.0 1947.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-11" stroke-width="2px" d="M1995,527.0 C1995,439.5 2125.0,439.5 2125.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2125.0,529.0 L2133.0,517.0 2117.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-12" stroke-width="2px" d="M2345,527.0 C2345,439.5 2475.0,439.5 2475.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,529.0 L2337,517.0 2353,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-13" stroke-width="2px" d="M1995,527.0 C1995,264.5 2485.0,264.5 2485.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2485.0,529.0 L2493.0,517.0 2477.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-14" stroke-width="2px" d="M1645,527.0 C1645,89.5 2670.0,89.5 2670.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2670.0,529.0 L2678.0,517.0 2662.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-15" stroke-width="2px" d="M2870,527.0 C2870,352.0 3180.0,352.0 3180.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2870,529.0 L2862,517.0 2878,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-16" stroke-width="2px" d="M3045,527.0 C3045,439.5 3175.0,439.5 3175.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3045,529.0 L3037,517.0 3053,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-17" stroke-width="2px" d="M2695,527.0 C2695,264.5 3185.0,264.5 3185.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3185.0,529.0 L3193.0,517.0 3177.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-18" stroke-width="2px" d="M3395,527.0 C3395,177.0 4065.0,177.0 4065.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3395,529.0 L3387,517.0 3403,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-19" stroke-width="2px" d="M3570,527.0 C3570,264.5 4060.0,264.5 4060.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3570,529.0 L3562,517.0 3578,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-20" stroke-width="2px" d="M3745,527.0 C3745,352.0 4055.0,352.0 4055.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-20" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3745,529.0 L3737,517.0 3753,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-21" stroke-width="2px" d="M3920,527.0 C3920,439.5 4050.0,439.5 4050.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-21" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3920,529.0 L3912,517.0 3928,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-22" stroke-width="2px" d="M1645,527.0 C1645,2.0 4075.0,2.0 4075.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-22" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4075.0,529.0 L4083.0,517.0 4067.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-23" stroke-width="2px" d="M4270,527.0 C4270,439.5 4400.0,439.5 4400.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-23" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4270,529.0 L4262,517.0 4278,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-24" stroke-width="2px" d="M4095,527.0 C4095,352.0 4405.0,352.0 4405.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-24" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4405.0,529.0 L4413.0,517.0 4397.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-25" stroke-width="2px" d="M4620,527.0 C4620,352.0 4930.0,352.0 4930.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-25" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4620,529.0 L4612,517.0 4628,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-26" stroke-width="2px" d="M4795,527.0 C4795,439.5 4925.0,439.5 4925.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-26" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4795,529.0 L4787,517.0 4803,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-27" stroke-width="2px" d="M4445,527.0 C4445,264.5 4935.0,264.5 4935.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-27" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4935.0,529.0 L4943.0,517.0 4927.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-28" stroke-width="2px" d="M4970,527.0 C4970,439.5 5100.0,439.5 5100.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-28" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dative</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5100.0,529.0 L5108.0,517.0 5092.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-29" stroke-width="2px" d="M5145,527.0 C5145,439.5 5275.0,439.5 5275.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e7e2bdcb60eb4d35a08ed715d2f23581-0-29" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5275.0,529.0 L5283.0,517.0 5267.0,517.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  There comes a time when you have to choose between turning the page and closing the book.
    There                | ADV                  | EX                   | expl                
    comes                | VERB                 | VBZ                  | ROOT                
    a                    | DET                  | DT                   | det                 
    time                 | NOUN                 | NN                   | attr                
    when                 | ADV                  | WRB                  | advmod              
    you                  | PRON                 | PRP                  | nsubj               
    have                 | VERB                 | VBP                  | relcl               
    to                   | PART                 | TO                   | aux                 
    choose               | VERB                 | VB                   | xcomp               
    between              | ADP                  | IN                   | prep                
    turning              | VERB                 | VBG                  | pcomp               
    the                  | DET                  | DT                   | det                 
    page                 | NOUN                 | NN                   | dobj                
    and                  | CCONJ                | CC                   | cc                  
    closing              | VERB                 | VBG                  | conj                
    the                  | DET                  | DT                   | det                 
    book                 | NOUN                 | NN                   | dobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="d654f4aa687c415ba3f43026b8393a97-0" class="displacy" width="3025" height="487.0" direction="ltr" style="max-width: none; height: 487.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="50">There</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="225">comes</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="400">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="575">time</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="750">when</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="925">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">have</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">choose</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">between</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">turning</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">page</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">closing</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">book.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-0" stroke-width="2px" d="M70,352.0 C70,264.5 210.0,264.5 210.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">expl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,354.0 L62,342.0 78,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-1" stroke-width="2px" d="M420,352.0 C420,264.5 560.0,264.5 560.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,354.0 L412,342.0 428,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-2" stroke-width="2px" d="M245,352.0 C245,177.0 565.0,177.0 565.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M565.0,354.0 L573.0,342.0 557.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-3" stroke-width="2px" d="M770,352.0 C770,177.0 1090.0,177.0 1090.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,354.0 L762,342.0 778,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-4" stroke-width="2px" d="M945,352.0 C945,264.5 1085.0,264.5 1085.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,354.0 L937,342.0 953,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-5" stroke-width="2px" d="M595,352.0 C595,89.5 1095.0,89.5 1095.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1095.0,354.0 L1103.0,342.0 1087.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-6" stroke-width="2px" d="M1295,352.0 C1295,264.5 1435.0,264.5 1435.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,354.0 L1287,342.0 1303,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-7" stroke-width="2px" d="M1120,352.0 C1120,177.0 1440.0,177.0 1440.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1440.0,354.0 L1448.0,342.0 1432.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-8" stroke-width="2px" d="M1470,352.0 C1470,264.5 1610.0,264.5 1610.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1610.0,354.0 L1618.0,342.0 1602.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-9" stroke-width="2px" d="M1645,352.0 C1645,264.5 1785.0,264.5 1785.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1785.0,354.0 L1793.0,342.0 1777.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-10" stroke-width="2px" d="M1995,352.0 C1995,264.5 2135.0,264.5 2135.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,354.0 L1987,342.0 2003,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-11" stroke-width="2px" d="M1820,352.0 C1820,177.0 2140.0,177.0 2140.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2140.0,354.0 L2148.0,342.0 2132.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-12" stroke-width="2px" d="M1820,352.0 C1820,89.5 2320.0,89.5 2320.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2320.0,354.0 L2328.0,342.0 2312.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-13" stroke-width="2px" d="M1820,352.0 C1820,2.0 2500.0,2.0 2500.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2500.0,354.0 L2508.0,342.0 2492.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-14" stroke-width="2px" d="M2695,352.0 C2695,264.5 2835.0,264.5 2835.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,354.0 L2687,342.0 2703,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d654f4aa687c415ba3f43026b8393a97-0-15" stroke-width="2px" d="M2520,352.0 C2520,177.0 2840.0,177.0 2840.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d654f4aa687c415ba3f43026b8393a97-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2840.0,354.0 L2848.0,342.0 2832.0,342.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  To live is the rarest thing in the world. Most people exist, that is all.
    To                   | PART                 | TO                   | aux                 
    live                 | VERB                 | VB                   | acomp               
    is                   | VERB                 | VBZ                  | ROOT                
    the                  | DET                  | DT                   | det                 
    rarest               | ADJ                  | JJS                  | amod                
    thing                | NOUN                 | NN                   | attr                
    in                   | ADP                  | IN                   | prep                
    the                  | DET                  | DT                   | det                 
    world                | NOUN                 | NN                   | pobj                
    .                    | PUNCT                | .                    | punct               
    Most                 | ADJ                  | JJS                  | amod                
    people               | NOUN                 | NNS                  | nsubj               
    exist                | VERB                 | VBP                  | ROOT                
    ,                    | PUNCT                | ,                    | punct               
    that                 | DET                  | DT                   | nsubj               
    is                   | VERB                 | VBZ                  | ccomp               
    all                  | DET                  | DT                   | attr                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="d964afebd3154b0f886872274af8223b-0" class="displacy" width="2675" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">To</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">live</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">rarest</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">thing</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">world.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">Most</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">people</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">exist,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">all.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">DET</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-0" stroke-width="2px" d="M70,264.5 C70,177.0 215.0,177.0 215.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-1" stroke-width="2px" d="M245,264.5 C245,177.0 390.0,177.0 390.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,266.5 L237,254.5 253,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-2" stroke-width="2px" d="M595,264.5 C595,89.5 920.0,89.5 920.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,266.5 L587,254.5 603,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-3" stroke-width="2px" d="M770,264.5 C770,177.0 915.0,177.0 915.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,266.5 L762,254.5 778,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-4" stroke-width="2px" d="M420,264.5 C420,2.0 925.0,2.0 925.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M925.0,266.5 L933.0,254.5 917.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-5" stroke-width="2px" d="M945,264.5 C945,177.0 1090.0,177.0 1090.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1090.0,266.5 L1098.0,254.5 1082.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-6" stroke-width="2px" d="M1295,264.5 C1295,177.0 1440.0,177.0 1440.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,266.5 L1287,254.5 1303,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-7" stroke-width="2px" d="M1120,264.5 C1120,89.5 1445.0,89.5 1445.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1445.0,266.5 L1453.0,254.5 1437.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-8" stroke-width="2px" d="M1645,264.5 C1645,177.0 1790.0,177.0 1790.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,266.5 L1637,254.5 1653,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-9" stroke-width="2px" d="M1820,264.5 C1820,177.0 1965.0,177.0 1965.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,266.5 L1812,254.5 1828,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-10" stroke-width="2px" d="M2170,264.5 C2170,177.0 2315.0,177.0 2315.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,266.5 L2162,254.5 2178,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-11" stroke-width="2px" d="M1995,264.5 C1995,89.5 2320.0,89.5 2320.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2320.0,266.5 L2328.0,254.5 2312.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d964afebd3154b0f886872274af8223b-0-12" stroke-width="2px" d="M2345,264.5 C2345,177.0 2490.0,177.0 2490.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d964afebd3154b0f886872274af8223b-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2490.0,266.5 L2498.0,254.5 2482.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is what happens to you while you're busy making other plans.
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    what                 | PRON                 | WP                   | nsubj               
    happens              | VERB                 | VBZ                  | ccomp               
    to                   | ADP                  | IN                   | prep                
    you                  | PRON                 | PRP                  | pobj                
    while                | ADP                  | IN                   | mark                
    you                  | PRON                 | PRP                  | nsubj               
    're                  | VERB                 | VBP                  | advcl               
    busy                 | ADJ                  | JJ                   | acomp               
    making               | VERB                 | VBG                  | xcomp               
    other                | ADJ                  | JJ                   | amod                
    plans                | NOUN                 | NNS                  | dobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="b82abdb18c8a431c92f709d3fe22714f-0" class="displacy" width="2325" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">what</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">happens</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">while</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">'re</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">busy</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">making</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">other</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">plans.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-0" stroke-width="2px" d="M70,264.5 C70,177.0 215.0,177.0 215.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-1" stroke-width="2px" d="M420,264.5 C420,177.0 565.0,177.0 565.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,266.5 L412,254.5 428,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-2" stroke-width="2px" d="M245,264.5 C245,89.5 570.0,89.5 570.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M570.0,266.5 L578.0,254.5 562.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-3" stroke-width="2px" d="M595,264.5 C595,177.0 740.0,177.0 740.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M740.0,266.5 L748.0,254.5 732.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-4" stroke-width="2px" d="M770,264.5 C770,177.0 915.0,177.0 915.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M915.0,266.5 L923.0,254.5 907.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-5" stroke-width="2px" d="M1120,264.5 C1120,89.5 1445.0,89.5 1445.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,266.5 L1112,254.5 1128,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-6" stroke-width="2px" d="M1295,264.5 C1295,177.0 1440.0,177.0 1440.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,266.5 L1287,254.5 1303,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-7" stroke-width="2px" d="M595,264.5 C595,2.0 1450.0,2.0 1450.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1450.0,266.5 L1458.0,254.5 1442.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-8" stroke-width="2px" d="M1470,264.5 C1470,177.0 1615.0,177.0 1615.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1615.0,266.5 L1623.0,254.5 1607.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-9" stroke-width="2px" d="M1645,264.5 C1645,177.0 1790.0,177.0 1790.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1790.0,266.5 L1798.0,254.5 1782.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-10" stroke-width="2px" d="M1995,264.5 C1995,177.0 2140.0,177.0 2140.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,266.5 L1987,254.5 2003,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b82abdb18c8a431c92f709d3fe22714f-0-11" stroke-width="2px" d="M1820,264.5 C1820,89.5 2145.0,89.5 2145.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b82abdb18c8a431c92f709d3fe22714f-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2145.0,266.5 L2153.0,254.5 2137.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well.     
    The                  | DET                  | DT                   | det                 
    purpose              | NOUN                 | NN                   | nsubj               
    of                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    is                   | VERB                 | VBZ                  | ROOT                
    not                  | ADV                  | RB                   | neg                 
    to                   | PART                 | TO                   | aux                 
    be                   | VERB                 | VB                   | xcomp               
    happy                | ADJ                  | JJ                   | acomp               
    .                    | PUNCT                | .                    | punct               
    It                   | PRON                 | PRP                  | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    to                   | PART                 | TO                   | aux                 
    be                   | VERB                 | VB                   | xcomp               
    useful               | ADJ                  | JJ                   | acomp               
    ,                    | PUNCT                | ,                    | punct               
    to                   | PART                 | TO                   | aux                 
    be                   | VERB                 | VB                   | conj                
    honorable            | ADJ                  | JJ                   | acomp               
    ,                    | PUNCT                | ,                    | punct               
    to                   | PART                 | TO                   | aux                 
    be                   | VERB                 | VB                   | conj                
    compassionate        | ADJ                  | JJ                   | acomp               
    ,                    | PUNCT                | ,                    | punct               
    to                   | PART                 | TO                   | aux                 
    have                 | VERB                 | VB                   | pobj                
    it                   | PRON                 | PRP                  | nsubj               
    make                 | VERB                 | VB                   | ccomp               
    some                 | DET                  | DT                   | det                 
    difference           | NOUN                 | NN                   | dobj                
    that                 | DET                  | WDT                  | mark                
    you                  | PRON                 | PRP                  | nsubj               
    have                 | VERB                 | VBP                  | aux                 
    lived                | VERB                 | VBN                  | ccomp               
    and                  | CCONJ                | CC                   | cc                  
    lived                | VERB                 | VBD                  | conj                
    well                 | ADV                  | RB                   | advmod              
    .                    | PUNCT                | .                    | punct               
                         | SPACE                | _SP                  |                     



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="099a8c3f850246ce94123d7c9d7bb203-0" class="displacy" width="6000" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">The</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">purpose</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">be</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">happy.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">It</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">be</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">useful,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2675">be</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2850">honorable,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3025">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3200">be</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3375">compassionate,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3550">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3725">have</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3725">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3900">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3900">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="4075">make</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4075">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="4250">some</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4250">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="4425">difference</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4425">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="4600">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4600">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="4775">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4775">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="4950">have</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4950">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="5125">lived</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5125">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="5300">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5300">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="5475">lived</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5475">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="5650">well.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5650">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="5825">    </tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5825">SPACE</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-0" stroke-width="2px" d="M70,439.5 C70,352.0 205.0,352.0 205.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-1" stroke-width="2px" d="M245,439.5 C245,177.0 740.0,177.0 740.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,441.5 L237,429.5 253,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-2" stroke-width="2px" d="M245,439.5 C245,352.0 380.0,352.0 380.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M380.0,441.5 L388.0,429.5 372.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-3" stroke-width="2px" d="M420,439.5 C420,352.0 555.0,352.0 555.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M555.0,441.5 L563.0,429.5 547.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-4" stroke-width="2px" d="M945,439.5 C945,264.5 1260.0,264.5 1260.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,441.5 L937,429.5 953,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-5" stroke-width="2px" d="M1120,439.5 C1120,352.0 1255.0,352.0 1255.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,441.5 L1112,429.5 1128,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-6" stroke-width="2px" d="M770,439.5 C770,177.0 1265.0,177.0 1265.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1265.0,441.5 L1273.0,429.5 1257.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-7" stroke-width="2px" d="M1295,439.5 C1295,352.0 1430.0,352.0 1430.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1430.0,441.5 L1438.0,429.5 1422.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-8" stroke-width="2px" d="M1645,439.5 C1645,352.0 1780.0,352.0 1780.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,441.5 L1637,429.5 1653,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-9" stroke-width="2px" d="M1995,439.5 C1995,352.0 2130.0,352.0 2130.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,441.5 L1987,429.5 2003,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-10" stroke-width="2px" d="M1820,439.5 C1820,264.5 2135.0,264.5 2135.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2135.0,441.5 L2143.0,429.5 2127.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-11" stroke-width="2px" d="M2170,439.5 C2170,352.0 2305.0,352.0 2305.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2305.0,441.5 L2313.0,429.5 2297.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-12" stroke-width="2px" d="M2520,439.5 C2520,352.0 2655.0,352.0 2655.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2520,441.5 L2512,429.5 2528,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-13" stroke-width="2px" d="M2170,439.5 C2170,177.0 2665.0,177.0 2665.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2665.0,441.5 L2673.0,429.5 2657.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-14" stroke-width="2px" d="M2695,439.5 C2695,352.0 2830.0,352.0 2830.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2830.0,441.5 L2838.0,429.5 2822.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-15" stroke-width="2px" d="M3045,439.5 C3045,352.0 3180.0,352.0 3180.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3045,441.5 L3037,429.5 3053,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-16" stroke-width="2px" d="M2695,439.5 C2695,177.0 3190.0,177.0 3190.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3190.0,441.5 L3198.0,429.5 3182.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-17" stroke-width="2px" d="M3220,439.5 C3220,352.0 3355.0,352.0 3355.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3355.0,441.5 L3363.0,429.5 3347.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-18" stroke-width="2px" d="M3570,439.5 C3570,352.0 3705.0,352.0 3705.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3570,441.5 L3562,429.5 3578,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-19" stroke-width="2px" d="M3395,439.5 C3395,264.5 3710.0,264.5 3710.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3710.0,441.5 L3718.0,429.5 3702.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-20" stroke-width="2px" d="M3920,439.5 C3920,352.0 4055.0,352.0 4055.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-20" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3920,441.5 L3912,429.5 3928,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-21" stroke-width="2px" d="M3745,439.5 C3745,264.5 4060.0,264.5 4060.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-21" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4060.0,441.5 L4068.0,429.5 4052.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-22" stroke-width="2px" d="M4270,439.5 C4270,352.0 4405.0,352.0 4405.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-22" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4270,441.5 L4262,429.5 4278,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-23" stroke-width="2px" d="M4095,439.5 C4095,264.5 4410.0,264.5 4410.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-23" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4410.0,441.5 L4418.0,429.5 4402.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-24" stroke-width="2px" d="M4620,439.5 C4620,177.0 5115.0,177.0 5115.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-24" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4620,441.5 L4612,429.5 4628,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-25" stroke-width="2px" d="M4795,439.5 C4795,264.5 5110.0,264.5 5110.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-25" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4795,441.5 L4787,429.5 4803,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-26" stroke-width="2px" d="M4970,439.5 C4970,352.0 5105.0,352.0 5105.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-26" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4970,441.5 L4962,429.5 4978,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-27" stroke-width="2px" d="M4095,439.5 C4095,89.5 5120.0,89.5 5120.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-27" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5120.0,441.5 L5128.0,429.5 5112.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-28" stroke-width="2px" d="M5145,439.5 C5145,352.0 5280.0,352.0 5280.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-28" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5280.0,441.5 L5288.0,429.5 5272.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-29" stroke-width="2px" d="M5145,439.5 C5145,264.5 5460.0,264.5 5460.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-29" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5460.0,441.5 L5468.0,429.5 5452.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-30" stroke-width="2px" d="M1820,439.5 C1820,2.0 5650.0,2.0 5650.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-30" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">punct</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5650.0,441.5 L5658.0,429.5 5642.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-099a8c3f850246ce94123d7c9d7bb203-0-31" stroke-width="2px" d="M5670,439.5 C5670,352.0 5805.0,352.0 5805.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-099a8c3f850246ce94123d7c9d7bb203-0-31" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle"></textPath>
    </text>
    <path class="displacy-arrowhead" d="M5805.0,441.5 L5813.0,429.5 5797.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Be not afraid of life. Believe that life is worth living, and your belief will help create the fact.
    Be                   | VERB                 | VB                   | ROOT                
    not                  | ADV                  | RB                   | neg                 
    afraid               | ADJ                  | JJ                   | acomp               
    of                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    .                    | PUNCT                | .                    | punct               
    Believe              | VERB                 | VB                   | ROOT                
    that                 | ADP                  | IN                   | mark                
    life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ccomp               
    worth                | ADJ                  | JJ                   | acomp               
    living               | VERB                 | VBG                  | xcomp               
    ,                    | PUNCT                | ,                    | punct               
    and                  | CCONJ                | CC                   | cc                  
    your                 | DET                  | PRP$                 | poss                
    belief               | NOUN                 | NN                   | nsubj               
    will                 | VERB                 | MD                   | aux                 
    help                 | VERB                 | VB                   | conj                
    create               | VERB                 | VB                   | xcomp               
    the                  | DET                  | DT                   | det                 
    fact                 | NOUN                 | NN                   | dobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="bd1461271abe48b98e3eabc5a99381d5-0" class="displacy" width="3375" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Be</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">afraid</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">life.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">Believe</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">worth</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">living,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">your</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">belief</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">will</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2675">help</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2850">create</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3025">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3200">fact.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-0" stroke-width="2px" d="M70,439.5 C70,352.0 205.0,352.0 205.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M205.0,441.5 L213.0,429.5 197.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-1" stroke-width="2px" d="M70,439.5 C70,264.5 385.0,264.5 385.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M385.0,441.5 L393.0,429.5 377.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-2" stroke-width="2px" d="M420,439.5 C420,352.0 555.0,352.0 555.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M555.0,441.5 L563.0,429.5 547.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-3" stroke-width="2px" d="M595,439.5 C595,352.0 730.0,352.0 730.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M730.0,441.5 L738.0,429.5 722.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-4" stroke-width="2px" d="M1120,439.5 C1120,264.5 1435.0,264.5 1435.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,441.5 L1112,429.5 1128,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-5" stroke-width="2px" d="M1295,439.5 C1295,352.0 1430.0,352.0 1430.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,441.5 L1287,429.5 1303,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-6" stroke-width="2px" d="M945,439.5 C945,177.0 1440.0,177.0 1440.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1440.0,441.5 L1448.0,429.5 1432.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-7" stroke-width="2px" d="M1470,439.5 C1470,352.0 1605.0,352.0 1605.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1605.0,441.5 L1613.0,429.5 1597.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-8" stroke-width="2px" d="M1645,439.5 C1645,352.0 1780.0,352.0 1780.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1780.0,441.5 L1788.0,429.5 1772.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-9" stroke-width="2px" d="M945,439.5 C945,89.5 1970.0,89.5 1970.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1970.0,441.5 L1978.0,429.5 1962.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-10" stroke-width="2px" d="M2170,439.5 C2170,352.0 2305.0,352.0 2305.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,441.5 L2162,429.5 2178,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-11" stroke-width="2px" d="M2345,439.5 C2345,264.5 2660.0,264.5 2660.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,441.5 L2337,429.5 2353,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-12" stroke-width="2px" d="M2520,439.5 C2520,352.0 2655.0,352.0 2655.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2520,441.5 L2512,429.5 2528,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-13" stroke-width="2px" d="M945,439.5 C945,2.0 2675.0,2.0 2675.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2675.0,441.5 L2683.0,429.5 2667.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-14" stroke-width="2px" d="M2695,439.5 C2695,352.0 2830.0,352.0 2830.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2830.0,441.5 L2838.0,429.5 2822.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-15" stroke-width="2px" d="M3045,439.5 C3045,352.0 3180.0,352.0 3180.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3045,441.5 L3037,429.5 3053,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bd1461271abe48b98e3eabc5a99381d5-0-16" stroke-width="2px" d="M2870,439.5 C2870,264.5 3185.0,264.5 3185.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bd1461271abe48b98e3eabc5a99381d5-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3185.0,441.5 L3193.0,429.5 3177.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is a progress, and not a station.
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    a                    | DET                  | DT                   | det                 
    progress             | NOUN                 | NN                   | attr                
    ,                    | PUNCT                | ,                    | punct               
    and                  | CCONJ                | CC                   | cc                  
    not                  | ADV                  | RB                   | neg                 
    a                    | DET                  | DT                   | det                 
    station              | NOUN                 | NN                   | conj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="3fac989009d34fce8007abd01fe2005d-0" class="displacy" width="1450" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">progress,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">station.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-3fac989009d34fce8007abd01fe2005d-0-0" stroke-width="2px" d="M70,264.5 C70,177.0 215.0,177.0 215.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-3fac989009d34fce8007abd01fe2005d-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-3fac989009d34fce8007abd01fe2005d-0-1" stroke-width="2px" d="M420,264.5 C420,177.0 565.0,177.0 565.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-3fac989009d34fce8007abd01fe2005d-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,266.5 L412,254.5 428,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-3fac989009d34fce8007abd01fe2005d-0-2" stroke-width="2px" d="M245,264.5 C245,89.5 570.0,89.5 570.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-3fac989009d34fce8007abd01fe2005d-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M570.0,266.5 L578.0,254.5 562.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-3fac989009d34fce8007abd01fe2005d-0-3" stroke-width="2px" d="M595,264.5 C595,177.0 740.0,177.0 740.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-3fac989009d34fce8007abd01fe2005d-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M740.0,266.5 L748.0,254.5 732.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-3fac989009d34fce8007abd01fe2005d-0-4" stroke-width="2px" d="M945,264.5 C945,89.5 1270.0,89.5 1270.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-3fac989009d34fce8007abd01fe2005d-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,266.5 L937,254.5 953,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-3fac989009d34fce8007abd01fe2005d-0-5" stroke-width="2px" d="M1120,264.5 C1120,177.0 1265.0,177.0 1265.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-3fac989009d34fce8007abd01fe2005d-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,266.5 L1112,254.5 1128,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-3fac989009d34fce8007abd01fe2005d-0-6" stroke-width="2px" d="M595,264.5 C595,2.0 1275.0,2.0 1275.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-3fac989009d34fce8007abd01fe2005d-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1275.0,266.5 L1283.0,254.5 1267.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  To live is so startling it leaves little time for anything else.
    To                   | PART                 | TO                   | aux                 
    live                 | VERB                 | VB                   | csubj               
    is                   | VERB                 | VBZ                  | ROOT                
    so                   | ADV                  | RB                   | advmod              
    startling            | ADJ                  | JJ                   | acomp               
    it                   | PRON                 | PRP                  | nsubj               
    leaves               | VERB                 | VBZ                  | ccomp               
    little               | ADJ                  | JJ                   | amod                
    time                 | NOUN                 | NN                   | dobj                
    for                  | ADP                  | IN                   | prep                
    anything             | NOUN                 | NN                   | pobj                
    else                 | ADV                  | RB                   | advmod              
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="566746d0491e4502803361a4dabe3c7b-0" class="displacy" width="2150" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">To</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">live</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">so</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">startling</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">leaves</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">little</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">time</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">for</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">anything</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">else.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADV</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-0" stroke-width="2px" d="M70,264.5 C70,177.0 215.0,177.0 215.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-1" stroke-width="2px" d="M245,264.5 C245,177.0 390.0,177.0 390.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">csubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,266.5 L237,254.5 253,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-2" stroke-width="2px" d="M595,264.5 C595,177.0 740.0,177.0 740.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,266.5 L587,254.5 603,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-3" stroke-width="2px" d="M420,264.5 C420,89.5 745.0,89.5 745.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M745.0,266.5 L753.0,254.5 737.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-4" stroke-width="2px" d="M945,264.5 C945,177.0 1090.0,177.0 1090.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,266.5 L937,254.5 953,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-5" stroke-width="2px" d="M770,264.5 C770,89.5 1095.0,89.5 1095.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1095.0,266.5 L1103.0,254.5 1087.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-6" stroke-width="2px" d="M1295,264.5 C1295,177.0 1440.0,177.0 1440.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,266.5 L1287,254.5 1303,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-7" stroke-width="2px" d="M1120,264.5 C1120,89.5 1445.0,89.5 1445.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1445.0,266.5 L1453.0,254.5 1437.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-8" stroke-width="2px" d="M1120,264.5 C1120,2.0 1625.0,2.0 1625.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1625.0,266.5 L1633.0,254.5 1617.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-9" stroke-width="2px" d="M1645,264.5 C1645,177.0 1790.0,177.0 1790.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1790.0,266.5 L1798.0,254.5 1782.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-566746d0491e4502803361a4dabe3c7b-0-10" stroke-width="2px" d="M1820,264.5 C1820,177.0 1965.0,177.0 1965.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-566746d0491e4502803361a4dabe3c7b-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1965.0,266.5 L1973.0,254.5 1957.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  It is not the length of life, but depth of life.     
    It                   | PRON                 | PRP                  | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    not                  | ADV                  | RB                   | neg                 
    the                  | DET                  | DT                   | det                 
    length               | NOUN                 | NN                   | attr                
    of                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    ,                    | PUNCT                | ,                    | punct               
    but                  | CCONJ                | CC                   | cc                  
    depth                | NOUN                 | NN                   | conj                
    of                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    .                    | PUNCT                | .                    | punct               
                         | SPACE                | _SP                  |                     



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="50e839906918461da1ce2afabe9a7fef-0" class="displacy" width="2150" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">It</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">length</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">life,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">but</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">depth</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">life.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">    </tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">SPACE</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-0" stroke-width="2px" d="M70,439.5 C70,352.0 205.0,352.0 205.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-1" stroke-width="2px" d="M245,439.5 C245,352.0 380.0,352.0 380.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M380.0,441.5 L388.0,429.5 372.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-2" stroke-width="2px" d="M595,439.5 C595,352.0 730.0,352.0 730.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,441.5 L587,429.5 603,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-3" stroke-width="2px" d="M245,439.5 C245,264.5 735.0,264.5 735.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M735.0,441.5 L743.0,429.5 727.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-4" stroke-width="2px" d="M770,439.5 C770,352.0 905.0,352.0 905.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M905.0,441.5 L913.0,429.5 897.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-5" stroke-width="2px" d="M945,439.5 C945,352.0 1080.0,352.0 1080.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1080.0,441.5 L1088.0,429.5 1072.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-6" stroke-width="2px" d="M245,439.5 C245,177.0 1265.0,177.0 1265.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1265.0,441.5 L1273.0,429.5 1257.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-7" stroke-width="2px" d="M245,439.5 C245,89.5 1445.0,89.5 1445.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1445.0,441.5 L1453.0,429.5 1437.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-8" stroke-width="2px" d="M1470,439.5 C1470,352.0 1605.0,352.0 1605.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1605.0,441.5 L1613.0,429.5 1597.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-9" stroke-width="2px" d="M245,439.5 C245,2.0 1800.0,2.0 1800.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">punct</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1800.0,441.5 L1808.0,429.5 1792.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-50e839906918461da1ce2afabe9a7fef-0-10" stroke-width="2px" d="M1820,439.5 C1820,352.0 1955.0,352.0 1955.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-50e839906918461da1ce2afabe9a7fef-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle"></textPath>
    </text>
    <path class="displacy-arrowhead" d="M1955.0,441.5 L1963.0,429.5 1947.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is 10% what happens to us and 90% how we react to it.
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    10                   | NUM                  | CD                   | nummod              
    %                    | NOUN                 | NN                   | attr                
    what                 | PRON                 | WP                   | nsubj               
    happens              | VERB                 | VBZ                  | relcl               
    to                   | ADP                  | IN                   | prep                
    us                   | PRON                 | PRP                  | pobj                
    and                  | CCONJ                | CC                   | cc                  
    90                   | NUM                  | CD                   | nummod              
    %                    | NOUN                 | NN                   | conj                
    how                  | ADV                  | WRB                  | advmod              
    we                   | PRON                 | PRP                  | nsubj               
    react                | VERB                 | VBP                  | ccomp               
    to                   | ADP                  | IN                   | prep                
    it                   | PRON                 | PRP                  | pobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="e24578534c554adcb32bb842f7af37c4-0" class="displacy" width="2500" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">10%</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">what</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">happens</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">us</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">90%</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">how</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">react</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">it.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">PRON</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-0" stroke-width="2px" d="M70,439.5 C70,352.0 205.0,352.0 205.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-1" stroke-width="2px" d="M245,439.5 C245,352.0 380.0,352.0 380.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M380.0,441.5 L388.0,429.5 372.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-2" stroke-width="2px" d="M595,439.5 C595,352.0 730.0,352.0 730.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,441.5 L587,429.5 603,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-3" stroke-width="2px" d="M420,439.5 C420,264.5 735.0,264.5 735.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M735.0,441.5 L743.0,429.5 727.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-4" stroke-width="2px" d="M770,439.5 C770,352.0 905.0,352.0 905.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M905.0,441.5 L913.0,429.5 897.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-5" stroke-width="2px" d="M945,439.5 C945,352.0 1080.0,352.0 1080.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1080.0,441.5 L1088.0,429.5 1072.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-6" stroke-width="2px" d="M420,439.5 C420,177.0 1265.0,177.0 1265.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1265.0,441.5 L1273.0,429.5 1257.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-7" stroke-width="2px" d="M420,439.5 C420,89.5 1445.0,89.5 1445.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1445.0,441.5 L1453.0,429.5 1437.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-8" stroke-width="2px" d="M1645,439.5 C1645,264.5 1960.0,264.5 1960.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,441.5 L1637,429.5 1653,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-9" stroke-width="2px" d="M1820,439.5 C1820,352.0 1955.0,352.0 1955.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,441.5 L1812,429.5 1828,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-10" stroke-width="2px" d="M245,439.5 C245,2.0 1975.0,2.0 1975.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1975.0,441.5 L1983.0,429.5 1967.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-11" stroke-width="2px" d="M1995,439.5 C1995,352.0 2130.0,352.0 2130.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2130.0,441.5 L2138.0,429.5 2122.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e24578534c554adcb32bb842f7af37c4-0-12" stroke-width="2px" d="M2170,439.5 C2170,352.0 2305.0,352.0 2305.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e24578534c554adcb32bb842f7af37c4-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2305.0,441.5 L2313.0,429.5 2297.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Many of life's failures are experienced by people who did not realize how close they were to success when they gave up.
    Many                 | ADJ                  | JJ                   | nsubjpass           
    of                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | poss                
    's                   | PART                 | POS                  | case                
    failures             | NOUN                 | NNS                  | pobj                
    are                  | VERB                 | VBP                  | auxpass             
    experienced          | VERB                 | VBN                  | ROOT                
    by                   | ADP                  | IN                   | agent               
    people               | NOUN                 | NNS                  | pobj                
    who                  | PRON                 | WP                   | nsubj               
    did                  | VERB                 | VBD                  | aux                 
    not                  | ADV                  | RB                   | neg                 
    realize              | VERB                 | VB                   | relcl               
    how                  | ADV                  | WRB                  | advmod              
    close                | ADJ                  | JJ                   | acomp               
    they                 | PRON                 | PRP                  | nsubj               
    were                 | VERB                 | VBD                  | ccomp               
    to                   | ADP                  | IN                   | prep                
    success              | NOUN                 | NN                   | pobj                
    when                 | ADV                  | WRB                  | advmod              
    they                 | PRON                 | PRP                  | nsubj               
    gave                 | VERB                 | VBD                  | advcl               
    up                   | PART                 | RP                   | prt                 
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="901ec1a661494e7db3e59c254cfd3d41-0" class="displacy" width="4075" height="662.0" direction="ltr" style="max-width: none; height: 662.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Many</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="225">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="400">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="575">'s</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="750">failures</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="925">are</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">experienced</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">by</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">people</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">who</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">did</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">realize</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">how</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">close</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">they</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">were</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">success</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3375">when</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3550">they</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3725">gave</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3725">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3900">up.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3900">PART</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-0" stroke-width="2px" d="M70,527.0 C70,2.0 1100.0,2.0 1100.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubjpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,529.0 L62,517.0 78,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-1" stroke-width="2px" d="M70,527.0 C70,439.5 200.0,439.5 200.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M200.0,529.0 L208.0,517.0 192.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-2" stroke-width="2px" d="M420,527.0 C420,352.0 730.0,352.0 730.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,529.0 L412,517.0 428,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-3" stroke-width="2px" d="M420,527.0 C420,439.5 550.0,439.5 550.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">case</textPath>
    </text>
    <path class="displacy-arrowhead" d="M550.0,529.0 L558.0,517.0 542.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-4" stroke-width="2px" d="M245,527.0 C245,264.5 735.0,264.5 735.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M735.0,529.0 L743.0,517.0 727.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-5" stroke-width="2px" d="M945,527.0 C945,439.5 1075.0,439.5 1075.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">auxpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,529.0 L937,517.0 953,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-6" stroke-width="2px" d="M1120,527.0 C1120,439.5 1250.0,439.5 1250.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">agent</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1250.0,529.0 L1258.0,517.0 1242.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-7" stroke-width="2px" d="M1295,527.0 C1295,439.5 1425.0,439.5 1425.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1425.0,529.0 L1433.0,517.0 1417.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-8" stroke-width="2px" d="M1645,527.0 C1645,264.5 2135.0,264.5 2135.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,529.0 L1637,517.0 1653,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-9" stroke-width="2px" d="M1820,527.0 C1820,352.0 2130.0,352.0 2130.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,529.0 L1812,517.0 1828,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-10" stroke-width="2px" d="M1995,527.0 C1995,439.5 2125.0,439.5 2125.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,529.0 L1987,517.0 2003,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-11" stroke-width="2px" d="M1470,527.0 C1470,177.0 2140.0,177.0 2140.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2140.0,529.0 L2148.0,517.0 2132.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-12" stroke-width="2px" d="M2345,527.0 C2345,439.5 2475.0,439.5 2475.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,529.0 L2337,517.0 2353,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-13" stroke-width="2px" d="M2520,527.0 C2520,352.0 2830.0,352.0 2830.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2520,529.0 L2512,517.0 2528,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-14" stroke-width="2px" d="M2695,527.0 C2695,439.5 2825.0,439.5 2825.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,529.0 L2687,517.0 2703,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-15" stroke-width="2px" d="M2170,527.0 C2170,177.0 2840.0,177.0 2840.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2840.0,529.0 L2848.0,517.0 2832.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-16" stroke-width="2px" d="M2870,527.0 C2870,439.5 3000.0,439.5 3000.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3000.0,529.0 L3008.0,517.0 2992.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-17" stroke-width="2px" d="M3045,527.0 C3045,439.5 3175.0,439.5 3175.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3175.0,529.0 L3183.0,517.0 3167.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-18" stroke-width="2px" d="M3395,527.0 C3395,352.0 3705.0,352.0 3705.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3395,529.0 L3387,517.0 3403,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-19" stroke-width="2px" d="M3570,527.0 C3570,439.5 3700.0,439.5 3700.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3570,529.0 L3562,517.0 3578,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-20" stroke-width="2px" d="M2870,527.0 C2870,89.5 3720.0,89.5 3720.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-20" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3720.0,529.0 L3728.0,517.0 3712.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-901ec1a661494e7db3e59c254cfd3d41-0-21" stroke-width="2px" d="M3745,527.0 C3745,439.5 3875.0,439.5 3875.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-901ec1a661494e7db3e59c254cfd3d41-0-21" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prt</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3875.0,529.0 L3883.0,517.0 3867.0,517.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Our lives begin to end the day we become silent about things that matter.
    Our                  | DET                  | PRP$                 | poss                
    lives                | NOUN                 | NNS                  | nsubj               
    begin                | VERB                 | VBP                  | ROOT                
    to                   | PART                 | TO                   | aux                 
    end                  | VERB                 | VB                   | xcomp               
    the                  | DET                  | DT                   | det                 
    day                  | NOUN                 | NN                   | npadvmod            
    we                   | PRON                 | PRP                  | nsubj               
    become               | VERB                 | VBP                  | relcl               
    silent               | ADJ                  | JJ                   | acomp               
    about                | ADP                  | IN                   | prep                
    things               | NOUN                 | NNS                  | pobj                
    that                 | DET                  | WDT                  | nsubj               
    matter               | NOUN                 | NN                   | relcl               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="29051d41e8854932af641a6eed75156b-0" class="displacy" width="2500" height="312.0" direction="ltr" style="max-width: none; height: 312.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Our</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="225">lives</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="400">begin</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="575">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="750">end</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="925">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">day</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">become</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">silent</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">about</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">things</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">matter.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-0" stroke-width="2px" d="M70,177.0 C70,89.5 220.0,89.5 220.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,179.0 L62,167.0 78,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-1" stroke-width="2px" d="M245,177.0 C245,89.5 395.0,89.5 395.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,179.0 L237,167.0 253,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-2" stroke-width="2px" d="M595,177.0 C595,89.5 745.0,89.5 745.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,179.0 L587,167.0 603,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-3" stroke-width="2px" d="M420,177.0 C420,2.0 750.0,2.0 750.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M750.0,179.0 L758.0,167.0 742.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-4" stroke-width="2px" d="M945,177.0 C945,89.5 1095.0,89.5 1095.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,179.0 L937,167.0 953,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-5" stroke-width="2px" d="M770,177.0 C770,2.0 1100.0,2.0 1100.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">npadvmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1100.0,179.0 L1108.0,167.0 1092.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-6" stroke-width="2px" d="M1295,177.0 C1295,89.5 1445.0,89.5 1445.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,179.0 L1287,167.0 1303,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-7" stroke-width="2px" d="M1120,177.0 C1120,2.0 1450.0,2.0 1450.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1450.0,179.0 L1458.0,167.0 1442.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-8" stroke-width="2px" d="M1470,177.0 C1470,89.5 1620.0,89.5 1620.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1620.0,179.0 L1628.0,167.0 1612.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-9" stroke-width="2px" d="M1645,177.0 C1645,89.5 1795.0,89.5 1795.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1795.0,179.0 L1803.0,167.0 1787.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-10" stroke-width="2px" d="M1820,177.0 C1820,89.5 1970.0,89.5 1970.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1970.0,179.0 L1978.0,167.0 1962.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-11" stroke-width="2px" d="M2170,177.0 C2170,89.5 2320.0,89.5 2320.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,179.0 L2162,167.0 2178,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-29051d41e8854932af641a6eed75156b-0-12" stroke-width="2px" d="M1995,177.0 C1995,2.0 2325.0,2.0 2325.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-29051d41e8854932af641a6eed75156b-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2325.0,179.0 L2333.0,167.0 2317.0,167.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is about making an impact, not making an income. 
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    about                | ADP                  | IN                   | prep                
    making               | VERB                 | VBG                  | pcomp               
    an                   | DET                  | DT                   | det                 
    impact               | NOUN                 | NN                   | dobj                
    ,                    | PUNCT                | ,                    | punct               
    not                  | ADV                  | RB                   | neg                 
    making               | VERB                 | VBG                  | dep                 
    an                   | DET                  | DT                   | det                 
    income               | NOUN                 | NN                   | dobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="5da71b93d81848b8b0e11d586d475b10-0" class="displacy" width="1800" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">about</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">making</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">an</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">impact,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">making</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">an</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">income.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-5da71b93d81848b8b0e11d586d475b10-0-0" stroke-width="2px" d="M70,264.5 C70,177.0 215.0,177.0 215.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-5da71b93d81848b8b0e11d586d475b10-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-5da71b93d81848b8b0e11d586d475b10-0-1" stroke-width="2px" d="M245,264.5 C245,177.0 390.0,177.0 390.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-5da71b93d81848b8b0e11d586d475b10-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M390.0,266.5 L398.0,254.5 382.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-5da71b93d81848b8b0e11d586d475b10-0-2" stroke-width="2px" d="M420,264.5 C420,177.0 565.0,177.0 565.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-5da71b93d81848b8b0e11d586d475b10-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M565.0,266.5 L573.0,254.5 557.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-5da71b93d81848b8b0e11d586d475b10-0-3" stroke-width="2px" d="M770,264.5 C770,177.0 915.0,177.0 915.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-5da71b93d81848b8b0e11d586d475b10-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,266.5 L762,254.5 778,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-5da71b93d81848b8b0e11d586d475b10-0-4" stroke-width="2px" d="M595,264.5 C595,89.5 920.0,89.5 920.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-5da71b93d81848b8b0e11d586d475b10-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M920.0,266.5 L928.0,254.5 912.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-5da71b93d81848b8b0e11d586d475b10-0-5" stroke-width="2px" d="M1120,264.5 C1120,177.0 1265.0,177.0 1265.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-5da71b93d81848b8b0e11d586d475b10-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,266.5 L1112,254.5 1128,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-5da71b93d81848b8b0e11d586d475b10-0-6" stroke-width="2px" d="M595,264.5 C595,2.0 1275.0,2.0 1275.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-5da71b93d81848b8b0e11d586d475b10-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1275.0,266.5 L1283.0,254.5 1267.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-5da71b93d81848b8b0e11d586d475b10-0-7" stroke-width="2px" d="M1470,264.5 C1470,177.0 1615.0,177.0 1615.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-5da71b93d81848b8b0e11d586d475b10-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1470,266.5 L1462,254.5 1478,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-5da71b93d81848b8b0e11d586d475b10-0-8" stroke-width="2px" d="M1295,264.5 C1295,89.5 1620.0,89.5 1620.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-5da71b93d81848b8b0e11d586d475b10-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1620.0,266.5 L1628.0,254.5 1612.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  An unexamined life is not worth living.
    An                   | DET                  | DT                   | det                 
    unexamined           | ADJ                  | JJ                   | amod                
    life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    not                  | ADV                  | RB                   | neg                 
    worth                | ADJ                  | JJ                   | acomp               
    living               | VERB                 | VBG                  | xcomp               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="763fb59832f842d79688af41b43c08fb-0" class="displacy" width="1275" height="312.0" direction="ltr" style="max-width: none; height: 312.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="50">An</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="225">unexamined</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="400">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="575">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="750">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="925">worth</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">living.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-763fb59832f842d79688af41b43c08fb-0-0" stroke-width="2px" d="M70,177.0 C70,2.0 400.0,2.0 400.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-763fb59832f842d79688af41b43c08fb-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,179.0 L62,167.0 78,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-763fb59832f842d79688af41b43c08fb-0-1" stroke-width="2px" d="M245,177.0 C245,89.5 395.0,89.5 395.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-763fb59832f842d79688af41b43c08fb-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,179.0 L237,167.0 253,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-763fb59832f842d79688af41b43c08fb-0-2" stroke-width="2px" d="M420,177.0 C420,89.5 570.0,89.5 570.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-763fb59832f842d79688af41b43c08fb-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,179.0 L412,167.0 428,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-763fb59832f842d79688af41b43c08fb-0-3" stroke-width="2px" d="M595,177.0 C595,89.5 745.0,89.5 745.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-763fb59832f842d79688af41b43c08fb-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M745.0,179.0 L753.0,167.0 737.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-763fb59832f842d79688af41b43c08fb-0-4" stroke-width="2px" d="M595,177.0 C595,2.0 925.0,2.0 925.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-763fb59832f842d79688af41b43c08fb-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M925.0,179.0 L933.0,167.0 917.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-763fb59832f842d79688af41b43c08fb-0-5" stroke-width="2px" d="M945,177.0 C945,89.5 1095.0,89.5 1095.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-763fb59832f842d79688af41b43c08fb-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1095.0,179.0 L1103.0,167.0 1087.0,167.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Your time is limited, so don't waste it living someone else's life.
    Your                 | DET                  | PRP$                 | poss                
    time                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ccomp               
    limited              | ADJ                  | JJ                   | acomp               
    ,                    | PUNCT                | ,                    | punct               
    so                   | ADV                  | RB                   | advmod              
    do                   | VERB                 | VB                   | aux                 
    n't                  | ADV                  | RB                   | neg                 
    waste                | VERB                 | VB                   | ROOT                
    it                   | PRON                 | PRP                  | dobj                
    living               | VERB                 | VBG                  | xcomp               
    someone              | NOUN                 | NN                   | poss                
    else                 | ADV                  | RB                   | advmod              
    's                   | PART                 | POS                  | case                
    life                 | NOUN                 | NN                   | dobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="63c5c3ea1a204af8b9b52fd6d2afd684-0" class="displacy" width="2500" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Your</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">time</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">limited,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">so</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">do</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">n't</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">waste</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">living</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">someone</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">else</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">'s</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">life.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-0" stroke-width="2px" d="M70,439.5 C70,352.0 205.0,352.0 205.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-1" stroke-width="2px" d="M245,439.5 C245,352.0 380.0,352.0 380.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,441.5 L237,429.5 253,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-2" stroke-width="2px" d="M420,439.5 C420,2.0 1275.0,2.0 1275.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,441.5 L412,429.5 428,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-3" stroke-width="2px" d="M420,439.5 C420,352.0 555.0,352.0 555.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M555.0,441.5 L563.0,429.5 547.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-4" stroke-width="2px" d="M770,439.5 C770,177.0 1265.0,177.0 1265.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,441.5 L762,429.5 778,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-5" stroke-width="2px" d="M945,439.5 C945,264.5 1260.0,264.5 1260.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,441.5 L937,429.5 953,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-6" stroke-width="2px" d="M1120,439.5 C1120,352.0 1255.0,352.0 1255.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,441.5 L1112,429.5 1128,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-7" stroke-width="2px" d="M1295,439.5 C1295,352.0 1430.0,352.0 1430.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1430.0,441.5 L1438.0,429.5 1422.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-8" stroke-width="2px" d="M1295,439.5 C1295,264.5 1610.0,264.5 1610.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1610.0,441.5 L1618.0,429.5 1602.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-9" stroke-width="2px" d="M1820,439.5 C1820,177.0 2315.0,177.0 2315.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,441.5 L1812,429.5 1828,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-10" stroke-width="2px" d="M1820,439.5 C1820,352.0 1955.0,352.0 1955.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1955.0,441.5 L1963.0,429.5 1947.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-11" stroke-width="2px" d="M1995,439.5 C1995,352.0 2130.0,352.0 2130.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">case</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2130.0,441.5 L2138.0,429.5 2122.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-12" stroke-width="2px" d="M1645,439.5 C1645,89.5 2320.0,89.5 2320.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-63c5c3ea1a204af8b9b52fd6d2afd684-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2320.0,441.5 L2328.0,429.5 2312.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  The two most important days in your life are the day you are born and the day you find out why.
    The                  | DET                  | DT                   | det                 
    two                  | NUM                  | CD                   | nummod              
    most                 | ADV                  | RBS                  | advmod              
    important            | ADJ                  | JJ                   | amod                
    days                 | NOUN                 | NNS                  | nsubj               
    in                   | ADP                  | IN                   | prep                
    your                 | DET                  | PRP$                 | poss                
    life                 | NOUN                 | NN                   | pobj                
    are                  | VERB                 | VBP                  | ROOT                
    the                  | DET                  | DT                   | det                 
    day                  | NOUN                 | NN                   | attr                
    you                  | PRON                 | PRP                  | nsubjpass           
    are                  | VERB                 | VBP                  | auxpass             
    born                 | VERB                 | VBN                  | relcl               
    and                  | CCONJ                | CC                   | cc                  
    the                  | DET                  | DT                   | det                 
    day                  | NOUN                 | NN                   | conj                
    you                  | PRON                 | PRP                  | nsubj               
    find                 | VERB                 | VBP                  | relcl               
    out                  | PART                 | RP                   | prt                 
    why                  | ADV                  | WRB                  | ccomp               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="6e9f6eefd5954603854abe078b3ecac2-0" class="displacy" width="3725" height="487.0" direction="ltr" style="max-width: none; height: 487.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="50">The</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="225">two</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="400">most</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="575">important</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="750">days</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="925">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">your</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">are</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">day</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">are</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">born</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">day</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">find</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3375">out</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3550">why.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">ADV</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-0" stroke-width="2px" d="M70,352.0 C70,2.0 750.0,2.0 750.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,354.0 L62,342.0 78,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-1" stroke-width="2px" d="M245,352.0 C245,89.5 745.0,89.5 745.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nummod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,354.0 L237,342.0 253,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-2" stroke-width="2px" d="M420,352.0 C420,264.5 560.0,264.5 560.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,354.0 L412,342.0 428,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-3" stroke-width="2px" d="M595,352.0 C595,264.5 735.0,264.5 735.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,354.0 L587,342.0 603,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-4" stroke-width="2px" d="M770,352.0 C770,2.0 1450.0,2.0 1450.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,354.0 L762,342.0 778,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-5" stroke-width="2px" d="M770,352.0 C770,264.5 910.0,264.5 910.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M910.0,354.0 L918.0,342.0 902.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-6" stroke-width="2px" d="M1120,352.0 C1120,264.5 1260.0,264.5 1260.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,354.0 L1112,342.0 1128,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-7" stroke-width="2px" d="M945,352.0 C945,177.0 1265.0,177.0 1265.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1265.0,354.0 L1273.0,342.0 1257.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-8" stroke-width="2px" d="M1645,352.0 C1645,264.5 1785.0,264.5 1785.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,354.0 L1637,342.0 1653,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-9" stroke-width="2px" d="M1470,352.0 C1470,177.0 1790.0,177.0 1790.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1790.0,354.0 L1798.0,342.0 1782.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-10" stroke-width="2px" d="M1995,352.0 C1995,177.0 2315.0,177.0 2315.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubjpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,354.0 L1987,342.0 2003,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-11" stroke-width="2px" d="M2170,352.0 C2170,264.5 2310.0,264.5 2310.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">auxpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,354.0 L2162,342.0 2178,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-12" stroke-width="2px" d="M1820,352.0 C1820,89.5 2320.0,89.5 2320.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2320.0,354.0 L2328.0,342.0 2312.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-13" stroke-width="2px" d="M2345,352.0 C2345,264.5 2485.0,264.5 2485.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2485.0,354.0 L2493.0,342.0 2477.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-14" stroke-width="2px" d="M2695,352.0 C2695,264.5 2835.0,264.5 2835.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,354.0 L2687,342.0 2703,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-15" stroke-width="2px" d="M2345,352.0 C2345,89.5 2845.0,89.5 2845.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2845.0,354.0 L2853.0,342.0 2837.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-16" stroke-width="2px" d="M3045,352.0 C3045,264.5 3185.0,264.5 3185.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3045,354.0 L3037,342.0 3053,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-17" stroke-width="2px" d="M2870,352.0 C2870,177.0 3190.0,177.0 3190.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3190.0,354.0 L3198.0,342.0 3182.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-18" stroke-width="2px" d="M3220,352.0 C3220,264.5 3360.0,264.5 3360.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prt</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3360.0,354.0 L3368.0,342.0 3352.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-6e9f6eefd5954603854abe078b3ecac2-0-19" stroke-width="2px" d="M3220,352.0 C3220,177.0 3540.0,177.0 3540.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-6e9f6eefd5954603854abe078b3ecac2-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3540.0,354.0 L3548.0,342.0 3532.0,342.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Accept responsibility for your life. Know that it is you who will get you where you want to go, no one else.
    Accept               | VERB                 | VB                   | compound            
    responsibility       | NOUN                 | NN                   | ROOT                
    for                  | ADP                  | IN                   | prep                
    your                 | DET                  | PRP$                 | poss                
    life                 | NOUN                 | NN                   | pobj                
    .                    | PUNCT                | .                    | punct               
    Know                 | VERB                 | VB                   | ROOT                
    that                 | ADP                  | IN                   | mark                
    it                   | PRON                 | PRP                  | nsubj               
    is                   | VERB                 | VBZ                  | ccomp               
    you                  | PRON                 | PRP                  | attr                
    who                  | PRON                 | WP                   | nsubj               
    will                 | VERB                 | MD                   | aux                 
    get                  | VERB                 | VB                   | ccomp               
    you                  | PRON                 | PRP                  | dobj                
    where                | ADV                  | WRB                  | advmod              
    you                  | PRON                 | PRP                  | nsubj               
    want                 | VERB                 | VBP                  | advcl               
    to                   | PART                 | TO                   | aux                 
    go                   | VERB                 | VB                   | xcomp               
    ,                    | PUNCT                | ,                    | punct               
    no                   | DET                  | DT                   | det                 
    one                  | NOUN                 | NN                   | npadvmod            
    else                 | ADV                  | RB                   | advmod              
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="4a249f4a8f834f42a3a79001859e239c-0" class="displacy" width="3900" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Accept</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">responsibility</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">for</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">your</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">life.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">Know</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">who</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">will</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">get</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">where</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2675">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2850">want</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3025">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3200">go,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3375">no</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3550">one</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3725">else.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3725">ADV</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-0" stroke-width="2px" d="M70,439.5 C70,352.0 205.0,352.0 205.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">compound</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-1" stroke-width="2px" d="M245,439.5 C245,352.0 380.0,352.0 380.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M380.0,441.5 L388.0,429.5 372.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-2" stroke-width="2px" d="M595,439.5 C595,352.0 730.0,352.0 730.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,441.5 L587,429.5 603,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-3" stroke-width="2px" d="M420,439.5 C420,264.5 735.0,264.5 735.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M735.0,441.5 L743.0,429.5 727.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-4" stroke-width="2px" d="M1120,439.5 C1120,264.5 1435.0,264.5 1435.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,441.5 L1112,429.5 1128,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-5" stroke-width="2px" d="M1295,439.5 C1295,352.0 1430.0,352.0 1430.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,441.5 L1287,429.5 1303,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-6" stroke-width="2px" d="M945,439.5 C945,177.0 1440.0,177.0 1440.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1440.0,441.5 L1448.0,429.5 1432.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-7" stroke-width="2px" d="M1470,439.5 C1470,352.0 1605.0,352.0 1605.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1605.0,441.5 L1613.0,429.5 1597.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-8" stroke-width="2px" d="M1820,439.5 C1820,264.5 2135.0,264.5 2135.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,441.5 L1812,429.5 1828,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-9" stroke-width="2px" d="M1995,439.5 C1995,352.0 2130.0,352.0 2130.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,441.5 L1987,429.5 2003,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-10" stroke-width="2px" d="M1470,439.5 C1470,89.5 2145.0,89.5 2145.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2145.0,441.5 L2153.0,429.5 2137.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-11" stroke-width="2px" d="M2170,439.5 C2170,352.0 2305.0,352.0 2305.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2305.0,441.5 L2313.0,429.5 2297.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-12" stroke-width="2px" d="M2520,439.5 C2520,89.5 3195.0,89.5 3195.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2520,441.5 L2512,429.5 2528,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-13" stroke-width="2px" d="M2695,439.5 C2695,352.0 2830.0,352.0 2830.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,441.5 L2687,429.5 2703,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-14" stroke-width="2px" d="M2170,439.5 C2170,89.5 2845.0,89.5 2845.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2845.0,441.5 L2853.0,429.5 2837.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-15" stroke-width="2px" d="M3045,439.5 C3045,352.0 3180.0,352.0 3180.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3045,441.5 L3037,429.5 3053,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-16" stroke-width="2px" d="M2870,439.5 C2870,264.5 3185.0,264.5 3185.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3185.0,441.5 L3193.0,429.5 3177.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-17" stroke-width="2px" d="M3395,439.5 C3395,352.0 3530.0,352.0 3530.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3395,441.5 L3387,429.5 3403,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-18" stroke-width="2px" d="M945,439.5 C945,2.0 3550.0,2.0 3550.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">npadvmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3550.0,441.5 L3558.0,429.5 3542.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a249f4a8f834f42a3a79001859e239c-0-19" stroke-width="2px" d="M3570,439.5 C3570,352.0 3705.0,352.0 3705.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a249f4a8f834f42a3a79001859e239c-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3705.0,441.5 L3713.0,429.5 3697.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  The great pleasure in life is doing what people say you cannot do.  
    The                  | DET                  | DT                   | det                 
    great                | ADJ                  | JJ                   | amod                
    pleasure             | NOUN                 | NN                   | nsubj               
    in                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    is                   | VERB                 | VBZ                  | aux                 
    doing                | VERB                 | VBG                  | ROOT                
    what                 | PRON                 | WP                   | dobj                
    people               | NOUN                 | NNS                  | nsubj               
    say                  | VERB                 | VBP                  | ccomp               
    you                  | PRON                 | PRP                  | nsubj               
    can                  | AUX                  | MD                   | aux                 
    not                  | ADV                  | RB                   | neg                 
    do                   | VERB                 | VB                   | ccomp               
    .                    | PUNCT                | .                    | punct               
                         | SPACE                | _SP                  |                     



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="e703a3b2ce3a40f8ac3235d647f837c9-0" class="displacy" width="2675" height="662.0" direction="ltr" style="max-width: none; height: 662.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="50">The</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="225">great</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="400">pleasure</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="575">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="750">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="925">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">doing</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">what</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">people</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">say</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">can</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">do.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2500"> </tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">SPACE</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-0" stroke-width="2px" d="M70,527.0 C70,352.0 380.0,352.0 380.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,529.0 L62,517.0 78,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-1" stroke-width="2px" d="M245,527.0 C245,439.5 375.0,439.5 375.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,529.0 L237,517.0 253,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-2" stroke-width="2px" d="M420,527.0 C420,177.0 1090.0,177.0 1090.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,529.0 L412,517.0 428,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-3" stroke-width="2px" d="M420,527.0 C420,439.5 550.0,439.5 550.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M550.0,529.0 L558.0,517.0 542.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-4" stroke-width="2px" d="M595,527.0 C595,439.5 725.0,439.5 725.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M725.0,529.0 L733.0,517.0 717.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-5" stroke-width="2px" d="M945,527.0 C945,439.5 1075.0,439.5 1075.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,529.0 L937,517.0 953,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-6" stroke-width="2px" d="M1295,527.0 C1295,89.5 2320.0,89.5 2320.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,529.0 L1287,517.0 1303,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-7" stroke-width="2px" d="M1470,527.0 C1470,439.5 1600.0,439.5 1600.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1470,529.0 L1462,517.0 1478,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-8" stroke-width="2px" d="M1120,527.0 C1120,264.5 1610.0,264.5 1610.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1610.0,529.0 L1618.0,517.0 1602.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-9" stroke-width="2px" d="M1820,527.0 C1820,264.5 2310.0,264.5 2310.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,529.0 L1812,517.0 1828,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-10" stroke-width="2px" d="M1995,527.0 C1995,352.0 2305.0,352.0 2305.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,529.0 L1987,517.0 2003,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-11" stroke-width="2px" d="M2170,527.0 C2170,439.5 2300.0,439.5 2300.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,529.0 L2162,517.0 2178,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-12" stroke-width="2px" d="M1120,527.0 C1120,2.0 2325.0,2.0 2325.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">punct</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2325.0,529.0 L2333.0,517.0 2317.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-13" stroke-width="2px" d="M2345,527.0 C2345,439.5 2475.0,439.5 2475.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-e703a3b2ce3a40f8ac3235d647f837c9-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle"></textPath>
    </text>
    <path class="displacy-arrowhead" d="M2475.0,529.0 L2483.0,517.0 2467.0,517.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Keep your eyes on the stars and your feet on the ground.
    Keep                 | VERB                 | VB                   | ROOT                
    your                 | DET                  | PRP$                 | poss                
    eyes                 | NOUN                 | NNS                  | dobj                
    on                   | ADP                  | IN                   | prep                
    the                  | DET                  | DT                   | det                 
    stars                | NOUN                 | NNS                  | pobj                
    and                  | CCONJ                | CC                   | cc                  
    your                 | DET                  | PRP$                 | poss                
    feet                 | NOUN                 | NNS                  | conj                
    on                   | ADP                  | IN                   | prep                
    the                  | DET                  | DT                   | det                 
    ground               | NOUN                 | NN                   | pobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="582fdd5e71124202a74df112d90e94a7-0" class="displacy" width="2150" height="487.0" direction="ltr" style="max-width: none; height: 487.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Keep</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="225">your</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="400">eyes</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="575">on</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="750">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="925">stars</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">your</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">feet</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">on</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">ground.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-0" stroke-width="2px" d="M245,352.0 C245,264.5 385.0,264.5 385.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,354.0 L237,342.0 253,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-1" stroke-width="2px" d="M70,352.0 C70,177.0 390.0,177.0 390.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M390.0,354.0 L398.0,342.0 382.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-2" stroke-width="2px" d="M70,352.0 C70,89.5 570.0,89.5 570.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M570.0,354.0 L578.0,342.0 562.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-3" stroke-width="2px" d="M770,352.0 C770,264.5 910.0,264.5 910.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,354.0 L762,342.0 778,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-4" stroke-width="2px" d="M595,352.0 C595,177.0 915.0,177.0 915.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M915.0,354.0 L923.0,342.0 907.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-5" stroke-width="2px" d="M945,352.0 C945,264.5 1085.0,264.5 1085.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1085.0,354.0 L1093.0,342.0 1077.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-6" stroke-width="2px" d="M1295,352.0 C1295,264.5 1435.0,264.5 1435.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,354.0 L1287,342.0 1303,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-7" stroke-width="2px" d="M945,352.0 C945,89.5 1445.0,89.5 1445.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1445.0,354.0 L1453.0,342.0 1437.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-8" stroke-width="2px" d="M945,352.0 C945,2.0 1625.0,2.0 1625.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1625.0,354.0 L1633.0,342.0 1617.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-9" stroke-width="2px" d="M1820,352.0 C1820,264.5 1960.0,264.5 1960.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,354.0 L1812,342.0 1828,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-582fdd5e71124202a74df112d90e94a7-0-10" stroke-width="2px" d="M1645,352.0 C1645,177.0 1965.0,177.0 1965.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-582fdd5e71124202a74df112d90e94a7-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1965.0,354.0 L1973.0,342.0 1957.0,342.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life's too mysterious to take too serious.
    Life                 | NOUN                 | NN                   | nsubj               
    's                   | VERB                 | VBZ                  | ROOT                
    too                  | ADV                  | RB                   | advmod              
    mysterious           | ADJ                  | JJ                   | acomp               
    to                   | PART                 | TO                   | aux                 
    take                 | VERB                 | VB                   | xcomp               
    too                  | ADV                  | RB                   | advmod              
    serious              | ADJ                  | JJ                   | oprd                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="13e7845db1864c228a73f37c9c435066-0" class="displacy" width="1450" height="312.0" direction="ltr" style="max-width: none; height: 312.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="225">'s</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="400">too</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="575">mysterious</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="750">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="925">take</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">too</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="222.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">serious.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">ADJ</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-13e7845db1864c228a73f37c9c435066-0-0" stroke-width="2px" d="M70,177.0 C70,89.5 220.0,89.5 220.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-13e7845db1864c228a73f37c9c435066-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,179.0 L62,167.0 78,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-13e7845db1864c228a73f37c9c435066-0-1" stroke-width="2px" d="M420,177.0 C420,89.5 570.0,89.5 570.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-13e7845db1864c228a73f37c9c435066-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,179.0 L412,167.0 428,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-13e7845db1864c228a73f37c9c435066-0-2" stroke-width="2px" d="M245,177.0 C245,2.0 575.0,2.0 575.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-13e7845db1864c228a73f37c9c435066-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M575.0,179.0 L583.0,167.0 567.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-13e7845db1864c228a73f37c9c435066-0-3" stroke-width="2px" d="M770,177.0 C770,89.5 920.0,89.5 920.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-13e7845db1864c228a73f37c9c435066-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,179.0 L762,167.0 778,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-13e7845db1864c228a73f37c9c435066-0-4" stroke-width="2px" d="M595,177.0 C595,2.0 925.0,2.0 925.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-13e7845db1864c228a73f37c9c435066-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M925.0,179.0 L933.0,167.0 917.0,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-13e7845db1864c228a73f37c9c435066-0-5" stroke-width="2px" d="M1120,177.0 C1120,89.5 1270.0,89.5 1270.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-13e7845db1864c228a73f37c9c435066-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,179.0 L1112,167.0 1128,167.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-13e7845db1864c228a73f37c9c435066-0-6" stroke-width="2px" d="M945,177.0 C945,2.0 1275.0,2.0 1275.0,177.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-13e7845db1864c228a73f37c9c435066-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">oprd</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1275.0,179.0 L1283.0,167.0 1267.0,167.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  It's not about how hard you can hit; it's about how hard you can get hit and keep moving forward.
    It                   | PRON                 | PRP                  | nsubj               
    's                   | VERB                 | VBZ                  | ccomp               
    not                  | ADV                  | RB                   | neg                 
    about                | ADP                  | IN                   | prep                
    how                  | ADV                  | WRB                  | advmod              
    hard                 | ADJ                  | JJ                   | advmod              
    you                  | PRON                 | PRP                  | nsubj               
    can                  | VERB                 | MD                   | aux                 
    hit                  | VERB                 | VB                   | pcomp               
    ;                    | PUNCT                | :                    | punct               
    it                   | PRON                 | PRP                  | nsubj               
    's                   | VERB                 | VBZ                  | ROOT                
    about                | ADP                  | IN                   | prep                
    how                  | ADV                  | WRB                  | advmod              
    hard                 | ADJ                  | JJ                   | advmod              
    you                  | PRON                 | PRP                  | nsubjpass           
    can                  | VERB                 | MD                   | aux                 
    get                  | VERB                 | VB                   | auxpass             
    hit                  | VERB                 | VB                   | pcomp               
    and                  | CCONJ                | CC                   | cc                  
    keep                 | VERB                 | VB                   | conj                
    moving               | VERB                 | VBG                  | xcomp               
    forward              | ADV                  | RB                   | advmod              
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="2d5fcc81154043aab95638063438b231-0" class="displacy" width="3900" height="662.0" direction="ltr" style="max-width: none; height: 662.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="50">It</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="225">'s</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="400">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="575">about</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="750">how</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="925">hard</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">can</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">hit;</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">'s</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">about</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">how</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">hard</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">can</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">get</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">hit</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3375">keep</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3550">moving</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3725">forward.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3725">ADV</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-0" stroke-width="2px" d="M70,527.0 C70,439.5 200.0,439.5 200.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,529.0 L62,517.0 78,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-1" stroke-width="2px" d="M245,527.0 C245,2.0 1800.0,2.0 1800.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,529.0 L237,517.0 253,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-2" stroke-width="2px" d="M245,527.0 C245,439.5 375.0,439.5 375.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M375.0,529.0 L383.0,517.0 367.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-3" stroke-width="2px" d="M245,527.0 C245,352.0 555.0,352.0 555.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M555.0,529.0 L563.0,517.0 547.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-4" stroke-width="2px" d="M770,527.0 C770,439.5 900.0,439.5 900.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,529.0 L762,517.0 778,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-5" stroke-width="2px" d="M945,527.0 C945,264.5 1435.0,264.5 1435.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,529.0 L937,517.0 953,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-6" stroke-width="2px" d="M1120,527.0 C1120,352.0 1430.0,352.0 1430.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,529.0 L1112,517.0 1128,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-7" stroke-width="2px" d="M1295,527.0 C1295,439.5 1425.0,439.5 1425.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,529.0 L1287,517.0 1303,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-8" stroke-width="2px" d="M595,527.0 C595,177.0 1440.0,177.0 1440.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1440.0,529.0 L1448.0,517.0 1432.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-9" stroke-width="2px" d="M1645,527.0 C1645,439.5 1775.0,439.5 1775.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,529.0 L1637,517.0 1653,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-10" stroke-width="2px" d="M1820,527.0 C1820,439.5 1950.0,439.5 1950.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1950.0,529.0 L1958.0,517.0 1942.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-11" stroke-width="2px" d="M2170,527.0 C2170,439.5 2300.0,439.5 2300.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,529.0 L2162,517.0 2178,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-12" stroke-width="2px" d="M2345,527.0 C2345,89.5 3370.0,89.5 3370.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,529.0 L2337,517.0 2353,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-13" stroke-width="2px" d="M2520,527.0 C2520,264.5 3010.0,264.5 3010.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubjpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2520,529.0 L2512,517.0 2528,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-14" stroke-width="2px" d="M2695,527.0 C2695,352.0 3005.0,352.0 3005.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,529.0 L2687,517.0 2703,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-15" stroke-width="2px" d="M2870,527.0 C2870,439.5 3000.0,439.5 3000.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">auxpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2870,529.0 L2862,517.0 2878,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-16" stroke-width="2px" d="M1995,527.0 C1995,89.5 3020.0,89.5 3020.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3020.0,529.0 L3028.0,517.0 3012.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-17" stroke-width="2px" d="M3045,527.0 C3045,439.5 3175.0,439.5 3175.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3175.0,529.0 L3183.0,517.0 3167.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-18" stroke-width="2px" d="M3045,527.0 C3045,352.0 3355.0,352.0 3355.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3355.0,529.0 L3363.0,517.0 3347.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-19" stroke-width="2px" d="M3395,527.0 C3395,439.5 3525.0,439.5 3525.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3525.0,529.0 L3533.0,517.0 3517.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2d5fcc81154043aab95638063438b231-0-20" stroke-width="2px" d="M3570,527.0 C3570,439.5 3700.0,439.5 3700.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2d5fcc81154043aab95638063438b231-0-20" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3700.0,529.0 L3708.0,517.0 3692.0,517.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Nothing in life is to be feared; it is only to be understood. Now is the time to understand more so that we may fear less. 
    Nothing              | NOUN                 | NN                   | nsubj               
    in                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    is                   | VERB                 | VBZ                  | ccomp               
    to                   | PART                 | TO                   | aux                 
    be                   | VERB                 | VB                   | auxpass             
    feared               | VERB                 | VBN                  | xcomp               
    ;                    | PUNCT                | :                    | punct               
    it                   | PRON                 | PRP                  | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    only                 | ADV                  | RB                   | advmod              
    to                   | PART                 | TO                   | aux                 
    be                   | VERB                 | VB                   | auxpass             
    understood           | VERB                 | VBN                  | xcomp               
    .                    | PUNCT                | .                    | punct               
    Now                  | ADV                  | RB                   | advmod              
    is                   | VERB                 | VBZ                  | ROOT                
    the                  | DET                  | DT                   | det                 
    time                 | NOUN                 | NN                   | nsubj               
    to                   | PART                 | TO                   | aux                 
    understand           | VERB                 | VB                   | relcl               
    more                 | ADJ                  | JJR                  | dobj                
    so                   | ADP                  | IN                   | mark                
    that                 | ADP                  | IN                   | mark                
    we                   | PRON                 | PRP                  | nsubj               
    may                  | VERB                 | MD                   | aux                 
    fear                 | VERB                 | VB                   | advcl               
    less                 | ADJ                  | JJR                  | dobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="0e91ec78b0b54fb0a180d7593ba4775c-0" class="displacy" width="4600" height="662.0" direction="ltr" style="max-width: none; height: 662.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Nothing</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="225">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="400">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="575">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="750">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="925">be</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">feared;</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">only</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">be</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">understood.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">Now</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">time</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">understand</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3375">more</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3550">so</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3725">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3725">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3900">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3900">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="4075">may</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4075">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="4250">fear</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4250">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="4425">less.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4425">ADJ</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-0" stroke-width="2px" d="M70,527.0 C70,264.5 560.0,264.5 560.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,529.0 L62,517.0 78,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-1" stroke-width="2px" d="M70,527.0 C70,439.5 200.0,439.5 200.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M200.0,529.0 L208.0,517.0 192.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-2" stroke-width="2px" d="M245,527.0 C245,439.5 375.0,439.5 375.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M375.0,529.0 L383.0,517.0 367.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-3" stroke-width="2px" d="M595,527.0 C595,89.5 1445.0,89.5 1445.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,529.0 L587,517.0 603,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-4" stroke-width="2px" d="M770,527.0 C770,352.0 1080.0,352.0 1080.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,529.0 L762,517.0 778,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-5" stroke-width="2px" d="M945,527.0 C945,439.5 1075.0,439.5 1075.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">auxpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,529.0 L937,517.0 953,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-6" stroke-width="2px" d="M595,527.0 C595,264.5 1085.0,264.5 1085.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1085.0,529.0 L1093.0,517.0 1077.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-7" stroke-width="2px" d="M1295,527.0 C1295,439.5 1425.0,439.5 1425.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,529.0 L1287,517.0 1303,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-8" stroke-width="2px" d="M1645,527.0 C1645,264.5 2135.0,264.5 2135.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,529.0 L1637,517.0 1653,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-9" stroke-width="2px" d="M1820,527.0 C1820,352.0 2130.0,352.0 2130.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,529.0 L1812,517.0 1828,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-10" stroke-width="2px" d="M1995,527.0 C1995,439.5 2125.0,439.5 2125.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">auxpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,529.0 L1987,517.0 2003,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-11" stroke-width="2px" d="M1470,527.0 C1470,177.0 2140.0,177.0 2140.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2140.0,529.0 L2148.0,517.0 2132.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-12" stroke-width="2px" d="M2345,527.0 C2345,439.5 2475.0,439.5 2475.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,529.0 L2337,517.0 2353,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-13" stroke-width="2px" d="M2695,527.0 C2695,439.5 2825.0,439.5 2825.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,529.0 L2687,517.0 2703,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-14" stroke-width="2px" d="M2520,527.0 C2520,352.0 2830.0,352.0 2830.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2830.0,529.0 L2838.0,517.0 2822.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-15" stroke-width="2px" d="M3045,527.0 C3045,439.5 3175.0,439.5 3175.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3045,529.0 L3037,517.0 3053,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-16" stroke-width="2px" d="M2870,527.0 C2870,352.0 3180.0,352.0 3180.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3180.0,529.0 L3188.0,517.0 3172.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-17" stroke-width="2px" d="M3220,527.0 C3220,439.5 3350.0,439.5 3350.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3350.0,529.0 L3358.0,517.0 3342.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-18" stroke-width="2px" d="M3570,527.0 C3570,177.0 4240.0,177.0 4240.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3570,529.0 L3562,517.0 3578,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-19" stroke-width="2px" d="M3745,527.0 C3745,264.5 4235.0,264.5 4235.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3745,529.0 L3737,517.0 3753,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-20" stroke-width="2px" d="M3920,527.0 C3920,352.0 4230.0,352.0 4230.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-20" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3920,529.0 L3912,517.0 3928,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-21" stroke-width="2px" d="M4095,527.0 C4095,439.5 4225.0,439.5 4225.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-21" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4095,529.0 L4087,517.0 4103,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-22" stroke-width="2px" d="M3220,527.0 C3220,2.0 4250.0,2.0 4250.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-22" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4250.0,529.0 L4258.0,517.0 4242.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-23" stroke-width="2px" d="M4270,527.0 C4270,439.5 4400.0,439.5 4400.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-0e91ec78b0b54fb0a180d7593ba4775c-0-23" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4400.0,529.0 L4408.0,517.0 4392.0,517.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Do not wait to strike till the iron is hot; but make it hot by striking.
    Do                   | VERB                 | VB                   | aux                 
    not                  | ADV                  | RB                   | neg                 
    wait                 | VERB                 | VB                   | ROOT                
    to                   | PART                 | TO                   | aux                 
    strike               | VERB                 | VB                   | xcomp               
    till                 | ADP                  | IN                   | mark                
    the                  | DET                  | DT                   | det                 
    iron                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | advcl               
    hot                  | ADJ                  | JJ                   | acomp               
    ;                    | PUNCT                | :                    | punct               
    but                  | CCONJ                | CC                   | cc                  
    make                 | VERB                 | VB                   | conj                
    it                   | PRON                 | PRP                  | nsubj               
    hot                  | ADJ                  | JJ                   | ccomp               
    by                   | ADP                  | IN                   | prep                
    striking             | VERB                 | VBG                  | pcomp               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="2fbba6f86af84f3b996f52941e30027d-0" class="displacy" width="2850" height="662.0" direction="ltr" style="max-width: none; height: 662.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Do</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="225">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="400">wait</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="575">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="750">strike</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="925">till</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">iron</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">hot;</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">but</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">make</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">hot</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">by</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">striking.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">VERB</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-0" stroke-width="2px" d="M70,527.0 C70,352.0 380.0,352.0 380.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,529.0 L62,517.0 78,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-1" stroke-width="2px" d="M245,527.0 C245,439.5 375.0,439.5 375.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,529.0 L237,517.0 253,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-2" stroke-width="2px" d="M595,527.0 C595,439.5 725.0,439.5 725.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,529.0 L587,517.0 603,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-3" stroke-width="2px" d="M420,527.0 C420,352.0 730.0,352.0 730.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M730.0,529.0 L738.0,517.0 722.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-4" stroke-width="2px" d="M945,527.0 C945,264.5 1435.0,264.5 1435.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,529.0 L937,517.0 953,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-5" stroke-width="2px" d="M1120,527.0 C1120,439.5 1250.0,439.5 1250.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,529.0 L1112,517.0 1128,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-6" stroke-width="2px" d="M1295,527.0 C1295,439.5 1425.0,439.5 1425.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,529.0 L1287,517.0 1303,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-7" stroke-width="2px" d="M770,527.0 C770,177.0 1440.0,177.0 1440.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1440.0,529.0 L1448.0,517.0 1432.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-8" stroke-width="2px" d="M1470,527.0 C1470,439.5 1600.0,439.5 1600.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1600.0,529.0 L1608.0,517.0 1592.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-9" stroke-width="2px" d="M420,527.0 C420,89.5 1795.0,89.5 1795.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1795.0,529.0 L1803.0,517.0 1787.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-10" stroke-width="2px" d="M420,527.0 C420,2.0 1975.0,2.0 1975.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1975.0,529.0 L1983.0,517.0 1967.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-11" stroke-width="2px" d="M2170,527.0 C2170,439.5 2300.0,439.5 2300.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,529.0 L2162,517.0 2178,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-12" stroke-width="2px" d="M1995,527.0 C1995,352.0 2305.0,352.0 2305.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2305.0,529.0 L2313.0,517.0 2297.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-13" stroke-width="2px" d="M1995,527.0 C1995,264.5 2485.0,264.5 2485.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2485.0,529.0 L2493.0,517.0 2477.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2fbba6f86af84f3b996f52941e30027d-0-14" stroke-width="2px" d="M2520,527.0 C2520,439.5 2650.0,439.5 2650.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2fbba6f86af84f3b996f52941e30027d-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2650.0,529.0 L2658.0,517.0 2642.0,517.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Do not watch the clock. Do what it does. Keep going.
    Do                   | VERB                 | VB                   | aux                 
    not                  | ADV                  | RB                   | neg                 
    watch                | VERB                 | VB                   | ROOT                
    the                  | DET                  | DT                   | det                 
    clock                | NOUN                 | NN                   | dobj                
    .                    | PUNCT                | .                    | punct               
    Do                   | VERB                 | VB                   | ROOT                
    what                 | PRON                 | WP                   | dobj                
    it                   | PRON                 | PRP                  | nsubj               
    does                 | VERB                 | VBZ                  | ccomp               
    .                    | PUNCT                | .                    | punct               
    Keep                 | VERB                 | VB                   | ROOT                
    going                | VERB                 | VBG                  | xcomp               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="4a707da41c1343f18d3059004aee5af6-0" class="displacy" width="1975" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Do</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">watch</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">clock.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">Do</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">what</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">does.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">Keep</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">going.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a707da41c1343f18d3059004aee5af6-0-0" stroke-width="2px" d="M70,264.5 C70,89.5 395.0,89.5 395.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a707da41c1343f18d3059004aee5af6-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a707da41c1343f18d3059004aee5af6-0-1" stroke-width="2px" d="M245,264.5 C245,177.0 390.0,177.0 390.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a707da41c1343f18d3059004aee5af6-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,266.5 L237,254.5 253,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a707da41c1343f18d3059004aee5af6-0-2" stroke-width="2px" d="M595,264.5 C595,177.0 740.0,177.0 740.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a707da41c1343f18d3059004aee5af6-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,266.5 L587,254.5 603,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a707da41c1343f18d3059004aee5af6-0-3" stroke-width="2px" d="M420,264.5 C420,89.5 745.0,89.5 745.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a707da41c1343f18d3059004aee5af6-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M745.0,266.5 L753.0,254.5 737.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a707da41c1343f18d3059004aee5af6-0-4" stroke-width="2px" d="M1120,264.5 C1120,89.5 1445.0,89.5 1445.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a707da41c1343f18d3059004aee5af6-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,266.5 L1112,254.5 1128,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a707da41c1343f18d3059004aee5af6-0-5" stroke-width="2px" d="M1295,264.5 C1295,177.0 1440.0,177.0 1440.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a707da41c1343f18d3059004aee5af6-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,266.5 L1287,254.5 1303,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a707da41c1343f18d3059004aee5af6-0-6" stroke-width="2px" d="M945,264.5 C945,2.0 1450.0,2.0 1450.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a707da41c1343f18d3059004aee5af6-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1450.0,266.5 L1458.0,254.5 1442.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-4a707da41c1343f18d3059004aee5af6-0-7" stroke-width="2px" d="M1645,264.5 C1645,177.0 1790.0,177.0 1790.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-4a707da41c1343f18d3059004aee5af6-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1790.0,266.5 L1798.0,254.5 1782.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  In youth we learn, in age we understand.  
    In                   | ADP                  | IN                   | prep                
    youth                | NOUN                 | NN                   | pobj                
    we                   | PRON                 | PRP                  | nsubj               
    learn                | VERB                 | VBP                  | relcl               
    ,                    | PUNCT                | ,                    | punct               
    in                   | ADP                  | IN                   | prep                
    age                  | NOUN                 | NN                   | pobj                
    we                   | PRON                 | PRP                  | nsubj               
    understand           | VERB                 | VBP                  | ROOT                
    .                    | PUNCT                | .                    | punct               
                         | SPACE                | _SP                  |                     



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="f5a3c589af694a9f854c5831de815ed7-0" class="displacy" width="1625" height="487.0" direction="ltr" style="max-width: none; height: 487.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="50">In</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="225">youth</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="400">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="575">learn,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="750">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="925">age</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">understand.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1450"> </tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">SPACE</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-f5a3c589af694a9f854c5831de815ed7-0-0" stroke-width="2px" d="M70,352.0 C70,2.0 1275.0,2.0 1275.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-f5a3c589af694a9f854c5831de815ed7-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,354.0 L62,342.0 78,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-f5a3c589af694a9f854c5831de815ed7-0-1" stroke-width="2px" d="M70,352.0 C70,264.5 210.0,264.5 210.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-f5a3c589af694a9f854c5831de815ed7-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M210.0,354.0 L218.0,342.0 202.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-f5a3c589af694a9f854c5831de815ed7-0-2" stroke-width="2px" d="M420,352.0 C420,264.5 560.0,264.5 560.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-f5a3c589af694a9f854c5831de815ed7-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,354.0 L412,342.0 428,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-f5a3c589af694a9f854c5831de815ed7-0-3" stroke-width="2px" d="M245,352.0 C245,177.0 565.0,177.0 565.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-f5a3c589af694a9f854c5831de815ed7-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M565.0,354.0 L573.0,342.0 557.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-f5a3c589af694a9f854c5831de815ed7-0-4" stroke-width="2px" d="M770,352.0 C770,89.5 1270.0,89.5 1270.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-f5a3c589af694a9f854c5831de815ed7-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,354.0 L762,342.0 778,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-f5a3c589af694a9f854c5831de815ed7-0-5" stroke-width="2px" d="M770,352.0 C770,264.5 910.0,264.5 910.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-f5a3c589af694a9f854c5831de815ed7-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M910.0,354.0 L918.0,342.0 902.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-f5a3c589af694a9f854c5831de815ed7-0-6" stroke-width="2px" d="M1120,352.0 C1120,264.5 1260.0,264.5 1260.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-f5a3c589af694a9f854c5831de815ed7-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,354.0 L1112,342.0 1128,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-f5a3c589af694a9f854c5831de815ed7-0-7" stroke-width="2px" d="M1295,352.0 C1295,264.5 1435.0,264.5 1435.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-f5a3c589af694a9f854c5831de815ed7-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle"></textPath>
    </text>
    <path class="displacy-arrowhead" d="M1435.0,354.0 L1443.0,342.0 1427.0,342.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  The greatest use of life is to spend it for something that will outlast it.
    The                  | DET                  | DT                   | det                 
    greatest             | ADJ                  | JJS                  | amod                
    use                  | NOUN                 | NN                   | nsubj               
    of                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    is                   | VERB                 | VBZ                  | ROOT                
    to                   | PART                 | TO                   | aux                 
    spend                | VERB                 | VB                   | xcomp               
    it                   | PRON                 | PRP                  | dobj                
    for                  | ADP                  | IN                   | prep                
    something            | NOUN                 | NN                   | pobj                
    that                 | DET                  | WDT                  | nsubj               
    will                 | VERB                 | MD                   | aux                 
    outlast              | VERB                 | VB                   | relcl               
    it                   | PRON                 | PRP                  | dobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="2139b2528693490693c6901d49ce44be-0" class="displacy" width="2675" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">The</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">greatest</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">use</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">spend</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">for</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">something</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">will</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">outlast</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">it.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">PRON</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-0" stroke-width="2px" d="M70,264.5 C70,89.5 395.0,89.5 395.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-1" stroke-width="2px" d="M245,264.5 C245,177.0 390.0,177.0 390.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,266.5 L237,254.5 253,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-2" stroke-width="2px" d="M420,264.5 C420,2.0 925.0,2.0 925.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,266.5 L412,254.5 428,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-3" stroke-width="2px" d="M420,264.5 C420,177.0 565.0,177.0 565.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M565.0,266.5 L573.0,254.5 557.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-4" stroke-width="2px" d="M595,264.5 C595,177.0 740.0,177.0 740.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M740.0,266.5 L748.0,254.5 732.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-5" stroke-width="2px" d="M1120,264.5 C1120,177.0 1265.0,177.0 1265.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,266.5 L1112,254.5 1128,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-6" stroke-width="2px" d="M945,264.5 C945,89.5 1270.0,89.5 1270.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1270.0,266.5 L1278.0,254.5 1262.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-7" stroke-width="2px" d="M1295,264.5 C1295,177.0 1440.0,177.0 1440.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1440.0,266.5 L1448.0,254.5 1432.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-8" stroke-width="2px" d="M1295,264.5 C1295,89.5 1620.0,89.5 1620.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1620.0,266.5 L1628.0,254.5 1612.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-9" stroke-width="2px" d="M1645,264.5 C1645,177.0 1790.0,177.0 1790.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1790.0,266.5 L1798.0,254.5 1782.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-10" stroke-width="2px" d="M1995,264.5 C1995,89.5 2320.0,89.5 2320.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,266.5 L1987,254.5 2003,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-11" stroke-width="2px" d="M2170,264.5 C2170,177.0 2315.0,177.0 2315.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,266.5 L2162,254.5 2178,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-12" stroke-width="2px" d="M1820,264.5 C1820,2.0 2325.0,2.0 2325.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2325.0,266.5 L2333.0,254.5 2317.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-2139b2528693490693c6901d49ce44be-0-13" stroke-width="2px" d="M2345,264.5 C2345,177.0 2490.0,177.0 2490.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-2139b2528693490693c6901d49ce44be-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2490.0,266.5 L2498.0,254.5 2482.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Never to do anything which I should be afraid to do if it were the last hour of my life.
    Never                | ADV                  | RB                   | neg                 
    to                   | PART                 | TO                   | aux                 
    do                   | VERB                 | VB                   | ROOT                
    anything             | NOUN                 | NN                   | dobj                
    which                | DET                  | WDT                  | dobj                
    I                    | PRON                 | PRP                  | nsubj               
    should               | VERB                 | MD                   | aux                 
    be                   | VERB                 | VB                   | relcl               
    afraid               | ADJ                  | JJ                   | acomp               
    to                   | PART                 | TO                   | aux                 
    do                   | VERB                 | VB                   | xcomp               
    if                   | ADP                  | IN                   | mark                
    it                   | PRON                 | PRP                  | nsubj               
    were                 | VERB                 | VBD                  | ccomp               
    the                  | DET                  | DT                   | det                 
    last                 | ADJ                  | JJ                   | amod                
    hour                 | NOUN                 | NN                   | attr                
    of                   | ADP                  | IN                   | prep                
    my                   | DET                  | PRP$                 | poss                
    life                 | NOUN                 | NN                   | pobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="7394c91a41a748059e3d5e45f9e606cb-0" class="displacy" width="3550" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Never</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">do</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">anything</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">which</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">I</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">should</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">be</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">afraid</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">do</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">if</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">were</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2675">last</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2850">hour</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3025">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3200">my</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3375">life.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-0" stroke-width="2px" d="M70,439.5 C70,264.5 385.0,264.5 385.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-1" stroke-width="2px" d="M245,439.5 C245,352.0 380.0,352.0 380.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,441.5 L237,429.5 253,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-2" stroke-width="2px" d="M420,439.5 C420,352.0 555.0,352.0 555.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M555.0,441.5 L563.0,429.5 547.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-3" stroke-width="2px" d="M770,439.5 C770,2.0 1800.0,2.0 1800.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,441.5 L762,429.5 778,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-4" stroke-width="2px" d="M945,439.5 C945,264.5 1260.0,264.5 1260.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,441.5 L937,429.5 953,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-5" stroke-width="2px" d="M1120,439.5 C1120,352.0 1255.0,352.0 1255.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,441.5 L1112,429.5 1128,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-6" stroke-width="2px" d="M595,439.5 C595,89.5 1270.0,89.5 1270.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1270.0,441.5 L1278.0,429.5 1262.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-7" stroke-width="2px" d="M1295,439.5 C1295,352.0 1430.0,352.0 1430.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1430.0,441.5 L1438.0,429.5 1422.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-8" stroke-width="2px" d="M1645,439.5 C1645,352.0 1780.0,352.0 1780.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,441.5 L1637,429.5 1653,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-9" stroke-width="2px" d="M1470,439.5 C1470,264.5 1785.0,264.5 1785.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1785.0,441.5 L1793.0,429.5 1777.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-10" stroke-width="2px" d="M1995,439.5 C1995,264.5 2310.0,264.5 2310.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,441.5 L1987,429.5 2003,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-11" stroke-width="2px" d="M2170,439.5 C2170,352.0 2305.0,352.0 2305.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,441.5 L2162,429.5 2178,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-12" stroke-width="2px" d="M1820,439.5 C1820,177.0 2315.0,177.0 2315.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2315.0,441.5 L2323.0,429.5 2307.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-13" stroke-width="2px" d="M2520,439.5 C2520,264.5 2835.0,264.5 2835.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2520,441.5 L2512,429.5 2528,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-14" stroke-width="2px" d="M2695,439.5 C2695,352.0 2830.0,352.0 2830.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,441.5 L2687,429.5 2703,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-15" stroke-width="2px" d="M2345,439.5 C2345,177.0 2840.0,177.0 2840.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2840.0,441.5 L2848.0,429.5 2832.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-16" stroke-width="2px" d="M2870,439.5 C2870,352.0 3005.0,352.0 3005.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3005.0,441.5 L3013.0,429.5 2997.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-17" stroke-width="2px" d="M3220,439.5 C3220,352.0 3355.0,352.0 3355.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3220,441.5 L3212,429.5 3228,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-7394c91a41a748059e3d5e45f9e606cb-0-18" stroke-width="2px" d="M3045,439.5 C3045,264.5 3360.0,264.5 3360.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-7394c91a41a748059e3d5e45f9e606cb-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3360.0,441.5 L3368.0,429.5 3352.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life must be lived and curiosity kept alive. One must never, for whatever reason, turn his back on life.
    Life                 | NOUN                 | NN                   | nsubjpass           
    must                 | VERB                 | MD                   | aux                 
    be                   | VERB                 | VB                   | auxpass             
    lived                | VERB                 | VBN                  | ROOT                
    and                  | CCONJ                | CC                   | cc                  
    curiosity            | NOUN                 | NN                   | nsubj               
    kept                 | VERB                 | VBD                  | conj                
    alive                | ADJ                  | JJ                   | oprd                
    .                    | PUNCT                | .                    | punct               
    One                  | PRON                 | PRP                  | nsubj               
    must                 | VERB                 | MD                   | aux                 
    never                | ADV                  | RB                   | neg                 
    ,                    | PUNCT                | ,                    | punct               
    for                  | ADP                  | IN                   | prep                
    whatever             | DET                  | WDT                  | det                 
    reason               | NOUN                 | NN                   | pobj                
    ,                    | PUNCT                | ,                    | punct               
    turn                 | VERB                 | VB                   | ROOT                
    his                  | DET                  | PRP$                 | poss                
    back                 | NOUN                 | NN                   | advmod              
    on                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="b893d6ab6f6b4c93940c54e95fce3156-0" class="displacy" width="3375" height="662.0" direction="ltr" style="max-width: none; height: 662.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="225">must</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="400">be</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="575">lived</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="750">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="925">curiosity</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">kept</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">alive.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">One</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">must</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">never,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">for</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">whatever</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">reason,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">turn</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">his</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">back</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">on</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="572.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">life.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-0" stroke-width="2px" d="M70,527.0 C70,264.5 560.0,264.5 560.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubjpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,529.0 L62,517.0 78,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-1" stroke-width="2px" d="M245,527.0 C245,352.0 555.0,352.0 555.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,529.0 L237,517.0 253,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-2" stroke-width="2px" d="M420,527.0 C420,439.5 550.0,439.5 550.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">auxpass</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,529.0 L412,517.0 428,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-3" stroke-width="2px" d="M595,527.0 C595,439.5 725.0,439.5 725.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M725.0,529.0 L733.0,517.0 717.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-4" stroke-width="2px" d="M945,527.0 C945,439.5 1075.0,439.5 1075.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,529.0 L937,517.0 953,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-5" stroke-width="2px" d="M595,527.0 C595,264.5 1085.0,264.5 1085.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1085.0,529.0 L1093.0,517.0 1077.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-6" stroke-width="2px" d="M1120,527.0 C1120,439.5 1250.0,439.5 1250.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">oprd</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1250.0,529.0 L1258.0,517.0 1242.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-7" stroke-width="2px" d="M1470,527.0 C1470,2.0 2500.0,2.0 2500.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1470,529.0 L1462,517.0 1478,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-8" stroke-width="2px" d="M1645,527.0 C1645,89.5 2495.0,89.5 2495.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,529.0 L1637,517.0 1653,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-9" stroke-width="2px" d="M1820,527.0 C1820,177.0 2490.0,177.0 2490.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,529.0 L1812,517.0 1828,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-10" stroke-width="2px" d="M1995,527.0 C1995,264.5 2485.0,264.5 2485.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,529.0 L1987,517.0 2003,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-11" stroke-width="2px" d="M2170,527.0 C2170,439.5 2300.0,439.5 2300.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2170,529.0 L2162,517.0 2178,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-12" stroke-width="2px" d="M1995,527.0 C1995,352.0 2305.0,352.0 2305.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2305.0,529.0 L2313.0,517.0 2297.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-13" stroke-width="2px" d="M2695,527.0 C2695,439.5 2825.0,439.5 2825.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,529.0 L2687,517.0 2703,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-14" stroke-width="2px" d="M2520,527.0 C2520,352.0 2830.0,352.0 2830.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2830.0,529.0 L2838.0,517.0 2822.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-15" stroke-width="2px" d="M2870,527.0 C2870,439.5 3000.0,439.5 3000.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3000.0,529.0 L3008.0,517.0 2992.0,517.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-b893d6ab6f6b4c93940c54e95fce3156-0-16" stroke-width="2px" d="M3045,527.0 C3045,439.5 3175.0,439.5 3175.0,527.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-b893d6ab6f6b4c93940c54e95fce3156-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3175.0,529.0 L3183.0,517.0 3167.0,517.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  The game of life is not so much in holding a good hand as playing a poor hand well.
    The                  | DET                  | DT                   | det                 
    game                 | NOUN                 | NN                   | nsubj               
    of                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    is                   | VERB                 | VBZ                  | ROOT                
    not                  | ADV                  | RB                   | neg                 
    so                   | ADV                  | RB                   | advmod              
    much                 | ADV                  | RB                   | advmod              
    in                   | ADP                  | IN                   | prep                
    holding              | VERB                 | VBG                  | pcomp               
    a                    | DET                  | DT                   | det                 
    good                 | ADJ                  | JJ                   | amod                
    hand                 | NOUN                 | NN                   | dobj                
    as                   | ADP                  | IN                   | prep                
    playing              | VERB                 | VBG                  | pcomp               
    a                    | DET                  | DT                   | det                 
    poor                 | ADJ                  | JJ                   | amod                
    hand                 | NOUN                 | NN                   | dobj                
    well                 | ADV                  | RB                   | advmod              
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="add51d1647514a60bd982097e9fecd5a-0" class="displacy" width="3375" height="487.0" direction="ltr" style="max-width: none; height: 487.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="50">The</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="225">game</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="400">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="575">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="750">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="925">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">so</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">much</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">holding</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">good</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">hand</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">as</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">playing</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">poor</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">hand</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">well.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">ADV</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-0" stroke-width="2px" d="M70,352.0 C70,264.5 210.0,264.5 210.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,354.0 L62,342.0 78,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-1" stroke-width="2px" d="M245,352.0 C245,89.5 745.0,89.5 745.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,354.0 L237,342.0 253,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-2" stroke-width="2px" d="M245,352.0 C245,264.5 385.0,264.5 385.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M385.0,354.0 L393.0,342.0 377.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-3" stroke-width="2px" d="M420,352.0 C420,264.5 560.0,264.5 560.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M560.0,354.0 L568.0,342.0 552.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-4" stroke-width="2px" d="M770,352.0 C770,264.5 910.0,264.5 910.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M910.0,354.0 L918.0,342.0 902.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-5" stroke-width="2px" d="M1120,352.0 C1120,264.5 1260.0,264.5 1260.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,354.0 L1112,342.0 1128,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-6" stroke-width="2px" d="M770,352.0 C770,89.5 1270.0,89.5 1270.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1270.0,354.0 L1278.0,342.0 1262.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-7" stroke-width="2px" d="M770,352.0 C770,2.0 1450.0,2.0 1450.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1450.0,354.0 L1458.0,342.0 1442.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-8" stroke-width="2px" d="M1470,352.0 C1470,264.5 1610.0,264.5 1610.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1610.0,354.0 L1618.0,342.0 1602.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-9" stroke-width="2px" d="M1820,352.0 C1820,177.0 2140.0,177.0 2140.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,354.0 L1812,342.0 1828,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-10" stroke-width="2px" d="M1995,352.0 C1995,264.5 2135.0,264.5 2135.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1995,354.0 L1987,342.0 2003,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-11" stroke-width="2px" d="M1645,352.0 C1645,89.5 2145.0,89.5 2145.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2145.0,354.0 L2153.0,342.0 2137.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-12" stroke-width="2px" d="M1645,352.0 C1645,2.0 2325.0,2.0 2325.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2325.0,354.0 L2333.0,342.0 2317.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-13" stroke-width="2px" d="M2345,352.0 C2345,264.5 2485.0,264.5 2485.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2485.0,354.0 L2493.0,342.0 2477.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-14" stroke-width="2px" d="M2695,352.0 C2695,177.0 3015.0,177.0 3015.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,354.0 L2687,342.0 2703,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-15" stroke-width="2px" d="M2870,352.0 C2870,264.5 3010.0,264.5 3010.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2870,354.0 L2862,342.0 2878,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-16" stroke-width="2px" d="M2520,352.0 C2520,89.5 3020.0,89.5 3020.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3020.0,354.0 L3028.0,342.0 3012.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-add51d1647514a60bd982097e9fecd5a-0-17" stroke-width="2px" d="M2520,352.0 C2520,2.0 3200.0,2.0 3200.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-add51d1647514a60bd982097e9fecd5a-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3200.0,354.0 L3208.0,342.0 3192.0,342.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is not always a matter of holding good cards, but sometimes, playing a poor hand well.
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    not                  | ADV                  | RB                   | neg                 
    always               | ADV                  | RB                   | advmod              
    a                    | DET                  | DT                   | det                 
    matter               | NOUN                 | NN                   | attr                
    of                   | ADP                  | IN                   | prep                
    holding              | VERB                 | VBG                  | pcomp               
    good                 | ADJ                  | JJ                   | amod                
    cards                | NOUN                 | NNS                  | dobj                
    ,                    | PUNCT                | ,                    | punct               
    but                  | CCONJ                | CC                   | cc                  
    sometimes            | ADV                  | RB                   | advmod              
    ,                    | PUNCT                | ,                    | punct               
    playing              | VERB                 | VBG                  | advcl               
    a                    | DET                  | DT                   | det                 
    poor                 | ADJ                  | JJ                   | amod                
    hand                 | NOUN                 | NN                   | dobj                
    well                 | ADV                  | RB                   | advmod              
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="d970e8ac633f4f559e6680778d33eb3d-0" class="displacy" width="3025" height="749.5" direction="ltr" style="max-width: none; height: 749.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="400">not</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="575">always</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="750">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="925">matter</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">holding</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">good</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">cards,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">but</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">sometimes,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">playing</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">poor</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="2675">hand</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="659.5">
    <tspan class="displacy-word" fill="currentColor" x="2850">well.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">ADV</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-0" stroke-width="2px" d="M70,614.5 C70,527.0 195.0,527.0 195.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,616.5 L62,604.5 78,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-1" stroke-width="2px" d="M245,614.5 C245,527.0 370.0,527.0 370.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">neg</textPath>
    </text>
    <path class="displacy-arrowhead" d="M370.0,616.5 L378.0,604.5 362.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-2" stroke-width="2px" d="M245,614.5 C245,439.5 550.0,439.5 550.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M550.0,616.5 L558.0,604.5 542.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-3" stroke-width="2px" d="M770,614.5 C770,527.0 895.0,527.0 895.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,616.5 L762,604.5 778,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-4" stroke-width="2px" d="M245,614.5 C245,264.5 910.0,264.5 910.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M910.0,616.5 L918.0,604.5 902.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-5" stroke-width="2px" d="M945,614.5 C945,527.0 1070.0,527.0 1070.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1070.0,616.5 L1078.0,604.5 1062.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-6" stroke-width="2px" d="M1120,614.5 C1120,527.0 1245.0,527.0 1245.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1245.0,616.5 L1253.0,604.5 1237.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-7" stroke-width="2px" d="M1470,614.5 C1470,527.0 1595.0,527.0 1595.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1470,616.5 L1462,604.5 1478,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-8" stroke-width="2px" d="M1295,614.5 C1295,439.5 1600.0,439.5 1600.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1600.0,616.5 L1608.0,604.5 1592.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-9" stroke-width="2px" d="M245,614.5 C245,177.0 1790.0,177.0 1790.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1790.0,616.5 L1798.0,604.5 1782.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-10" stroke-width="2px" d="M245,614.5 C245,89.5 1970.0,89.5 1970.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1970.0,616.5 L1978.0,604.5 1962.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-11" stroke-width="2px" d="M245,614.5 C245,2.0 2150.0,2.0 2150.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2150.0,616.5 L2158.0,604.5 2142.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-12" stroke-width="2px" d="M2345,614.5 C2345,439.5 2650.0,439.5 2650.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,616.5 L2337,604.5 2353,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-13" stroke-width="2px" d="M2520,614.5 C2520,527.0 2645.0,527.0 2645.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2520,616.5 L2512,604.5 2528,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-14" stroke-width="2px" d="M2170,614.5 C2170,352.0 2655.0,352.0 2655.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2655.0,616.5 L2663.0,604.5 2647.0,604.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-d970e8ac633f4f559e6680778d33eb3d-0-15" stroke-width="2px" d="M2170,614.5 C2170,264.5 2835.0,264.5 2835.0,614.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-d970e8ac633f4f559e6680778d33eb3d-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2835.0,616.5 L2843.0,604.5 2827.0,604.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is like walking through Paradise with peas in your shoes.
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    like                 | ADP                  | IN                   | prep                
    walking              | VERB                 | VBG                  | pcomp               
    through              | ADP                  | IN                   | prep                
    Paradise             | PROPN                | NNP                  | pobj                
    with                 | ADP                  | IN                   | prep                
    peas                 | NOUN                 | NNS                  | pobj                
    in                   | ADP                  | IN                   | prep                
    your                 | DET                  | PRP$                 | poss                
    shoes                | NOUN                 | NNS                  | pobj                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="1d9fc3e837aa43d5a9214bc6ee9c0cdb-0" class="displacy" width="1975" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">like</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">walking</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">through</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">Paradise</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">PROPN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">with</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">peas</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">your</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">shoes.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-0" stroke-width="2px" d="M70,264.5 C70,177.0 215.0,177.0 215.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-1" stroke-width="2px" d="M245,264.5 C245,177.0 390.0,177.0 390.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M390.0,266.5 L398.0,254.5 382.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-2" stroke-width="2px" d="M420,264.5 C420,177.0 565.0,177.0 565.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M565.0,266.5 L573.0,254.5 557.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-3" stroke-width="2px" d="M595,264.5 C595,177.0 740.0,177.0 740.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M740.0,266.5 L748.0,254.5 732.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-4" stroke-width="2px" d="M770,264.5 C770,177.0 915.0,177.0 915.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M915.0,266.5 L923.0,254.5 907.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-5" stroke-width="2px" d="M595,264.5 C595,2.0 1100.0,2.0 1100.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1100.0,266.5 L1108.0,254.5 1092.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-6" stroke-width="2px" d="M1120,264.5 C1120,177.0 1265.0,177.0 1265.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1265.0,266.5 L1273.0,254.5 1257.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-7" stroke-width="2px" d="M1295,264.5 C1295,177.0 1440.0,177.0 1440.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1440.0,266.5 L1448.0,254.5 1432.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-8" stroke-width="2px" d="M1645,264.5 C1645,177.0 1790.0,177.0 1790.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,266.5 L1637,254.5 1653,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-9" stroke-width="2px" d="M1470,264.5 C1470,89.5 1795.0,89.5 1795.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-1d9fc3e837aa43d5a9214bc6ee9c0cdb-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1795.0,266.5 L1803.0,254.5 1787.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Most important thing in life ... is learning how to fall.
    Most                 | ADV                  | RBS                  | advmod              
    important            | ADJ                  | JJ                   | amod                
    thing                | NOUN                 | NN                   | nsubj               
    in                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    ...                  | PUNCT                | :                    | punct               
    is                   | VERB                 | VBZ                  | aux                 
    learning             | VERB                 | VBG                  | ROOT                
    how                  | ADV                  | WRB                  | advmod              
    to                   | PART                 | TO                   | aux                 
    fall                 | VERB                 | VB                   | xcomp               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="fa7b8daaa1654ca7b72858700ab2acea-0" class="displacy" width="1800" height="487.0" direction="ltr" style="max-width: none; height: 487.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Most</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="225">important</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="400">thing</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="575">in</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="750">life ...</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="925">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">learning</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">how</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">fall.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">VERB</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa7b8daaa1654ca7b72858700ab2acea-0-0" stroke-width="2px" d="M70,352.0 C70,264.5 210.0,264.5 210.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa7b8daaa1654ca7b72858700ab2acea-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,354.0 L62,342.0 78,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa7b8daaa1654ca7b72858700ab2acea-0-1" stroke-width="2px" d="M245,352.0 C245,264.5 385.0,264.5 385.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa7b8daaa1654ca7b72858700ab2acea-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,354.0 L237,342.0 253,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa7b8daaa1654ca7b72858700ab2acea-0-2" stroke-width="2px" d="M420,352.0 C420,2.0 1100.0,2.0 1100.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa7b8daaa1654ca7b72858700ab2acea-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,354.0 L412,342.0 428,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa7b8daaa1654ca7b72858700ab2acea-0-3" stroke-width="2px" d="M420,352.0 C420,264.5 560.0,264.5 560.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa7b8daaa1654ca7b72858700ab2acea-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M560.0,354.0 L568.0,342.0 552.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa7b8daaa1654ca7b72858700ab2acea-0-4" stroke-width="2px" d="M595,352.0 C595,264.5 735.0,264.5 735.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa7b8daaa1654ca7b72858700ab2acea-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M735.0,354.0 L743.0,342.0 727.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa7b8daaa1654ca7b72858700ab2acea-0-5" stroke-width="2px" d="M945,352.0 C945,264.5 1085.0,264.5 1085.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa7b8daaa1654ca7b72858700ab2acea-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,354.0 L937,342.0 953,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa7b8daaa1654ca7b72858700ab2acea-0-6" stroke-width="2px" d="M1295,352.0 C1295,177.0 1615.0,177.0 1615.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa7b8daaa1654ca7b72858700ab2acea-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,354.0 L1287,342.0 1303,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa7b8daaa1654ca7b72858700ab2acea-0-7" stroke-width="2px" d="M1470,352.0 C1470,264.5 1610.0,264.5 1610.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa7b8daaa1654ca7b72858700ab2acea-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1470,354.0 L1462,342.0 1478,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-fa7b8daaa1654ca7b72858700ab2acea-0-8" stroke-width="2px" d="M1120,352.0 C1120,89.5 1620.0,89.5 1620.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-fa7b8daaa1654ca7b72858700ab2acea-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1620.0,354.0 L1628.0,342.0 1612.0,342.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is all memory except for the one present moment that goes by so quick you can hardly catch it going.
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    all                  | DET                  | DT                   | dep                 
    memory               | NOUN                 | NN                   | attr                
    except               | ADP                  | IN                   | prep                
    for                  | ADP                  | IN                   | prep                
    the                  | DET                  | DT                   | det                 
    one                  | NUM                  | CD                   | nummod              
    present              | ADJ                  | JJ                   | amod                
    moment               | NOUN                 | NN                   | pobj                
    that                 | DET                  | WDT                  | nsubj               
    goes                 | VERB                 | VBZ                  | relcl               
    by                   | ADV                  | RB                   | prep                
    so                   | ADV                  | RB                   | advmod              
    quick                | ADJ                  | JJ                   | acomp               
    you                  | PRON                 | PRP                  | nsubj               
    can                  | VERB                 | MD                   | aux                 
    hardly               | ADV                  | RB                   | advmod              
    catch                | VERB                 | VB                   | ccomp               
    it                   | PRON                 | PRP                  | nsubj               
    going                | VERB                 | VBG                  | ccomp               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="44e97f83f91c4a228f8dceecc3a71d2f-0" class="displacy" width="3725" height="487.0" direction="ltr" style="max-width: none; height: 487.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="400">all</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="575">memory</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="750">except</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="925">for</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">one</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">present</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">moment</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">goes</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">by</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">so</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">quick</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">can</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">hardly</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">catch</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3375">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="3550">going.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">VERB</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-0" stroke-width="2px" d="M70,352.0 C70,264.5 210.0,264.5 210.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,354.0 L62,342.0 78,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-1" stroke-width="2px" d="M245,352.0 C245,264.5 385.0,264.5 385.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M385.0,354.0 L393.0,342.0 377.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-2" stroke-width="2px" d="M245,352.0 C245,177.0 565.0,177.0 565.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M565.0,354.0 L573.0,342.0 557.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-3" stroke-width="2px" d="M245,352.0 C245,89.5 745.0,89.5 745.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M745.0,354.0 L753.0,342.0 737.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-4" stroke-width="2px" d="M770,352.0 C770,264.5 910.0,264.5 910.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M910.0,354.0 L918.0,342.0 902.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-5" stroke-width="2px" d="M1120,352.0 C1120,89.5 1620.0,89.5 1620.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,354.0 L1112,342.0 1128,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-6" stroke-width="2px" d="M1295,352.0 C1295,177.0 1615.0,177.0 1615.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nummod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,354.0 L1287,342.0 1303,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-7" stroke-width="2px" d="M1470,352.0 C1470,264.5 1610.0,264.5 1610.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1470,354.0 L1462,342.0 1478,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-8" stroke-width="2px" d="M945,352.0 C945,2.0 1625.0,2.0 1625.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1625.0,354.0 L1633.0,342.0 1617.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-9" stroke-width="2px" d="M1820,352.0 C1820,264.5 1960.0,264.5 1960.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1820,354.0 L1812,342.0 1828,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-10" stroke-width="2px" d="M1645,352.0 C1645,177.0 1965.0,177.0 1965.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1965.0,354.0 L1973.0,342.0 1957.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-11" stroke-width="2px" d="M1995,352.0 C1995,264.5 2135.0,264.5 2135.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2135.0,354.0 L2143.0,342.0 2127.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-12" stroke-width="2px" d="M2345,352.0 C2345,264.5 2485.0,264.5 2485.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,354.0 L2337,342.0 2353,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-13" stroke-width="2px" d="M1995,352.0 C1995,89.5 2495.0,89.5 2495.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2495.0,354.0 L2503.0,342.0 2487.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-14" stroke-width="2px" d="M2695,352.0 C2695,89.5 3195.0,89.5 3195.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,354.0 L2687,342.0 2703,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-15" stroke-width="2px" d="M2870,352.0 C2870,177.0 3190.0,177.0 3190.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2870,354.0 L2862,342.0 2878,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-16" stroke-width="2px" d="M3045,352.0 C3045,264.5 3185.0,264.5 3185.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3045,354.0 L3037,342.0 3053,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-17" stroke-width="2px" d="M2520,352.0 C2520,2.0 3200.0,2.0 3200.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3200.0,354.0 L3208.0,342.0 3192.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-18" stroke-width="2px" d="M3395,352.0 C3395,264.5 3535.0,264.5 3535.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3395,354.0 L3387,342.0 3403,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-19" stroke-width="2px" d="M3220,352.0 C3220,177.0 3540.0,177.0 3540.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-44e97f83f91c4a228f8dceecc3a71d2f-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3540.0,354.0 L3548.0,342.0 3532.0,342.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is a spell so exquisite that everything conspires to break it.  
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    a                    | DET                  | DT                   | det                 
    spell                | NOUN                 | NN                   | attr                
    so                   | ADV                  | RB                   | advmod              
    exquisite            | ADJ                  | JJ                   | acomp               
    that                 | ADP                  | IN                   | mark                
    everything           | NOUN                 | NN                   | nsubj               
    conspires            | VERB                 | VBZ                  | ccomp               
    to                   | PART                 | TO                   | aux                 
    break                | VERB                 | VB                   | advcl               
    it                   | PRON                 | PRP                  | dobj                
    .                    | PUNCT                | .                    | punct               
                         | SPACE                | _SP                  |                     



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="9b28adf1143441369536528bd266b75d-0" class="displacy" width="2325" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">spell</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">so</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">exquisite</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">that</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">everything</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">conspires</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">break</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">it.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150"> </tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">SPACE</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-0" stroke-width="2px" d="M70,439.5 C70,352.0 205.0,352.0 205.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-1" stroke-width="2px" d="M420,439.5 C420,352.0 555.0,352.0 555.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,441.5 L412,429.5 428,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-2" stroke-width="2px" d="M245,439.5 C245,264.5 560.0,264.5 560.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M560.0,441.5 L568.0,429.5 552.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-3" stroke-width="2px" d="M770,439.5 C770,352.0 905.0,352.0 905.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,441.5 L762,429.5 778,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-4" stroke-width="2px" d="M245,439.5 C245,89.5 920.0,89.5 920.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M920.0,441.5 L928.0,429.5 912.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-5" stroke-width="2px" d="M1120,439.5 C1120,264.5 1435.0,264.5 1435.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">mark</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,441.5 L1112,429.5 1128,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-6" stroke-width="2px" d="M1295,439.5 C1295,352.0 1430.0,352.0 1430.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,441.5 L1287,429.5 1303,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-7" stroke-width="2px" d="M945,439.5 C945,177.0 1440.0,177.0 1440.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1440.0,441.5 L1448.0,429.5 1432.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-8" stroke-width="2px" d="M1645,439.5 C1645,352.0 1780.0,352.0 1780.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,441.5 L1637,429.5 1653,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-9" stroke-width="2px" d="M1470,439.5 C1470,264.5 1785.0,264.5 1785.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1785.0,441.5 L1793.0,429.5 1777.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-10" stroke-width="2px" d="M245,439.5 C245,2.0 1975.0,2.0 1975.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">punct</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1975.0,441.5 L1983.0,429.5 1967.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-9b28adf1143441369536528bd266b75d-0-11" stroke-width="2px" d="M1995,439.5 C1995,352.0 2130.0,352.0 2130.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-9b28adf1143441369536528bd266b75d-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle"></textPath>
    </text>
    <path class="displacy-arrowhead" d="M2130.0,441.5 L2138.0,429.5 2122.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  Life is a game. Money is how we keep score.
    Life                 | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    a                    | DET                  | DT                   | det                 
    game                 | NOUN                 | NN                   | attr                
    .                    | PUNCT                | .                    | punct               
    Money                | NOUN                 | NN                   | nsubj               
    is                   | VERB                 | VBZ                  | ROOT                
    how                  | ADV                  | WRB                  | advmod              
    we                   | PRON                 | PRP                  | nsubj               
    keep                 | VERB                 | VBP                  | ccomp               
    score                | NOUN                 | NN                   | oprd                
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="55761211f4204c678a61694a77097b1a-0" class="displacy" width="1800" height="399.5" direction="ltr" style="max-width: none; height: 399.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="50">Life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="225">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="400">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="575">game.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="750">Money</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="925">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">how</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">ADV</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">we</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">keep</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="309.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">score.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">NOUN</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-55761211f4204c678a61694a77097b1a-0-0" stroke-width="2px" d="M70,264.5 C70,177.0 215.0,177.0 215.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-55761211f4204c678a61694a77097b1a-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,266.5 L62,254.5 78,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-55761211f4204c678a61694a77097b1a-0-1" stroke-width="2px" d="M420,264.5 C420,177.0 565.0,177.0 565.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-55761211f4204c678a61694a77097b1a-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,266.5 L412,254.5 428,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-55761211f4204c678a61694a77097b1a-0-2" stroke-width="2px" d="M245,264.5 C245,89.5 570.0,89.5 570.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-55761211f4204c678a61694a77097b1a-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M570.0,266.5 L578.0,254.5 562.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-55761211f4204c678a61694a77097b1a-0-3" stroke-width="2px" d="M770,264.5 C770,177.0 915.0,177.0 915.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-55761211f4204c678a61694a77097b1a-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M770,266.5 L762,254.5 778,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-55761211f4204c678a61694a77097b1a-0-4" stroke-width="2px" d="M1120,264.5 C1120,89.5 1445.0,89.5 1445.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-55761211f4204c678a61694a77097b1a-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,266.5 L1112,254.5 1128,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-55761211f4204c678a61694a77097b1a-0-5" stroke-width="2px" d="M1295,264.5 C1295,177.0 1440.0,177.0 1440.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-55761211f4204c678a61694a77097b1a-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,266.5 L1287,254.5 1303,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-55761211f4204c678a61694a77097b1a-0-6" stroke-width="2px" d="M945,264.5 C945,2.0 1450.0,2.0 1450.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-55761211f4204c678a61694a77097b1a-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1450.0,266.5 L1458.0,254.5 1442.0,254.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-55761211f4204c678a61694a77097b1a-0-7" stroke-width="2px" d="M1470,264.5 C1470,177.0 1615.0,177.0 1615.0,264.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-55761211f4204c678a61694a77097b1a-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">oprd</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1615.0,266.5 L1623.0,254.5 1607.0,254.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  The first step to getting the things you want out of life is this: Decide what you want.
    The                  | DET                  | DT                   | det                 
    first                | ADJ                  | JJ                   | amod                
    step                 | NOUN                 | NN                   | nsubj               
    to                   | ADP                  | IN                   | prep                
    getting              | VERB                 | VBG                  | pcomp               
    the                  | DET                  | DT                   | det                 
    things               | NOUN                 | NNS                  | dobj                
    you                  | PRON                 | PRP                  | nsubj               
    want                 | VERB                 | VBP                  | relcl               
    out                  | ADP                  | IN                   | prep                
    of                   | ADP                  | IN                   | prep                
    life                 | NOUN                 | NN                   | pobj                
    is                   | VERB                 | VBZ                  | ROOT                
    this                 | DET                  | DT                   | attr                
    :                    | PUNCT                | :                    | punct               
    Decide               | VERB                 | VB                   | acl                 
    what                 | PRON                 | WP                   | dobj                
    you                  | PRON                 | PRP                  | nsubj               
    want                 | VERB                 | VBP                  | ccomp               
    .                    | PUNCT                | .                    | punct               



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="014e5f0b72cc4f58b3f8c247244c30b7-0" class="displacy" width="3200" height="574.5" direction="ltr" style="max-width: none; height: 574.5px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="50">The</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="225">first</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">ADJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="400">step</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="575">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="750">getting</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="925">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1100">things</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1275">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1450">want</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1625">out</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1800">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="1975">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2150">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2325">this:</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2500">Decide</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2675">what</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="2850">you</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="484.5">
    <tspan class="displacy-word" fill="currentColor" x="3025">want.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">VERB</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-0" stroke-width="2px" d="M70,439.5 C70,264.5 385.0,264.5 385.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,441.5 L62,429.5 78,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-1" stroke-width="2px" d="M245,439.5 C245,352.0 380.0,352.0 380.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">amod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,441.5 L237,429.5 253,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-2" stroke-width="2px" d="M420,439.5 C420,2.0 2150.0,2.0 2150.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,441.5 L412,429.5 428,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-3" stroke-width="2px" d="M420,439.5 C420,352.0 555.0,352.0 555.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M555.0,441.5 L563.0,429.5 547.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-4" stroke-width="2px" d="M595,439.5 C595,352.0 730.0,352.0 730.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M730.0,441.5 L738.0,429.5 722.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-5" stroke-width="2px" d="M945,439.5 C945,352.0 1080.0,352.0 1080.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,441.5 L937,429.5 953,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-6" stroke-width="2px" d="M770,439.5 C770,264.5 1085.0,264.5 1085.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1085.0,441.5 L1093.0,429.5 1077.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-7" stroke-width="2px" d="M1295,439.5 C1295,352.0 1430.0,352.0 1430.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1295,441.5 L1287,429.5 1303,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-8" stroke-width="2px" d="M1120,439.5 C1120,264.5 1435.0,264.5 1435.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">relcl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1435.0,441.5 L1443.0,429.5 1427.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-9" stroke-width="2px" d="M770,439.5 C770,89.5 1620.0,89.5 1620.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1620.0,441.5 L1628.0,429.5 1612.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-10" stroke-width="2px" d="M1645,439.5 C1645,352.0 1780.0,352.0 1780.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1780.0,441.5 L1788.0,429.5 1772.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-11" stroke-width="2px" d="M1820,439.5 C1820,352.0 1955.0,352.0 1955.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1955.0,441.5 L1963.0,429.5 1947.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-12" stroke-width="2px" d="M2170,439.5 C2170,352.0 2305.0,352.0 2305.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2305.0,441.5 L2313.0,429.5 2297.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-13" stroke-width="2px" d="M2345,439.5 C2345,352.0 2480.0,352.0 2480.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2480.0,441.5 L2488.0,429.5 2472.0,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-14" stroke-width="2px" d="M2695,439.5 C2695,264.5 3010.0,264.5 3010.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2695,441.5 L2687,429.5 2703,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-15" stroke-width="2px" d="M2870,439.5 C2870,352.0 3005.0,352.0 3005.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2870,441.5 L2862,429.5 2878,429.5" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-16" stroke-width="2px" d="M2520,439.5 C2520,177.0 3015.0,177.0 3015.0,439.5" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-014e5f0b72cc4f58b3f8c247244c30b7-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3015.0,441.5 L3023.0,429.5 3007.0,429.5" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------
    sentence :  A life without cause is a life without effect.   
    A                    | DET                  | DT                   | det                 
    life                 | NOUN                 | NN                   | nsubj               
    without              | ADP                  | IN                   | prep                
    cause                | ADP                  | IN                   | pcomp               
    is                   | VERB                 | VBZ                  | ROOT                
    a                    | DET                  | DT                   | det                 
    life                 | NOUN                 | NN                   | attr                
    without              | ADP                  | IN                   | prep                
    effect               | NOUN                 | NN                   | pobj                
    .                    | PUNCT                | .                    | punct               
                         | SPACE                | _SP                  |                     



<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="bdbcb1fc4c3c4821b0a83ff9ebac0b25-0" class="displacy" width="1800" height="487.0" direction="ltr" style="max-width: none; height: 487.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="50">A</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="225">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="400">without</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="575">cause</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="750">is</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="925">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">life</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">without</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">effect.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="397.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">  </tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">SPACE</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-0" stroke-width="2px" d="M70,352.0 C70,264.5 210.0,264.5 210.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,354.0 L62,342.0 78,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-1" stroke-width="2px" d="M245,352.0 C245,89.5 745.0,89.5 745.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,354.0 L237,342.0 253,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-2" stroke-width="2px" d="M245,352.0 C245,264.5 385.0,264.5 385.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M385.0,354.0 L393.0,342.0 377.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-3" stroke-width="2px" d="M420,352.0 C420,264.5 560.0,264.5 560.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M560.0,354.0 L568.0,342.0 552.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-4" stroke-width="2px" d="M945,352.0 C945,264.5 1085.0,264.5 1085.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M945,354.0 L937,342.0 953,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-5" stroke-width="2px" d="M770,352.0 C770,177.0 1090.0,177.0 1090.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">attr</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1090.0,354.0 L1098.0,342.0 1082.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-6" stroke-width="2px" d="M1120,352.0 C1120,264.5 1260.0,264.5 1260.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1260.0,354.0 L1268.0,342.0 1252.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-7" stroke-width="2px" d="M770,352.0 C770,2.0 1450.0,2.0 1450.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">punct</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1450.0,354.0 L1458.0,342.0 1442.0,342.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-8" stroke-width="2px" d="M1470,352.0 C1470,264.5 1610.0,264.5 1610.0,352.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-bdbcb1fc4c3c4821b0a83ff9ebac0b25-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle"></textPath>
    </text>
    <path class="displacy-arrowhead" d="M1610.0,354.0 L1618.0,342.0 1602.0,342.0" fill="currentColor"/>
</g>
</svg>


    ----------------------------------------------------



```python
print('terminology for each index')
def explain_index(index):
    for word in index:
        print('{0:20}: {1}'.format(word, spacy.explain(word)))
print('\nPOS\n------------------')
explain_index(pos_index)
print('\nTAG\n------------------')
explain_index(tag_index)
print('\nDEP\n------------------')
explain_index(dep_index)
```

    terminology for each index
    
    POS
    ------------------
    NOUN                : noun
    VERB                : verb
    ADV                 : adverb
    ADP                 : adposition
    PRON                : pronoun
    PUNCT               : punctuation
    DET                 : determiner
    ADJ                 : adjective
    PART                : particle
    CCONJ               : coordinating conjunction
    NUM                 : numeral
    AUX                 : auxiliary
    PROPN               : proper noun
    SPACE               : space
    
    TAG
    ------------------
    NN                  : noun, singular or mass
    VBZ                 : verb, 3rd person singular present
    RB                  : adverb
    IN                  : conjunction, subordinating or preposition
    VBG                 : verb, gerund or present participle
    PRP                 : pronoun, personal
    .                   : punctuation mark, sentence closer
    DT                  : determiner
    RBS                 : adverb, superlative
    JJ                  : adjective
    TO                  : infinitival to
    VB                  : verb, base form
    PRP$                : pronoun, possessive
    :                   : punctuation mark, colon or ellipsis
    WDT                 : wh-determiner
    VBP                 : verb, non-3rd person singular present
    VBN                 : verb, past participle
    ,                   : punctuation mark, comma
    MD                  : verb, modal auxiliary
    CC                  : conjunction, coordinating
    NNS                 : noun, plural
    EX                  : existential there
    CD                  : cardinal number
    WRB                 : wh-adverb
    WP                  : wh-pronoun, personal
    POS                 : possessive ending
    NNP                 : noun, proper singular
    JJS                 : adjective, superlative
    VBD                 : verb, past tense
    _SP                 : None
    RP                  : adverb, particle
    JJR                 : adjective, comparative
    
    DEP
    ------------------
    nsubj               : nominal subject
    ROOT                : None
    neg                 : negation modifier
    prep                : prepositional modifier
    pcomp               : complement of preposition
    dobj                : direct object
    punct               : punctuation
    det                 : determiner
    advmod              : adverbial modifier
    amod                : adjectival modifier
    ccomp               : clausal complement
    aux                 : auxiliary
    xcomp               : open clausal complement
    poss                : possession modifier
    conj                : conjunct
    acomp               : adjectival complement
    attr                : attribute
    relcl               : relative clause modifier
    mark                : marker
    advcl               : adverbial clause modifier
    cc                  : coordinating conjunction
    pobj                : object of preposition
    expl                : expletive
    nummod              : numeric modifier
    appos               : appositional modifier
    case                : case marking
    nsubjpass           : nominal subject (passive)
    dep                 : unclassified dependent
    intj                : interjection
    auxpass             : auxiliary (passive)
    dative              : dative
                        : None
    csubj               : clausal subject
    agent               : agent
    prt                 : particle
    npadvmod            : noun phrase as adverbial modifier
    compound            : compound
    oprd                : object predicate
    acl                 : clausal modifier of noun (adjectival clause)



```python

```
