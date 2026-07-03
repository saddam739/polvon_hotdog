import json
import urllib.request

url = "https://script.google.com/macros/s/AKfycbznLh5nT1spgrmgKwLUiWquVV2oY0f61yLbfK8MLIPnHDkeOcxeZATHkLxjT-5zOvG-/exec"
data = {
  "inventory": [{"id": 1, "name": "Gosht", "qty": 3, "unitPrice": 130, "unit": "gramm"}],
  "recipes": [],
  "sales": [],
  "expenses": []
}
body = json.dumps(data).encode('utf-8')

req = urllib.request.Request(url, data=body, method='POST')
req.add_header('Content-Type', 'text/plain')

# Custom handler to NOT follow redirects immediately so we can inspect or follow correctly
class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Google returns 302. We should do a GET to the newurl.
        print("Redirecting to:", newurl)
        return urllib.request.Request(newurl, method='GET')

opener = urllib.request.build_opener(NoRedirectHandler)
try:
    with opener.open(req) as response:
        print("Status:", response.status)
        print("Response:", response.read().decode('utf-8'))
except Exception as e:
    print("Error:", e)
