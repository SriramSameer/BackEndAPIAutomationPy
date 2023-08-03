import requests

# http://rahulshettyacademy.com
# 'visit-month'
cookie = {'visit-month' : 'February'}
response = requests.get('http://rahulshettyacademy.com', cookies=cookie)
print(response.status_code)

se = requests.session()
se.cookies.update({'visit-month' : 'February'})

res = se.get("https://httpbin.org/cookies", cookies={'visit-year' : '2022'})
print(res.text)