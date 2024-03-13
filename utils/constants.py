date_format_search = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"
date_format = "%Y-%m-%dT%H:%M:%SZ"
date_format_message = "Date format must be YYYY-MM-DDTHH:MM:SSZ"
deletion_message = "Deletion was successful!"

abbreviation_ct = "KÜ"
abbreviation_co = "EK"
abbreviation_rq = "RQ"
abbreviation_se = "SE"
abbreviation_fo = "FO"
abbreviation_rm = "ZL"
abbreviation_an = "AN"
abbreviation_ec = "ÜB"
abbreviation_ex = "BE"
abbreviation_ra = "AB"
abbreviation_cc = "ZF"
abbreviation_as = "LZ"

name_kü = "kurzuebersicht"
name_lz = "lernziele"
name_ms = "manuskript"
name_ek = "manuskript_ek"
name_ab = "manuskript_ab"
name_be = "manuskript_be"
name_rq = "quiz_rq"
name_se = "quiz_se"
name_qu = "quiz"
name_üb = "uebung"
name_zf = "zusammenfassung"
name_za = "zusatzmaterial_auditiv"
name_zl = "zusatzmaterial_textuell"
name_zv = "zusatzmaterial_visuell"
name_an = "animation"
name_ko = "kollaborativ"

name_perception_dimension = "perception_dimension"
name_input_dimension = "input_dimension"
name_processing_dimension = "processing_dimension"
name_understanding_dimension = "understanding_dimension"
name_perception_value = "perception_value"
name_input_value = "input_value"
name_processing_value = "processing_value"
name_understanding_value = "understanding_value"

# the following are the LE formats used in RGB
rgb_le_variables = [
    "CT",
    "BO",
    "LG",
    "MS",
    "QU",
    "EX",
    "SU",
    "AAM",
    "VAM",
    "TAM",
]

# this dict maps output variable states of BN
# to RGB LE formats
le_name_map = {
    "{'CT': 'Yes'}": "kollaborativ",
    "{'BO': 'Yes'}": "kurzuebersicht",
    "{'LG': 'Yes'}": "lernziele",
    "{'MS': 'Yes'}": "manuskript",
    "{'QU': 'Yes'}": "quiz",
    "{'EX': 'Yes'}": "uebung",
    "{'SU': 'Yes'}": "zusammenfassung",
    "{'AAM': 'Yes'}": "zusatzmaterial_auditiv",
    "{'VAM': 'Yes'}": "zusatzmaterial_visuell",
    "{'TAM': 'Yes'}": "zusatzmaterial_textuell",
}

# this dict maps FSLSM model learning style nomenclature
# used in HASKI to nomenclature
# used in trained Nestor.
ls_map_common_HASKI_to_nestor = {
    "act": "Active",
    "ref": "Reflective",
    "sns": "Sensory",
    "int": "Intuitive",
    "vis": "Visual",
    "vrb": "Verbal",
    "seq": "Sequential",
    "glo": "Global",
}

# In case of BFI and/or LIST-k
# this dict is used to decode the numerical values
likert_scale = {
    1: "strong_disagree",
    2: "disagree",
    3: "neither_agree_disagree",
    4: "agree",
    5: "strong_agree",
}
