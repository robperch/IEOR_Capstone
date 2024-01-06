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
from pkg_dir.src.utils import (

    create_directory_if_nonexistent,

)





"----------------------------------------------------------------------------------------------------------------------"
############### Extract general functions ##############################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Unitary functions ---------------"

## Download data from source database and convert it into a dataframe
def ingest_from_pc_database():
    """
    Download data from Punto Clínico's source database and convert it into a dataframe

    :param:
    :return:
    """


    return



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
            os.path.join(pipeline_pkl_extract_local_dir, pipeline_pkl_extract_name) + data_prefix + file.split(sep='.')[0] + '.pkl',
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
    def ingest_from_pc_database():

    ## Saving locally train and test dataset as df-pickle
    save_extract_local_df_pkl()


    return





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############################################# END OF FILE ##############################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
