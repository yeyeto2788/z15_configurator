import time

import numpy

from prettytable import PrettyTable


SETTINGS = {
    0: {
        "name": "DVR_SETTING_JPEGQFACTOR",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "Low", "description": "", "value": 0x01},
            {"name": "Medium", "description": "", "value": 0x02},
            {"name": "High", "description": "", "value": 0x04},
        ],
    },
    1: {
        "name": "DVR_SETTING_RESOLUTION",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "320 x 240", "description": "320 x 240", "value": 0x00},
            {"name": "640 x 480", "description": "640 x 480", "value": 0x01},
            {"name": "640 x 360", "description": "640 x 360", "value": 0x02},
            {"name": "1280 x 720", "description": "1280 x 720", "value": 0x03},
        ],
    },
    2: {
        "name": "DVR_SETTING_MOTIONDETECT",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "Disabled", "description": "Disabled", "value": 0x00},
            {"name": "Low", "description": "Low intensity", "value": 0x01},
            {"name": "Medium", "description": "Medium intensity", "value": 0x02},
            {"name": "High", "description": "High intensity", "value": 0x03},
        ],
    },
    3: {
        "name": "DVR_SETTING_SHOWTIMESTAMP",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "Enable", "description": "Enable option", "value": 0x01},
            {"name": "Disable", "description": "Disable option", "value": 0x00},
        ],
    },
    4: {
        "name": "DVR_SETTING_CIRCULARREC",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "Enable", "description": "Enable option", "value": 0x01},
            {"name": "Disable", "description": "Disable option", "value": 0x00},
        ],
    },
    5: {
        "name": "DVR_SETTING_FRAMERATE",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "High", "description": "High", "value": 0x01},
            {"name": "Low", "description": "Low", "value": 0x00},
        ],
    },
    6: {
        "name": "DVR_SETTING_SPLITFILETIME",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "SPLIT_FILE_TIME_60MINS", "description": "", "value": 0x08},
            {"name": "SPLIT_FILE_TIME_30MINS", "description": "", "value": 0x04},
            {"name": "SPLIT_FILE_TIME_20MINS", "description": "", "value": 0x03},
            {"name": "SPLIT_FILE_TIME_15MINS", "description": "", "value": 0x02},
            {"name": "SPLIT_FILE_TIME_10MINS", "description": "", "value": 0x01},
        ],
    },
    7: {
        "name": "DVR_SETTING_DAYNIGHTMODE",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "AUTO_DAY_NIGHT_MODE", "description": "Auto switch between day and night mode.", "value": 0x02},
            {"name": "NIGHT_MODE", "description": "Nigh mode", "value": 0x01},
            {"name": "DAY_MODE", "description": "Day mode", "value": 0x00},
        ],
    },
    8: {
        "name": "DVR_SETTING_ORIENTATION",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "ORIENTATION_VERT_FLIP", "description": "Vertical orientation", "value": 0x02},
            {"name": "ORIENTATION_NORMAL", "description": "Normal orientation", "value": 0x01},
        ],
    },
    9: {
        "name": "DVR_SETTING_AUTOSTARTMODE",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "SCHEDULER_START", "description": "", "value": 0x05},
            {"name": "APAPTER_PRESENT_START", "description": "", "value": 0x04},
            {"name": "APAPTER_PRESENT_ACTIVATED", "description": "", "value": 0x03},
            {"name": "APAPTER_ABSENT_ACTIVATED", "description": "", "value": 0x02},
            {"name": "NO_AUTOSTART", "description": "", "value": 0x01},
        ],
    },
    10: {
        "name": "DVR_SETTING_VOXSENS",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "VOX_SENS_HIGH", "description": "", "value": 0x04},
            {"name": "VOX_SENS_MED", "description": "", "value": 0x03},
            {"name": "VOX_SENS_LOW", "description": "", "value": 0x02},
            {"name": "VOX_OFF", "description": "", "value": 0x01},
        ],
    },
    11: {
        "name": "DVR_SETTING_VOICEREC",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "VOICE_REC_ON", "description": "", "value": 0x02},
            {"name": "VOICE_REC_OFF", "description": "", "value": 0x01},
        ],
    },
    12: {
        "name": "DVR_SETTING_VIBDETECTSENS",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "VIB_DETECT_SENS_HIGH", "description": "", "value": 0x04},
            {"name": "VIB_DETECT_SENS_MED", "description": "", "value": 0x03},
            {"name": "VIB_DETECT_SENS_LOW", "description": "", "value": 0x02},
            {"name": "VIB_DETECT_OFF", "description": "", "value": 0x01},
        ],
    },
    13: {
        "name": "DVR_SETTING_VIBSTANDBYMODE",
        "notes": ["POWER_SAVING_MODE AND VOX/MOTION_DETECT CANNOT BE ACTIVATED SAME TIME"],
        "description": "",
        "enabled": True,
        "options": [
            {"name": "VIB_STANDBY_FAST_RESP", "description": "", "value": 0x02},
            {"name": "VIB_STANDBY_POWER_SAVE", "description": "", "value": 0x01},
        ],
    },
    14: {
        "name": "DVR_SETTING_ALIVEDURATION",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "ALIVE_DURATION_5MINS", "description": "", "value": 0x01},
            {"name": "ALIVE_DURATION_2MINS", "description": "", "value": 0x02},
        ],
    },
    15: {
        "name": "DVR_SETTING_LEDINDICATION",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "LED_INDICATION_ON", "description": "", "value": 0x02},
            {"name": "LED_INDICATION_OFF", "description": "", "value": 0x01},
        ],
    },
    16: {
        "name": "DVR_SETTING_BANDINGFILTER",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "BANDING_FILTER_OUTDOOR", "description": "", "value": 0x03},
            {"name": "BANDING_FILTER_60HZ", "description": "", "value": 0x02},
            {"name": "BANDING_FILTER_50HZ", "description": "", "value": 0x01},
        ],
    },
    17: {
        "name": "DVR_SETTING_EXTINTYPE",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "EXT_IN_NC", "description": "", "value": 0x03},
            {"name": "EXT_IN_NO", "description": "", "value": 0x02},
            {"name": "EXT_IN_OFF", "description": "", "value": 0x01},
        ],
    },
    18: {
        "name": "DVR_SETTING_EXTOUTTYPE",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "EXT_OUT_NC", "description": "", "value": 0x03},
            {"name": "EXT_OUT_NO", "description": "", "value": 0x02},
            {"name": "EXT_OUT_OFF", "description": "", "value": 0x01},
        ],
    },
    19: {
        "name": "DVR_SETTING_BUZZARDURATION",
        "description": "",
        "enabled": False,
        "options": [
            {"name": "ALARM_DURATION_1MINS", "description": "", "value": 0x04},
            {"name": "ALARM_DURATION_5MINS", "description": "", "value": 0x03},
            {"name": "ALARM_DURATION_WHILE_REC", "description": "", "value": 0x02},
            {"name": "ALARM_DURATION_OFF", "description": "", "value": 0x01},
        ],
    },
    20: {
        "name": "DVR_SETTING_SENSORSENS",
        "description": "",
        "enabled": False,
        "options": [
            {"name": "SENSOR_SENS_HIGH", "description": "", "value": 0x03},
            {"name": "SENSOR_SENS_MED", "description": "", "value": 0x02},
            {"name": "SENSOR_SENS_LOW", "description": "", "value": 0x01},
        ],
    },
    21: {
        "name": "DVR_SETTING_PIR",
        "description": "",
        "enabled": True,
        "options": [
            {"name": "PIR_ON", "description": "", "value": 0x02},
            {"name": "PIR_OFF", "description": "", "value": 0x01},
        ],
    },
    22: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    23: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    24: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    25: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    26: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    27: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    28: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    29: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    30: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    31: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    32: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    33: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    34: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    35: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    36: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    37: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    38: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    39: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    40: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    41: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    42: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    43: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    44: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    45: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    46: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
    47: {"name": "", "description": "", "enabled": False, "options": [{"name": "", "description": "", "value": 1}]},
}


