import json
import types
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
    # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
    # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
    cred = credential.Credential()
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    httpProfile = HttpProfile()
    httpProfile.endpoint = "hunyuan.tencentcloudapi.com"

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 实例化要请求产品的client对象,clientProfile是可选的
    client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou", clientProfile)

    # 实例化一个请求对象,每个接口都会对应一个request对象
    req = models.ChatCompletionsRequest()
    params = {
        "Model": "hunyuan-vision",
        "Messages": [
            {
                "Role": "user",
                "Contents": [
                    {
                        "Type": "text",
                        "Text": "下面图片中是哪个公司的 Logo？"
                    },
                    {
                        "Type": "image_url",
                        "ImageUrl": {
                            "Url": "https://cloudcache.tencent-cloud.com/qcloud/ui/portal-set/build/About/images/bg-product-series_87d.png"
                        }
                    }
                ]
            }
        ],
        "Stream": False
        #"Stream": True

    }
    req.from_json_string(json.dumps(params))

    # 返回的resp是一个ChatCompletionsResponse的实例，与请求对象对应
    resp = client.ChatCompletions(req)
    # 输出json格式的字符串回包
    if isinstance(resp, types.GeneratorType):  # 流式响应
        for event in resp:
            print(event)
    else:  # 非流式响应
        print(resp)


except TencentCloudSDKException as err:
    print(err)
