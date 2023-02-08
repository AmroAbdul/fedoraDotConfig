#!/bin/python
# Google Earth view wallpaper Downloader https://earthview.withgoogle.com/
# Author: Amro Abdulvahit 
# License: ???
import random
import shutil
import requests as req
# import logging



DATA_URL = "https://earthview.withgoogle.com/_api/photos.json"
# logger = logging.getLogger("variety")
random.seed()

# class EarthViewDownloader():
#     DESCRIPTION = _("Google Earth View Wallpapers")
#     ROOT_URL = "https://earthview.withgoogle.com/"
#     def download_queue_item(self, item):
#         item = req.get("https://earthview.withgoogle.com/_api/" + item["slug"] + ".json").json
#         region = item["region"]
#         filename = "{}{} (ID-{}).jpg".format(
#             region + ", " if region and region != "-" else "", item["country"], item["id"]
#         )
#         origin_url = EarthviewDownloader.ROOT_URL + str(item["slug"])
#         image_url = item["photoUrl"]
#         if not image_url.startswith("http"):
#             image_url = "https://" + image_url

#         return self.save_locally(
#             origin_url, image_url, local_filename=filename, extra_metadata=extra_metadata
#         )

def download_queue_item(self, item):
        item = req.get("https://earthview.withgoogle.com/_api/" + item["slug"] + ".json").json
        region = item["region"]
        filename = "{}{} (ID-{}).jpg".format(
            region + ", " if region and region != "-" else "", item["country"], item["id"]
        )
        origin_url = EarthviewDownloader.ROOT_URL + str(item["slug"])
        image_url = item["photoUrl"]
        if not image_url.startswith("http"):
            image_url = "https://" + image_url
        res = req.get(image_url, stream = True)
        # if res.status_code == 200:
        #     with open(file_name,'wb') as f:
        #     shutil.copyfileobj(res.raw, f)
        #     print('Image sucessfully Downloaded: ',item)
        # else:
        #     print('Image Couldn\'t be retrieved')
        
download_queue_item