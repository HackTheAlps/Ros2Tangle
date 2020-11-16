import rospy
import requests
import json
import time
from rospy_message_converter import json_message_converter
from std_msgs.msg import String

class DataPublisher(object):
    def __init__(self, url, device_id):
        self.url = url
        self.device_id = device_id

    def send_message_to_tangle(self, sensor_key, msg):
        try:
            rosMsgJson = json_message_converter.convert_ros_message_to_json(msg)
            rosMsgDict = json.loads(rosMsgJson)

            iot2tangle = [ {'sensor': sensor_key, 'data': [rosMsgDict]}]
            
            myobj = {'device': self.device_id, 'timestamp': int(time.time()), 'iot2tangle': iot2tangle}
            headers = {'Content-Type': 'application/json'}
            jsonobj = json.dumps(myobj, indent=4)
            x = requests.post(self.url, headers= headers, data = jsonobj)

            rospy.loginfo('Sent message of sensor ' + sensor_key + ' to tangle: ' + jsonobj)
        except Exception as e:
            rospy.logerr('Sending the message of sensor ' + sensor_key + ' to the tangle failed. ' + str(e))
