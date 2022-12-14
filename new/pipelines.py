# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface

class NewPipeline:
        def open_spider(self, spider):
            db = spider.settings.get('MYSQL_DB_NAME', 'bilibili')
            host = spider.settings.get('MYSQL_HOST', 'localhost')
            port = spider.settings.get('MYSQL_PORT', 3306)
            user = spider.settings.get('MYSQL_USER', 'root')
            passwd = spider.settings.get('MYSQL_PASSWORD', 'iii459303')

            self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
            self.db_cur = self.db_conn.cursor()

        # 关闭数据库
        def close_spider(self, spider):
            self.db_conn.commit()
            self.db_conn.close()

        # 对数据进行处理
        def process_item(self, item, spider):
            self.insert_db(item)
            return item

        # 插入数据
        def insert_db(self, item):
            values = (
                item['name'],
                item['view'],
                item['thumb'],
                item['coin'],
                item['favor'],
                item['forward']
            )
            sql = 'INSERT INTO bigdata VALUES(%s,%s,%s,%s,%s,%s)'
            self.db_cur.execute(sql, values)
