# -*- coding: utf-8 -*-
##############################################################################
#
#   Innova Africa Ltd
#
##############################################################################

import logging

import openerp
from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

class purchase_order(osv.osv):

	_inherit = 'purchase','product'


	def view_picking(self, cr, uid, ids, context=None):
        '''
        This function returns an action that display existing picking orders of given purchase order ids.
        '''
        if context is None:
            context = {}
        mod_obj = self.pool.get('ir.model.data')
        dummy, action_id = tuple(mod_obj.get_object_reference(cr, uid, 'stock', 'action_picking_tree'))
        action = self.pool.get('ir.actions.act_window').read(cr, uid, action_id, context=context)

        pick_ids = []
        for po in self.browse(cr, uid, ids, context=context):
            pick_ids += [picking.id for picking in po.picking_ids]

				#aviimo
        for purchase in self.browse('purchase.order', uid, ids, context=context):
            prod_id = purchase.product_id

						product = search('product', uid, args[('id','=',prod_id), offset=0, limit=None, order=None, context=None, count=False)
						
						barcode = '000'
						for product in self.browse('product', uid, prod, context=context):
            	barcode += product.default_code

						write('product', uid, ids, { 'ean13' : 'confirmed' })

        #override the context to get rid of the default filtering on picking type
        action['context'] = {}
        #choose the view_mode accordingly
        if len(pick_ids) > 1:
            action['domain'] = "[('id','in',[" + ','.join(map(str, pick_ids)) + "])]"
        else:
            res = mod_obj.get_object_reference(cr, uid, 'stock', 'view_picking_form')
            action['views'] = [(res and res[1] or False, 'form')]
            action['res_id'] = pick_ids and pick_ids[0] or False
        return action


