#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from oehealth_globals import *
from oehealth_admin_groups_id import *
from oehealth_data import *

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],[(t*1000,),1000,60,60])

def oehealh_install():

    update = True
    #update = False

    adapt = True
    #adapt = False

    demo_data = True
    demo_data = False

    print '--> create_database()'
    newDB = create_database(dbname, admin_user_pw, lang)
    if newDB:
        print '--> OeHealth()'
        OeHealth()
        print '--> Administrator()'
        Administrator()
        print '--> Administrator_groups_id_updt()'
        Administrator_groups_id_updt()
        print '--> Demo_User()'
        Demo_User()

    #
    # oebase_base
    print '--> oebase_base'
    new_oebase_base = install_update_module('oebase_base', dbname, admin_user_pw, update)
    if new_oebase_base:
        print '--> Administrator_groups_id_oebase_base()'
        Administrator_groups_id_oebase_base()
    #
    # oebase_tag
    print '--> oebase_tag'
    new_oebase_tag = install_update_module('oebase_tag', dbname, admin_user_pw, update)
    #
    # oebase_annotation
    print '--> oebase_annotation'
    new_oebase_annotation = install_update_module('oebase_annotation', dbname, admin_user_pw, update)
    #
    # oebase_event
    print '--> oebase_event'
    new_oebase_event = install_update_module('oebase_event', dbname, admin_user_pw, update)
    if new_oebase_event:
        print '--> Administrator_groups_id_oebase_event()'
        Administrator_groups_id_oebase_event()
    #
    # oebase_group
    print '--> oebase_group'
    new_oebase_group = install_update_module('oebase_group', dbname, admin_user_pw, update)
    if new_oebase_group:
        print '--> Administrator_groups_id_oebase_group()'
        Administrator_groups_id_oebase_group()
    #
    # oebase_specialty
    print '--> oebase_specialty'
    new_oebase_specialty = install_update_module('oebase_specialty', dbname, admin_user_pw, update)
    #
    # oebase_profesional
    print '--> oebase_professional'
    new_oebase_professional = install_update_module('oebase_professional', dbname, admin_user_pw, update)
    if new_oebase_professional:
        print '--> Administrator_groups_id_oebase_professional()'
        Administrator_groups_id_oebase_professional()

if __name__ == '__main__':

    from time import time
    start = time()

    print '--> Executing oe_healh_install.py ...'
    oehealh_install()

    print '--> oe_healh_install.py'
    print '--> Execution time:', secondsToStr(time() - start)
