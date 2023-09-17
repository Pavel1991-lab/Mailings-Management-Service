import psycopg2


class DBManager():
    def __init__(self):

        self.is_mail_sent = False

        self.conn = psycopg2.connect(database="male",
                                     user="pavel",
                                     password="password",
                                     host="localhost")
        self.cur = self.conn.cursor()

    def get_mail_time(self):
        self.cur.execute("SELECT mailing_time FROM catalog_product")
        rows = self.cur.fetchall()
        return rows

    def mail(self):
        self.cur.execute("SELECT email FROM catalog_client")
        rows = self.cur.fetchall()
        return rows

    def for_email_prod_id(self):
        self.cur.execute("SELECT email,  product_id FROM catalog_client")
        rows = self.cur.fetchall()
        return rows

    def product_all(self):
        self.cur.execute("SELECT id, topic, description, mailing_time, period FROM catalog_product")
        rows = self.cur.fetchall()
        return rows



