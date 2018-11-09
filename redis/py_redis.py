import  redis
from redis import *
#red = StrictRedis(host='192.168.200.100', port=6379, db=1)
if __name__=="__main__":
    try:
        #创建StrictRedis对象，与redis服务器连接
        redis=StrictRedis(host='192.168.200.100', port=6379, db=1)

        # 新增一个string类型
        result=redis.set('name','xianyuplus')
        # 成功打印True,失败打印False
        print(result)

        #获取键name的值
        result = redis.get('name')
        #输出键的值，如果键不存在则返回None
        print(result)

        #设置键name的值，如果键已经存在则进行修改，如果键不存在则进行添加
        result = redis.set('name','xianyu')
       #输出响应结果，如果操作成功则返回True，否则返回False
        print(result)


        #result = redis.delete('name')
        #输出响应结果，如果删除成功则返回受影响的键数，否则则返回0
        #print(result)

        #获取所有的键
        #result=sr.keys()
        #输出响应结果，所有的键构成⼀个列表，如果没有键则返回空列表
        #print(result)
    except Exception as e:
        print(e)
