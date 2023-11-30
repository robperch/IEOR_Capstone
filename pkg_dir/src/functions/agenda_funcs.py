## MODULE WITH AGENDA OCCUPATION FUNCTIONS





"----------------------------------------------------------------------------------------------------------------------"
############################################# Imports ##################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Standard library imports ---------------"

"--------------- Third party imports ---------------"
import pandas as pd

"--------------- Local application imports ---------------"
from pkg_dir.config import *
from pkg_dir.src.parameters import *
from pkg_dir.src.utils import *





"----------------------------------------------------------------------------------------------------------------------"
############################################# Agenda base metrics ######################################################
"----------------------------------------------------------------------------------------------------------------------"


'--------------- Unitary functions ---------------'


## Concatenating string hours to obtain unique entries
def concatenate_string_hours(dfx):
    """
    Concatenating string hours to obtain unique entries

    :param dfx (dataframe): df with no hours string range column added
    :return dfx (dataframe): df with hours range column included
    """


    ## Creating new column with hour strings concatenated
    dfx.insert(
        1,
        "Hora_rango",
        dfx["hora_inicio_(syspc)"] + "-" + dfx["hora_final_(syspc)"]
    )


    return dfx



## Converting hours in dataframe columns to integers and decimals
def convert_df_hours_to_numbers(dfx):
    """
    Converting hours in dataframe columns to integers and decimals

    :param dfx (dataframe): df with hour columns as strings
    :return dfx (dataframe): df with hour columns converted
    """


    ## Converting string hours into numbers with decimals
    def convert_string_hours_to_numbers(row):
        """
        Converting string hours into numbers with decimals

        :param row (string): hour as a string in traditional format (e.g. "14:45")
        :return final_time (float): hour as integers and minutes as decimal (e.g. "14.75")
        """

        ## Generating list of values separated between hours and minutes
        hours_mins = row.split(sep=":")

        ## Obtaing hours as integer and minutes as decimals
        final_time = int(hours_mins[0]) + int(hours_mins[1]) / 60

        return final_time


    ## Converting columns with string hours
    dfx["hora_inicio_(syspc)"] = dfx["hora_inicio_(syspc)"].apply(lambda x: convert_string_hours_to_numbers(x))
    dfx["hora_final_(syspc)"] = dfx["hora_final_(syspc)"].apply(lambda x: convert_string_hours_to_numbers(x))

    ## Adding column with active work time
    dfx.insert(
        4,
        "tiempo_contratado",
        dfx["hora_final_(syspc)"] - dfx["hora_inicio_(syspc)"]
    )

    ## Printing reference value of total active time
    print("- Total active time (before splitting):", dfx["tiempo_contratado"].sum())


    return dfx



## Finding the turn corresponding to the specific hour plus adjustment
def finding_turn_of_hour(row):
    """
    Finding the turn corresponding to the specific hour plus adjustment

    :param row (float): value with adjustment corresponding to the reference hour
    :return res (string): string referencing the turn corresponding to the hour with adjustment
    """


    for turn in pc_turns_hours:

        res = "no_turn"

        if (row > pc_turns_hours[turn]["start"]) & (row < pc_turns_hours[turn]["end"]):
            res = turn
            break

    return res



## Determining active turn based on results of start and finish hour turn
def finding_active_turn(row):


    ## Conditional for consistency
    if row["Hora_inicio_turno"] == row["Hora_final_turno"]:
        res = row["Hora_inicio_turno"]
    else:
        res = "all_day_turn"


    return res



