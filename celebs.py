#importing sqlite3
import sqlite3
print('sqlite imported')
#connect to data base
conn = sqlite3.connect('celebs.db')
print('database successfull')
#create cursor
c = conn.cursor()
print('cursor successful')
#creating table
# c.execute("""
#           CREATE TABLE celebs(
#               name text,
#               genre text,
#               num_albums int,
#               age int,
#               awards int,
#               year_in_industry int
#             )
# """)
#check
print('celebs created')
#inserting data1
#creating more rows
celeb_list = [('Adele', 'pop_soul', '10', '34', '75', '2006'),
                 ('Aitch', 'hip_hop', '6', '22', '50', '2015'),
                 ('AJ_Tracey', 'hip_hop', '4', '28', '30', '2011'),
                 ('Anne_Marie', 'randb', '12', '31', '55', '2002'),  
                 ('Ariana_Grande', 'randb', '8', '29', '54', '2008'),
                 ('Beyoncé', 'pop', '22', '40', '78', '1997'),
                 ('Billie Eilish', 'electric_pop', '8', '20', '15', '2015'),  
                 ('Blackpink', 'trap', '12', '22', '18', '2015'), 
                 ('Britney_Spears', 'hip_hop', '13', '36', '34', '2009'),  
                 ('Bruno_Mars', 'funk', '22', '26', '32', '2004'),  
                 ('BTS', 'disco', '26', '11', '21', '2010'),
                 ('Calvin_Harris', 'reggea', '35', '28', '54', '2003'),  
                 ('Camila_Cambello', 'hip_hop', '13', '46', '41', '2007'),  
                 ('Cardi_B', 'hip_hop', '10', '30', '70', '2015'),  
                 ('Charlie_Puth', 'randb', '11', '30', '35', '2009'),  
                 ('Rhianna', 'reggea', '4', '36', '89', '2003'),
                 ('David_Guetta', 'hip_hop', '9', '40', '39', '1996'),  
                 ('Demi_Lovato', 'randb', '16', '44', '48', '2010'),   
                 ('Drake', 'disco', '13', '33', '55', '1999'), 
                 ('Ed_Sheeran', 'soft_rock', '7', '45', '90', '2003') 
                ]
#insert multiple rows into table
c.executemany('INSERT INTO celebs VALUES( ?,?,?,?,?,?)', celeb_list)
print('have inserted', c.rowcount, 'records to table celebs.')

# #VIEWING TABLE
# c.execute("SELECT * FROM celebs")

# #FETCH ITEMS
# items = c.fetchall()
# #for item in items:
#   #print(items)
  

# #FORMATTING
# print('NAME' + '\t\t\tGENRE' + '\t\t\tNUM_ALBUMS' + '\t\tAGE' + '\t\tAWARDS', '\t\tYEAR_IN_INDUSRTY')
# print('....' + '\t\t\t.....' + '\t\t\t..........' + '\t\t...' + '\t\t......' + '\t\t...............')
# #LOOPING THROUGH
# for item in items:
#  name, genre, num_albums, age, awards, year_in_industry = item
#  print(f"{name:24}{genre:16}{num_albums:16}{age:19}{awards:18}{year_in_industry:20}")
 
#MOST DECORATED
#MOST POPULAR GENRE
# query = """
#  SELECT * FROM CELEBS
#  WHERE GENRE LIKE 'hip_hop'
#  """
# c.execute(query)
# item = c.fetchall()
# print(f" MOST POPULAR GENRE\n{'-' * 100}")
# #for item in item:
#   #print(item)
  
