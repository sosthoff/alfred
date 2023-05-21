from llama_index import GPTSQLStructStoreIndex, SQLDatabase, GPTVectorStoreIndex, LLMPredictor, ServiceContext, SimpleDirectoryReader, GPTKeywordTableIndex, PromptHelper, StorageContext
from llama_index.indices.struct_store import SQLContextContainerBuilder
from langchain.llms import AzureOpenAI
from langchain.embeddings import OpenAIEmbeddings
from llama_index import LangchainEmbedding
import pandas as pd
from langchain import OpenAI
from sqlalchemy import create_engine

# define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-002"))
# define prompt helper
# set maximum input size
max_input_size = 2048
# set number of output tokens
num_output = 256
# set maximum chunk overlap
max_chunk_overlap = 20
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)


# # rebuild storage context
# storage_context = StorageContext.from_defaults(persist_dir="./storage")
# # load index
# index = load_index_from_storage(storage_context)

engine = create_engine("sqlite:///foo.db")
sql_database = SQLDatabase(engine)
# sql_database.table_info

# build a vector index from the table schema information
context_builder = SQLContextContainerBuilder(sql_database)
table_schema_index = context_builder.derive_index_from_context(
    GPTVectorStoreIndex,
)

index = GPTSQLStructStoreIndex(
    [],
    sql_database=sql_database, service_context=service_context
)
query_str = "Who knows John Doe?"

context_builder.query_index_for_context(table_schema_index, query_str, store_context_str=True)
context_container = context_builder.build_context_container()

# display(Markdown(f"<b>{context_container.context_str}</b>"))


query_engine = index.as_query_engine(
    sql_context_container=context_container
)
response = query_engine.query(query_str)

str(response)

# response.extra_info

# index.storage_context.persist(persist_dir="./storage")
print(response)