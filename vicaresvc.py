from PyViCare.PyViCare import PyViCare
import os

_client_id = os.environ['VICARE_CLIENT_ID']
_email = os.environ['VICARE_EMAIL']
_password = os.environ['VICARE_PASSWORD']


_vicare = PyViCare()
_vicare.initWithCredentials(_email, _password, _client_id, "token.save")
_device = _vicare.devices[0]
print(_device.getModel())
print("Online" if _device.isOnline() else "Offline")

heatpump = _device.asHeatPump()
circuit = heatpump.circuits[0]
compressor = heatpump.compressors[0]
