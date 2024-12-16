from sqlalchemy import Column, Integer, String
from database import Base
from collections import OrderedDict


class Pasien(Base):
    __tablename__ = "tb_pasien"

    id_pasien = Column(Integer, primary_key=True, index=True)
    name_pasien = Column(String, index=True)
    alamat = Column(String)
    jenis_kelamin = Column(String)
    diagnosa = Column(String)

    def to_dict(self):
        return OrderedDict([
            ("id_pasien", self.id_pasien),
            ("name_pasien", self.name_pasien),
            ("jenis_kelamin", self.jenis_kelamin),
            ("alamat", self.alamat),
            ("diagnosa", self.diagnosa),
        ])

