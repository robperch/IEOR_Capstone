## MODULE TO EXTRACT DATA FROM SOURCE





"----------------------------------------------------------------------------------------------------------------------"
############################################# Imports ##################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--- Standard library imports ---"
import zipfile
import pickle
import os

"--- Third party imports ---"
import pandas as pd

"--- Local application imports ---"
from pkg_dir.config import *
from pkg_dir.src.utils import *
from pkg_dir.src.parameters import *





"----------------------------------------------------------------------------------------------------------------------"
############### Extract general functions ##############################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Unitary functions ---------------"

## Download data from source database and convert it into a dataframe
def ingest_from_pc_database():
    """
    Download data from Punto Clínico's source database and convert it into a dataframe

    :param:
    :return dfx: (dataframe) data extracted from database
    """


    ## Obtaining query results as tuples
    dfx = sql_to_df(db_pc_prod_yaml, sql_files_path, main_appts_query_filename, sql_params_appointments)


    return dfx



## Saving locally train and test dataset as df-pickle
def save_extract_local_df_pkl(dfx):
    """
    Saving locally train and test dataset as df-pickle

    :param dfx: (dataframe) df with the raw data extracted from querying the database
    :return None:
    """


    ## Saving df as pickle and storing it locally
    pickle.dump(
        dfx,
        open(
            os.path.join(pipeline_pkl_extract_path, pipeline_pkl_extract_name),
            'wb'
        )
    )


    return





"--------------- Compounded functions ---------------"


## Extract pipeline function
def extract_pipeline_func():
    """
    Extract pipeline function

    :return None:
    """


    ## Download data from source database and convert it into a dataframe
    dfx = ingest_from_pc_database()

    ## Saving locally train and test dataset as df-pickle
    save_extract_local_df_pkl(dfx)


    return





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############################################# END OF FILE ##############################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
