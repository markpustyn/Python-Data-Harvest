Data Harvest Inc. - Web Scraper

A Python-based online web scraper designed to gather important information including images, text, HTML, metadata, and links, all sorted and stored in a local SQL database.
![Screenshot 2024-09-30 103853](https://github.com/user-attachments/assets/09869de6-d291-4597-857a-fb3db543d2a9)


    Note: It is recommended to run this program on a Linux distribution or Windows Subsystem for Linux (WSL) to properly execute the .sh (shell) scripts.

![Screenshot 2024-09-30 103938](https://github.com/user-attachments/assets/12695f4b-283a-4a02-90bf-43d68daf39b4)
    Note: Run sudo apt install sqlite3 to install needed sql to run program. 
To view saved data in the database to enter Sql shell. 

RUN: sqlite3 'dataHarvest.db'

Example: RUN  SELECT * from metaData; or SELECT * FROM urls;

Saved images will be stored in /Images folder. 

![Screenshot 2024-09-30 104833](https://github.com/user-attachments/assets/b81c9be5-3760-405b-8604-74c891635ea1)




