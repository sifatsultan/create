import random
import time
from datetime import datetime


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)


def random_date_time(start, end, prop):
    return  strTimeProp(start, end, '%Y-%m-%d %I:%M %p', prop)

def customer():
    # customer_id, name, date_of_birth, email
    tablename = input('Enter table name for CUSTOMER details ')
    populatefile = open('populate_customer.txt', 'w')
    namefile = open('randomnames.txt', 'r')

    names = namefile.read().splitlines()
    namefile.close()

    newnames = []
    for name in names:
        if name:
            newnames.append(name)

    sql =   'INSERT INTO '+tablename+'\n'
    sql +=  'VALUES \n'


    # Creating random dates list for date of birth...
    dates = []
    for i in range(50):
        year = random.randint(1990, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        birth_date = datetime(year, month, day)
        dates.append(birth_date)

    count = 0
    for name in newnames:
        count += 1
        splitname = name.split()

        firstname = splitname[0]
        lastname = splitname[1]
        email = firstname.lower()+'@gmail.com'
        date_of_birth = str(dates[count-1])

        sql +=	"   ("
        sql += 	"'" +  "{:<12}".format(firstname+"',")
        sql += 	"'" +  "{:<12}".format(lastname+"',")
        sql += 	"{:<15}".format("'"+date_of_birth+"',")
        sql += 	"{:<20}".format("'"+email+"'")
        sql +=  ")"
        if count < len(newnames):
            sql += ","
        sql += "\n"


    print(" 'customer' populate script is successfully built")
    populatefile.write(sql)
    populatefile.close()


def reviews():
    tablename = input('Enter table name for "review" details ')
    sql =   'INSERT INTO '+tablename+'\n'
    sql +=  'VALUES \n'


    f = open('randomtext.txt','r')
    review_text = []
    text = f.read().split(".")
    for t in text:
        if t:
            review_text.append(t.strip('\n').strip())

    count = 0
    movienum = 20

    for i in range(1,movienum):
        count += 1
        movie_id_sql = str(i) + ","

        number_of_reviews = random.randint(1,25)
        custome_id_random = random.sample(range(1,50), number_of_reviews)
        for j in range(1, number_of_reviews):
            customer_id = custome_id_random[j]
            k = random.randint(0,50)
            review = review_text[k]
            rating = random.randint(0,5)
            date = random_date_time("2015-01-05 1:30 PM", "2015-07-28 4:50 PM", random.random())

            customer_id_sql =  str(customer_id) +","
            review_rating_sql = str(rating) + ","
            review_content_sql  = " ' " + review + " ' " + " , "
            review_datetime_sql	= " ' " + date + " ' "

            sql += "    (" + movie_id_sql + customer_id_sql + review_content_sql + review_rating_sql+review_datetime_sql+")"
            if count < movienum:
                sql +=","
            sql += "\n"

    print("'review' populate script is successfully built")
    f = open('populate_review.txt','w')
    f.write(sql)
    f.close()


def tickets():
    session_id_count = 17
    customer_id_count = 50

    sql = ""
    table = input("Enter the table you wish to store your 'tickets' detail ")
    sql = 'INSERT INTO ' + table + '\n'
    sql += 'VALUES \n'

    count = 0
    for i in range(1,session_id_count):
        count += 1
        for j in range(1,20):
            random_customer_id = random.randint(1,50)
            session_id_sql = str(i)
            customer_id_sql = str(random_customer_id)
            sql += '    (' + "{:<4}".format(customer_id_sql) + ',' + "{:<3}".format(session_id_sql) + ')'
            sql += ',\n'

    filename = 'populate_tickets.txt'
    f = open(filename,'w')
    f.write(sql)
    f.close()
    print(' "tickets" populate script is successfully built in '+filename)


def main():
    customer()
    reviews()
    tickets()

main()
