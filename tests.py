
import pandas as pd,numpy as np,os
'''---------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------'''
global state,model,model_range,alpha_nums
state=['IDLE','LOADING','LOADED','DELIVERING','DELIVERED','RETURNING' ]
model=['Lightweight','Middleweight','Cruiserweight','Heavyweight']
model_range=['0g-125g','125g-250g','250g-375g','375g-500g']
alpha_nums=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

D=pd.DataFrame
'''---------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------'''
global nr;
nr=np.random.randint
def __ID__(n):return ''.join([alpha_nums[nr(len(alpha_nums))] for _ in np.arange(n)])    
'''---------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------'''
def weight(x):
    '''0:'Lightweight',1:'Middleweight',2:'Cruiserweight',3:'Heavyweight']'''
    a={0:nr(0,125+1),1:nr(125,250+1),2:nr(250,375+1),3:nr(375,500+1)}
    return a[x]

def generate_drones(n):
    list_drons=[]
    for i in np.arange(len(list_drons)+1,len(list_drons)+n+1):
        xn=nr(len(model))
        w=weight(xn)
        s=state[nr(len(state))]
        list_meds=[]
        b=nr(100)
        if s not in ['IDLE','RETURNING','DELIVERED'] and b>=25:list_meds=generate_medicine(w)
                
        list_drons.append([i,__ID__(100),model[xn],model_range[xn],w,b,s,list_meds])
    print(list_drons)
    '''---------------------------------------------------------------------------'''
    '''---------------------------------------------------------------------------'''
    '''---------------------------------------------------------------------------'''
    '''if os.path.exists('almacen.csv'):os.remove("almacen.csv")'''
    
    df =D(list_drons,columns=['id','serial_number', 'model', 'model_range','weight_limit','battery_capacity','state','box'])    
    
    print(df)
    import json
    json_list = {'list':list(df.T.to_dict().values())}
    'json_list = json.loads(json.dumps(list(df.T.to_dict().values())))'
    print(json_list)
    open('drones.json', 'w').write(str(json_list))
    

'generate_drones(10)'


def add_auto_generate_drones(n):
    data = open('drones.json', 'r').read()
    import ast
    data=ast.literal_eval(data)
    print(type (data) )
    D=pd.DataFrame
    list_drons=list(D(data['list']).values)
   
    for i in np.arange(len(list_drons)+1,len(list_drons)+n+1):
        xn=nr(len(model))
        w=weight(xn)
        s=state[nr(len(state))]
        list_meds=[]
        b=nr(100)
        if s not in ['IDLE','RETURNING','DELIVERED'] and b>=25:list_meds=generate_medicine(w)
                
        list_drons.append([i,__ID__(100),model[xn],model_range[xn],w,b,s,list_meds])
    print(list_drons)
    '''---------------------------------------------------------------------------'''
    '''---------------------------------------------------------------------------'''
    '''---------------------------------------------------------------------------'''
    '''if os.path.exists('almacen.csv'):os.remove("almacen.csv")'''
    
    df =D(list_drons,columns=['id','serial_number', 'model', 'model_range','weight_limit','battery_capacity','state','box'])    
    
    print(df)
    import json
    json_list = {'list':list(df.T.to_dict().values())}
    'json_list = json.loads(json.dumps(list(df.T.to_dict().values())))'
    print(json_list)
    open('drones.json', 'w').write(str(json_list))



meds_names=['paracetamol','omeprazol','salbutamol','aspirina',
            'metformina','naproxeno','captopril',
            'loratadina','ibuprofeno','ambroxol']


def generate_medicine(weight):
    list_meds=[]
    med_weight=0
    i=1
    while 1:
        med_weight=nr(5,100)
        if weight < med_weight:break
        weight -= med_weight
        xn=nr(len(meds_names))
        list_meds.append([i,meds_names[xn],__ID__(30),med_weight])
        i+=1
    print(list_meds)
    if(len(list_meds)==0):return list_meds
    
    df =D(list_meds,columns=['id','medicine', 'code', 'weight'])
    
    print(df)

    return list(df.T.to_dict().values())
    

y=generate_medicine(300)
print(y)

