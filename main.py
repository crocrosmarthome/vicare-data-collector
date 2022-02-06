from vicaresvc import *
from dbsvc import *

from datetime import datetime

now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

writeMeasure(now, "heatpump", "outside_temperature", heatpump.getOutsideTemperature())
writeMeasure(now, "heatpump", "outsideTemperature", heatpump.getOutsideTemperature())
writeMeasure(now, "heatpump", "domesticHotWaterConfiguredTemperature", heatpump.getDomesticHotWaterConfiguredTemperature())
writeMeasure(now, "heatpump", "hotWaterStorageTemperatureTop", heatpump.getHotWaterStorageTemperatureTop())
writeMeasure(now, "heatpump", "domesticHotWaterConfiguredTemperature2", heatpump.getDomesticHotWaterConfiguredTemperature2())
writeMeasure(now, "heatpump", "domesticHotWaterActiveMode", heatpump.getDomesticHotWaterActiveMode())
writeMeasure(now, "heatpump", "domesticHotWaterDesiredTemperature", heatpump.getDomesticHotWaterDesiredTemperature())
writeMeasure(now, "heatpump", "domesticHotWaterStorageTemperature", heatpump.getDomesticHotWaterStorageTemperature())
writeMeasure(now, "heatpump", "domesticHotWaterPumpActive", heatpump.getDomesticHotWaterPumpActive())
writeMeasure(now, "heatpump", "domesticHotWaterCirculationPumpActive", heatpump.getDomesticHotWaterCirculationPumpActive())
writeMeasure(now, "heatpump", "domesticHotWaterActive", heatpump.getDomesticHotWaterActive())
writeMeasure(now, "heatpump", "domesticHotWaterMaxTemperature", heatpump.getDomesticHotWaterMaxTemperature())
writeMeasure(now, "heatpump", "domesticHotWaterMinTemperature", heatpump.getDomesticHotWaterMinTemperature())
writeMeasure(now, "heatpump", "domesticHotWaterChargingActive", heatpump.getDomesticHotWaterChargingActive())
writeMeasure(now, "heatpump", "oneTimeCharge", heatpump.getOneTimeCharge())
writeMeasure(now, "heatpump", "domesticHotWaterCirculationMode", heatpump.getDomesticHotWaterCirculationMode())
writeMeasure(now, "heatpump", "controllerSerial", heatpump.getControllerSerial())
writeMeasure(now, "heatpump", "returnTemperature", heatpump.getReturnTemperature())
writeMeasure(now, "heatpump", "supplyTemperaturePrimaryCircuit", heatpump.getSupplyTemperaturePrimaryCircuit())
writeMeasure(now, "heatpump", "supplyTemperatureSecondaryCircuit", heatpump.getSupplyTemperatureSecondaryCircuit())
writeMeasure(now, "heatpump", "returnTemperatureSecondaryCircuit", heatpump.getReturnTemperatureSecondaryCircuit())
writeMeasure(now, "heatpump", "bufferTopTemperature", heatpump.getBufferTopTemperature())
writeMeasure(now, "heatpump", "bufferMainTemperature", heatpump.getBufferMainTemperature())
writeMeasure(now, "heatpump", "outsideTemperature", heatpump.getOutsideTemperature())
writeMeasure(now, "heatpump", "domesticHotWaterConfiguredTemperature", heatpump.getDomesticHotWaterConfiguredTemperature())
writeMeasure(now, "heatpump", "domesticHotWaterStorageTemperature", heatpump.getDomesticHotWaterStorageTemperature())
writeMeasure(now, "circuit", "supplyTemperature", circuit.getSupplyTemperature())
writeMeasure(now, "circuit", "heatingCurveShift", circuit.getHeatingCurveShift())
writeMeasure(now, "circuit", "heatingCurveSlope", circuit.getHeatingCurveSlope())
writeMeasure(now, "circuit", "activeProgram", circuit.getActiveProgram())
writeMeasure(now, "circuit", "currentDesiredTemperature", circuit.getCurrentDesiredTemperature())
writeMeasure(now, "circuit", "desiredTemperatureForProgram", circuit.getDesiredTemperatureForProgram("comfort"))
writeMeasure(now, "circuit", "ActiveMode", circuit.getActiveMode())
writeMeasure(now, "circuit", "DesiredTemperatureForProgram", circuit.getDesiredTemperatureForProgram("comfort"))
writeMeasure(now, "compressor","active", compressor.getActive())



