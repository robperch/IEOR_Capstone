## MODULE TO TRANSFORM DATA





"----------------------------------------------------------------------------------------------------------------------"
############################################# Imports ##################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--- Standard library imports ---"
import random
import pickle
import os

"--- Third party imports ---"

"--- Local application imports ---"
from pkg_dir.config import *
from pkg_dir.src.utils import *
from pkg_dir.src.parameters import *





"----------------------------------------------------------------------------------------------------------------------"
############### Downloading dataset from Kaggle ########################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Unitary functions ---------------"

## Setting the id feature as the index
def set_id_feature_as_index(dfx):
    """
    Setting the id feature as the index

    :param dfx: (pd.DataFrame) data after the wrangling process
    :return dfx: (pd.DataFrame) data with the id feature set as index
    """


    ## Id feature
    id_feature = [
        col
        for col in titanicsp_base_data_schema
        if 'id_feature' in titanicsp_base_data_schema[col]
    ][0]

    ## Set id feature as index
    dfx.set_index(id_feature, inplace=True)


    return dfx



## Separating features from labels in the training dataset
def split_features_and_labels(Xy_train):
    """
    Separating features from labels in the training dataset

    :param Xy_train: (pd.DataFrame or similar) training dataset mixing features and labels
    :return X_train: (pd.DataFrame or similar) training dataset features only
    :return y_train: (pd.DataFrame or similar) training dataset labels only
    """


    ## Name of the label feature
    label_name = [
        titanicsp_full_data_schema[feat]['clean_col_name']
        for feat in titanicsp_full_data_schema
        if
        'predict_label' in titanicsp_full_data_schema[feat]
        and
        titanicsp_full_data_schema[feat]['predict_label']
    ][0]

    ## Isolating labels
    y_train = Xy_train.loc[:, [label_name]].copy()

    ## Isolating features
    X_train = Xy_train.drop(label_name, axis=1)


    return X_train, y_train



## Updating the dataset objects dictionary with the additional data
def update_dataset_objects_dict(dataset_dict, X_train, X_val, y_train, y_val):
    """
    Updating the dataset objects dictionary with the additional data

    :param dataset_dict: (dictionary) dict containing all the dataset objects (e.g. train_x, train_y, test_x, test_y)
    :param X_train: (pd.DataFrame or similar) features of the training dataset
    :param X_val: (pd.DataFrame or similar) features of the validation dataset
    :param y_train: (pd.DataFrame or similar) labels of the training dataset
    :param y_val: (pd.DataFrame or similar) labels of the validation dataset
    :return dataset_dict: (dictionary) dataset dictionary with updated elements derived from the training dataset
    """


    ## Overwriting original dataset object (mixture between features and labels) for only training labels
    dataset_dict.update({'y_train': y_train})

    ## Adding new objects
    dataset_dict['X_train'] = X_train
    dataset_dict['X_val'] = X_val
    dataset_dict['y_val'] = y_val


    return dataset_dict



## Adding test dummy labels
def add_test_labels(X_test, dataset_dict):
    """
    Adding test dummy labels

    :param X_test: (pd.DataFrame or similar) test dataset features
    :param dataset_dict: (dictionary) dataset dictionary with only features for the test dataset
    :return dataset_dict: (dictionary) dataset dictionary with a new element containing random labels for the test dataset (the main objective is to keep the indices available for the final results)
    """


    ## Adding column with random values
    X_test['dummy_label'] = [
        bool(random.getrandbits(1))
        for i in range(1, X_test.shape[0] + 1)
    ]

    ## Leaving only the index and the new dummy label column
    y_test = X_test.loc[:, ['dummy_label']].copy()

    ## Adding this new element to the dataset dictionary
    dataset_dict['y_test'] = y_test


    return dataset_dict





"--------------- Compounded functions ---------------"

## Transform pipeline function
def transform_pipeline_func():
    """
    Transform pipeline function

    :return None:
    """


    ## Reading extract object saved as pickle locally
    pkl_obj = pipeline_pkl_extract_path + "/" + pipeline_pkl_extract_name

    with open(pkl_obj, 'rb') as obj_content:
        dfx = pickle.load(obj_content)


    ## Apply data wrangling functions based on a predefined dataschema
    dfx = data_wrangling_schema_functions(dfx, base_data_schema)


    ## Saving df as pickle and storing it locally
    pickle.dump(
        dfx,
        open(
            os.path.join(pipeline_pkl_transform_path, pipeline_pkl_transform_name),
            'wb'
        )
    )



    return





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############################################# END OF FILE ##############################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
