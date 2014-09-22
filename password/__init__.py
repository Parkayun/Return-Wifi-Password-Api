# -*- coding:utf-8 -*-

def from_ssids(ssids):
    results = {}

    for ssid in ssids:
        passwords = []
        ssid_lower = ssid.lower()

        if 'sk' in ssid_lower:
            passwords.append('a123456789')
        elif 'mcdonald' in ssid_lower:
            passwords.append('16005252')
        elif 'seveneleven' in ssid_lower or '7eleven' in ssid_lower \
                or 'seven11' in ssid_lower:
            passwords.append('2127393302')
        elif 'SO070VOIP' in ssid_lower or 'hellowd' in ssid_lower \
                or 'hellowireless' in ssid_lower:
            passwords.append('534f4b4354')
        elif 'tbroadnet' in ssid_lower:
            passwords.append('123456789')
            passwords.append('a123456789')
        elif 'tobis' in ssid_lower:
            passwords.append('1234')
        elif 'paris' in ssid_lower:
            passwords.append('vkflzmfktkd')
        elif 'kwi-b' in ssid_lower and 't' in ssid_lower:
            passwords.append('SHOW3382')
            passwords.append('password')
        elif 'admin' in ssid_lower:
            passwords.append('password')
        else:
            passwords.append('1234567890')
            passwords.append('123456789a')

            if 'kt' in ssid_lower and not 'skt' in ssid_lower:
                passwords.append('1234567890c')

        results[ssid] = passwords
