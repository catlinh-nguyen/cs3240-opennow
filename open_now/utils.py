from django.contrib.gis.geoip2 import GeoIP2

# helper functions

# get the current location based on the ip address
def get_ip_address(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip



# get geographic information
def get_geo(ip):
	g = GeoIP2()
	country = g.country(ip)
	city = g.city(ip)
	lat, lon = g.lat_lon(ip)
	return country, city, lat, lon

# centers the map
def get_center_coordinates(latA, longA, latB=None, longB=None):
	cord = (latA, longA)

	# if we are given an actual destination, overwrite the coordinates
	if latB:
		cord = [(latA+latB)/2, (longA+longB)/2]
	return cord

# adjusts the zoom based on the distance
def get_zoom(distance):
	if distance <= 100:
		return 8
	elif distance > 100 and distance <= 5000:
		return 4
	else:
		return 2