## Defining active turn based on start and finish hours results
def finding_service_turn(dfx):
    """
    Defining active turn based on start and finish hours results

    :param dfx (dataframe): df with start and finish hours as floats
    :return dfx (dataframe): df with the active turn defined
    """


    ## Inserting columns with turns of start and finish hours

    #### Start hour
    dfx.insert(
        4,
        "Hora_inicio_turno",
        dfx["hora_inicio_(syspc)"].apply(lambda x: finding_turn_of_hour(x + 0.1))
    )

    #### Finish hour
    dfx.insert(
        5,
        "Hora_final_turno",
        dfx["hora_final_(syspc)"].apply(lambda x: finding_turn_of_hour(x - 0.1))
    )


    ## Determining active turn based on start and finish information
    dfx.insert(
        6,
        "turno_activo",
        dfx.apply(lambda x: finding_active_turn(x), axis=1)
    )


    ## Eliminating support start and finish hour columns
    dfx.drop(["Hora_inicio_turno", "Hora_final_turno"], axis=1, inplace=True)


    ## Finding active turns that are outside the base time parameters set for the turns
    dfy = dfx[dfx["turno_activo"] == "no_turn"].groupby(["proveedor_(syspc)", "fecha_(syspc)"], as_index=False).agg(
        {
            "hora_inicio_(syspc)": "count"
        }
    )

    #### Printing relevant metrics to keep track of corner cases
    # print("- Support info to keep track of active work spaces outside defined turns: ")

    ###### Number of cases identified
    # print("    - Number of cases in data: ", dfy.shape[0])

    ###### List of doctors who have active work spots outside the defined turns
    docs_outside_turns = list(dfy["proveedor_(syspc)"].unique())
    # print("    - Number of doctors working outside turns: ", len(docs_outside_turns))


    ## Eliminating entries of active spaces outside the working hours
    mr1 = dfx["turno_activo"] != "no_turn"
    mrs = mr1
    dfx = dfx.loc[mrs, :]


    return dfx



## Splitting "all_day_turn" entries into a 1st turn row and a 2nd turn row
def split_allday_entries(dfx):
    """
    Splitting "all_day_turn" entries into a 1st turn row and a 2nd turn row

    :param dfx (dataframe): df with "all_day_turns" entries
    :return dfx (dataframe): df with "all_day_turns" entries separated into 1st and 2nd turn
    """


    ## Reference columns in dataframe
    ref_cols = ["clinica_(syspc)", "proveedor_(syspc)", "especialidad_(syspc)", "fecha_(syspc)", "Hora_rango"]

    ## String used as a base to build filtering conditions
    filter_string = "(dfx['{}'] == "

    ## Creating dictionary with entries that will be splitted into 1st and 2nd turn
    split_dict = dfx.loc[dfx["turno_activo"] == "all_day_turn", ref_cols].to_dict(orient="index")

    ## Printing number of rows that will be splitted
    print("- Number of rows that will be splitted", len(split_dict))


    ## Iterating over all the columns that need to be splitted into 1st and 2nd turn
    for split_entry in split_dict:


        ## Building list of conditions to filter
        filter_conditions = [
            filter_string.format(col) + "'" + split_dict[split_entry][col] + "'" + ")" if col != "fecha_(syspc)"
            else filter_string.format(col) + "'" + str(split_dict[split_entry][col]) + "'" + ")"
            for col in ref_cols
        ]

        ## Joining list to build condition
        filter_conditions = " & ".join(filter_conditions)

        ## Filtering dataframe using built conditions
        dfy = dfx[eval(filter_conditions)].copy()


        ## Obtaining row with grouped information

        #### Setting index to final number for row that will be splitted
        dfy.rename({dfy.index[0]: dfx.shape[0] + 1}, inplace=True)

        #### Creating new row exactly as the one that will be splitted
        dfy.loc[max(dfy.index) + 1, :] = dfy.loc[max(dfy.index), :]

        #### Changing first row contents to generate the first split
        index_split1 = min(dfy.index)
        split_max_range = dfy.loc[index_split1, ["Hora_rango"]][0][:-5] + str(int(turn_div_hour)) + ":00"
        dfy.loc[index_split1, ["Hora_rango", "hora_final_(syspc)", "turno_activo"]] = [split_max_range, turn_div_hour, "1st_turn"]

        ## Changing second row contents to generate the second split
        index_split2 = max(dfy.index)
        split_min_range = str(int(turn_div_hour)) + ":00-" + dfy.loc[index_split2, ["Hora_rango"]][0][:5]
        dfy.loc[index_split2, ["Hora_rango", "hora_inicio_(syspc)", "turno_activo"]] = [split_min_range, turn_div_hour, "2nd_turn"]


        ## Adding the obtaind row into the original dataframe

        #### Droppping the rows that were already merged in dfy
        dfx.drop([split_entry], inplace=True)

        #### Adding the row that groups all the "all_day_info"
        dfx = pd.concat([dfx, dfy])


    ## Eliminating "all_day_turn" rows that might remain due to duplicity despite filters
    mr1 = dfx["turno_activo"] == "all_day_turn"
    mrs = mr1
    # print("- Number of 'all_day_turns' purged due to filtering failure: ", dfx.loc[mrs, ["turno_activo"]].shape[0])
    dfx = dfx.loc[~mrs, :]

    ## Recalculating active time based on range data
    dfx["tiempo_contratado"] = dfx["hora_final_(syspc)"] - dfx["hora_inicio_(syspc)"]
    print("- Total active time (after splitting):", dfx["tiempo_contratado"].sum())


    return dfx



