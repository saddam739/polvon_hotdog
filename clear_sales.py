import json
import urllib.request
import ssl

# Ignore SSL errors if any
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://script.google.com/macros/s/AKfycbznLh5nT1spgrmgKwLUiWquVV2oY0f61yLbfK8MLIPnHDkeOcxeZATHkLxjT-5zOvG-/exec"

class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return urllib.request.Request(newurl, method='GET')

opener = urllib.request.build_opener(NoRedirectHandler)

print("Fetching current database from Cloud...")
try:
    with opener.open(url) as response:
        content = response.read().decode('utf-8')
        cloud_data = json.loads(content)
        print("Data fetched successfully!")
except Exception as e:
    print("Error fetching data:", e)
    cloud_data = None

if cloud_data:
    print(f"Current sales count: {len(cloud_data.get('sales', []))}")
    
    # Clear sales
    cloud_data['sales'] = []
    # If there are archives, clear them too to completely wipe the history of sales/prices
    if 'monthlyArchive' in cloud_data:
        cloud_data['monthlyArchive'] = []
    if 'yearlyArchive' in cloud_data:
        cloud_data['yearlyArchive'] = []
        
    print("Sales and archives have been cleared in memory.")
    
    # Save back to Cloud
    body = json.dumps(cloud_data).encode('utf-8')
    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('Content-Type', 'text/plain')
    
    print("Saving cleared data to Cloud...")
    try:
        with opener.open(req) as response:
            print("Status:", response.status)
            print("Response:", response.read().decode('utf-8'))
            print("Database successfully cleared!")
    except Exception as e:
        print("Error saving data:", e)
