from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://ax3radryanprq4dlxucn:pscale_pw_WSn3wVYLbase6eq3I22XX6JN3k0v5yLZEzvogSTzF6v@aws.connect.psdb.cloud/strongcareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args = {
    "ssl":{
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)


with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  result_dict = []
  for row in result.all():
    result_dict.append(dict(row))
  return result_dict
