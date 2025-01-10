from linkml.validator import validate

instance = {
    "id": "isk:measurementMassEPDM",
    "value": 95,
}

report = validate(instance, "confidenceLevel.yaml", "stato:STATO_0000561")

if not report.results:
    print('The instance is valid!')
else:
    for result in report.results:
        print(result.message)