def create_time_file(file_path: str):
    epoch_time = numpy.int32(int(time.time())).tobytes()
    null_info = numpy.int32().tobytes()

    data_bytes = bytearray()
    # Add epoch time
    data_bytes += epoch_time
    # Add unused timezone information
    data_bytes += null_info
    # Add unused daylight information
    data_bytes += null_info

    # Save new time into file.
    with open(file_path, "wb") as time_file:
        time_file.write(bytes(data_bytes))


def read_time_file(file_path: str):
    table = PrettyTable(field_names=["Epoch time", "Timezone", "Daylight"])
    # Make table alignment to the left
    for field in table.field_names:
        table.align[field] = "l"

    with open(file_path, "rb") as time_file:
        data = time_file.read()
        byte_data = bytearray(data)
        print(f"File {file_path} has {len(byte_data)} bytes.")
        # Get the epoch from the first 4 bytes
        epoch_time = int.from_bytes(byte_data[:4], byteorder="little", signed=False)
        # Convert the integer (epoch time) into more readable format.
        string_epoch = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(epoch_time))
        # Add row to table.
        table.add_row(
            [
                string_epoch,
                int.from_bytes(byte_data[5:8], byteorder="little", signed=False),
                int.from_bytes(byte_data[8:12], byteorder="little", signed=False),
            ]
        )
    # Print time file data in a nicer way
    print(table)


