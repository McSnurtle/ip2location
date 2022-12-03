# import
import sys
import requests
import random
import string
import art


art.tprint("IP2LOCATION", font="qwertyui")
print("")
print("-------------------------------------------------------------------------------------------------------------------")
print("Enter 'self' to view your own IP and location\n"
      "Enter 'rand' to view a random valid IP and location\n"
      "Note: random IP options may take a very long time to find a valid IP\n"
      "Thanks for using IP2LOCATION!~\n"
      "\n"
      "By Mc_Snurtle")
print("-------------------------------------------------------------------------------------------------------------------")
print("")


def random_ip():
    print("Generating Random IP")
    nums = string.digits
    possible_lens = [1, 2, 3]
    ip1 = "".join(random.choice(nums) for v in range(random.choice(possible_lens)))
    ip2 = "".join(random.choice(nums) for v in range(random.choice(possible_lens)))
    ip3 = "".join(random.choice(nums) for v in range(random.choice(possible_lens)))
    ip4 = "".join(random.choice(nums) for v in range(random.choice(possible_lens)))
    final_ip = f"{ip1}.{ip2}.{ip3}.{ip4}"
    ip_chunks = [int(ip1), int(ip2), int(ip3), int(ip4)]
    print("Verifying Random IP")
    if "None]" in str(get_location(final_ip)):
        print(f"Random IP '{final_ip}' Invalid. Trying Again (-1)")
        random_ip()
    if any(i > 255 for i in ip_chunks):
        print(f"Rand IP '{final_ip}' Invalid. Trying Again (-255)")
        random_ip()
    else:
        print("Random IP Found")
        return final_ip


def self_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location(ip_address):
    print("Fetching Location Data...")
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "type": response.get("version"),
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    location_format = list(location_data.values())
    return location_format


ipInput = input("Enter an IP Address: ")
if "self" in ipInput:
    ipInput = self_ip()

if "rand" in ipInput:
    ipInput = random_ip()

if "None" in str(get_location(ipInput)):
    print(f"No IP Address found under: '{get_location(ipInput)[0]}'")
    sys.exit()

print(get_location(ipInput))
print("Loading Location Data...")
print(f"Based on the {get_location(ipInput)[1]} Address {get_location(ipInput)[0]}, the user's location is {get_location(ipInput)[2]}, {get_location(ipInput)[3]} {get_location(ipInput)[4]}")
