# Sky control

This package is currently a work in progress. The idea behind this is to work as a middleman between sky websocket and ros2 on the robot. The websocket comunication protocol for robotmoto to sky is explained in the two PDF attached to the repo.

## Message formats

>:warning: Some of the PDF is out of date. The correct JSON formats that were found so far using Postman

### Handshake to send

client_id should be the robots namie ie A091
connection_id is "00000000-0000-0000-0000-000000000000" for brand new connection

```JSON
{ 
    "type":"handshake", 
    "handshake":{
        "client_id":"", 
        "connection_id":"00000000-0000-0000-0000-000000000000", 
        "role":"robot", 
        "last_msg_id":0
    } 
}
```

### Recieving Handshake

```JSON
{
    "type": "handshake",
    "handshake": {
        "connection_id": "",
        "last_msg_id": 0
    }
}
```

### Payload Example message

```JSON
{
    "type": "msg",
    "msg": {
        "id": 0,
        "payload": "batteryStatus",
        "batteryStatus": {
            "SoC": 89,
            "SoH": 92,
            "calibrationThreshold": "clear"
        }
    }
}
```

## Ros Diagrams

### High Level Diagram
