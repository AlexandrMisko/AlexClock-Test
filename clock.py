import requests
import datetime
import time
    
resp = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/?username=alexandrmisko', headers={
    'X-IG-App-ID': '936619743392459',
    'Cookie': 'csrftoken=UcTWfv2NroJABRj4dIWfe38eRpb1CXU1; mid=YZIUAwALAAHIMaHw27iWm4uRNhXm; ig_did=267B8A84-7E4C-4AE8-8310-89537C6AE002; ig_nrcb=1; ds_user_id=48282355544; sessionid=48282355544%3AuWW0eZDfR8CL3u%3A27; datr=ZWq4YgmzX9ZT1JWqg_JKOBhe; dpr=1.25; shbid="12194\05448282355544\0541688611539:01f75d3a60c811bfcd880e4e8f3baefa76a97af80c8452eb788f385d096964b8d7380896"; shbts="1657075539\05448282355544\0541688611539:01f790a0918bea636a217097bd7087021d8198bf00f019bb8c87e02a0a702e02d87c1d7e"; rur="NAO\05448282355544\0541688617994:01f7c149d91540dacf8374476beca35130e516943a12ed01f4c487859acfb14033ca7907'
})
shortcode = resp.json()['data']['user']['edge_owner_to_timeline_media']['edges'][1]['node']['shortcode']
taken_stamp = resp.json()['data']['user']['edge_owner_to_timeline_media']['edges'][1]['node']['taken_at_timestamp']
taken_at = datetime.datetime.fromtimestamp(taken_stamp) + datetime.timedelta(hours=8)
now_at = datetime.datetime.now() + datetime.timedelta(hours=8)
print(f'https://www.instagram.com/p/{shortcode}')
print(taken_at)
print(now_at)
if taken_at < now_at:
    print('该更新了')
