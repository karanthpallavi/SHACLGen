# Auto generated from lowerConfidenceLimit.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-19T12:11:16
# Schema: LowerConfidenceLimit
#
# id: https://tib.eu/ontologies/PMD_shapes/LowerConfidenceLimit
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/obi.owl/')
IAO = CurieNamespace('iao', 'http://purl.obolibrary.org/obo/iao.owl/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/obi.owl/')
OBO = CurieNamespace('obo', 'http://purl.obolibrary.org/obo/')
PMD = CurieNamespace('pmd', 'https://w3id.org/pmd/co/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
STATO = CurieNamespace('stato', 'http://purl.obolibrary.org/stato.owl/')
DEFAULT_ = CurieNamespace('', 'https://tib.eu/ontologies/PMD_shapes/LowerConfidenceLimit/')


# Types

# Class references



@dataclass
class LowerConfidenceLimit(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = STATO["STATO_0000315"]
    class_class_curie: ClassVar[str] = "stato:STATO_0000315"
    class_name: ClassVar[str] = "lower confidence limit"
    class_model_uri: ClassVar[URIRef] = URIRef("https://tib.eu/ontologies/PMD_shapes/LowerConfidenceLimit/LowerConfidenceLimit")

    value: Union[dict, "ValueLabel"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, ValueLabel):
            self.value = ValueLabel()

        super().__post_init__(**kwargs)


class ValueLabel(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["OBI_0001931"]
    class_class_curie: ClassVar[str] = "obi:OBI_0001931"
    class_name: ClassVar[str] = "valueLabel"
    class_model_uri: ClassVar[URIRef] = URIRef("https://tib.eu/ontologies/PMD_shapes/LowerConfidenceLimit/ValueLabel")


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.value = Slot(uri=OBI.OBI_0001938, name="value", curie=OBI.curie('OBI_0001938'),
                   model_uri=DEFAULT_.value, domain=None, range=Union[dict, ValueLabel])
