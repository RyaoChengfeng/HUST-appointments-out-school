import yaml
import os
import logging

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
env = os.getenv('ENVIRONMENT', "config")
# 获取yaml文件路径
yamlPath = os.path.join(curPath, str(env) + ".yml")
try:
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    Config = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
except Exception as e:
    # logger.error(e)
    raise e
else:
    # logger.info("读取配置文件:" + yamlPath)
    print("读取配置文件:" + yamlPath)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S')

log = logger = logging
