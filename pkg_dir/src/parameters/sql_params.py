## MODULE WITH SQL PARAMETERS





"----------------------------------------------------------------------------------------------------------------------"
############################################# Imports ##################################################################
"----------------------------------------------------------------------------------------------------------------------"


"--------------- Standard library imports ---------------"


"--------------- Third party imports ---------------"


"--------------- Local application imports ---------------"





"----------------------------------------------------------------------------------------------------------------------"
############################################# SQL parameters ###########################################################
"----------------------------------------------------------------------------------------------------------------------"


## Working hours in doctor's agendas
sql_params_workhrs = {
    "params": {
        "$1": "'2021-08-05'",
        "$2": "'2021-08-06'",
        "$3": "'%SAID%'",
    },
    "colnames": {
        0: "Fecha",
        1: "Hora_inicio",
        2: "Hora_final",
        3: "Usuario_id",
        4: "Estado_cita",
        5: "Usuario_nom",
        6: "Especialidad_nom",
        7: "Sucursal",
    }
}


## Information about the doctor's agendas
sql_params_fullagenda = {
    "params": {
        "$1": "'1900-01-01'",
        "$2": "'1900-01-02'",
    },
    "colnames": {
        0: "fecha_(syspc)",
        1: "hora_inicio_(syspc)",
        2: "hora_final_(syspc)",
        3: "estatus_cita_(syspc)",
        4: "usuarioid_(syspc)",
        5: "proveedor_(syspc)",
        6: "proveedor_estado_(syspc)",
        7: "especialidad_(syspc)",
        8: "clinica_(syspc)",
        9: "paciente_(syspc)",
    }
}


## Information about the doctor's agendas
sql_params_appts_creation = {
    "params": {
        "$1": "'1900-01-01'",
        "$2": "'1900-01-02'",
    },
    "colnames": {
        0: "fecha",
        1: "hora_inicio",
        2: "hora_final",
        3: "creacion_cita",
        4: "estatus_cita",
        5: "usuarioid",
        6: "proveedor",
        7: "especialidad",
        8: "clinica",
        9: "paciente",
    }
}


## Pharma sales data
sql_params_pharmasales = {
    "params": {
        "$1": "'1900-01-01'",
        "$2": "'1900-01-02'",
    },
    "colnames": {
        0: "id_venta_(sicar)",
        1: "fecha_(sicar)",
        2: 'vendedor_(sicar)',
        3: 'descuento_(sicar)',
        4: "total_(sicar)",
        5: "total_compra_(sicar)",
        6: "total_utilidad_(sicar)",
    }
}


## Income registered in PC's system
sql_params_income_syspc = {
    "params": {
        "$1": "'1900-01-01'",
        "$2": "'1900-01-02'",
    },
    "colnames": {
        0: "id_venta_(syspc)",
        1: "fecha_(syspc)",
        2: "clinica_(syspc)",
        3: "piso_(syspc)",
        4: "usuarioid_(syspc)",
        5: "especialidad_(syspc)",
        6: "proveedor_(syspc)",
        7: "grupo_servicio_(syspc)",
        8: "tipo_servicio_(syspc)",
        9: "servicio_(syspc)",
        10: "paciente_(syspc)",
        11: "lista_precio_(syspc)",
        12: "forma_pago_(syspc)",
        13: "descuento_(syspc)",
        14: "precio_(syspc)",
        15: "total_(syspc)",
        # 16: "estatus_venta",
    }
}


### Doctor's information in the database
sql_params_docs_data = {
    "params": {
    },
    "colnames": {
        0: "usuarioid_(syspc)",
        1: "usuarionomfull_(syspc)",
        2: "especialidadnom_(syspc)",
    }
}






"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
############################################# END OF FILE ##############################################################
"----------------------------------------------------------------------------------------------------------------------"
"----------------------------------------------------------------------------------------------------------------------"