## Grouping dataframe to obtain the hours that a doctor theoretically has to work (m2) and the hours available to work (m3)
def base_turn_hours(dfx):
    """
    Grouping dataframe to obtain the hours that a doctor theoretically has to work (m2) and the hours available to work (m3)

    :param dfx (dataframe): raw dataframe with identified turns
    :return dfy (dataframe): grouped dataframe with the sum of all active hours (hired hours/m2) and available hours (hired minus blocked hours/m3)
    """


    '----- Total hours hired for a doctor -----'

    ## Eliminating entries that cover the same amount of time
    dfy = dfx.drop_duplicates(
        subset=[
            "clinica_(syspc)",
            "usuarioid_(syspc)",
            "proveedor_(syspc)",
            "especialidad_(syspc)",
            "fecha_(syspc)",
            "Hora_rango",
        ]
    )


    ## Obtaining total hiring time per turn for each doctor's day
    dfy = dfy.groupby(
        [
            "clinica_(syspc)",
            "usuarioid_(syspc)",
            "proveedor_(syspc)",
            "especialidad_(syspc)",
            "fecha_(syspc)",
            "turno_activo"
        ],
        as_index=False
    ).agg(
        {
            "tiempo_contratado": "sum"
        }
    )


    ## Setting cap for base hours whose values might have grown too much due to errors in hourly assignments
    dfy["tiempo_contratado"] = dfy["tiempo_contratado"].apply(lambda x: 10 if x > 10 else x)



    '----- Total hours available for a doctor (hired hours minus blocked hours) -----'

    ## Filtering rows to include only blocked hours
    mr1 = dfx["estatus_cita_(syspc)"] == "BLOQUEADO"
    mr2 = dfx["paciente_(syspc)"].str.contains('BLOQUEA')
    mrs = mr1 | mr2
    dfy2 = dfx.loc[mrs, :].copy()

    ## Grouping to add number of completed hours
    dfy2 = dfy2.groupby(
        [
            "clinica_(syspc)",
            "usuarioid_(syspc)",
            "proveedor_(syspc)",
            "especialidad_(syspc)",
            "fecha_(syspc)",
            "turno_activo"
        ],
        as_index=False).agg(
        {
            "tiempo_contratado": "sum"
        }
    )

    ## Renaming column to specify that it contains completed hours
    dfy2.rename(columns={"tiempo_contratado": "tiempo_bloqueado"}, inplace=True)

    ## Merging the blocked time results with the original results
    dfy = pd.merge(
        dfy,
        dfy2,
        on=[
            "clinica_(syspc)",
            "usuarioid_(syspc)",
            "proveedor_(syspc)",
            "especialidad_(syspc)",
            "fecha_(syspc)",
            "turno_activo"
        ],
        how="outer"
    )

    ## Filling NAN's after the merge
    dfy.fillna(0, inplace=True)

    ## Calculating the amount of active time
    dfy['tiempo_disponible'] = dfy['tiempo_contratado'] - dfy['tiempo_bloqueado']


    return dfy



## Grouping dataframe to obtain completed hours of doctors
def completed_doc_hours(dfx):
    """
    Grouping dataframe to obtain completed hours of doctors

    :param dfx (dataframe): raw df with all the calendar entries
    :return dfw (dataframe): df with sum of completed hours for each doctor's day
    """


    ## Filtering rows to include only completed hours
    mr1 = dfx["estatus_cita_(syspc)"] == "COMPLETADA"
    mrs = mr1
    dfw = dfx.loc[mrs, :].copy()

    ## Grouping to add number of completed hours
    dfw = dfw.groupby(
        [
            "clinica_(syspc)",
            "usuarioid_(syspc)",
            "proveedor_(syspc)",
            "especialidad_(syspc)",
            "fecha_(syspc)",
            "turno_activo"
        ],
        as_index=False).agg(
        {
            "tiempo_contratado": "sum"
        }
    )

    ## Renaming column to specify that it contains completed hours
    dfw.rename(columns={"tiempo_contratado": "tiempo_completado"}, inplace=True)


    return dfw



