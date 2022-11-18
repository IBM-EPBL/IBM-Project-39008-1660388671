from flask import Flask
import ibm_db


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bvx19292;PWD=yDuuJH7Oqdzbnxnk;", "", "")
print(conn)
print("connection successful...")