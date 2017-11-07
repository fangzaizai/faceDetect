# -*- coding:utf-8 -*-
import websocket
import json
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, url_for,session
from flask_bootstrap import Bootstrap
from forms import SendForm, SendBlack
import urllib
import urllib2

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'HEUFEWHQUIFHOEWFJA'
'''
@app.route('/send_data')
def send_face_dat1():
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
'''
#websocket protocol
@app.route('/send_face_data', methods=['GET', 'POST'])
def send_face_data():
	form = SendForm()
	ws = websocket.create_connection("ws://192.168.9.208:19101/FACE-DETECT-WS/websck")
	face_unid_unique=int(21234)
	face_refid_unique=int(25678)
	event_refid=int(21357)
	time=session.get('time')
	print time
	print type(time)
	for i in range(19999,19999+int(time)):
		data={
		"type":"request",
		"id":face_unid_unique,
		"command":"send_face_events",
		"params":[
			{
				"face_refid":face_refid_unique,
				"event_refid":"anmeifang",
				"event_dt":'2017-10-17T08:30:39.028',
				#"pic_url":"http://192.168.9.208:7788//LINDASceneAlarm/20171017/16/" + str(picname+1) + ".jpg",
				"pic_url":"http://192.168.9.208:7788//LINDASceneAlarm/20171017/16/"+ str(i) +".jpg",
				"accord_event_refid":"DF452E44-B458-446D-9273-35472618DE73}-20171011160011826",
				"accord_similarity":90,
				"camera_refid":"0557fc08-565d-449d-82b9-22ad08e6bc54",
				"sex":"1",
				"age":29,
			}],
		}
		try:
			ws.send(json.dumps(data))
			result = ws.recv()
			print result
		except socket.error, e:
			render_template('404.html')		
		face_unid_unique=face_unid_unique+1
		face_refid_unique=face_refid_unique+1
		event_refid=event_refid+1
	ws.close()
	print "send over"
	return render_template('index.html', form=form)

#except socket.error

@app.route('/add_black_face', methods=['GET', 'POST'])
def add_black_face():
	form = SendBlack()
	black_info={
	"refid": "1111",       # 可选，人脸的refid
    "name": "1111" ,      
    "is_crucial" : 1,       # 可选，人脸名称
    "crucial_type": "ny_black"
    }

	black = urllib.urlencode(black_info)

	headers={
    "authorization" : "6fd5eab0-4fbc-4ace-a54f-9eac09a03d09",
    "Content-Type" : "application/json"
    }
    #header = urllib.urlencode(header_info)
	
	request_path='http://192.168.9.208:20080/api/v1/face_web/faces'
	req=urllib2.Request(request_path, black, headers)
	response = urllib2.urlopen(req)
	print response.read()
	return render_template('index.html', form=form)



@app.route('/add_black_pic')
def add_black_pic():
	pass

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
	form = SendBlack()
	print 'hello'
	if form.validate_on_submit():
		print 'submit'
		session['time']=form.time.data
		return redirect(url_for('add_black_face'))
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)