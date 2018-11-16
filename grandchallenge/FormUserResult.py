from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

# change DB into Blockchain DB
class UserResult:
    Result=dict()

    def __init__(self, userID):
        # Input: User ID
        # Output: dict{EMR1:[v1, ...],EMR2:[v1, ...]}
        query_parsed=[]

        # Connect to Azure Cosmos DB
        the_connection_string = "DefaultEndpointsProtocol=https;AccountName=grand-challenge;AccountKey=zG8AM0FVzaE0cPcQ1NMYPxjE7tSTEQSPvl0CwWlLRTn10ixYlYMF6KFU36dt4D00e66QUoF01hBx0DdNTEtnqQ==;TableEndpoint=https://grand-challenge.table.cosmosdb.azure.com:443/;"
        table_service=TableService(endpoint_suffix = "table.cosmosdb.azure.com", connection_string= the_connection_string)

        
        # Query EMR data of certain user
        query_filter="id eq "+"'"+userID+"'" #find all entities correspoding userID
        tasks=table_service.query_entities('EMR', filter=query_filter)
        
        # Parse qeuried data 
        for task in tasks:
            entity=dict()
            entity['id']=task.Eid    #can be editted
            entity['EMR_hash']=task.EMR
            entity['date']=task.datae
            Result[entity['id']]=[]
            query_parsed.append(entity)

        # Store data into dictionary
        for entity in query_parsed:
            Result[entity['EMR_id']].append(entity)
        
        # Sort the entity list 
        for Eid in Result:
            Result[Eid]=sorted(Result[Eid], key= lambda date: date['commit_date'])