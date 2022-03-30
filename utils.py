import json
import os
import time
import traceback


def cache_json_data(data: dict, cache_main_name: str) -> bool:
    """

    :param cache_main_name:
    :param data:
    :return:
    """

    try:
        if not os.path.exists("cache"):
            os.mkdir("cache")

        cahce_file_name = f"{cache_main_name}_{time.strftime('%Y%m%d_%H%M%S', time.localtime())}.json"
        cache_full_name = os.path.join("cache", cahce_file_name)

        with open(cache_full_name, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        return True
    except:
        traceback.print_exc()  # Почитать про конструкцию print_exc
        return False


if __name__ == '__main__':
    cache_json_data("1234", "avito_avto")
