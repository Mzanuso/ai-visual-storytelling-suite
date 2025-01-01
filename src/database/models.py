from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class SREF(Base):
    __tablename__ = 'srefs'
    
    id = Column(Integer, primary_key=True)
    sref_id = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    metadata = Column(JSON)
    analysis = Column(JSON)
    category = Column(String)
    tags = Column(JSON)
    
    # Relationships
    variations = relationship('SREFVariation', back_populates='sref')
    scenes = relationship('Scene', back_populates='sref')

class SREFVariation(Base):
    __tablename__ = 'sref_variations'
    
    id = Column(Integer, primary_key=True)
    sref_id = Column(Integer, ForeignKey('srefs.id'))
    variation_type = Column(String)  # upscale, variation
    image_path = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    metadata = Column(JSON)
    
    # Relationships
    sref = relationship('SREF', back_populates='variations')

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(JSON)
    
    # Relationships
    scenes = relationship('Scene', back_populates='project')

class Scene(Base):
    __tablename__ = 'scenes'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    sref_id = Column(Integer, ForeignKey('srefs.id'))
    sequence = Column(Integer)
    duration = Column(Float)
    script = Column(String)
    metadata = Column(JSON)
    
    # Relationships
    project = relationship('Project', back_populates='scenes')
    sref = relationship('SREF', back_populates='scenes')