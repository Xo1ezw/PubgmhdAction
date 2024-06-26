import os
import traceback

import requests


def post_common(url, params, base_params):
    base_params.update(params)
    try:
        resp = requests.post(url, base_params)
        resp_json = resp.json()
        if resp_json["returnCode"] == 0:
            return resp_json
        else:
            print(resp_json["returnMsg"])
            return None
    except Exception as e:
        print(f"接口{url}异常: {e}")
        traceback.print_exc()
        return None


def post_h5api(url, params):
    common_params = {
        "algorithm": "v2",
        "encode": "2",
        "source": "heping_yingdi",
        "version": "3.1.96i",
        "appid": os.environ["appid"],
        "msdkEncodeParam": os.environ["msdkEncodeParam"],
        "openid": os.environ["openid"],
        "sig": os.environ["sig"],
        "timestamp": os.environ["timestamp"],
        "roleId": os.environ["roleId"],
    }
    return post_common("https://c.gp.qq.com/gp/api/php" + url, params, common_params)


def post_api(url, params):
    common_params = {
        "gameId": "20004",
        "cGameId": "20004",
        "userId": os.environ["userId"],
        "token": os.environ["token"],
    }
    return post_common("https://formal.api.gp.qq.com" + url, params, common_params)
