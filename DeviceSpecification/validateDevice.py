from linkml.validator import validate

instance = {
    "id": "ID:1",
    "physical_quality": "https://w3id.org/pmd/co/Quality/Temperature",
    "device_setting": "http://purl.obolibrary.org/obo/obi.owl/OBI_0000654/RotorTemperatureSetting"
}

report = validate(instance, "device.yaml", "Device")

if not report.results:
    print('The instance is valid!')
else:
    for result in report.results:
        print(result.message)