#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from oehealth_globals import *

def Administrator_groups_id_oebase_base():

    '''
    Reference: http://help.openerp.com/question/18704/hide-menu-for-existing-group/

    There are actually0-6 numbers for representing each job for a many2many/ one2many field

        (0, 0, { values }) -- link to a new record that needs to be created with the given values dictionary
        (1, ID, { values }) -- update the linked record with id = ID (write values on it)
        (2, ID) -- remove and delete the linked record with id = ID (calls unlink on ID, that will delete the 
                   object completely, and the link to it as well)
        (3, ID) -- cut the link to the linked record with id = ID (delete the relationship between the two 
                   objects but does not delete the target object itself)
        (4, ID) -- link to existing record with id = ID (adds a relationship)
        (5) -- unlink all (like using (3,ID) for all linked records)
        (6, 0, [IDs]) -- replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
    '''

    print 'Executing Administrator_groups_id_oebase_base...'

    sock_common = xmlrpclib.ServerProxy(sock_common_url)
    uid = sock_common.login(dbname, admin_user, admin_user_pw)
    sock = xmlrpclib.ServerProxy(sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(dbname, uid, admin_user_pw, 'res.users', 'search', args)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Super User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Register Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Super Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_oebase_event():

    print 'Executing Administrator_groups_id_oebase_event...'

    sock_common = xmlrpclib.ServerProxy(sock_common_url)
    uid = sock_common.login(dbname, admin_user, admin_user_pw)
    sock = xmlrpclib.ServerProxy(sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(dbname, uid, admin_user_pw, 'res.users', 'search', args)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Event User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Event Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_oebase_group():

    print 'Executing Administrator_groups_id_oebase_group...'

    sock_common = xmlrpclib.ServerProxy(sock_common_url)
    uid = sock_common.login(dbname, admin_user, admin_user_pw)
    sock = xmlrpclib.ServerProxy(sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(dbname, uid, admin_user_pw, 'res.users', 'search', args)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Group User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Group Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

def Administrator_groups_id_oebase_professional():

    print 'Executing Administrator_groups_id_oebase_professional...'

    sock_common = xmlrpclib.ServerProxy(sock_common_url)
    uid = sock_common.login(dbname, admin_user, admin_user_pw)
    sock = xmlrpclib.ServerProxy(sock_str)

    args = [('name', '=', 'Administrator'),]
    user_id = sock.execute(dbname, uid, admin_user_pw, 'res.users', 'search', args)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Professional User')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(4, sock.execute(dbname, uid, admin_user_pw, 'res.groups', 'search', [('name', '=', 'Base Professional Manager')])[0])],
        }
    sock.execute(dbname, uid, admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'

