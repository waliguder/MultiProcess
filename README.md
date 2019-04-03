# MultiProcess
python 多进程池+多线程执行指定任务

在python中，在处理大量数据的时候，为了提高处理速度，尽可能的多利用系统的资源。可以使用多进程加多线程处理数据任务。

这里提供一个简易的进程+多线程的项目框架

首先，初始化一个进程池，可指定进程数量
=
```python
# 初始化进程池的数量为2
mtpool = InitProcessing.MultiProcessPool(2)
```

其次，定义一个任务列表，可自定义传入参数
=
```python
 # 任务列表 【 任务模块，任务文件】
 task = [['task1', 'a'], ['task2', 'b']]
``` 

之后就可启动进程池
```python
   for idx in task:
       mtpool.run(wokers, idx)

# 这句代码可以让主进程保持阻塞，等待子进程执行完成后继续执行，如不添加，则主进程后面的代码会直接执行完毕。
mtpool.keepToDone()

# 获取任务执行完毕的返回值，必须保证任务程序有return值
result = mtpool.getResult()

# 可循环结果列表，每个进程的返回值都在这里面
    for res in result:
        print(":::", res.get())
    print("所有进程已完成任务.")
    
   
 # 任务执行函数，进程执行的方法，可以理解为，子进程的主程序
def wokers(msg):
    print("msg:执行任务%s" % msg[0])
    threads = []
    p = threading.Thread(target=mainThreadProd, args=(q, msg[0] + '.txt', msg[1]))
    threads.append(p)
    c = threading.Thread(target=logThreadCons, args=(q, msg[0] + '.txt',), daemon=True)
    threads.append(c)
    for t in threads:
        t.setDaemon(True)
        t.start()
    threads[0].join()
    print("%s end" % msg[0])
    return "done %s" % msg[1]
```
