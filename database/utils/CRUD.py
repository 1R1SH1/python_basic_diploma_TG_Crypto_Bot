from typing import Dict, List, TypeVar
from ..common.models import db
from database.common.models import ModelBase

T = TypeVar('T')


def _store_data(db: db, model: T, *data: List[Dict]) -> None:
    with db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(db: db, model: T, *columns: ModelBase) -> None:
    with db.atomic():
        response = model.select(*columns)

    return response

class CRUDInterface():
    @staticmethod
    def create():
        return _store_data(db)
    @staticmethod
    def retrieve():
        return _retrieve_all_data(db)

if __name__ == '__main__':
    _store_data()
    _retrieve_all_data()
    CRUDInterface
