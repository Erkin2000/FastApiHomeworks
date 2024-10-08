from sqlalchemy import select, func, insert

from src.database import engine
from src.respositories.base import BaseRepository
from src.models.hotels import HotelsOrm
from src.schemas import hotels


class HotelsRepository(BaseRepository):
    model = HotelsOrm

    async def get_all(
            self,
            location,
            title,
            limit,
            offset,
            sorter,
    ):
        query = select(HotelsOrm).order_by(HotelsOrm.id)

        if sorter == True:
            query = select(HotelsOrm).order_by(HotelsOrm.id).order_by('-id')

        if location:
            query = query.filter(func.lower(HotelsOrm.location).contains(location.strip().lower()))
        if title:
            query = query.filter(func.lower(HotelsOrm.title).contains(title.strip().lower()))
        query = (
            query
            .limit(limit)
            .offset(offset)
        )
        results = await self.session.execute(query)

        return results.scalars().all()


    # async def add(self, data: hotels):
    #     add_hotel_stmt = insert(self.model).values(**data.model_dump())
    #     print(add_hotel_stmt.compile(engine, compile_kwargs={"literal_binds": True}))
    #     results = await self.session.execute(add_hotel_stmt)
    #
    #     return results