def read_setting_file(file_path: str):
    table = PrettyTable(field_names=["Setting index", "Setting name", "Description", "Value", "Hex value"])
    # Make table alignment to the left
    for field in table.field_names:
        table.align[field] = "l"

    with open(file_path, "rb") as time_file:
        data = time_file.read()
        byte_data = bytearray(data)
        print(f"File {file_path} has {len(byte_data)} bytes.")
        # Loop through the available bytes in the file and get their values.
        for index, byte in enumerate(byte_data):
            # Append value from the file with all its attributes.
            table.add_row(
                [
                    index,
                    SETTINGS.get(index).get("name"),
                    SETTINGS.get(index).get("description"),
                    # Get the name of the value selected.
                    get_option_from_setting(byte_index=index, byte_value=byte),
                    hex(byte),
                ]
            )
        # Print settings file data in a nicer way
        print(table)


def get_option_from_setting(byte_index: int, byte_value: bytes):

    for option in SETTINGS.get(byte_index).get("options"):
        if option.get("value") == byte_value:
            value = option.get("name")
            break
        else:
            value = "Unknown"

    return value


def choose_value(setting: dict) -> bytes:
    print("\n")
    values = {}
    print(f"Select value for {setting.get('name')}:")
    for index, option in enumerate(setting.get("options")):
        # Build option selection
        msg = f"{index}) > {option.get('name')}"
        # Only add description if present
        if option.get("description"):
            msg += f": {option.get('description')}"

        print(msg)
        values[index] = option.get("value")

    selected_value = int(input())

    if selected_value not in values.keys():
        print(f"Selected value {selected_value} is not one of in the available options.")
        return choose_value(setting=setting)

    return values[selected_value]


def create_settings_file(file_path: str) -> bytearray:
    data_bytes = bytearray()

    for index, setting in SETTINGS.items():
        if setting.get("enabled"):
            selected_value = choose_value(setting=setting)
            data_bytes.append(selected_value)
        else:
            data_bytes.append(0xFF)

    with open(file_path, "wb") as time_file:
        time_file.write(bytes(data_bytes))

    print(f"{data_bytes}\n\n{len(data_bytes)}")