#!/usr/bin/env python3

s_queue_item = {
    'is_terminal':True,
    'prob':0.001,
    'parse_tree':
        [
            0,0,
            [
                [
                    1,0,
                    [
                        4,1
                    ]
                ],
                [
                    3,1
                ]
            ]
        ]
    }


s_preterminal = [
    0,0,
        [
            [
                1,0,
                [
                    [
                        4,1,[]
                    ]
                ]
            ],
            [
                3,1,[]
            ]
        ]
    ]

    
    
s_grammar = [
    {
        'name':'S',
        'replacements':[
            {
                'is_terminal':False,
                'pos':[1,3],
                'prob':0.5,
                'function':'transparent'
            },
            {
                'is_terminal':False,
                'pos':[2],
                'prob':0.30,
                'function':'transparent'
            },
            {
                'is_terminal':False,
                'pos':[2,3],
                'prob':0.20,
                'function':'transparent'
            }
        ]
    },
    {
        'name':"L3",
        'replacements':[
            {
                'is_terminal':False,
                'pos':[4],
                'prob':0.8,
                'pre_terminal':[
                    "pas",
                    "cat",
                    "dog",
                    "hat"
                ],
                'function':'shadow'
            },
            {
                'is_terminal':False,
                'pos':[4],
                'prob':0.2,
                'pre_terminal':[
                    "mat",
                    "bat"
                ],
                'function':'shadow'
            }
        ]
    },
    {
        'name':"L5",
        'replacements':[
            {
                'is_terminal':False,
                'pos':[5],
                'prob':0.7,
                'pre_terminal':[
                    "passw",
                    "secur"
                ],
                'function':'shadow'
            },
            {
                'is_terminal':False,
                'pos':[5],
                'prob':0.3,
                'pre_terminal':[
                    "chair",
                    "hairs"
                ],
                'function':'shadow'
            }
        ]
    },
    {
        'name':"D2",
        'replacements':[
            {
                'is_terminal':True,
                'prob':0.7,
                'terminal':[
                    '1',
                ],
                'function':'copy'
            },
            {
                'is_terminal':True,
                'prob':0.3,
                'terminal':[
                    '2',
                    '3',
                    '4'
                ],
                'function':'copy'
            }
        ]
    },
    {
        'name':'C3',
        'replacements':[
            {
                'is_terminal':True,
                'prob':0.8,
                'terminal':[
                    'LLL'
                ],
                'function':'capitalize'
            },
            {
                'is_terminal':True,
                'prob':0.20,
                'terminal':[
                    'ULL',
                    'UUU'
                ],
                'function':'capitalize'
            }
        ]
    },
    {
        'name':'C5',
        'replacements':[
            {
                'is_terminal':True,
                'prob':0.8,
                'terminal':[
                    'LLLLL'
                ],
                'function':'capitalize'
            },
            {
                'is_terminal':True,
                'prob':0.20,
                'terminal':[
                    'ULLLL',
                    'UUUUU'
                ],
                'function':'capitalize'
            }
        ]
    },
]
