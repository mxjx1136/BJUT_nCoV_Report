import json
import time

import requests

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

	# init
	s = requests.session()
	headers = {
	}

	# login
	data = {
		'username': username,
		'password': password
	}
	r = s.post('https://itsapp.bjut.edu.cn/uc/wap/login/check', data=data, headers=headers)
	print('【登录】' + json.loads(r.text)['m'])
	if not '成功' in r.text:
		time.sleep(3)
		exit()

	# report
	data = {
		'ismoved': '0',
		'jhfjrq': '',  # 计划返京日期
		'jhfjjtgj': '',  # 计划返京交通工具
		'jhfjhbcc': '',  # 计划返京航班车次
		'tw': '3',  # 体温范围所对应的页面上的序号（下标从 1 开始）
		'sfcxtz': '0',
		'sfjcbh': '0',
		'sfcxzysx': '0',
		'qksm': '',  # 情况说明
		'sfyyjc': '0',
		'jcjgqr': '0',
		'remark': '',
		'address': '中国',  # 地址
		'geo_api_info': {
			'type': 'complete',
			'info': 'SUCCESS',
			'status': 1,
			'Eia': 'jsonp_913580_',
			'position': {
				'O': 116.4774823,  # 经度
				'P': 39.873005,  # 纬度
				'lng': 116.4774823,  # 经度
				'lat': 39.873005  # 纬度
			},
			'message': 'Get+ipLocation+success.Get+address+success.',
			'location_type': 'ip',
			'accuracy': None,
			'isConverted': True,
			'addressComponent': {
				'citycode': '',
				'adcode': '',  # 行政区划代码
				'businessAreas': [],
				'neighborhoodType': '',
				'neighborhood': '',
				'building': '',
				'buildingType': '',
				'street': '',
				'streetNumber': '',
				'province': '',  # 所在省
				'city': '',  # 所在市
				'district': '',  # 所在区
				'township': ''  # 所在街道
			},
			'formattedAddress': '',  # 拼接后的地址
			'roads': [],
			'crosses': [],
			'pois': []},
		'area': '中国',  # 所在区域
		'province': '',
		'city': '',
		'sfzx': '0',
		'sfjcwhry': '0',  # 是否接触武汉人员
		'sfjchbry': '0',  # 是否接触湖北人员
		'sfcyglq': '0',  # 是否处于隔离期
		'gllx': '',  # 隔离类型
		'glksrq': '',  # 隔离开始日期
		'jcbhlx': '',
		'jcbhrq': '',
		'bztcyy': '',
		'sftjhb': '0',  # 是否停经湖北
		'sftjwh': '0',  # 是否停经武汉
		'sfsfbh': '0',
		'xjzd': '',
		'jcwhryfs': '',  # 接触武汉人员方式
		'jchbryfs': '',  # 接触湖北人员方式
		'szgj': '',
		'jcjg': ''
	}
	r = s.post('https://itsapp.bjut.edu.cn/ncov/wap/default/save', data=data, headers=headers)
	print('【上报】' + json.loads(r.text)['m'])
	time.sleep(3)
