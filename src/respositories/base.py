from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import session
from pydantic import BaseModel


class BaseRepository:
    model = None

    def __init__(self, session):
        self.session = session


    async def get_all(self, **kwargs):
        query = select(self.model)
        results = await self.session.execute(query)

        return results.scalars().all()


    async def get_one_or_one(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        results = await self.session.execute(query)

        return results.scalars().one_or_none()


    async def add(self, data:BaseModel):
        add_data_stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(add_data_stmt)

        return result.scalars().one()


    async def edit(self, data: BaseModel, **filter_by) -> None:
        query = update(self.model).filter_by(**filter_by)
        query = query.values(**data.model_dump())
        await self.session.execute(query)
        await self.session.commit()


    async def delete(self, **filter_by) -> None:
        query = delete(self.model).filter_by(**filter_by)
        await self.session.execute(query)
        await self.session.commit()
