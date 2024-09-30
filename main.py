import urllib.request
import re
import os
import sys
import sqlite3

def read_file(filename, lineNumber):
        try:
                with open(filename, 'r') as file:
                        for i, line in enumerate(file):
                                if i == lineNumber -1:
                                        return line.strip()
        except FileNotFoundError:
                print("File is not found save as input.txt")
                return None

def userInput():
        filename = 'input.txt'
        lineNumber = 1
        url = read_file(filename, lineNumber)
        lineNumber = 2
        format_choice = read_file(filename, lineNumber)

        imgOp = None

        if format_choice == '1':
                htmlInput(url)
        elif format_choice == '2':
                imgOp = input('Would you to Download the Images or save to Database type? (Down/Save): ')
        if imgOp == 'Down':
                download_image(url, filename = "image.jpg")
        elif imgOp == 'Save':
                urlimage(url)
        elif format_choice == '3':
                metaData(url)
        elif format_choice == '4':
                urlInput(url)
        elif format_choice == '5':
                htmlInput(url)
                download_image(url, filename = "image.jpg")
                urlInput(url)
                metaData(url)
        else:
                print("Please enter a vaild format ")


def htmlInput(url):
        text = urllib.request.urlopen(url)
        text_bytes = text.read()
        text_str = text_bytes.decode("utf8")
        print(text_str)

def urlInput(url):
        try:
                text = urllib.request.urlopen(url)
                text_bytes = text.read()
                htmlContent = text_bytes.decode("utf8")
                hrefs = re.findall(r'href="https://(.*?)"', htmlContent)

                connection = sqlite3.connect('dataHarvest.db')
                cursor = connection.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS urls (
                                id INTEGER PRIMARY KEY,
                                dataUrl TEXT
                                )''')

                for href in hrefs:
                        newHrefs = ("https://" + href)
                        cursor.execute("INSERT INTO urls (dataUrl) VALUES (?)", (newHrefs,))

                cursor.execute("SELECT * FROM urls")
                rows = cursor.fetchall()
                for row in rows:
                        print(row)
                connection.commit()
                connection.close()
                print("All file where stored in DB: urls\n")
                print("RUN: sqlite3 'dataHarvest.db'\n ")
                print("RUN  SELECT * from urls\n")
                print("To view sql table\n")
        except Exception as e:
                print("Error:", e)


def metaData(url):
        try:
                text = urllib.request.urlopen(url)
                text_bytes = text.read()
                htmlContent = text_bytes.decode("utf8")
                title = re.findall(r'<title>(.*?)</title>', htmlContent)
                description = re.findall(r'<meta property="og:description" content="(.*?)"', htmlContent)
                icon = re.findall(r'<link rel="icon" href="(.*?)"', htmlContent)
                for titles in title:
                        print("Titles: " + titles)
                for descriptions in description:
                        print("Description: " + descriptions)
                for icons in icon:
                        print("Visit icon URL: " + icons)

                connection = sqlite3.connect('dataHarvest.db')
                cursor = connection.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS metaData (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                description TEXT,
                                icon TEXT
                                )''')
                cursor.execute("INSERT INTO metaData (title, description, icon) VALUES (?,?,?)", (title[0] if title else None, description[0] if description else None, icon[0] if icon else None))
                cursor.execute("SELECT * from metaData")
                rows = cursor.fetchall()
                connection.commit()
                connection.close()
                print("All file where stored in DB: metaData\n")
                print("RUN: sqlite3 'dataHarvest.db'\n ")
                print("RUN  SELECT * from metaData\n")
                print("To view sql table\n")
        except Exception as e:
                print("Error:", e)
def download_image(url, filename):
        try:
                with urllib.request.urlopen(url) as response:
                        html_content = response.read().decode("utf-8")
                image_urls = re.findall(r'<img.*?src="(.*?)"', html_content)
                if not os.path.exists("images"):
                        os.makedirs("images")
                for idx, image_url in enumerate(image_urls):
                        filename = f"images/image_{idx+1}.jpg"
                        urllib.request.urlretrieve(image_url, filename)
                        print(f"Downloaded image {idx+1} from {image_url} to {filename}")
        except Exception as e:
                print("Failed to download images from URL:", e)

def urlimage(url):
        try:
                with urllib.request.urlopen(url) as response:
                        html_content = response.read().decode("utf-8")
                        image_urls = re.findall(r'<img.*?src="(.*?)"', html_content)
                if not image_urls:
                        print('There were no images in this URL')
                else:

                        connection = sqlite3.connect('dataHarvest.db')
                        cursor = connection.cursor()

                        cursor.execute('''CREATE TABLE IF NOT EXISTS images (
                                                id INTEGER PRIMARY KEY,
                                                url TEXT
                                        )''')

                        for idx, image_url in enumerate(image_urls):
                                cursor.execute("INSERT INTO images (url) VALUES (?)", (image_url,))
                        cursor.execute("SELECT * from images")
                        rows = cursor.fetchall()
                        for row in rows:
                                print(row)

                        connection.commit()
                        connection.close()
                        print("All file where stored in DB: images\n")
                        print("RUN: sqlite3 'dataHarvest.db'\n ")
                        print("RUN  SELECT * from images\n")
                        print("To view sql table\n")
                        return image_urls
        except Exception as e:
                print("Failed to download images from URL:", e)
                return[]

userInput()


