FAIRPLAY_HDCP_ENFORCEMENT = (-1, 0, 1)

HDCP_NONE = FAIRPLAY_HDCP_ENFORCEMENT[0]  # 'HDCP_NONE'
HDCP_TYPE_0 = FAIRPLAY_HDCP_ENFORCEMENT[1]  # 'HDCP_TYPE_0'
HDCP_TYPE_2 = FAIRPLAY_HDCP_ENFORCEMENT[2]  # 'HDCP_TYPE_2',


def check(hdcp_enforcement):
    return hdcp_enforcement in FAIRPLAY_HDCP_ENFORCEMENT