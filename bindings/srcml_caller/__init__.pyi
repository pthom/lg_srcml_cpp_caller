# type: ignore
import sys
from typing import Literal, List, Any, Optional, Tuple
import numpy as np
import enum
import numpy

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:libsrcml_caller.h>    ####################


class CodeLanguage(enum.Enum):
    c = enum.auto()            # (= 0)
    c_sharp = enum.auto()      # (= 1)
    c_plus_cplus = enum.auto() # (= 2)
    java = enum.auto()         # (= 3)
    objective_c = enum.auto()  # (= 4)


def to_code(
    xml_str: str,
    encoding_src: str = "utf-8",
    encoding_xml: str = "utf-8"
    ) -> Optional[str]:
    pass


def to_srcml(
    code: str,
    language: CodeLanguage,
    include_positions: bool = True,
    encoding_src: str = "utf-8",
    encoding_xml: str = "utf-8"
    ) -> Optional[str]:
    pass
####################    </generated_from:libsrcml_caller.h>    ####################

# </litgen_stub>
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
