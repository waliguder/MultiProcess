import multiprocessing
import time


class MultiProcessPool(object):
    def __init__(self,num):
        self.pool = multiprocessing.Pool(processes=num)  # 创建一个进程池，并发执行任务
        self.result = []  # 收集处理结果

    # 运行相对应的任务
    def run(self, func, args):
        self.result.append(self.pool.apply_async(func, (args,)))

    # 保持进程运行为止
    def keepToDone(self):
        self.pool.close()
        self.pool.join()

    # 获取返回结果
    def getResult(self):
        return self.result
