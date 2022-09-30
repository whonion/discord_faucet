import requests

json_data = {
    'address': 'nois1v5xayfadhn3emtptsyc9nu7zyuyyze9s6d6swm',
	'denom' : 'unois'
}

response = requests.post('http://faucet.noislabs.com/credit', json=json_data)
