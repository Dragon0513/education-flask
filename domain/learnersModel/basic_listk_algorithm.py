# The basic calculating Method for the ListK
# Every answer has a value 1-5 and will contribute to the mean value of the
# dimension

# The basic learning strategy is calculated by the following formula:

# org = (org1 + org2 + org3) / 3
# elab = (elab1 + elab2 + elab3) / 3
# crit_rev = (crit_rev1 + crit_rev2 + crit_rev3) / 3
# rep = (rep1 + rep2 + rep3) / 3
# cogn_str = (org + elab + crit_rev + rep) / 4

# goal_plan = (goal_plan1 + goal_plan2 + goal_plan3(1-5 reversed)) / 3
# con = (con1 + con2 + con3) / 3
# reg = (reg1 + reg2 + reg3) / 3
# metacogn_str = (goal_plan + con + reg) / 3

# att = (att1 + att2 + att3) / 3 (1-5 reversed)
# eff = (eff1 + eff2 + eff3) / 3
# time = (time1 + time2 + time3) / 3
# int_res_mng_str = (att + eff + time) / 3

# lrn_w_cls = (lrn_w_cls1 + lrn_w_cls2 + lrn_w_cls3) / 3
# lit_res = (lit_res1 + lit_res2 + lit_res3) / 3
# lrn_env = (lrn_env1 + lrn_env2 + lrn_env3) / 3
# ext_res_mng_str = (lrn_w_cls + lit_res + lrn_env) / 3

def calculate_basic_learning_strategy(list_k_answers):
    cogn_str = calculate_cognitive_str(list_k_answers['org1_f1'],
                                       list_k_answers['org2_f2'],
                                       list_k_answers['org3_f3'],
                                       list_k_answers['elab1_f4'],
                                       list_k_answers['elab2_f5'],
                                       list_k_answers['elab3_f6'],
                                       list_k_answers['crit_rev1_f7'],
                                       list_k_answers['crit_rev2_f8'],
                                       list_k_answers['crit_rev3_f9'],
                                       list_k_answers['rep1_f10'],
                                       list_k_answers['rep2_f11'],
                                       list_k_answers['rep3_f12'])

    metacogn_str = calculate_metacognitive_str(
        list_k_answers['goal_plan1_f13'],
        list_k_answers['goal_plan2_f14'],
        list_k_answers['goal_plan3_f15'],
        list_k_answers['con1_f16'],
        list_k_answers['con2_f17'],
        list_k_answers['con3_f18'],
        list_k_answers['reg1_f19'],
        list_k_answers['reg2_f20'],
        list_k_answers['reg3_f21'])

    int_res_mng_str = calculate_internal_resource_management_str(
        list_k_answers['att1_f22'],
        list_k_answers['att2_f23'],
        list_k_answers['att3_f24'],
        list_k_answers['eff1_f25'],
        list_k_answers['eff2_f26'],
        list_k_answers['eff3_f27'],
        list_k_answers['time1_f28'],
        list_k_answers['time2_f29'],
        list_k_answers['time3_f30'])

    ext_res_mng_str = external_resource_management_str(
        list_k_answers['lrn_w_cls1_f31'],
        list_k_answers['lrn_w_cls2_f32'],
        list_k_answers['lrn_w_cls3_f33'],
        list_k_answers['lit_res1_f34'],
        list_k_answers['lit_res2_f35'],
        list_k_answers['lit_res3_f36'],
        list_k_answers['lrn_env1_f37'],
        list_k_answers['lrn_env2_f38'],
        list_k_answers['lrn_env3_f39'])

    return (cogn_str,
            metacogn_str,
            int_res_mng_str,
            ext_res_mng_str)


def calculate_cognitive_str(org1, org2, org3, elab1, elab2, elab3,
                            crit_rev1, crit_rev2, crit_rev3, rep1, rep2,
                            rep3):
    org = (org1 + org2 + org3) / 3
    elab = (elab1 + elab2 + elab3) / 3
    crit_rev = (crit_rev1 + crit_rev2 + crit_rev3) / 3
    rep = (rep1 + rep2 + rep3) / 3
    print("org: ", org, "elab: ", elab, "crit_rev: ", crit_rev, "rep: ", rep)
    return (round(org, 2),
            round(elab, 2),
            round(crit_rev, 2),
            round(rep, 2),
            round((org + elab + crit_rev + rep) / 4, 2))


def calculate_metacognitive_str(goal_plan1, goal_plan2, goal_plan3,
                                con1, con2, con3, reg1, reg2, reg3):
    print("calculate_metacognitive_strategy")
    goal_plan = (goal_plan1 + goal_plan2 + reverse_value(goal_plan3)) / 3
    con = (con1 + con2 + con3) / 3
    reg = (reg1 + reg2 + reg3) / 3
    return (round(goal_plan, 2),
            round(con,2),
            round(reg,2),
            round((goal_plan + con + reg) / 3,2))


def calculate_internal_resource_management_str(att1, att2, att3, eff1,
                                               eff2, eff3, time1, time2,
                                               time3):
    print("calculate_internal_resource_management_strategy")
    att = (reverse_value(att1) + reverse_value(att2) + reverse_value(att3)) / 3
    eff = (eff1 + eff2 + eff3) / 3
    time = (time1 + time2 + time3) / 3
    return (round(att, 2),
            round(eff, 2),
            round(time, 2),
            round((att + eff + time) / 3, 2))


def external_resource_management_str(lrn_w_cls1, lrn_w_cls2, lrn_w_cls3,
                                     lit_res1, lit_res2, lit_res3,
                                     lrn_env1, lrn_env2, lrn_env3):
    print("external_resource_management_strategy")
    lrn_w_cls = (lrn_w_cls1 + lrn_w_cls2 + lrn_w_cls3) / 3
    lit_res = (lit_res1 + lit_res2 + lit_res3) / 3
    lrn_env = (lrn_env1 + lrn_env2 + lrn_env3) / 3
    return (round(lrn_w_cls, 2),
            round(lit_res, 2),
            round(lrn_env, 2),
            round((lrn_w_cls + lit_res + lrn_env) / 3, 2))


def reverse_value(value):
    return 6 - value if 1 <= value <= 5 else value
