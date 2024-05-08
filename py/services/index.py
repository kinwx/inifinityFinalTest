# pip install mysql-connector-python
from mysql import connector

class mysqlConnection:
    def __init__(self) -> None:
        self.credentials = {
            "host": "localhost",
            "user": "root",
            "password": "Mysql102030",
            "database": "to_do_list"
        }
    
    def insertTask(self, title, descriptionTask, earlyDate, lastDate):
        try:
            connection = connector.connect(**self.credentials)
            if connection.is_connected():
                print("Conexão MySQL - ON.")

            cursor = connection.cursor()
            insert_query = ("INSERT INTO tasks "
                            "(title, description_task, early_date, last_date) "
                            "VALUES (%s, %s, %s, %s)")
            task_data = (title, descriptionTask, earlyDate, lastDate)

            cursor.execute(insert_query, task_data)
            connection.commit()

            print("Dados inseridos com sucesso na tabela (tasks)!")

        except connector.Error as error:
            print("Erro ao inserir dados:", error)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexão MySQL - OFF.")

    def insertInTable(self, tableName, id, title, descriptionTask, earlyDate, lastDate):
        try:
            connection = connector.connect(**self.credentials)
            if connection.is_connected():
                print("Conexão MySQL - ON.")

            cursor = connection.cursor()
            insert_query = (f"INSERT INTO {tableName} "
                            "(id, title, description_task, early_date, last_date) "
                            "VALUES (%s, %s, %s, %s, %s)")
            task_data = (id, title, descriptionTask, earlyDate, lastDate)

            cursor.execute(insert_query, task_data)
            connection.commit()

        except connector.Error as error:
            print("Erro ao inserir dados:", error)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print(f"Dados inseridos com sucesso na tabela ({tableName})!")
                print("Conexão MySQL - OFF.")

    def getTasks(self, tableName):
        try:
            connection = connector.connect(**self.credentials)
            if connection.is_connected():
                print("Conexão MySQL - ON.")

            cursor = connection.cursor()
            select_query = (f"SELECT * FROM {tableName}")
            cursor.execute(select_query)

            tasks = cursor.fetchall()

        except connector.Error as error:
            print("Erro ao recuperar dados:", error)
            return False

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print(f"Os Dados da tabela ({tableName}) foram carregados!")
                print("Conexão MySQL - OFF.")

            return tasks

    def deleteTask(self, tableName, taskId):
        try:
            connection = connector.connect(**self.credentials)
            if connection.is_connected():
                print("Conexão MySQL - ON.")
            cursor = connection.cursor()
            delete_query = (f"DELETE FROM {tableName} WHERE id = %s")
            # mano precisa dessa virgula pq como só há um elemento ele nao entenderia como tupla, chatgpt passou essa visão, confesso!
            task_data = (taskId,)

            cursor.execute(delete_query, task_data)
            connection.commit()

            print("Tarefa excluída com sucesso!")

        except connector.Error as error:
            print("Erro ao excluir a tarefa:", error)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexão MySQL - OFF.")
        
con = mysqlConnection()