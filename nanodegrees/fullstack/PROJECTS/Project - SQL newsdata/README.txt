Logs Analysis Project
-------------

Logs Analysis Project is the first project in the Udacity Fullstack 
nanodgree part 3 Backend and Database Application . This document details 
how to initiate to the news database then run the reporting tool that
prints out reports (in plain text) based on the data in the database.

To Prepare the software and data
 1 - Install the virtual machine
   Follow instruction in Lesson 2: Elements of SQL Installing the Virtual Machine
 2 - Download the The data
    https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

To load the data to the news database, use the command  

   psql -d news -f newsdata.sql
   
To run to report tool, use the command     

   python2 reporting_tool.py

To Explore the data Once you have the data loaded into your database, connect to 
your database using psql -d news and explore the tables.

news=> \dt
          List of relations
 Schema |   Name   | Type  |  Owner
--------+----------+-------+---------
 public | articles | table | vagrant
 public | authors  | table | vagrant
 public | log      | table | vagrant
(3 rows)

The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site

To explore the data in the tables, use the command    

	news=> select * from articles;

	news=> select * from authors;

	news=> select * from log limit 50;
	
	
The reporting_tool.py uses python psycopg2 module to fetch data from the postgresql DB, 
separating each query in smallers tables by using SQL's VIEW, in order the narrow down 
to tables containing the answers for:

Q1 - What are the most popular three articles of all time?
Q2 - Who are the most popular article authors of all time?
Q3 - On which days did more than 1% of requests lead to errors?

Detailed query explanation for Q1.

   Step 1 - Find the top 3 total of views per article 
         
   Step 2 -  Find the article title for each row in step 1.
          -  These query matchs slug in article with path by using the like operator.
		  -  in order to find the title.
		  
   Step 3 - Print formatted output
   

Detailed query explanation for Q2.

    Step 1 - Find the total of views per article
	       - CREATE VIEW topthree AS
		
	Step 2 - Find the author of each row in the first query

    Step 3 - SUM the total articles views by author 

	Step 4 - Print formatted output
		
Detailed query explanation for Q3.

	Step 1 - Create view table of DAY | TOTAL_Req 
	           CREATE VIEW allreq AS
	       - time::timestamp::date will cast from 
		   - '2016-07-01 07:00:00+0' to '2016-07-0'
		       SELECT time::timestamp::date as day
	 
	Step 2 - Create view table of DAY | Failed_Req = '404 NOT FOUND'
		       CREATE VIEW badreq AS
	 
	Step 4 - Return values where more than 1% of requests lead to errors
	       - to_char will format day '2016-07-31' to 'Jul 31, 2016'
 
	Step 5 - Print formatted output	   

	