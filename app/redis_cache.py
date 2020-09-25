"""redis_cache.py"""
import os
import redis


def get_redis_connection():
    """
    :return: Redis connection
    """
    redis_connection = redis.Redis(host=os.getenv("REDIS_URL"), port=os.getenv("REDIS_PORT"),
                                   charset="utf-8", decode_responses=True)
    return redis_connection


def redis_put(short_url, full_url):
    """
    :param short_url: short_url
    :param full_url: full_url
    :return: None
    """
    redis_connection = get_redis_connection()
    redis_connection.set(short_url, full_url)


def redis_get(short_url):
    """
    :param short_url: short_url
    :return: returns short_url if present in cache
    """
    redis_connection = get_redis_connection()
    return redis_connection.get(short_url)