## Grouping dataframe to obtain hours with a status modified (status different from "DISPONIBLE"; not considering "NO AGENDAR")
def occupied_doc_hours(dfx):
    """
    Grouping dataframe to obtain hours with a status modified (status different from "DISPONIBLE"; not considering "NO AGENDAR")

    :param dfx (dataframe): raw df with all the calendar entries
    :return dfz (dataframe): df with sum of hours that contained a status different from "DISPONIBLE" and not considering "NO AGENDAR"
    """


    ## Filtering rows to include only occupied hours
    mr1 = dfx["estatus_cita_(syspc)"] != "DISPONIBLE"
    mr2 = dfx["estatus_cita_(syspc)"] != "BLOQUEADO"
    mr3 = ~dfx["estatus_cita_(syspc)"].str.contains("CANCELA")
    mr4 = ~dfx["paciente_(syspc)"].str.contains("NO AGENDAR")
    mr5 = ~dfx["paciente_(syspc)"].str.contains('BLOQUEADO!')
    mr6 = ~dfx["paciente_(syspc)"].str.contains('NO OCUPAR!')
    mrs = mr1 & mr2 & mr3 & mr4 & mr5 & mr6
    dfz = dfx.loc[mrs, :].copy()

    ## Grouping to add number of completed hours
    dfz = dfz.groupby(
        [
            "clinica_(syspc)",
            "usuarioid_(syspc)",
            "proveedor_(syspc)",
            "especialidad_(syspc)",
            "fecha_(syspc)",
            "turno_activo"
        ],
        as_index=False).agg(
        {
            "tiempo_contratado": "sum"
        }
    )

    ## Renaming column to specify that it contains completed hours
    dfz.rename(columns={"tiempo_contratado": "tiempo_ocupado"}, inplace=True)


    return dfz



## Grouping "all_day_turn" entries into a single row
def group_allday_entries(dfx):
    """
    Grouping "all_day_turn" entries into a single row

    :param dfx (dataframe): df with "all_day_turns", "1st turn", and "2nd turn" separated
    :return dfx (dataframe): df with "all_day_turns", "1st turn", and "2nd turn" all compacted into one row
    """


    ## Reference columns in dataframe
    ref_cols = ["clinica_(syspc)", "proveedor_(syspc)", "especialidad_(syspc)", "fecha_(syspc)"]

    ## String used as a base to build filtering conditions
    filter_string = "(dfx['{}'] == "

    ## Creating dictionary with entries that will be compacted
    comp_dict = dfx.loc[dfx["turno_activo"] == "all_day_turn", ref_cols].to_dict(orient="index")


    ## Iterating over all the columns that need to be compacted
    for comp_entry in comp_dict:


        ## Building list of conditions to filter
        filter_conditions = [
            filter_string.format(col) + "'" + comp_dict[comp_entry][col] + "'" + ")" if col != "fecha_(syspc)"
            else filter_string.format(col) + "'" + str(comp_dict[comp_entry][col]) + "'" + ")"
            for col in ref_cols
        ]

        ## Joining list to build condition
        filter_conditions = " & ".join(filter_conditions)

        ## Filtering dataframe using built conditions
        dfy = dfx[eval(filter_conditions)].copy()

        ## Obtaining index of filtered rows
        dfy_index = list(dfy.index)


        ## Obtaining row with grouped information

        #### Adding special tag to the turn that will group all the results
        dfy.loc[comp_entry, "turno_activo"] = "all_day_adj_turn"

        #### Grouping "Horas_completadas" information in "all_day_adj_turn" row
        val = dfy.loc[:, "Horas_completadas"].sum()
        dfy.loc[comp_entry, "Horas_completadas"] = val

        #### Eliminating rows used before grouping
        mr1 = dfy["turno_activo"] == "all_day_adj_turn"
        mrs = mr1
        dfy = dfy.loc[mrs, :]


        ## Adding the obtaind row into the original dataframe

        #### Droppping the rows that were already merged in dfy
        mr1 = ~dfx.index.isin(dfy_index)
        mrs = mr1
        dfx = dfx.loc[mrs, :]

        #### Adding the row that groups all the "all_day_info"
        dfx = pd.concat([dfx, dfy])

        #### Sorting index to reacommodate in original place
        dfx.sort_index(inplace=True)


    return dfx



