from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

class HospitalKey:
    hoskey=dict()

    def __init__(self, key):
        # Input: hospital unique identifier
        # Output: instance of hospital key

        # Connect to Azure Cosmos DB
        the_connection_string = "DefaultEndpointsProtocol=https;AccountName=grand-challenge;AccountKey=zG8AM0FVzaE0cPcQ1NMYPxjE7tSTEQSPvl0CwWlLRTn10ixYlYMF6KFU36dt4D00e66QUoF01hBx0DdNTEtnqQ==;TableEndpoint=https://grand-challenge.table.cosmosdb.azure.com:443/;"
        table_serveice=TableService(endpoint_suffix = "table.cosmosdb.azure.com", connection_string= the_connection_string)

        # Get private key : a key attack prevention is needed
        query_filter="uKey eq "+"'"+key+"'"
        query_result=table_serveice.query_entities('hoskey', filter=query_filter,select='privkey, pubkey')
        
        # query result is unique.
        # Return empty dic if query_result is null
        for task in query_result:
            hoskey['priv']=task.privkey #for encryption
            hoskey['pub']=task.pubkey   #for decryption