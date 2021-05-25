from neo4j import GraphDatabase

from config import config


class Movie():

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def return_all_movies(self):
        with self.driver.session() as session:
            result = session.read_transaction(self._return_all_movies)

            return result

    @staticmethod
    def _return_all_movies(tx):
        query = """
        MATCH (m:Movie)
        OPTIONAL MATCH(p)-[:PRODUCED]->(m)

        WITH m, COLLECT(p.name) AS producers
        OPTIONAL MATCH (d)-[:DIRECTED]->(m)

        WITH m, producers, COLLECT(d.name) as directors
        OPTIONAL MATCH(a)-[:ACTED_IN]->(m)

        RETURN m.title AS title,
        m.released AS released,
        producers,
        directors,
        COLLECT(a.name) AS cast
        

        """
        result = tx.run(query)
        return [row for row in result.data()]

    def search_and_return_movie(self, title):
        with self.driver.session() as session:
            result = session.read_transaction(
                self._search_and_return_movie, title)

            return result

    @staticmethod
    def _search_and_return_movie(tx, title):
        query = """
        MATCH (m:Movie) 
        WHERE m.title = $title
        OPTIONAL MATCH(p)-[:PRODUCED]->(m)

        WITH m, COLLECT(p.name) AS producers
        OPTIONAL MATCH (d)-[:DIRECTED]->(m)

        WITH m, producers, COLLECT(d.name) as directors
        OPTIONAL MATCH(a)-[:ACTED_IN]->(m)

        RETURN m.title AS title,
        m.released AS released,
        producers,
        directors,
        COLLECT(a.name) AS cast
        """
        map = {'title': title}

        result = tx.run(query, map)
        try:
            return result.data()[0]
        except Exception as e:
            print(str(e))

movie_crud = Movie(uri=config['development'].BOLT_URL,
                   user=config['development'].USERNAME, password=config['development'].PASSWORD)