'--------------- Compounded functions ---------------'


## Obtaining turns active and number of completed hours - compounded function
def work_time_assesment(date_string):
    """
    Obtaining turns active and number of completed hours - compounded function

    :param date_string: (string) string that contain a start and end date in the format %Y-%m-%d_to_%Y-%m-%d
    :return dfa: (dataframe) summary dataframe with important metrics related to the doctors' schedules
    """


    ## Converting date string into a dictionary suitable for the sql parameters
    date_sql_param = datestring_to_sql_parameter(date_string)

    ### Message specifying dates used for the query
    print("- Date range used to query data: from {} to {}".format(
        date_sql_param["$1"],
        date_sql_param["$2"])
    )

    ## Updating sql parameters to query data in the specified date range
    sql_params_fullagenda["params"].update(date_sql_param)


    ## Executing sql query to obtain working dataframe
    dfx = sql_to_df("pc_db_prod", postgre_files_path, postgre_query_fullagenda, sql_params_fullagenda)


    ## Basic column\row formatting

    ### Converting dates into the proper format
    dfx["fecha_(syspc)"] = pd.to_datetime(dfx["fecha_(syspc)"], format="%Y-%m-%d")

    ### Filling NA values in the patient's column
    dfx["paciente_(syspc)"] = dfx["paciente_(syspc)"].astype("str")
    dfx["paciente_(syspc)"] = dfx["paciente_(syspc)"].map({"None": "SIN_PACIENTE"}).fillna(dfx["paciente_(syspc)"])

    ## Leaving only users that are active on the platform
    mr1 = dfx['proveedor_estado_(syspc)'] == 'A'
    mrs = mr1
    dfx = dfx.loc[mrs, :].copy()


    ## Adding column with string hours concatenated to form range
    dfx = concatenate_string_hours(dfx)

    ## Converting string hours into integers and floats
    dfx = convert_df_hours_to_numbers(dfx)

    ## Finding the turn related to the hour
    dfx = finding_service_turn(dfx)

    ## Splitting entries that cover through the turn line
    dfx = split_allday_entries(dfx)


    ## Obtaining dataframe with active hours in each turn
    dfy = base_turn_hours(dfx)


    ## Grouping dataframe to obtain hours with a status modified (status different from "DISPONIBLE"; not considering "NO AGENDAR")
    dfw = occupied_doc_hours(dfx)


    ## Obtaining dataframe with number of completed hours in a turn
    dfz = completed_doc_hours(dfx)


    ## Merging resulting dataframes into final result
    dfa = pd.merge(
        dfy,
        dfw,
        on=[
            "clinica_(syspc)",
            "usuarioid_(syspc)",
            "proveedor_(syspc)",
            "especialidad_(syspc)",
            "fecha_(syspc)",
            "turno_activo"
        ],
        how="outer"
    )
    dfa = pd.merge(
        dfa,
        dfz,
        on=[
            "clinica_(syspc)",
            "usuarioid_(syspc)",
            "proveedor_(syspc)",
            "especialidad_(syspc)",
            "fecha_(syspc)",
            "turno_activo"
        ],
        how="outer"
    )


    ## Filling "N/A" values not included in the merge
    dfa["tiempo_ocupado"].fillna(0, inplace=True)
    dfa["tiempo_completado"].fillna(0, inplace=True)


    # ## Grouping "all_day_turn" entries
    # dfa = group_allday_entries(dfa)


    ## Adding index columns

    ### Adding column with turn occupation index
    dfa["indice_ocupacion_turno"] = round(dfa["tiempo_ocupado"]/dfa["tiempo_contratado"], 2)

    ### Adding column with turn occupation index
    dfa["indice_conversion_turno"] = round(dfa["tiempo_completado"]/dfa["tiempo_contratado"], 2)


    return dfa





"----------------------------------------------------------------------------------------------------------------------"
############################## Appointments analysis ###################################################################
"----------------------------------------------------------------------------------------------------------------------"


