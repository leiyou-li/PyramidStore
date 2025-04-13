import os
import json
from pathlib import Path

def generate_pyjson():
    # 基础配置
    base_config = {
        "sites": [],
        "parses": [
            {
                "name": "4k",
                "url": "http://156.225.30.142:1001/api/index?parsesId=8&appid=10000&videoUrl=",
                "type": 1,
                "header": {
                    "User-Agent": "Mozilla/5.0"
                }
            },
            {
                "name": "巧计1https://zy.qiaoji8.com/gouzi.php?url=",
                "url": "1",
                "type": 0,
                "header": {
                    "User-Agent": "Mozilla/5.0"
                }
            },
            {
                "name": "巧计2",
                "url": "https://zy.qiaoji8.com/neibu.php?url=",
                "type": 1,
                "header": {
                    "User-Agent": "Mozilla/5.0"
                }
            },
            {
                "name": "虾米1",
                "url": "https://jx.xmflv.com/?url=",
                "type": 0,
                "header": {
                    "User-Agent": "Mozilla/5.0"
                }
            },
            {
                "name": "虾米2",
                "url": "https://jx.xmflv.cc/?url=",
                "type": 0,
                "header": {
                    "User-Agent": "Mozilla/5.0"
                }
            }
        ],
        "flags": [
            "imgo", "youku", "qq", "qq 预告及花絮", "iqiyi", "qiyi", "fun", "letv", "leshi",
            "sohu", "tudou", "xigua", "cntv", "1905", "pptv", "mgtv", "wasu", "bilibili",
            "优酷", "芒果", "芒果TV", "腾讯", "腾讯视频", "奇艺", "爱奇艺", "renrenmi"
        ],
        "lives": [
            {
                "name": "IPTV",
                "type": 0,
                "url": "https://raw.dgithub.xyz/jadehh/iptv-api/master/output/IPTV.m3u",
                "playerType": 2,
                "ua": "okhttp/3.12.13",
                "epg": "https://epg.mxdyeah.top/api/diyp/?ch={name}&date={date}",
                "logo": "https://live.mxdyeah.top/logo/{name}.png"
            },
            {
                "name": "广播",
                "type": 0,
                "url": "https://mirror.ghproxy.com/https://raw.githubusercontent.com/YueChan/Live/main/Radio.m3u",
                "playerType": 1,
                "ua": "okhttp/3.12.13",
                "epg": "https://epg.mxdyeah.top/api/diyp/?ch={name}&date={date}",
                "logo": "https://live.mxdyeah.top/logo/{name}.png"
            }
        ]
    }

    # 特殊配置
    special_configs = {
        "金牌.py": {
            "ext": {
                "site": "https://www.hkybqufgh.com,https://www.sizhengxt.com,https://0996zp.com,https://9zhoukj.com/,https://www.sizhengxt.com,https://www.tjrongze.com,https://www.jiabaide.cn,https://cqzuoer.com"
            }
        }
    }

    # 遍历plugin目录
    plugin_dir = Path("plugin")
    for root, dirs, files in os.walk(plugin_dir):
        for file in files:
            if file.endswith('.py'):
                # 获取相对路径
                rel_path = Path(root).relative_to(plugin_dir)
                file_path = f"./plugin/{rel_path}/{file}" if rel_path != Path('.') else f"./plugin/{file}"
                
                # 获取文件名（不含扩展名）
                name = file[:-3]
                
                # 创建站点配置
                site_config = {
                    "key": file,
                    "name": f"{name}(py)",
                    "type": 3,
                    "api": file_path,
                    "searchable": 1,
                    "quickSearch": 1,
                    "filterable": 1,
                    "order_num": 0,
                    "ext": special_configs.get(file, "")
                }
                
                base_config["sites"].append(site_config)

    # 写入文件
    with open("py.json", "w", encoding="utf-8") as f:
        json.dump(base_config, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_pyjson() 
