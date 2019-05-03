#!/usr/bin/env python3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os

#memasukkan keyword youtube yang ingin di cari
youtubeKeyWord = os.getenv('Key Word Youtube', 'Review Avengers Endgame')

if __name__ == '__main__':
	# Membuat driver/’jembatan’ ke Firefox
	driver = webdriver.Firefox()
	driver.get('https://www.youtube.com/')
	# Mencari tag HTML yang digunakan untuk memasukkan keywords
	keyword_input = driver.find_element_by_name('search_query')
	keyword_input.send_keys(youtubeKeyWord)
	# Melakukan submit form
	search_button = driver.find_element_by_id('search-icon-legacy')
	search_button.submit()
	# Tunggu paling lama 5 detik hingga browser mengembalikan halaman
	# baru
	driver.implicitly_wait(5)
	try:
		 # Jika gagal otomasi, cetak pesan error dari halaman Web ke shell
		 status_message = driver.find_element_by_id('status')
		 print(status_message.text)
	except NoSuchElementException:
		print('Berhasil otomasi browser')
		pass
	# finally:
	# 	# driver.close()
		
		
		
		
		
		
		
		
		
		
		
		