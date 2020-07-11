from sqlalchemy import create_engine
import mysql.connector



engine = create_engine("mysql+mysqlconnector://test:123456@47.105.166.136/dictionary?charset=utf8mb4",
                       max_overflow=0,  # 超过连接池大小外最多创建的连接
                       pool_size=20,  # 连接池大小
                       pool_pre_ping=True,
                       pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
                       pool_recycle=28000  # 多久之后对线程池中的线程进行一次连接的回收（重置）
                       )

