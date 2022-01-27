
import psycopg2

conn = psycopg2.connect(dbname = 'crm_test', user = 'postgres')
cursor = conn.cursor()