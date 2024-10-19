import os
import math
from functions import *

def create_patch_files(patch_folder, ratio_value, scaling_factor, visual_fixes):

    visual_fixesa = visual_fixes[0]
    scaling_factor = float(scaling_factor)
    ratio_value = float(ratio_value)
    print(f"The scaling factor is {scaling_factor}.")
    hex_value1, hex_value2= acnh_hex23(ratio_value)
    version_variables = ["2.0.6"]
    for version_variable in version_variables:
        file_name = f"main-{version_variable}.pchtxt"
        file_path = os.path.join(patch_folder, file_name)

        if version_variable == "2.0.6":
            nsobidid = "15765149DF53BA4105C75A3A1A5102FC"
            replace1 = "0045fd90"
            replace2 = "0045fd94"
            visual_fix = visual_fixesa

        patch_content = f'''@nsobid-{nsobidid}

@flag print_values
@flag offset_shift 0x100

@enabled
02c768e0 {hex_value1}
02c768e4 {hex_value2}
02c768e8 8003271e
00ef5c40 e003271e
@disabled

{visual_fix}

// Generated using acnh-aar by Fayaz (github.com/fayaz12g/acnh-aar)
// Made possible by Fl4sh_#9174'''
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as patch_file:
            patch_file.write(patch_content)
        print(f"Patch file created: {file_path}")