'--------------- Unitary functions ---------------'


## Extracting data from database
def extract_appts_data(date_string, db_source='pc_db_prod'):
    """
    Extracting data from database

    :param date_string: (string) string that contain a start and end date in the format %Y-%m-%d_to_%Y-%m-%d
    :param db_source: (string) selection of the database where the data will be extracted (options: pc_db_prod, pc_db_backup)
    :return:
    """


    ## Converting date string into a dictionary suitable for the sql parameters
    date_sql_param = datestring_to_sql_parameter(date_string)

    ### Message specifying dates used for the query
    print("- Date range used to query data: from {} to {}".format(
        date_sql_param["$1"],
        date_sql_param["$2"])
    )

    ## Updating sql parameters to query data in the specified date range
    sql_params_appts_creation["params"].update(date_sql_param)

    ## Executing sql query to obtain working dataframe
    dfx = sql_to_df(db_source, postgre_files_path, postgre_query_apptsct, sql_params_appts_creation)


    return dfx


## Wrangling data
def wrangle_appts_data(dfx):
    """
    Formatting data

    :param dfx: (dataframe) df with raw data as extracted from the database
    :return dfx: (dataframe) df after the initial wrangling process
    """


    ## Dealing with the empty values in the patient's column
    dfx["paciente"] = dfx["paciente"].astype("str")
    dfx["paciente"] = dfx["paciente"].map({"None": "SIN_PACIENTE"}).fillna(dfx["paciente"])


    ## Eliminating rows with appointments unrelated to patients
    filter_kwrds_pattern = '|'.join(
        [
        'NO OCUPAR',
        'BLOQUEADO',
        'NO AGENDAR',
        'NO OCUPAR',
        'COMIDA',
        ]
    )
    dfx = dfx[~dfx['paciente'].str.contains(filter_kwrds_pattern)].copy()


    return dfx


## Enhancing data
def enhance_appts_data(dfx):
    """
    Enhancing data

    :param dfx: (dataframe) df with data after the initial wrangling
    :return dfx: (dataframe) df with data enhanced
    """


    ## Column with the datetime of the appointment's start
    dfx.insert(
        dfx.columns.tolist().index('hora_inicio') + 1,
        'inicio_cita',
        pd.to_datetime(dfx['fecha'].astype('str') + ' ' + dfx['hora_inicio'].astype('str'), format='%Y-%m-%d %H:%M')
    )

    ## Column with the datetime of the appointment's end
    dfx.insert(
        dfx.columns.tolist().index('hora_inicio') + 2,
        'final_cita',
        pd.to_datetime(dfx['fecha'].astype('str') + ' ' + dfx['hora_final'].astype('str'), format='%Y-%m-%d %H:%M')
    )
    dfx.drop(['fecha', 'hora_inicio', 'hora_final'], axis=1, inplace=True)

    ## Formatting the creation time column
    dfx['creacion_cita'] = pd.to_datetime(dfx['creacion_cita'], format='%d/%m/%Y %H:%M:%S')

    ## Adding column with a count in hours of the time between the creation and the appointment time
    dfx.insert(
        dfx.columns.tolist().index('creacion_cita') + 1,
        'creacion_inicio_horas',
        ((dfx['inicio_cita'] - dfx['creacion_cita']).dt.total_seconds() / (60 * 60 * 24)).round(2)
    )

    ## Eliminating creation/appointment-start time differences lower than zero
    dfx = dfx[dfx['creacion_inicio_horas'] >= 0].copy()


    return dfx



'--------------- Compounded functions ---------------'


## Individual appointments with various analysis metrics
def appts_lysis_data(date_string, db_source='pc_db_prod'):
    """
    Individual appointments with various analysis metrics

    :param date_string: (string) string that contain a start and end date in the format %Y-%m-%d_to_%Y-%m-%d
    :param db_source: (string) selection of the database where the data will be extracted (options: pc_db_prod, pc_db_backup)
    :return dfx: (dataframe) df individual appointments and relevant related data
    """


    ## Extracting data from database
    dfx = extract_appts_data(date_string, db_source)

    ## Wrangling data
    dfx = wrangle_appts_data(dfx)

    ## Enhancing data
    dfx = enhance_appts_data(dfx)


    return dfx





"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############################################# END OF FILE ##############################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
