import genanki

#level,nom,description,construction,exemples,vocabs
my_model = genanki.Model(
  1863528675,
  'Simple Model',
  fields=[
    {'name': 'level'},
    {'name': 'gram_jp'},
    {'name': 'gram_fr'},
    {'name': 'descr'},
    {'name': 'construction'},
    {'name': 'exemples'},
    {'name': 'trad'},
    {'name': 'vocab'},
  ],
  templates=[
    {
      'name': 'gram Card 1',
      'qfmt': '{{exemples}}<br><br> {{vocab}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{trad}}<br><br> {{gram_jp}}<br><br> {{gram_fr}}<br><br> {{descr}}<br><br> {{construction}}',
    },
    {
      'name': 'gram Card 3',
      'qfmt': '{{trad}}<br><br> {{vocab}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{exemples}}<br><br> {{gram_jp}}<br><br> {{gram_fr}}<br><br> {{descr}}<br><br> {{construction}}',
    },
  ])
  
  
my_model2 = genanki.Model(
  1863528676,
  'Simple Model',
  fields=[
    {'name': 'level'},
    {'name': 'gram_jp'},
    {'name': 'gram_fr'},
    {'name': 'descr'},
    {'name': 'construction'},
    {'name': 'exemples'},
    {'name': 'trad'},
    {'name': 'vocab'},
  ],
  templates=[
    {
      'name': 'gram Card 2',
      'qfmt': '{{gram_fr}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{gram_jp}}<br><br> {{descr}}<br><br> {{construction}}<br><br> {{exemples}}',
    },
  ]) 
  
  
my_deck0 = genanki.Deck(
  1238372530,
  '5_Grammaire Autre')
my_deck2 = genanki.Deck(
  1238372531,
  '4_Grammaire N2')
my_deck3 = genanki.Deck(
  1238372532,
  '3_Grammaire N3')
my_deck4 = genanki.Deck(
  1238372533,
  '2_Grammaire N4')
my_deck5 = genanki.Deck(
  1238372534,
  '1_Grammaire N5')

for i in point:
    
    sex =''
    if not i['level']:
        i['level'] = '0'
    for j in i['exemple']:
        svoc = ''
        for k in j[2]:
            if len(k)==3:
                svoc+= k[2] + '(' + k[0] + ') : ' + k[1]  + '<br>'
            else:
             svoc+= '(' + k[0] + ') : ' + k[1]  + '<br>'
        sex += j[0] +'<br>'+j[1] + '<br>' + svoc + '<br>'
    
    
    fields = [i['level'] if i['level']  else '0' ,
    i['gram_jp'],
    i['gram_fr'],
    i['descr'],
    i['construction'],
    sex,
    "",
    ""
    ]
    
    my_note = genanki.Note(model=my_model2,fields=fields)

    exec('my_deck'+i['level']+'.add_note(my_note)')
    
    
    for j in i['exemple']:
        svoc = ''
        vocab = j[2]
        
        for k in vocab:
            if len(k)==3:
                svoc+= k[2] + '(' + k[0] + ') : ' + k[1]  + '<br>'
            else:
             svoc+= '(' + k[0] + ') : ' + k[1]  + '<br>'
        fields = [i['level'] if i['level']  else '0' ,
        i['gram_jp'],
        i['gram_fr'],
        i['descr'],
        i['construction'],
        j[0],
        j[1],
        svoc
        ]
    
        
        my_note = genanki.Note(model=my_model,fields=fields)
        exec('my_deck'+i['level']+'.add_note(my_note)')
    


    
    
genanki.Package(my_deck0).write_to_file('output0.apkg')
genanki.Package(my_deck2).write_to_file('output2.apkg')
genanki.Package(my_deck3).write_to_file('output3.apkg')
genanki.Package(my_deck4).write_to_file('output4.apkg')
genanki.Package(my_deck5).write_to_file('output5.apkg')