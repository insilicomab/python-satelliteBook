import os
import urllib


# 取得範囲を指定するための関数を定義
def selSquare(lon, lat, delta_lon, delta_lat):
    c1 = [lon + delta_lon, lat + delta_lat]
    c2 = [lon + delta_lon, lat - delta_lat]
    c3 = [lon - delta_lon, lat - delta_lat]
    c4 = [lon - delta_lon, lat + delta_lat]
    geometry = {"type": "Polygon", "coordinates": [[c1, c2, c3, c4, c1]]}
    return geometry


def sel_items(scene_items, product_id):
    item = [
        x.assets
        for x in scene_items
        if x.properties["sentinel:product_id"] == product_id
    ]
    thumbUrl = [
        x.assets["thumbnail"].href
        for x in scene_items
        if x.properties["sentinel:product_id"] == product_id
    ]
    return item, thumbUrl


# URLからファイルをダウンロードする関数を定義
# 引用：https://note.nkmk.me/python-download-web-images/
def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file, open(
            dst_path, "wb"
        ) as local_file:
            local_file.write(web_file.read())
    except urllib.error.URLError as e:
        print(e)


def download_file_to_dir(url, dst_dir):
    download_file(url, os.path.join(dst_dir, os.path.basename(url)))
