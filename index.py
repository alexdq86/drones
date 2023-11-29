'''
                            author:Alexander D. Q.
                            email:alexdiazq86@gmail.com
                            phone:+5358051818
'''
import json,ast,tests
from flask import Flask, request, jsonify
from threading import Thread as T
global file,df
import pandas as pd,numpy as np
D=pd.DataFrame
nr=np.random.randint
file='drones.json'


app = Flask(__name__)
'http://127.0.0.1:5000'
def load_data():
    data = open(file, 'r').read()
    print(type (data) )
    data=ast.literal_eval(data)
    print(type (data) )
    data=data['list']
    print(data)
    return data


        
@app.route('/', methods=['POST'])
def create_record():
    info = json.loads(request.data)
    '///////////////////////////////////////////////////////////////////////////////////'
    '                              AUTO-CREATED DRONES                                  '
    '///////////////////////////////////////////////////////////////////////////////////'
    '{ "type":"generate_DRONES","n":15}<---------CREATE NEW DRONES STORAGE'
    if info['type']=='generate_DRONES':
        open(file, 'w').write(str({'list':[]}))
        tests.generate_drones(info['n'])
        return jsonify(load_data())
    '{ "type":"autogenerate_DRONES","n":3}<------ADD AUTO-CREATED DRONES'
    if info['type']=='autogenerate_DRONES':
        tests.add_auto_generate_drones(info['n'])
        return jsonify(load_data())
    '///////////////////////////////////////////////////////////////////////////////////'
    '                            SHOW DRONE(S)                                          '
    '///////////////////////////////////////////////////////////////////////////////////'
    '{"type":"show_one","id":8}'
    if info['type']=='show_one':
        df=D(load_data());df=df[df['id']==info['id']]
        return jsonify(df.to_dict(orient='records'))
    '{"type":"show_some","ids":[3,5,9]}'
    if info['type']=='show_some':
        df=D(load_data());df=df[df['id'].isin(info['ids'])]
        return jsonify(df.to_dict(orient='records'))    
    '{ "type":"show_all" }'
    if info['type']=='show_all':return jsonify(load_data())
    '///////////////////////////////////////////////////////////////////////////////////'
    '                            ADD DRONES                                             '
    '///////////////////////////////////////////////////////////////////////////////////'
    '''
    { 
    "type":"add",
    "drone":{ "serial_number":"A1042031CCC31A81B8DBB2D7BA6AA6AB1170916F6149717AC95BB41A4BBE425C1C2104E524B6ED18B5160C0734B5BCDAD2F8", "model":"Heavyweight", "model_range": "375g-500g", "weight_limit": 433,
    "battery_capacity": 65, "state": "IDLE"}
    }
    '''
    if info['type']=='add':
        df=D(load_data());d=info['drone'];idd=1
        if len(df.index)>0:idd=df.id.max()+1
        d['id']=idd;print(d);df = pd.concat([df, D([d])],ignore_index=True)
        open(file, 'w').write(str({'list':df.to_dict(orient='records')}))
        return jsonify(load_data())
    '''
    {
    "type":"add_some",
    "drones":[{ "serial_number":"A1042031CCC31A81B8DBB2D7BA6AA6AB1170916F6149717AC95BB41A4BBE425C1C2104E524B6ED18B5160C0734B5BCDAD2F8", "model":"Heavyweight", "model_range": "375g-500g", "weight_limit": 433,
    "battery_capacity": 65, "state": "IDLE","box":[]},
    { "serial_number":"B1042031CCC31A81B8DBB2D7BA6AA6AB1170916F6149717AC95BB41A4BBE425C1C2104E524B6ED18B5160C0734B5BCDAD2F8", "model":"Heavyweight", "model_range": "375g-500g", "weight_limit": 433,
    "battery_capacity": 52, "state": "RETURNING","box":[]},
    { "serial_number":"C1042031CCC31A81B8DBB2D7BA6AA6AB1170916F6149717AC95BB41A4BBE425C1C2104E524B6ED18B5160C0734B5BCDAD2F8", "model":"Heavyweight", "model_range": "375g-500g", "weight_limit": 433,
    "battery_capacity": 61, "state": "IDLE","box":[]}]
    }
    '''
    if info['type']=='add_some':
        df_2=D(info['drones'])
        df=D(load_data());idd=1
        if len(df.index)>0:idd=df.id.max()+1
        df_2['id']=list(range(idd,idd+len(df_2.index)))
        df = pd.concat([df, df_2],ignore_index=True)
        open(file, 'w').write(str({'list':df.to_dict(orient='records')}))
        return jsonify(load_data())
    '///////////////////////////////////////////////////////////////////////////////////'
    '                             SHOW BATTERY                                          '
    '///////////////////////////////////////////////////////////////////////////////////'
    '{"type":"check_batery_one","id":8}'
    if info['type']=='check_batery_one':
        df=D(load_data());df=df[df['id']==info['id']][['id', 'battery_capacity']]
        return jsonify(df.to_dict(orient='records'))
    '{"type":"show_some_battery","ids":[3,5,9]}'
    if info['type']=='show_some_battery':
        df=D(load_data());df=df[df['id'].isin(info['ids'])][['id', 'battery_capacity']]
        return jsonify(df.to_dict(orient='records'))
    '{ "type":"show_all_battery" }'
    if info['type']=='show_all_battery':
        df=D(load_data());df=df[['id', 'battery_capacity']]
        return jsonify(df.to_dict(orient='records'))
    '///////////////////////////////////////////////////////////////////////////////////'
    '                             DELETE DRONES                                         '
    '///////////////////////////////////////////////////////////////////////////////////'
    '{ "type":"delete_one","id":4 }'
    if info['type']=='delete_one':
        df=D(load_data());df=df[df['id']!=info['id']]
        open(file, 'w').write(str({'list':df.to_dict(orient='records')}))
        return jsonify(load_data())
    '{"type":"delete_some","ids":[3,5,9]}'
    if info['type']=='delete_some':
        df=D(load_data());df=df[~df['id'].isin(info['ids'])]
        open(file, 'w').write(str({'list':df.to_dict(orient='records')}))
        return jsonify(load_data())
    '{ "type":"delete_all"}'
    if info['type']=='delete_all':
        open(file, 'w').write(str({'list':[]}))
        return jsonify(load_data())
    '///////////////////////////////////////////////////////////////////////////////////'
    '                             CHANGE BATTERY                                        '
    '///////////////////////////////////////////////////////////////////////////////////'
    '{"type":"change_battery","id":1,"battery":50}'
    if info['type']=='change_battery':
        df=D(load_data());df.loc[df['id']==info['id'], 'battery_capacity'] = info['battery']
        open(file, 'w').write(str({'list':df.to_dict(orient='records')}));return jsonify(load_data())
    '{"type":"change_some_battery","ids":[2,5,7],"batteries":[20,50,30]}'
    if info['type']=='change_some_battery':
        df=D(load_data());df.loc[df['id'].isin(info['ids']), 'battery_capacity'] = info['batteries']
        open(file, 'w').write(str({'list':df.to_dict(orient='records')}));return jsonify(load_data())
    '{"type":"change_all_battery_to_full"}'
    if info['type']=='change_all_battery_to_full':
        df=D(load_data());df['battery_capacity'] = 100
        open(file, 'w').write(str({'list':df.to_dict(orient='records')}));return jsonify(load_data())
    '{"type":"change_ramdon_all_battery"}'
    if info['type']=='change_ramdon_all_battery':
        df=D(load_data());df['battery_capacity'] = [nr(100+1) for _ in np.arange(len(df.index))]
        open(file, 'w').write(str({'list':df.to_dict(orient='records')}));return jsonify(load_data())
    
    '///////////////////////////////////////////////////////////////////////////////////'
    '                                SHOW MEDICINE                                      '
    '///////////////////////////////////////////////////////////////////////////////////'
    '{"type":"check_medicine_one","id":8}'
    if info['type']=='check_medicine_one':
        df=D(load_data());df=df[df['id']==info['id']][['id', 'box']]
        return jsonify(df.to_dict(orient='records'))
    '{"type":"show_some_medicine","ids":[3,5,9]}'
    if info['type']=='show_some_medicine':
        df=D(load_data());df=df[df['id'].isin(info['ids'])][['id', 'box']]
        return jsonify(df.to_dict(orient='records'))
    '{ "type":"show_all_medicine" }'
    if info['type']=='show_all_medicine':
        df=D(load_data());df=df[['id', 'box']]
        return jsonify(df.to_dict(orient='records'))
    '///////////////////////////////////////////////////////////////////////////////////'
    '                                ADD MEDICINE PACK TO DRONE(s)                      '
    '///////////////////////////////////////////////////////////////////////////////////'
    '''
    {
    "type":"add_medicine_one",
    "id":12,
    "medicine": [
            {
                "code": "26C904F9340E89E5B7052812BCF8E5",
                "medicine": "metformina",
                "weight": 67
            },
            {
                "code": "54E671C29AA3A44B1DD3FBC95AB8B7",
                "medicine": "paracetamol",
                "weight": 36
            },
            {
                "code": "A2A2BCB8C8DEDA4536EF4A0A0C34E2",
                "medicine": "captopril",
                "weight": 53
            }
        ]
    }
    '''
    def process_med(df,item):
        meds=D(item['medicine'])
        flag=False
            
        print(len(df.loc[df['id']==item['id'], 'box'].values[0]))
        if len(df.loc[df['id']==item['id'], 'box'].values[0])==0:
            flag=True
        else:
            meds_box=D(D(df.loc[df['id']==item['id'], 'box']).values[0][0])
            if float(df.loc[df['id']==item['id'], 'weight_limit'])>=meds.weight.sum()+meds_box.weight.sum():
                flag=True
        if flag:
            idd=1
            if len(df.loc[df['id']==item['id'], 'box'].values[0])>0:
                idd=D(D(df.loc[df['id']==item['id'], 'box']).values[0][0]).id.max()+1
            meds['id']=list(range(idd,len(meds.index)+idd))
            df.loc[df['id']==item['id'], 'box'].values[0]+=meds.to_dict(orient='records')
            df.loc[df['id']==item['id'], 'state']='LOADING'
    
    if info['type']=='add_medicine_one':
        df=D(load_data())
        process_med(df,info)      
        open(file, 'w').write(str({'list':df.to_dict(orient='records')}))
        return jsonify(load_data())
    """
        {
        "type":"add_medicine_some",
        "array_med_dron_ids":[{
        "id":12,
        "medicine": [
                {
                    "code": "26C904F9340E89E5B7052812BCF8E5",
                    "medicine": "metformina",
                    "weight": 67
                },
                {
                    "code": "54E671C29AA3A44B1DD3FBC95AB8B7",
                    "medicine": "paracetamol",
                    "weight": 36
                },
                {
                    "code": "A2A2BCB8C8DEDA4536EF4A0A0C34E2",
                    "medicine": "captopril",
                    "weight": 53
                }
            ]
        },
        {
        "id":11,
        "medicine": [
                {
                    "code": "30C904F9340E89E5B7052812BCF8E5",
                    "medicine": "metformina",
                    "weight": 20
                },
                {
                    "code": "78E671C29AA3A44B1DD3FBC95AB8B7",
                    "medicine": "paracetamol",
                    "weight": 12
                }]
        },
        {
        "id":10,
        "medicine": [
                {
                    "code": "30C904F9340E89E5B7052812BCF8E5",
                    "medicine": "metformina",
                    "weight": 40
                }]
        }]
        }
    """
    
        
    if info['type']=='add_medicine_some':
        df=D(load_data())
        for item in info['array_med_dron_ids']:
            'PARALLEL PROCESS'
            t=T(target=process_med, args=(df,item))
            t.start()
            t.join()
        open(file, 'w').write(str({'list':df.to_dict(orient='records')}))
        return jsonify(load_data())
    '///////////////////////////////////////////////////////////////////////////////////'
    '                   CHECK AVAILABLE DRONE(S) FOR MEDICINE PACKAGE(S)                '
    '///////////////////////////////////////////////////////////////////////////////////'
    '''
    {
    "type":"check_one_drone_for_package",
    "medicine": [
            {
                "code": "26C904F9340E89E5B7052812BCF8E5",
                "medicine": "metformina",
                "weight": 67
            },
            {
                "code": "54E671C29AA3A44B1DD3FBC95AB8B7",
                "medicine": "paracetamol",
                "weight": 36
            },
            {
                "code": "A2A2BCB8C8DEDA4536EF4A0A0C34E2",
                "medicine": "captopril",
                "weight": 53
            }
        ]
    }
    '''
    
    def check_dron_pack(df,info):
        meds=D(info)
        meds_weight=meds.weight.sum()
        df=df[['id','weight_limit','box']]
        print(df)
        def length_(xd):return len(xd.box)
        df['box_length']=df.apply(lambda x:length_(x),axis=1)
        print(df)
        def sum_w(xd):
            if xd.box_length==0:return 0
            g=D(xd.box);return g.weight.sum()
        df['box_weight']=df.apply(lambda x:sum_w(x),axis=1)
        print(df)
        df['weight_limit_box_meds']=df.weight_limit-df.box_weight-meds_weight
        print(df)
        df=df[df.weight_limit_box_meds>=0]
        print(df)
        return list(df.id.values)
        
    if info['type']=='check_one_drone_for_package':
        df=D(load_data())
        ids_list=check_dron_pack(df,info['medicine'])
        return jsonify(str({'drone_ids':ids_list}))

    """
        {
        "type":"check_some_drones_for_packages",
        "array_meds_drons":[
        [
                {
                    "code": "26C904F9340E89E5B7052812BCF8E5",
                    "medicine": "metformina",
                    "weight": 67
                },
                {
                    "code": "54E671C29AA3A44B1DD3FBC95AB8B7",
                    "medicine": "paracetamol",
                    "weight": 36
                },
                {
                    "code": "A2A2BCB8C8DEDA4536EF4A0A0C34E2",
                    "medicine": "captopril",
                    "weight": 53
                }
            ],
            [
                {
                    "code": "30C904F9340E89E5B7052812BCF8E5",
                    "medicine": "metformina",
                    "weight": 20
                },
                {
                    "code": "78E671C29AA3A44B1DD3FBC95AB8B7",
                    "medicine": "paracetamol",
                    "weight": 12
                }],
                 [
                {
                    "code": "30C904F9340E89E5B7052812BCF8E5",
                    "medicine": "metformina",
                    "weight": 40
                }]
            ]
        }
    """
    if info['type']=='check_some_drones_for_packages':
        df=D(load_data())
        aux={}
        for i,item in enumerate(info['array_meds_drons']):
            aux[i]=check_dron_pack(df,item)
        return jsonify(str({'packs_pos__drone_ids':aux}))
            
        
        
    
    
    return jsonify('Not Found!!')

app.run()
