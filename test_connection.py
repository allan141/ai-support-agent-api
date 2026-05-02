from app.database import engine


try:
    conn = engine.connect()
    print("Conectado com sucesso ao Azure PostgreSQL!")
    conn.close()

except Exception as e:

    print("Erro", e)