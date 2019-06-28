c={
    'a':{
        'a1':{
            'a11','a12'
        },
        'a2':{
            'a21','a22','a23'
        }
    },
    'b':{
        'b1':{
            'b11','b12','b13','b14'
        }
    }
}
d=input('select sheng')
if d in c.keys():
    while True:
        shi=input('select shi')
        shis=c[d].keys()
        if shi=='q':
            break
        elif shi in shis:
            for i in shis:
                if shi==i:
                    print(c[d][shi])