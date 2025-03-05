import requests
from bs4 import BeautifulSoup
import argparse

def find_upload_form(url):
    try:
        # Mengirim permintaan GET ke URL
        response = requests.get(url)
        response.raise_for_status()  # Memastikan permintaan berhasil

        # Parsing konten HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Mencari formulir dengan metode POST
        forms = soup.find_all('form', method='post')

        for form in forms:
            # Mencari input file dalam formulir
            file_inputs = form.find_all('input', type='file')
            if file_inputs:
                print(f"Formulir upload ditemukan di: {url}")
                print("Formulir HTML:")
                print(form.prettify())
                return
        print(f"Tidak ditemukan formulir upload di: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengakses {url}: {e}")

def main():
    # Mengatur argumen baris perintah
    parser = argparse.ArgumentParser(description='Cari formulir upload file pada situs web.')
    parser.add_argument('url', type=str, help='URL situs web yang ingin diuji')
    args = parser.parse_args()

    # Menjalankan pencarian formulir upload pada URL yang dimasukkan
    find_upload_form(args.url)

if __name__ == '__main__':
    main()