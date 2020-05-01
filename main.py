#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import time
import datetime
import pickle
import requests
import random
import os


def notification(param, key='', action='changed'):
	# Define your own notification.
	# Get notification of warnings and status
	# If return False, then stop the submit process
	return True


if __name__ == '__main__':

	# load config

	try:
		f = open('account.txt')
	except:
		print('account.txt not found!')
		time.sleep(3)
		exit()

	username = f.readline().strip()
	password = f.readline().strip()
	location = f.readline().strip()
	f.close()
	if location == '':
		print('【生成地址】没有指定地址，正在生成随机地址…')
		lng = 116.397499 + random.random() / 10.0 - 0.05
		lat = 39.908722 + random.random() / 10.0 - 0.05
		coordination = str(lng) + ',' + str(lat)
		PARAMS = {
			'key': '729923f88542d91590470f613adb27b5',
			's': 'rsv3',
			'location': coordination
		}
		r = requests.get(url='https://restapi.amap.com/v3/geocode/regeo', params=PARAMS)
		f = open('account.txt', "w")
		location = r.json()
		location['lng'] = lng
		location['lat'] = lat
		f.write(username + '\n' + password + '\n' + json.dumps(location, ensure_ascii=False))
		f.close()
		try:
			print(r.json()['regeocode']['formatted_address'])
			print('10 秒钟后继续')
			time.sleep(10)
		except:
			print('生成地址时遇到问题')
			exit('程序已经中断')
	else:
		location = json.loads(location)
		lng = location['lng']
		lat = location['lat']
		print('【使用地址】' + location['regeocode']['formatted_address'])

	# init
	s = requests.session()
	headers = {}
	log = open('log.txt', 'a')
	curr_time = datetime.datetime.now()

	try:
		with open('cookie.txt', 'rb') as f:
			s.cookies.update(pickle.load(f))
	except:
		print('cookie.txt not found!')
		# login
		data = {'username': username, 'password': password}
		r = s.post('https://itsapp.bjut.edu.cn/uc/wap/login/check',
		           data=data, headers=headers)
		tmp = '【登录】' + r.json()['m']
		print(tmp)
		log.write('\n' + curr_time.strftime('%Y-%m-%d-%H:%M:%S') + tmp)
		if not '成功' in r.text:
			time.sleep(3)
			exit()
		with open('cookie.txt', 'wb') as f:
			pickle.dump(s.cookies, f)

	# previous data
	r = s.get('https://itsapp.bjut.edu.cn/ncov/wap/default')
	default = r.text[r.text.find('var def = ') + 10:]
	default = json.loads(default[:default.find(';')])
	oldInfo = r.text[r.text.find('oldInfo: ') + 9:]
	oldInfo = json.loads(oldInfo[:oldInfo.find(',\n')])

	# report
	data = {
		'ismoved': '0',
		'dqjzzt': '1',  # 当前居住状态，0在校、1在京不在校
		'jhfjrq': '',  # 计划返京日期
		'jhfjjtgj': '',  # 计划返京交通工具
		'jhfjhbcc': '',  # 计划返京航班车次
		'tw': str(random.randint(2, 3)),  # 体温范围所对应的页面上的序号（下标从 1 开始）
		'sfcxtz': '0',  # 今日是否出现发热、乏力、干咳、呼吸困难等症状？
		'sfjcbh': '0',  # 今日是否接触疑似/确诊人群？
		'sfcxzysx': '0',  # 是否有任何与疫情相关的注意事项？
		'qksm': '',  # 情况说明
		'sfyyjc': '0',  # 是否医院检查
		'jcjgqr': '0',  # 检查结果确认
		'remark': '',
		'address': location['regeocode']['formatted_address'],
		'geo_api_info': json.dumps({
			'type': 'complete',
			'info': 'SUCCESS',
			'status': 1,
			'position': {
				'O': lng,
				'P': lat,
				'lng': lng,
				'lat': lat
			},
			'message': 'Get geolocation success.Convert Success.Get address success.',
			'location_type': 'html5',
			'accuracy': 65,
			'isConverted': True,
			'addressComponent': location['regeocode']['addressComponent'],
			'formatted_address': location['regeocode']['formatted_address'],
			'roads': [],
			'crosses': [],
			'pois': [],
		}, ensure_ascii=False),
		'area': '北京市  ' + location['regeocode']['addressComponent']['district'],
		'province': '北京市',
		'city': '北京市',
		'sfzx': '0',  # 是否已经返校
		'sfjcwhry': '0',  # 是否接触武汉人员
		'sfjchbry': '0',  # 是否接触湖北人员
		'sfcyglq': '0',  # 是否处于隔离期
		'gllx': '',  # 隔离类型
		'glksrq': '',  # 隔离开始日期
		'jcbhlx': '',  # 接触病患类型
		'jcbhrq': '',  # 接触病患日期
		'bztcyy': '',  # 当前地点与上次不在同一城市，原因如下：2 探亲, 3 旅游, 4 回家, 1 其他
		'sftjhb': '0',  # 是否停经湖北
		'sftjwh': '0',  # 是否停经武汉
		'sfsfbh': '0',  # 是否所在省份变化
		'xjzd': '',  # 现居住地
		'jcwhryfs': '',  # 接触武汉人员方式
		'jchbryfs': '',  # 接触湖北人员方式
		'szgj': '',  # 所在国家
		'jcjg': '',  # 检查结果
		# --- The following are uncommented field --- #
		'date': datetime.datetime.now().strftime('%Y%m%d'),
		# 'uid': '0',
		'created': int(time.time()),
		'jcqzrq': '',
		'sfjcqz': '',
		'szsqsfybl': 0,
		'sfsqhzjkk': 0,
		'sqhzjkkys': '',
		'sfygtjzzfj': 0,
		'gtjzzfjsj': '',
		'ljrq': '',
		'ljjtgj': '',
		'ljhbcc': '',
		'fjrq': '',
		'fjjtgj': '',
		'fjhbcc': '',
		'fjqszgj': '',
		'fjq_province': '',
		'fjq_city': '',
		'fjq_szdz': '',
		'jrfjjtgj': '',
		'jrfjhbcc': '',
		'fjyy': '',
		'szsqsfty': '',
		'sfxxxbb': '',
		'created_uid': 0,
		# 'id': 0,
		'gwszdd': '',
		'sfyqjzgc': '',
		'jrsfqzys': '',
		'jrsfqzfy': ''
	}

	go_on = True

	for key, value in default.items():
		if not data.__contains__(key):
			data[key] = value
			if key != 'id' and key != 'uid':
				warn = 'Warn: [' + key + '] New key'
				go_on = go_on and notification(warn, key, 'new')
				print(warn)

	for key, value in oldInfo.items():
		if data.__contains__(key):
			if data[key] != oldInfo[key] and key != 'geo_api_info' and key != 'tw' and key != 'date' \
					and key != 'created' and key != 'id':
				warn = 'Warn: [' + key + '] ' + str(oldInfo[key]) + ' -> ' + str(data[key])
				go_on = go_on and notification(warn, key, 'changed')
				print(warn)
		else:
			warn = 'Warn: [' + key + '] New key'
			go_on = go_on and notification(warn, key, 'new')
			print(warn)

	if go_on:
		r = s.post('https://itsapp.bjut.edu.cn/ncov/wap/default/save',
		           data=data, headers=headers)
		tmp = '【上报】' + json.loads(r.text)['m']
		print(tmp)
		log.write('\n' + curr_time.strftime('%Y-%m-%d-%H:%M:%S') + tmp)
		log.close()
		r.raise_for_status()
		if r.status_code != 200:
			err = 'Err: Login failed!'
			print(err)
			notification(err)
			os.remove('cookie.txt')

		if str(r.json()['e']) == '0':
			notification(r.json()['m'])
