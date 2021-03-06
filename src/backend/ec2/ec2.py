import urllib.request
import json
import logging
import traceback

logger = logging.getLogger("django")

class EC2:
    def __init__(self):
        self.baseurl = "http://169.254.169.254/latest/"
        self.path = {
            "InstanceType": "meta-data/instance-type",
            "InstanceIDDocument": "dynamic/instance-identity/document"
        }
        self.response = dict()

    def __queryAll(self) -> dict:
        try:
            for target in self.path.keys():
                self.query(target)
            return self.response
        except Exception as e:
            raise e

    def query(self, target="") -> dict:
        try:
            if target == "": return self.__queryAll()
            url = self.baseurl + self.path[target]
            response = urllib.request.Request(url)
            with urllib.request.urlopen(response) as data:
                body = data.read().decode("ascii")
                try:
                    self.response[target] = json.loads(body)
                    return self.response
                except json.decoder.JSONDecodeError as e:
                    self.response[target] = body
                    logger.info(traceback.format_exc())
                    return self.response
        except (urllib.error.URLError, OSError) as e:
            self.response["Traceback"] = traceback.format_exc().splitlines()[-1]
            self.response["Message"] = "Maybe this host is not EC2 or Metadata's URL is wrong."
            logger.error(traceback.format_exc())
            return self.response
        except:
            self.response["Traceback"] = traceback.format_exc().splitlines()[-1]
            self.response["Messages"] = "This error is out of scope."
            logger.error(traceback.format_exc())
            return self.response
