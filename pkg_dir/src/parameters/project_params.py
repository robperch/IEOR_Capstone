## MODULE WITH GENERAL PARAMETERS FOR THE PROJECT





"----------------------------------------------------------------------------------------------------------------------"
############################################# Imports ##################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--- Standard library imports ---"


"--- Third party imports ---"


"--- Local application imports ---"





"----------------------------------------------------------------------------------------------------------------------"
############### Data schema ############################################################################################
"----------------------------------------------------------------------------------------------------------------------"


## Data schema to handle data
base_data_schema = {

    'appointment_id': {
        'relevant': True,
        'clean_col_name': 'appointment_id',
        'data_type': 'str',
        'feature_type': 'categorical',
        'model_relevant': False,
        'id_feature': True,
    },

    'appointment_date': {
        'relevant': True,
        'clean_col_name': 'appointment_date',
        'data_type': 'str',
        'feature_type': 'categorical',
        'model_relevant': False,
        'imputation_strategy': 'drop',
    },

    'appointment_start_time': {
        'relevant': True,
        'clean_col_name': 'appointment_start_time',
        'data_type': 'str',
        'feature_type': 'categorical',
        'model_relevant': False,
        'imputation_strategy': 'drop',
    },

    'appointment_end_time': {
        'relevant': True,
        'clean_col_name': 'appointment_end_time',
        'data_type': 'str',
        'feature_type': 'categorical',
        'model_relevant': False,
        'imputation_strategy': 'drop',
    },

    'appointment_creation': {
        'relevant': True,
        'clean_col_name': 'appointment_creation',
        'data_type': 'datetime',
        'feature_type': 'categorical',
        'model_relevant': False,
        'imputation_strategy': 'drop',
    },

    'appointment_status': {
        'relevant': True,
        'clean_col_name': 'appointment_status',
        'data_type': 'str',
        'feature_type': 'categorical',
        'model_relevant': False,
        'imputation_strategy': 'drop',
    },

    'doctor': {
        'relevant': True,
        'clean_col_name': 'doctor',
        'data_type': 'str',
        'feature_type': 'categorical',
        'model_relevant': False,
        'imputation_strategy': 'drop',
    },

    'medical_specialty': {
        'relevant': True,
        'clean_col_name': 'medical_specialty',
        'data_type': 'str',
        'feature_type': 'categorical',
        'model_relevant': False,
        'imputation_strategy': 'drop',
    },

    'clinic': {
        'relevant': True,
        'clean_col_name': 'clinic',
        'data_type': 'str',
        'feature_type': 'categorical',
        'model_relevant': False,
        'imputation_strategy': 'drop',
    },

    'patient_id': {
        'relevant': True,
        'clean_col_name': 'clinic',
        'data_type': 'str',
        'feature_type': 'categorical',
        'model_relevant': False,
        'imputation_strategy': 'drop',
    },

    'patient_birth_date': {
        'relevant': True,
        'clean_col_name': 'patient_birth_date',
        'data_type': 'str',
        'feature_type': 'categorical',
        'model_relevant': False,
        'imputation_strategy': 'drop',
    },

}



"----------------------------------------------------------------------------------------------------------------------"
############### XXX ####################################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- XXX ---------------"





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############################################# END OF FILE ##############################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
