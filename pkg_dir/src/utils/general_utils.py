## MODULE WITH UTIL FUNCTIONS - GENERAL PURPOSE





"----------------------------------------------------------------------------------------------------------------------"
####################################################### Imports ########################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Standard library imports ---------------"
import yaml
import json
import os

"--------------- Third party imports ---------------"
import pandas as pd
import unidecode

"--------------- Local application imports ---------------"
from pkg_dir.config import *





"----------------------------------------------------------------------------------------------------------------------"
############################## Generic functions #######################################################################
"----------------------------------------------------------------------------------------------------------------------"


## Read contents of yaml file
def read_yaml(crds_loc):
    """
    Read yaml file

    :param crds_loc: (string) location of yaml file
    :return config: (?) read file
    """

    ## Configuration parameter
    config = None

    ## Safe loading file
    try:
        with open(crds_loc, "r") as file:
            config = yaml.safe_load(file)
    except:
        raise FileNotFoundError("Read yaml file error: could not load file")

    return config



## Format json
def format_json(json):
    """
    Format json

    :param json: (json) raw json
    :return json_clean: (json) cleaned json
    """

    ## Formatting response
    json_clean = json.dumps(json.loads(json), ensure_ascii=False, indent=2)

    return json_clean



## Generating the data dictionary
def generate_data_dictionary(df_cols, data_dicts_loc, data_dict_filename):
    """

    :param dfx (list): df columns obtained using df.columns
    :param data_dicts_loc (string): absolute path to the data dicts directory
    :param data_dict_filename (stirng): name of the resulting json file containing the data dict
    :return None:
    """


    ## Create the dictionary as a python object
    data_dict = {
        col: {
            "relevant": False,
            "clean_col_name": col,
            "data_type": "str",
            "value_map": {
            },
            "feature_type": "categorical",
            "model_relevant": True,
            "imputation_strategy": "drop"
        }

        for col in df_cols
    }

    ## Converting the python object into a json
    with open(data_dicts_loc + data_dict_filename, "w") as outfile:
        json.dump(
            data_dict,
            outfile,
            ensure_ascii=False,
            indent=2,
        )


    return



## Reading json file
def read_json(file_path):
    """

    :param file_path (string): json file location
    :return json_contents (dictionary): contents in json file
    """


    ## Reading json file
    with open(file_path) as json_file:
        json_contents = json.load(json_file)


    return json_contents



## Creating a directory if it doesn't already exists
def create_directory_if_nonexistent(dir_path, dir_name):
    """
    Creating a directory if it doesn't already exists

    :param dir_path: (string) path to where the new directory will be located
    :param dir_name: (string) name of the directory that will be created
    :return None:
    """


    ## Concatenating dir path and dir name
    dir_path_full = os.path.join(dir_path, dir_name)

    ## Creating directory
    if not os.path.exists(dir_path_full):
        os.mkdir(dir_path_full)


    return




"----------------------------------------------------------------------------------------------------------------------"
############################## Data schema based wrangling functions ###################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Data schema based unitary functions ---------------"


## Renaming columns based on a specified data schema
def rename_columns_with_data_schema(dfx, data_schema):
    """
    Renaming columns based on a specified data schema

    :param dfx (dataframe): df with the columns that will be cleaned
    :param data_schema (dictionary): data schema containing the clean column names
    :return dfx (dataframe): df after renaming the columns based on the data schema
    """


    ## Creating the data dictionary to rename the columns
    clean_col_names = {
        col: data_schema[col]["clean_col_name"]
        for col in data_schema
    }

    ## Renaming columns
    dfx.rename(columns=clean_col_names, inplace=True)


    return dfx



## Eliminating irrelevant columns based on specified data schema
def drop_irrelevant_columns_with_data_schema(dfx, data_schema):
    """

    :param dfx (dataframe): df containing irrelevant columns
    :param data_schema (dictionary): data schema containing distinction between relevant and irrelevant columns
    :return dfx (dataframe): df containing only relevant columns
    """


    ## Creating a list of the relevant columns
    rc = [
        data_schema[col]["clean_col_name"]
        for col in data_schema
        if data_schema[col]["relevant"]
    ]

    ## Dropping selected columns
    dfx = dfx.loc[:, rc]


    return dfx



