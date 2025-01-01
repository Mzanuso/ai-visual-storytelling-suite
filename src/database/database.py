from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from .models import Base

class Database:
    def __init__(self, connection_string):
        self.engine = create_engine(
            connection_string,
            poolclass=QueuePool,
            max_overflow=10,
            pool_size=5,
            pool_timeout=30
        )
        self.Session = sessionmaker(bind=self.engine)
        
    def create_tables(self):
        """Create all database tables"""
        Base.metadata.create_all(self.engine)
        
    def get_session(self):
        """Get a new database session"""
        return self.Session()
        
    def init_redis(self, redis_url):
        """Initialize Redis connection for caching"""
        import redis
        self.redis = redis.from_url(redis_url)
        
    def cache_set(self, key, value, expire=3600):
        """Set a cached value"""
        if hasattr(self, 'redis'):
            self.redis.setex(key, expire, value)
            
    def cache_get(self, key):
        """Get a cached value"""
        if hasattr(self, 'redis'):
            return self.redis.get(key)
        return None