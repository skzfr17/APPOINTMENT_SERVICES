from sqlalchemy.orm import Session
from models import Pasien

def create_pasien(db: Session, name_pasien: str, alamat: str, jenis_kelamin: str, diagnosa: str):
    db_pasien = Pasien(name_pasien=name_pasien, alamat=alamat, jenis_kelamin=jenis_kelamin, diagnosa=diagnosa)
    db.add(db_pasien)  # Menambahkan pasien baru ke sesi
    db.commit()  # Menyimpan perubahan ke database
    db.refresh(db_pasien)  # Mendapatkan data pasien yang baru ditambahkan
    return db_pasien

def get_pasien(db: Session):
    return db.query(Pasien).all()  # Mengambil semua data pasien dari database

def get_pasien_by_id(db: Session, pasien_id: int):
    return db.query(Pasien).filter(Pasien.id_pasien == pasien_id).first()

def update_pasien(db: Session, pasien_id: int, name_pasien: str, alamat: str, jenis_kelamin: str, diagnosa: str):
    pasien = db.query(Pasien).filter(Pasien.id_pasien == pasien_id).first()  # Mencari pasien berdasarkan ID
    if pasien:
        pasien.name_pasien = name_pasien  # Memperbarui nama pasien
        pasien.alamat = alamat  # Memperbarui alamat pasien
        pasien.jenis_kelamin = jenis_kelamin  # Memperbarui jenis kelamin
        pasien.diagnosa = diagnosa  # Memperbarui diagnosa pasien
        db.commit()  # Menyimpan perubahan ke database
        db.refresh(pasien)  # Mendapatkan data pasien yang telah diperbarui
        return pasien
    return None  # Jika pasien tidak ditemukan, kembalikan None

def delete_pasien(db: Session, pasien_id: int):
    pasien = db.query(Pasien).filter(Pasien.id_pasien == pasien_id).first()  # Mencari pasien berdasarkan ID
    if pasien:
        db.delete(pasien)  # Menghapus pasien dari database
        db.commit()  # Menyimpan perubahan ke database
        return True  # Berhasil menghapus pasien
    return False  # Jika pasien tidak ditemukan