## Formatting the columns' data types based on a specified data schema
def format_data_types_with_data_schema(dfx, data_schema):
    """
    Formatting the columns data types based on a specified data schema

    :param dfx (dataframe): df whose columns will be formatted according to the predefined data type
    :param data_schema (dictionary): data schema containing the columns data types
    :return dfx (dataframe): df with the columns formatted
    """


    ## Formatting each column based on it's datatype

    ### Strings
    rc = [
        data_schema[col]["clean_col_name"]
        for col in data_schema
        if data_schema[col]["relevant"]
           and data_schema[col]["data_type"] == "str"
    ]
    for col in rc:
        dfx[col] = dfx[col].astype("str")
        dfx[col] = dfx[col].apply(lambda x: unidecode.unidecode(x.upper()))


    ### Datetimes
    rc = [
        data_schema[col]["clean_col_name"]
        for col in data_schema
        if data_schema[col]["relevant"]
           and data_schema[col]["data_type"] == "datetime"
    ]
    for col in rc:
        dfx[col] = pd.to_datetime(dfx[col], errors="coerce")


    ### Integers
    rc = [
        data_schema[col]["clean_col_name"]
        for col in data_schema
        if data_schema[col]["relevant"]
           and data_schema[col]["data_type"] == "int"
    ]
    for col in rc:
        dfx[col] = pd.to_numeric(dfx[col], downcast="integer")


    ### Floats
    rc = [
        data_schema[col]["clean_col_name"]
        for col in data_schema
        if data_schema[col]["relevant"]
           and data_schema[col]["data_type"] == "float"
    ]
    for col in rc:
        dfx[col] = pd.to_numeric(dfx[col], downcast="float")
        dfx[col] = dfx[col].round(2)


    return dfx



## Mapping row values with information specified on the data schema
def map_row_values_with_data_schema(dfx, data_schema):
    """

    :param dfx (dataframe): df with rows as extracted from the data source
    :param data_schema (dictionary): data schema containing the value mapping
    :return dfx (dataframe): df with row values mapped
    """


    ## Creating dictionary with the clean column name and the mapping that will be used
    mapping_reference = {
        data_schema[col]["clean_col_name"]: data_schema[col]["values_map"]
        for col in data_schema
        if "values_map" in data_schema[col]
    }

    ## Mapping values according to reference
    for col in mapping_reference:
        dfx[col] = dfx[col].map(mapping_reference[col]).fillna(dfx[col])


    return dfx



"--------------- Data schema based compounded functions ---------------"


## Group of data wrangling functions that are based on the data schema
def data_wrangling_schema_functions(dfx, data_schema):
    """
    Group of data wrangling functions that are based on the data schema

    :param dfx: (dataframe) raw data previous to the wrangling process
    :param data_schema: (dictionary) data schema containing the parameters for the data wrangling
    :return dfx: (dataframe) data processed through the data wrangling functions
    """


    ## Renaming columns based on a specified data schema
    dfx = rename_columns_with_data_schema(dfx, data_schema)

    ## Eliminating irrelevant columns based on specified data schema
    dfx = drop_irrelevant_columns_with_data_schema(dfx, data_schema)

    ## Formatting the columns data types based on a specified data schema
    dfx = format_data_types_with_data_schema(dfx, data_schema)

    ## Mapping row values with information specified on the data schema
    dfx = map_row_values_with_data_schema(dfx, data_schema)


    return dfx





"----------------------------------------------------------------------------------------------------------------------"
############################## Useful general data wrangling functions #################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Useful general data wrangling unitary functions ---------------"


## Adding column with a distinction between the first and second half of the month (quincena)
def add_quincena_column(dfx, date_col_name):
    """
    Adding column with a distinction between the first and second half of the month (quincena)

    :param dfx: (dataframe) df without the quincena column added
    :param date_col_name: (string) name of the column that will be used as reference the create the new quincena column
    :return dfx: (dataframe) df with a column indicating the half of the month with the following format: %y-%m-qx (where 'x' stands for 1 or 2, depending on the month's half)
    """


    ## Creating support column to identify the half of the month
    dfx.insert(
        dfx.columns.to_list().index(date_col_name) + 1,
        'support_col_month_half',
        dfx[date_col_name].apply(lambda x: '1' if int(x.strftime('%d')) <= 15 else '2')
    )

    ## Creating quincena column
    dfx.insert(
        dfx.columns.to_list().index(date_col_name) + 1,
        'quincena',
        dfx[date_col_name].dt.strftime(date_format='%y-%m-q') + dfx['support_col_month_half']
    )

    ## Dropping support column
    dfx.drop(['support_col_month_half'], axis=1, inplace=True)


    return dfx





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############### END OF FILE ############################################################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
