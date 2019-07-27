import requests
page = requests.get("http://ercot.com/content/cdr/html/real_time_spp")
page_two = requests.get("http://ercot.com/content/cdr/html/current_np6788")
page_three = requests.get("http://ercot.com/content/cdr/html/dam_spp")

print(page.content)
print(page_two.content)
print(page_three.content)

