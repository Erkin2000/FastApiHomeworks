from sqlalchemy import select
from src.respositories.base import BaseRepository
from src.models.rooms import RoomsOrm


class HotelsRepository(BaseRepository):
    model = RoomsOrm
