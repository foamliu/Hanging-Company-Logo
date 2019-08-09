import os

from ocr_utils import detect, get_logger

if __name__ == "__main__":
    logger = get_logger()

    file_list = [f for f in os.listdir('images') if f.endswith('.jpg')]

    for file_name in file_list:
        file_path_name = os.path.join('images', file_name)
        logger.info('filename: ' + file_path_name)
        result = detect(file_path_name)
        # logger.info('seq no: ' + str(result))

        for r in result:
            print(r['words'])
