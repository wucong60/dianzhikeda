from dotenv import load_dotenv, find_dotenv
import os
import time
from selenium import webdriver
import pandas as pd
import course_service
import threading

load_dotenv(find_dotenv(filename='.env'))


def get_all_student():
    return pd.read_csv('students.csv', encoding='utf-8')

    print(df['password'].apply(lambda x: x[-6:]))


def run_all():
    df = get_all_student()
    tasks = []
    for index, value in df.iterrows():
        print(index, value['name'])
        task = threading.Thread(target=course_service.execute, args=(value['username'], value['password'][-6:]))
        # task = asyncio.create_task(course_service.execute(value['username'], value['password'][-6:]))
        tasks.append(task)
        # if index > 3:
        #     break
    print('task length', len(tasks))
    # await asyncio.gather(*tasks)

    for t in tasks:
        t.start()
        time.sleep(60)

    for t in tasks:
        t.join()

    if threading.active_count() == 1:
        print('全部做完')


if __name__ == '__main__':
    # asyncio.run(run_all())
    run_all()
