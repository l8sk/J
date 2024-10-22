import requests

url = "https://i.instagram.com/api/v1/users/check_username/"

payload = "signed_body=SIGNATURE.%7B%22is_group_creation%22%3A%22false%22%2C%22username%22%3A%22ahmed%22%2C%22_uuid%22%3A%22b457a760-b663-4a13-bba0-1ab148dfe1a2%22%7D"

headers = {
  'User-Agent': "Instagram 351.0.0.41.106 Android (30/11; 320dpi; 720x1448; realme; RMX3269; RED8F6; RMX3265; ar_IQ; 647663441)",
  'Accept-Encoding': "zstd, gzip, deflate",
  'x-ig-app-locale': "ar_IQ",
  'x-ig-device-locale': "ar_IQ",
  'x-ig-mapped-locale': "ar_AR",
  'x-pigeon-session-id': "UFS-116fefe2-8696-45bc-af52-c10678268ba3-6",
  'x-pigeon-rawclienttime': "1728080088.937",
  'x-ig-bandwidth-speed-kbps': "985.000",
  'x-ig-bandwidth-totalbytes-b': "4272298",
  'x-ig-bandwidth-totaltime-ms': "3220",
  'x-bloks-version-id': "145bdb95c874a8d81dfe9d44aeff8286378f930f5898c808f8d2f0bb1d931181",
  'x-ig-www-claim': "0",
  'x-bloks-prism-button-version': "CONTROL",
  'x-bloks-prism-colors-enabled': "false",
  'x-bloks-prism-font-enabled': "false",
  'x-bloks-is-layout-rtl': "true",
  'x-ig-device-id': "b457a760-b663-4a13-bba0-1ab148dfe1a2",
  'x-ig-family-device-id': "9d23de2b-3d73-4009-9529-63a43dd8c671",
  'x-ig-android-id': "android-f7a88f3e39abf27a",
  'x-ig-timezone-offset': "10800",
  'x-ig-nav-chain': "SelfFragment:self_profile:8:main_profile:1728080047.622::,ProfileMediaTabFragment:self_profile:9:button:1728080047.835::,AddAccountBottomSheetFragment:add_account_bottom_sheet:11:button:1728080052.271::,IgTabHostFragment:self_profile:12:button:1728080054.665::,com.bloks.www.caa.login.login_homepage:com.bloks.www.caa.login.login_homepage:13:button:1728080055.246::,CreateUsernameFragment:sac_create_username:14:warm_start:1728080087.770::",
  'x-fb-connection-type': "WIFI",
  'x-ig-connection-type': "WIFI",
  'x-ig-capabilities': "3brTv10=",
  'x-ig-app-id': "567067343352427",
  'priority': "u=3",
  'accept-language': "ar-IQ, en-US",
  'x-mid': "ZwBkXQABAAG1X2rWzXMlehgPi2dJ",
  'ig-intended-user-id': "0",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-fb-http-engine': "Liger",
  'x-fb-client-ip': "True",
  'x-fb-server-cluster': "True"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)
