# https://formulae.brew.sh/api/formula.json

import requests
import json

r = requests.get("https://formulae.brew.sh/api/formula.json")
packages_json = json.loads(r.text)

package_name = packages_json[0]["name"]
package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"

r = requests.get(package_url)
package_json = json.loads(r.text)


package_str = json.dumps(package_json, indent=2)

install_30 = package_json["analytics"]["install"]["30d"][package_name]
install_90 = package_json["analytics"]["install"]["90d"][package_name]
install_365 = package_json["analytics"]["install"]["365d"][package_name]

print(package_name,install_30,install_90,install_365)