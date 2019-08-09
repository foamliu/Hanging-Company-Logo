import logging

from aip import AipOcr

appId = '16466063'
apiKey = 'Z2jA1GKZmtIfEOcvjYXqVv0p'
secretKey = 'Vw7OhSLU0gR8h2kKAVvqyAIEpQGh2Mrt'
client = AipOcr(appId, apiKey, secretKey)


def detect(file_path_name):
    with open(file_path_name, 'rb') as f:
        content = f.read()
        api_result = client.basicGeneral(content)  # 调用通用文字识别接口
        # print(api_result)
        words_result = api_result['words_result']

    return words_result


def get_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s \t%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
