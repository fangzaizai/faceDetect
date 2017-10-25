# -*- coding:utf-8 -*-
import websocket
import json
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, url_for,session
from flask_bootstrap import Bootstrap
from forms import SendForm

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
@app.route('/send_face_data', methods=['GET', 'POST'])
def send_face_data():
	form = SendForm()
	ws = websocket.create_connection("ws://192.168.9.208:19101/FACE-DETECT-WS/websck")
	#init parameter
	face_unid_unique=int(1)
	face_refid_unique=int(1)
	event_refid=int(1)
	#get times
	#start sending
	time=session.get('time')
	print time
	print type(time)
	for i in range(1,int(time)):
		data={
		"type":"request",
		"id":face_unid_unique,
		"command":"send_face_events",
		"params":[
			{
				"face_refid":face_refid_unique,
				"event_refid":event_refid,
				"event_dt":'2017-10-17T08:30:39.028',
				#"pic_url":"http://192.168.9.208:7788//LINDASceneAlarm/20171017/16/" + str(picname+1) + ".jpg",
				"pic_url":"http://192.168.9.208:7788//LINDASceneAlarm/20171017/16/{DF452E44-B458-446D-9273-35472618DE73}-20171017164149674-00.jpg",
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
	return render_template('index.html', form=form)

#except socket.error

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
	form = SendForm()
	print 'hello'
	if form.validate_on_submit():
		print 'submit'
		session['time']=form.time.data
		return redirect(url_for('send_face_data'))
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)