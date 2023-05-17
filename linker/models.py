from sqlalchemy import Column, Integer, String, DateTime, func

from database.database import Base, engine


class Facility(Base):
    __tablename__ = "facility"

    index = Column(String, primary_key=True, index=True)
    sort = Column(String, index=True)
    address = Column(String)
    description = Column(String)
    status = Column(Integer, index=True)
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='修改时间')


Base.metadata.create_all(bind=engine)
