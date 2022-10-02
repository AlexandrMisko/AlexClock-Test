import requests
import datetime
import time
import yagmail
    
yag = yagmail.SMTP(user='1586924294@qq.com', password='xrpalckormpjjijh', host='smtp.qq.com')
resp = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/?username=alexandrmisko', headers={
    'X-IG-App-ID': '936619743392459',
    'Cookie': 'csrftoken=UcTWfv2NroJABRj4dIWfe38eRpb1CXU1; mid=YZIUAwALAAHIMaHw27iWm4uRNhXm; ig_did=267B8A84-7E4C-4AE8-8310-89537C6AE002; ig_nrcb=1; ds_user_id=48282355544; sessionid=48282355544%3AuWW0eZDfR8CL3u%3A27; datr=ZWq4YgmzX9ZT1JWqg_JKOBhe; dpr=1.25; shbid="12194\05448282355544\0541688611539:01f75d3a60c811bfcd880e4e8f3baefa76a97af80c8452eb788f385d096964b8d7380896"; shbts="1657075539\05448282355544\0541688611539:01f790a0918bea636a217097bd7087021d8198bf00f019bb8c87e02a0a702e02d87c1d7e"; rur="NAO\05448282355544\0541688617994:01f7c149d91540dacf8374476beca35130e516943a12ed01f4c487859acfb14033ca7907'
})
taken_stamp = ['']*4
taken_stamp[0] = resp.json()['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['taken_at_timestamp']
taken_stamp[1] = resp.json()['data']['user']['edge_owner_to_timeline_media']['edges'][1]['node']['taken_at_timestamp']
taken_stamp[2] = resp.json()['data']['user']['edge_owner_to_timeline_media']['edges'][2]['node']['taken_at_timestamp']
taken_stamp[3] = resp.json()['data']['user']['edge_owner_to_timeline_media']['edges'][3]['node']['taken_at_timestamp']
rank = 0
for i in range(1,4):
    if taken_stamp[0] < taken_stamp[i]:
        taken_stamp[0] = taken_stamp[i]
        rank = i
taken_at = (datetime.datetime.fromtimestamp(taken_stamp[rank]) + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
id = resp.json()['data']['user']['edge_owner_to_timeline_media']['edges'][rank]['node']['id']
print(id)
shortcode = resp.json()['data']['user']['edge_owner_to_timeline_media']['edges'][rank]['node']['shortcode']
# now_at = (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
# print(now_at)
url = f'https://www.instagram.com/p/{shortcode}'
print(url)
print(taken_at)
resp = requests.get('https://i.instagram.com/api/v1/accounts/edit/web_form_data/', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
    'X-IG-App-ID': '936619743392459',
    'Cookie': 'csrftoken=UcTWfv2NroJABRj4dIWfe38eRpb1CXU1; mid=YZIUAwALAAHIMaHw27iWm4uRNhXm; ig_did=267B8A84-7E4C-4AE8-8310-89537C6AE002; ig_nrcb=1; ds_user_id=48282355544; sessionid=48282355544%3AuWW0eZDfR8CL3u%3A27%3AAYdStGPAuKILQTiONRS6ue7nELp1L-iY5ST6OKlEhJo; datr=ZWq4YgmzX9ZT1JWqg_JKOBhe; dpr=1.25; shbid="12194\05448282355544\0541696081072:01f7d69ed0200ec38ee14a29d422334c1169d5d5169af9af61b29e2de4953b3be7303174"; shbts="1664545072\05448282355544\0541696081072:01f74d2063e970bc6f4b80a7a089c85acd30a459d48c285bf13282f13c9cb5e1a2bcddb8"; rur="NAO\05448282355544\0541696165910:01f7b9d8a44beaeeebd30b27f51a1bde5163a188b1d2da74c7d94b0e2a61223d51e79078'
})
store_at = resp.json()['form_data']['biography']
if taken_at == store_at:
    print('无需更新')
else:
    resp = requests.post('https://i.instagram.com/api/v1/web/accounts/edit/', data={
        'first_name': 'ZX+Su',
        'email': 'speedmilo40@gmail.com',
        'username': 'zx.su.77',
        'phone_number': '',
        'biography': '2022-09-28 22:53:31',
        'external_url': '',
        'chaining_enabled': 'on'
    }, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
        'X-IG-App-ID': '936619743392459',
        'X-CSRFToken': 'UcTWfv2NroJABRj4dIWfe38eRpb1CXU1',
        'Cookie': 'csrftoken=UcTWfv2NroJABRj4dIWfe38eRpb1CXU1; mid=YZIUAwALAAHIMaHw27iWm4uRNhXm; ig_did=267B8A84-7E4C-4AE8-8310-89537C6AE002; ig_nrcb=1; ds_user_id=48282355544; sessionid=48282355544%3AuWW0eZDfR8CL3u%3A27%3AAYdStGPAuKILQTiONRS6ue7nELp1L-iY5ST6OKlEhJo; datr=ZWq4YgmzX9ZT1JWqg_JKOBhe; dpr=1.25; shbid="12194\05448282355544\0541696081072:01f7d69ed0200ec38ee14a29d422334c1169d5d5169af9af61b29e2de4953b3be7303174"; shbts="1664545072\05448282355544\0541696081072:01f74d2063e970bc6f4b80a7a089c85acd30a459d48c285bf13282f13c9cb5e1a2bcddb8"; rur="NAO\05448282355544\0541696165910:01f7b9d8a44beaeeebd30b27f51a1bde5163a188b1d2da74c7d94b0e2a61223d51e79078'
    })
    print(resp.text)
    resp = requests.get(f'https://i.instagram.com/api/v1/media/{id}/info/', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
        'X-IG-App-ID': '936619743392459',
        'Cookie': 'csrftoken=UcTWfv2NroJABRj4dIWfe38eRpb1CXU1; mid=YZIUAwALAAHIMaHw27iWm4uRNhXm; ig_did=267B8A84-7E4C-4AE8-8310-89537C6AE002; ig_nrcb=1; ds_user_id=48282355544; sessionid=48282355544%3AuWW0eZDfR8CL3u%3A27%3AAYdStGPAuKILQTiONRS6ue7nELp1L-iY5ST6OKlEhJo; datr=ZWq4YgmzX9ZT1JWqg_JKOBhe; dpr=1.25; shbid="12194\05448282355544\0541696081072:01f7d69ed0200ec38ee14a29d422334c1169d5d5169af9af61b29e2de4953b3be7303174"; shbts="1664545072\05448282355544\0541696081072:01f74d2063e970bc6f4b80a7a089c85acd30a459d48c285bf13282f13c9cb5e1a2bcddb8"; rur="NAO\05448282355544\0541696165910:01f7b9d8a44beaeeebd30b27f51a1bde5163a188b1d2da74c7d94b0e2a61223d51e79078'
    })
    contents = resp.json()['items'][0]['video_versions'][0]['url']
    yag.send(to='1586924294@qq.com', subject='AlexandrMisko更新啦！', contents=url+'</br>'+contents)
    yag.close()
    print('发送邮件成功！')
    
