# client.py
import asyncio
import websockets
import rclpy
from rclpy.node import Node
import eirabot_interfaces.msg as eim
import json

#This code is a work in progress
async def websocket_control():
        # connecting to sky 
        async with websockets.connect("ws://172.16.0.231:9005") as websocket:
            # send init handshake
            await websocket.send('{ "type":"handshake", "handshake":{ "client_id":"A091", "connection_id":"00000000-0000-0000-0000-000000000000", "role":"robot", "last_msg_id":0} }')
            while(True):
                # recieve messages
                message = await websocket.recv()
                print(message)
                
# node for robotmoto to communicate with SKY
class robo_sky_com(Node):
    def __init__(self):
        # initalise node
        super().__init__('robo_sky_com')
        # set up node
        asyncio.run(websocket_control())
        # set up subcribers for messages from robot for sky(ie from robomoto)
        self.batterysub=self.create_subscription(eim.BatteryStatus,'battery_stat',10)
        self.chargersub=self.create_subscription(eim.ChargerStatus,'charger_stat',10)
        self.manoeuvresub=self.create_subscription(eim.ManoeuvreExec,'manoeuvre_exec',10)
        self.positionsub=self.create_subscription(eim.Position,'position_json',10)
        self.manoeuvresub=self.create_subscription(eim.Status,'status',10)
        self.manoeuvresub=self.create_subscription(eim.SafetyStatus,'safety_stat',10)
        self.manoeuvresub=self.create_subscription(eim.TableStatus,'table_stat',10)
            
def main(args=None):
    rclpy.init(args=args)
    robo_to_sky= robo_sky_com()
    rclpy.spin(robo_to_sky)

    # Destroy the node explicitly
    robo_to_sky.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
