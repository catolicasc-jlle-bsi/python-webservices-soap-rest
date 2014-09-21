from pysimplesoap.client import SoapClient, SoapFault

# create a simple consumer
client = SoapClient(location="http://192.168.33.10:8008/",
                    action='http://192.168.33.10:8008/',
                    namespace="http://example.com/sample.wsdl",
                    soap_ns='soap',
                    ns=False)

response = client.taxi_service(city_origin='new%20york',
                             state_origin='ny',
                             city_destiny='san%20francisco',
                             state_destiny='ca',
                             coin='BRL')
result = response

print 'origin latitude: %s' % float(result.origin.latitude)
print 'origin longitude: %s' % float(result.origin.longitude)
print 'origin zipcode: %s' % str(result.origin.zip_code)

print 'destiny latitude: %s' % float(result.destiny.latitude)
print 'destiny longitude: %s' % float(result.destiny.longitude)
print 'destiny zipcode: %s' % str(result.destiny.zip_code)

print 'distance em km: %s' % float(result.km_distance)
print 'gasoline price: %s' % float(result.gasoline_price)
print 'total price: %s' % float(result.total_price)
print 'total price formatted: %s' % str(result.total_price_formatted)