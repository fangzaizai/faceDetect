# -*- coding:utf-8 -*-
import websocket
import json

def send_face_data():
	ws = websocket.create_connection("ws://192.168.9.208:19101/FACE-DETECT-WS/websck")
	data={
	"type":"request",
	"id":"22222222222",
	"command":"send_face_events",
	"params":[
		{
			"face_refid":"ananananananaananan2",
			"event_refid":"anmeifang2",
			"event_dt":"2017-10-17T08:30:39.028",
			"pic_url":"http://192.168.9.208:7788//LINDASceneAlarm/20171017/16/{DF452E44-B458-446D-9273-35472618DE73}-20171017164149674-00.jpg",
			"accord_event_refid":"DF452E44-B458-446D-9273-35472618DE73}-20171011160011826",
			"accord_similarity":90,
			"camera_refid":"0557fc08-565d-449d-82b9-22ad08e6bc54",
			"sex":"1",
			"age":29,
		}],
	}
	ws.send(json.dumps(data))
	result = ws.recv()
	print result
	ws.close()

if __name__ == '__main__':
	send_face_data()