"""
    This file contains configuration for MySQL, Redis, RabbitMQ, etc.
"""

# App Config
IS_NAIVE = False
QUERY_INTERVAL = 10 # seconds
EXPIRE_TIME = 30 # minutes
QUERY_SQL = """
SELECT am_author.name, am_affiliation.name
FROM am_author, am_affiliation
WHERE   am_author.name like %s
    AND am_affiliation.affiliation_id = am_author.last_known_affiliation_id
ORDER BY am_author.author_id DESC
LIMIT 10;
"""

# MySQL
MYSQL_HOST = ""
MYSQL_PORT = 0
MYSQL_USER = ""
MYSQL_PASSWORD = ""
MYSQL_DB = ""
MYSQL_CHARSET = "utf8"

# Redis
REDIS_HOST = ""
REDIS_PORT = 0
REDIS_PASSWORD = ""

# RabbitMQ
RABBITMQ_HOST = ""
RABBITMQ_PORT = 0
QUEUE_NAME = "ace-power-rabbitmq-queue"
