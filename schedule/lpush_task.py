# -*- coding: utf-8 -*-
from config import redis_client


def lpush_url():
    with open('i2p_domain.txt', 'r', encoding='utf-8') as f:
        for task_url in f:
            task_url = task_url.strip()
            print(task_url)
            redis_client.lpush("whole", task_url)
        f.close()
    print('任务推送成功')

if __name__ == '__main__':
    lpush_url()