#   #FORMATTING
# print('NAME' + '\t\t\tGENRE' + '\t\t\tNUM_ALBUMS' + '\t\tAGE' + '\t\tAWARDS', '\t\tYEAR_IN_INDUSRTY')
# print('....' + '\t\t\t.....' + '\t\t\t..........' + '\t\t...' + '\t\t......' + '\t\t...............')
# #LOOPING THROUGH
# for item in item:
#  name, genre, num_albums, age, awards, year_in_industry = item
#  print(f"{name:24}{genre:16}{num_albums:16}{age:19}{awards:18}{year_in_industry:20}")
 
 
 
 
#  #OLDEST CELEBRITY
query = """
 SELECT * FROM CELEBS
 WHERE AGE = 46
 """
c.execute(query)
item = c.fetchall()
print(f" OLDEST CELEB\n{'-' * 100}")
#for item in item:
  #print(item)
  
  #FORMATTING
print('NAME' + '\t\t\tGENRE' + '\t\t\tNUM_ALBUMS' + '\t\tAGE' + '\t\tAWARDS', '\t\tYEAR_IN_INDUSRTY')
print('....' + '\t\t\t.....' + '\t\t\t..........' + '\t\t...' + '\t\t......' + '\t\t...............')
#LOOPING THROUGH
for item in item:
 name, genre, num_albums, age, awards, year_in_industry = item
 print(f"{name:24}{genre:16}{num_albums:16}{age:19}{awards:18}{year_in_industry:20}")
 
#  #LONGEST IN THE INDUSTRY
query = """
 SELECT * FROM CELEBS
 WHERE YEAR_IN_INDUSTRY <= 1996
 """
c.execute(query)
item = c.fetchall()
print(f" LONGEST IN INDUSTRY\n{'-' * 100}")
#for item in item:
  #print(item)
  
  #FORMATTING
print('NAME' + '\t\t\tGENRE' + '\t\t\tNUM_ALBUMS' + '\t\tAGE' + '\t\tAWARDS', '\t\tYEAR_IN_INDUSRTY')
print('....' + '\t\t\t.....' + '\t\t\t..........' + '\t\t...' + '\t\t......' + '\t\t...............')
#LOOPING THROUGH
for item in item:
 name, genre, num_albums, age, awards, year_in_industry = item
 print(f"{name:24}{genre:16}{num_albums:16}{age:19}{awards:18}{year_in_industry:20}")
 
#  #LEAST NUMBER OF ALBUMS
query = """
 SELECT * FROM CELEBS
 WHERE num_albums <= 4
 """
c.execute(query)
item = c.fetchall()
print(f" LEAST NUMBER OF ALBUMS\n{'-' * 100}")
#for item in item:
  #print(item)
  
  #FORMATTING
print('NAME' + '\t\t\tGENRE' + '\t\t\tNUM_ALBUMS' + '\t\tAGE' + '\t\tAWARDS', '\t\tYEAR_IN_INDUSRTY')
print('....' + '\t\t\t.....' + '\t\t\t..........' + '\t\t...' + '\t\t......' + '\t\t...............')
#LOOPING THROUGH
for item in item:
 name, genre, num_albums, age, awards, year_in_industry = item
 print(f"{name:24}{genre:16}{num_albums:16}{age:19}{awards:18}{year_in_industry:20}")
 
#  #MOST DECORATED ARTIST
query = """
 SELECT * FROM CELEBS
 WHERE AWARDS >= 90
 """
c.execute(query)
item = c.fetchall()
print(f" MOST DECORATED\n{'-' * 100}")
#for item in item:
  #print(item)
  
  #FORMATTING
print('NAME' + '\t\t\tGENRE' + '\t\t\tNUM_ALBUMS' + '\t\tAGE' + '\t\tAWARDS', '\t\tYEAR_IN_INDUSRTY')
print('....' + '\t\t\t.....' + '\t\t\t..........' + '\t\t...' + '\t\t......' + '\t\t...............')
#LOOPING THROUGH
for item in item:
 name, genre, num_albums, age, awards, year_in_industry = item
 print(f"{name:24}{genre:16}{num_albums:16}{age:19}{awards:18}{year_in_industry:20}")
 
  
  

