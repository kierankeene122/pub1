
"""Part 2.ipynb

**The solution**

Unless using less popular platforms, tools like FiveTran would likely be more cost effective, more flexible and provide a shorter route to market
"""

class DataSource:
  #Datasource details + connect to source
    def __init__(self, source_name, config):
        self.source_name = source_name
        self.config = config

  #query the data (load into DF)
    def extract(self):

  #you may want to restructure / manipulate data in a consistent way, across all sources
    def transform(self, data):

  #load the data into Redshift
    def load(self, transformed_data):



def run_etl_pipeline(data_source):
    try:
        #call the E
        data = data_source.extract()

        #call the T
        transformed_data = data_source.transform(data)

        #call the L
        data_source.load(transformed_data)

        print(f"ETL process completed for {data_source.source_name}")

    except Exception as e:
        print(f"Error in ETL process for {data_source.source_name}: {str(e)}")

if __name__ == "__main__":

    mongo_config = {
        "host": "mongodb_host",
        "port": 27017,
        "username": "mongo_username",
        "password": "mongo_password",
        "database": "mongo_database",
    }

    # pass config to datasource class
    mongo_data_source = DataSource("MongoDB", mongo_config)
    run_etl_pipeline(mongo_data_source)


