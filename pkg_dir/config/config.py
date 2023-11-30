## MODULE THE PACKAGE'S BASIC CONFIGURATION





"----------------------------------------------------------------------------------------------------------------------"
############################################# Imports ##################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Standard library imports ---------------"
import os

"--------------- Third party imports ---------------"
from pytz import timezone


"--------------- Local application imports ---------------"





"----------------------------------------------------------------------------------------------------------------------"
############################## Project and credentials paths ###########################################################
"----------------------------------------------------------------------------------------------------------------------"


## Package directory
package_dir = os.path.dirname(os.path.dirname(__file__))

## Local credentials
creds_file_path = os.path.join(package_dir, "config", "local", "credentials.yaml")



"----------------------------------------------------------------------------------------------------------------------"
############################## Data files paths ########################################################################
"----------------------------------------------------------------------------------------------------------------------"


"-------------- Data files base path --------------"

#### Data base file location
data_dir_path = os.path.join(package_dir, "data")

#### Results directory name
process_results_dirname = "results"




"-------------- SQL files -------------"

## Postgresql files

### Main directory
postgre_files_path = os.path.join(package_dir, "sql", "postgres") + "/"

### Working hours in doctor's agendas - path to file
postgre_docs_hrs = os.path.join("docs_working_hours", "docs_working_hours_py.sql")

### Information about the doctor's agendas - path to file
postgre_query_fullagenda = os.path.join("full_docs_agendas", "full_docs_agendas_py.sql")

### Data of appointments with their creation date - path to file
postgre_query_apptsct = os.path.join("appointments_creations", "appts_creation.sql")

### Income data - query to replicate the Income per type of service report
postgres_income_syspc = os.path.join("income_data", "v_service_income_data.sql")

### Doctor's information in the database
postgres_docs_data = os.path.join("docs_data", "db_docs.sql")





"----------------------------------------------------------------------------------------------------------------------"
############################## Time zone parameters ####################################################################
"----------------------------------------------------------------------------------------------------------------------"


## Relevant time zones
utc_tz = timezone('UTC')
mexico_tz = timezone('Mexico/General')





"----------------------------------------------------------------------------------------------------------------------"
############################## Useful parameters #######################################################################
"----------------------------------------------------------------------------------------------------------------------"


## Translation of keywords from english to spanish
word_translation = {

    "months": {

        'April': "Abril",
        'August': "Agosto",
        'December': "Diciembre",
        'February': "Febrero",
        'January': "Enero",
        'July': "Julio",
        'June': "Junio",
        'March': "Marzo",
        'May': "Mayo",
        'November': "Noviembre",
        'October': "Octubre",
        'September': "Septiembre",

    },

}





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############################################# END OF FILE ##############################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
