author:Alexander D. Q.
email:alexdiazq86@gmail.com
phone:+5358051818
////////////////////////////////////////////
              install:
/////////////////////////////////////////////
get installed "postman.exe" for doing tests in json
get installed python
-pip install Flask
-pip install pandas
/////////////////////////////////////////////
run index.py with F5
run server in http://127.0.0.1:5000/
///////////////////////////////////////////////////
------>drones.json is the file of storage

//////////////////json commnads/////////////////////////////
        JSON COMMANDS:(test in postman for instance)
///////////////////////////////////////////////
'///////////////////////////////////////////////////////'
'              AUTO-CREATED DRONES                      '
'///////////////////////////////////////////////////////'

///////////create 15 drones with ramdon pack of medicine////////////////
{ "type":"generate_DRONES","n":15}

///////////add 3 drones with ramdon pack of medicine////////////////
{ "type":"autogenerate_DRONES","n":3}

'///////////////////////////////////////////////////////'
'              SHOW DRONE(S) INFO                       '
'///////////////////////////////////////////////////////'
///////////show  drone with id=8////////////////
{"type":"show_one","id":8}

///////////show  drones with ids in [3,5,9]////////////////
{"type":"show_some","ids":[3,5,9]}

///////////show all drones////////////////
{ "type":"show_all" }


'///////////////////////////////////////////////////////'
'                      ADD DRONE(S)                       '
'///////////////////////////////////////////////////////'
///////////add one drone////////////////
{ 
    "type":"add",
    "drone":{ "serial_number":"A1042031CCC31A81B8DBB2D7BA6AA6AB1170916F6149717AC95BB41A4BBE425C1C2104E524B6ED18B5160C0734B5BCDAD2F8", "model":"Heavyweight", "model_range": "375g-500g", "weight_limit": 433,
    "battery_capacity": 65, "state": "IDLE"}
}


///////////add many drones////////////////
{
    "type":"add_some",
    "drones":[{ "serial_number":"A1042031CCC31A81B8DBB2D7BA6AA6AB1170916F6149717AC95BB41A4BBE425C1C2104E524B6ED18B5160C0734B5BCDAD2F8", "model":"Heavyweight", "model_range": "375g-500g", "weight_limit": 433,
    "battery_capacity": 65, "state": "IDLE","box":[]},
    { "serial_number":"B1042031CCC31A81B8DBB2D7BA6AA6AB1170916F6149717AC95BB41A4BBE425C1C2104E524B6ED18B5160C0734B5BCDAD2F8", "model":"Heavyweight", "model_range": "375g-500g", "weight_limit": 433,
    "battery_capacity": 52, "state": "RETURNING","box":[]},
    { "serial_number":"C1042031CCC31A81B8DBB2D7BA6AA6AB1170916F6149717AC95BB41A4BBE425C1C2104E524B6ED18B5160C0734B5BCDAD2F8", "model":"Heavyweight", "model_range": "375g-500g", "weight_limit": 433,
    "battery_capacity": 61, "state": "IDLE","box":[]}]
 }
'///////////////////////////////////////////////////////'
'                      SHOW BATTERY PERCENT             '
'///////////////////////////////////////////////////////'

///////////check batery of one drone with id=8////////////////
 {"type":"check_batery_one","id":8}

///check some bateries of many drones with ids in [3,5,9]/////
 {"type":"show_some_battery","ids":[3,5,9]}

///////////check bateries of all drones////////////////
 { "type":"show_all_battery" }


'///////////////////////////////////////////////////////'
'                      DELETE DRONES                    '
'///////////////////////////////////////////////////////'
///////////delete drone of id=4////////////////
 { "type":"delete_one","id":4 }

///////delete drones with ids in [3,5,9]/////////
 {"type":"delete_some","ids":[3,5,9]}

/////////delete all drones/////////////
 { "type":"delete_all"}


'///////////////////////////////////////////////////////'
'                      CHANGE BATTERY                   '
'///////////////////////////////////////////////////////'
/////////assign 50% of battery to drone with id=1/////////////
 {"type":"change_battery","id":1,"battery":50}

/////assign 20%,50%,30% of battery to drones with ids in [2,5,7]/////
 {"type":"change_some_battery","ids":[2,5,7],"batteries":[20,50,30]}

/////////put all dornes'batteries in 100% /////////////
 {"type":"change_all_battery_to_full"}

/////////assign ramdon battery percent to all drones/////////////
 {"type":"change_ramdon_all_battery"}


'///////////////////////////////////////////////////////'
'                      SHOW MEDICINE                    '
'///////////////////////////////////////////////////////'
////////////show the medicine's pack of drone with id=8///////
 {"type":"check_medicine_one","id":8}


////////////show the medicine's pack of drone with id in [3,5,9]///////
 {"type":"show_some_medicine","ids":[3,5,9]}


////////show medicine's pack of all drones///////
 { "type":"show_all_medicine" }

'///////////////////////////////////////////////////////'
'                 ADD MEDICINE PACK TO DRONE(s)         '
'///////////////////////////////////////////////////////'
////////add medicine's pack to drone with id=12/////// 
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

////////add medicine's packs to drones with ids in=[12,11,10]///////
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

'///////////////////////////////////////////////////////'
'   CHECK AVAILABLE DRONE(S) FOR MEDICINE PACKAGE(S)    '
'///////////////////////////////////////////////////////'
////////check all available drones for one package///////
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

////////check all available drones for many packages///////
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


/////////////THAT'S ALL FOR KNOW ..... THANKS!!!//////////////////






