from typing import Dict

def contstruct_nonadj_aaa_bbb(input_dict: Dict[int]) -> int:
    """length of longest string without aaa or bbb
        inputs: dictionary
            keys: "aa", "bb", "ab"
            values: counts
    """
    # note: 
    # 1) aa can only be followed by bb
    # 2) ab can be followed by aa or ab
    # 3) bb can be followed by ab or aa




