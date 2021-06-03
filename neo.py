from neo4j import GraphDatabase
import pandas as pd

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    #para los platillos
    def add_Platillos(self, message):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_Platillos,message)
            

    @staticmethod
    def _create_and_return_Platillos(tx,message):
        result = tx.run("CREATE (a:Platillos) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)

     #para los tiempos
    def add_Time(self, message):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_Time,message)
            

    @staticmethod
    def _create_and_return_Time(tx,message):
        result = tx.run("CREATE (a:Tiempo) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        

     #para el contenido nutricional
    def add_Nutricion(self, message):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_Nutricion,message)
            

    @staticmethod
    def _create_and_return_Nutricion(tx,message):
        result = tx.run("CREATE (a:Nutricion) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)


    #para los precios de los platillos
    def add_Precio(self, message):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_Precio,message)
            

    @staticmethod
    def _create_and_return_Precio(tx,message):
        result = tx.run("CREATE (a:Precio) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)

    #para realizar la relacion entre paltillo y tiempo
    def add_time_relation(self, message1, message2):
        with self.driver.session() as session:
            session.write_transaction(self.create_time_relation,message1,message2)

    @staticmethod
    def create_time_relation(tx, message1, message2):
        query = (
            "MATCH (p1:Tiempo {message : $message1}), (p2:Platillos {message: $message2})"
            "CREATE (p1)-[:relacion]->(p2) "
            "RETURN p1, p2"
        )
        result = tx.run(query, message1=message1, message2=message2)


if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://34.205.171.52:7687", "neo4j", "light-mirrors-plants")
    df = pd.read_csv("export.csv")
    transaction_list = df.values.tolist()
    transaction_execution_commands = []
    #para agregar los platillos a los nodos
    for i in transaction_list:
        greeter.add_Platillos(str(i[0]))

    #agregar los tiempos a los nodos
    greeter.add_Time("rapido")
    greeter.add_Time("medio")
    greeter.add_Time("lento")

    #agregar los tipos de nutricio
    greeter.add_Nutricion("alta")
    greeter.add_Nutricion("media")
    greeter.add_Nutricion("baja")

    #agregar los precios 
    greeter.add_Precio("alto")
    greeter.add_Precio("medio")
    greeter.add_Precio("bajo")

    #para realizar la relacion entre el platillo y tiempo
    for i in transaction_list:
        lista = str(i[2]).split()
        for j in lista:
            if(j==("rapido")):
                greeter.add_time_relation("rapido",str(i[0]))
            elif(j==("medio")):
                greeter.add_time_relation("medio",str(i[0]))
            elif(j==("lento")):
                greeter.add_time_relation("lento",str(i[0]))

    #para realizar la relacion entre platillo y precio
    

    greeter.close()