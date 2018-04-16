# -*- coding: utf-8 -*-
"""

"""
import json
#CATEGORIES = ['cuisine', 'coding', 'culture', 'misc', 'nature', 'perso', 'tech']

CATEGORIES = {
        'coding':'<i class="fa fa-terminal"></i><br><br>coding',
        'cuisine':'<i class="fa fa-cutlery"></i><br><br>cuisine',
        'culture':'<i class="fa fa-bookmark-o"></i><br><br>culture',
        'health':'<i class="fa fa-heartbeat"></i><br><br>health',
        'misc':'<i class="fa fa-asterisk"></i><br><br>misc',
        'nature':'<i class="fa fa-leaf"></i><br><br>nature',
        'perso':'<i class="fa fa-heart"></i><br><br>perso',
        'tech':'<i class="fa fa-newspaper-o"></i><br><br>tech'
        }

BEG = '''
<!DOCTYPE html>
<html>
<head>
    <title>Mauritian Blogs</title>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/3.1.0/css/flag-icon.min.css">
    <link href='https://fonts.googleapis.com/css?family=Ubuntu+Mono' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Indie+Flower' rel='stylesheet' type='text/css'>


    <link rel="stylesheet" type="text/css" href="ProtoTyp/prototyp.css">
    <link rel="stylesheet" type="text/css" href="font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
    <header>
        <div class="c">
            <p class="flag-icon flag-icon-mu flag-icon-squared"></p> MAURITIAN BLOGS <p class="flag-icon flag-icon-mu flag-icon-squared"></p>
        </div>
    </header>
    <div class="c">
        <div class="f">
            <a href="#">
                <div class="blog_type bgwhite cardsha2 c" title="">
                    {INFO}
                </div>
            </a>
        </div>
    </div>
    
    <div class="c">
        <div class="f">
            <a href="index.html">
                <div class="back programming bgwhite cardsha2 c">
                    <i class="fa fa-arrow-left"></i>&nbsp;back
                </div>
            </a>
        </div>
    </div>

    <div class="blogs">
'''

BLOG_ELEM = '''
        <div class="blog_elem bgwhite cardsha2 f">
            <div class="blog_img f">
                <img src="{ICON_LINK}">
            </div>
            <div class="blog_info f">
                <a href="{BLOG_LINK}" target="_blank">
                    <div class="blog_visit bggreen3 c">
                        visit
                    </div>
                </a>
                <div class="blog_descrip">
                    {BLOG_DESCRIP}
                </div>
            </div><br>
            <div class="f">
                <div class="blog_name">
                    {BLOG_NAME}
                </div>
            </div>
        </div>
        
'''
            
END = '''
    </div>

</body>
</html>
'''

def build_all():
    for category in CATEGORIES:
        with open(category+'.html', 'w+') as FILE:
            print('crunching',category)
            FILE.write(BEG.format(INFO=CATEGORIES[category]))
            json_file = open('data/'+category+'.json', 'r').read()
            BLOGS = json.loads(json_file)
            for blog in BLOGS['blogs']:
                name = descrip = icon = ''
                
                if blog['name'] == '':
                    name = 'name unavailable'
                elif len(blog['name']) <= 5:
                    name = blog['name'] + '&nbsp;'*5
                else:
                    name = blog['name']
                
                if blog['description'] == '':
                    descrip = 'description unavailable'
                else:
                    descrip = blog['description']
                    
                if blog['icon link'] == '':
                    icon = 'https://image.flaticon.com/icons/svg/204/204322.svg'
                    #icon = 'https://image.flaticon.com/icons/svg/291/291542.svg'
                else:
                    icon = blog['icon link']
                FILE.write( BLOG_ELEM.format(BLOG_NAME=name,
                                             BLOG_DESCRIP=descrip,
                                             BLOG_LINK=blog['blog link'],
                                             ICON_LINK=icon
                                            ) )
            FILE.write(END)

def build(category):
    with open(category+'.html', 'w+') as FILE:
        print('crunching',category)
        FILE.write(BEG.format(INFO=CATEGORIES[category]))
        json_file = open('data/'+category+'.json', 'r').read()
        BLOGS = json.loads(json_file)
        for blog in BLOGS['blogs']:
            name = descrip = icon = ''
            
            if blog['name'] == '':
                name = 'name unavailable'
            elif len(blog['name']) <= 5:
                name = blog['name'] + '&nbsp;'*5
            else:
                name = blog['name']
            
            if blog['description'] == '':
                descrip = 'description unavailable'
            else:
                descrip = blog['description']
                
            if blog['icon link'] == '':
                icon = 'https://image.flaticon.com/icons/svg/204/204322.svg'
                #icon = 'https://image.flaticon.com/icons/svg/291/291542.svg'
            else:
                icon = blog['icon link']
            FILE.write( BLOG_ELEM.format(BLOG_NAME=name,
                                         BLOG_DESCRIP=descrip,
                                         BLOG_LINK=blog['blog link'],
                                         ICON_LINK=icon
                                        ) )
        FILE.write(END)

repl_on = 1

help_message = '''   COMMANDS 
build all : builds whole website
build <category> : builds only one page
exit : exit program
'''

while(repl_on):
    In = input('>>> ')
    words = In.split()
    if words[0] == 'build':
        if words[1] == 'all':
            build_all()
            #print('would build all')
        else :
            if words[1] in CATEGORIES:
                build(words[1])
                #print('would build', words[1])
            else:
                print('unknown category, build aborted')
    elif words[0] == 'help':
        print(help_message)
    elif words[0] == 'exit':
        repl_on = 0
    else:
        print('unrecognised command, type help for more info')