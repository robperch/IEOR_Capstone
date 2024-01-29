## MODULE THE PACKAGE'S BASIC CONFIGURATION





"----------------------------------------------------------------------------------------------------------------------"
############################################# Imports ##################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Standard library imports ---------------"
import os

"--------------- Third party imports ---------------"
# from pytz import timezone


"--------------- Local application imports ---------------"





"----------------------------------------------------------------------------------------------------------------------"
############################## Project and credentials paths ###########################################################
"----------------------------------------------------------------------------------------------------------------------"


## Package directory
package_dir = os.path.dirname(os.path.dirname(__file__))

## Path to local credentials
creds_file_path = os.path.join(package_dir, "config", "local", "credentials.yaml")

## Local credentials reference
db_pc_prod_yaml = 'pc_db_prod'



"----------------------------------------------------------------------------------------------------------------------"
############################## Data files paths ########################################################################
"----------------------------------------------------------------------------------------------------------------------"


"-------------- Data files base path --------------"

#### Data base file location
data_dir_path = os.path.join(package_dir, "data")

#### Data base file location
pkl_dir_path = os.path.join(data_dir_path, "pickles")


"-------------- SQL files path --------------"

## Path to directory with SQL files
sql_files_path = os.path.join(package_dir, 'sql') + "/"

## File with main query to extract appointments data
main_appts_query_filename = "appointments.sql"


"-------------- Pipeline pickle files --------------"

## Local directory to pickles
pipeline_pkl_local_dir = os.path.join(data_dir_path, "pickles", "pipeline")

## Extract
pipeline_pkl_extract_path = os.path.join(pipeline_pkl_local_dir, "extract")
pipeline_pkl_extract_name = "extract.pkl"

## Transform
pipeline_pkl_transform_path = os.path.join(pipeline_pkl_local_dir, "transform")
pipeline_pkl_transform_name = "transform.pkl"





"----------------------------------------------------------------------------------------------------------------------"
############################## Time zone parameters ####################################################################
"----------------------------------------------------------------------------------------------------------------------"


# ## Relevant time zones
# utc_tz = timezone('UTC')
# mexico_tz = timezone('Mexico/General')






"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############################################# END OF FILE ##############################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
