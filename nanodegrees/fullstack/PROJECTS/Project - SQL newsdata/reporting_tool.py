#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 17:42:32 2017
A program to creates a reporting tool that prints out reports (in plain text)
based on the data in the news database.
@author: Silva
"""

import psycopg2

# template for the view output
template1 = '''
    "%s" — %s views
'''

# template for the error output
template2 = '''
    %s — %s%% errors
'''


def get_most_popular_articles():
    """
    Return the most popular three articles of all time.
    """

    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()

    cursor.execute("""
                   CREATE VIEW topthree AS
                   SELECT path , count(*) as sum
                   FROM log WHERE path like '%article%'
                   AND status = '200 OK'
                   GROUP BY path
                   ORDER BY sum DESC
                   LIMIT 3;

                   SELECT articles.title,topthree.sum
                   FROM   topthree, articles
                   WHERE  topthree.path like '%'||articles.slug||'%'
                   ORDER BY topthree.sum DESC
                   """,
                   )

    db_results = cursor.fetchall()

    db.close()

    answer = "".join(template1 % (title, num) for title, num in db_results)

    print("1. What are the most popular three articles of all time?\n" +
          str(answer))


def get_most_popular_author():
    """
    Return the most popular article authors of all time.
    """

    db = psycopg2.connect("dbname=news")

    cursor = db.cursor()

    cursor.execute("""
                   CREATE VIEW toparticles AS
                   SELECT path , count(*) as sum
                   FROM log WHERE path like '%article%'
                   AND status = '200 OK'
                   GROUP BY path
                   ORDER BY sum DESC;

                   CREATE VIEW toparticles2 AS
                   SELECT authors.name,toparticles.path,toparticles.sum
                   FROM   toparticles, articles,authors
                   WHERE  toparticles.path like '%'||articles.slug||'%'
                   AND authors.id = articles.author
                   ORDER BY toparticles.sum DESC;

                   SELECT data.name, SUM(sum)
                   FROM   toparticles2 as data
                   GROUP BY data.name
                   ORDER BY sum DESC
                   """,
                   )

    db_results = cursor.fetchall()

    db.close()

    answer = "".join(template1 % (name, sum) for name, sum in db_results)

    print("2. Who are the most popular article authors of all time?\n" +
          str(answer))


def get_failed_requestes():
    """
    Return the days where more than 1% of requests lead to errors.
    """

    db = psycopg2.connect("dbname=news")

    cursor = db.cursor()

    cursor.execute("""
                   CREATE VIEW allreq AS
                   SELECT time::timestamp::date as day , COUNT(status) as num
                   FROM   log
                   GROUP BY day
                   ORDER BY day DESC;

                   CREATE VIEW badreq AS
                   SELECT time::timestamp::date as day , COUNT(status) as num
                   FROM   log
                   WHERE  status = '404 NOT FOUND'
                   GROUP BY day
                   ORDER BY day DESC;

                   CREATE VIEW badreq2 AS
                   SELECT a.day as day, ROUND( 100.0 * (b.num*1.0/(a.num)),1)
                   as num_per
                   FROM badreq as b, allreq as a
                   WHERE b.day = a.day;

                   SELECT to_char(day,'Mon DD, YYYY'), num_per FROM badreq2
                   WHERE num_per > 1;
                   """,
                   )

    db_results = cursor.fetchall()
    db.close()

    answer = "".join(template2 % (day, errors) for day, errors in db_results)

    print("3. On which days did more than 1% of requests lead to errors?\n" +
          str(answer))


if __name__ == '__main__':
    get_most_popular_articles()
    get_most_popular_author()
    get_failed_requestes()
