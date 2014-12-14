from openerp.osv import osv, fields

class product_template(osv.Model):
    _inherit = 'product.template'
    
    _columns = {
        'x_secondpicture': fields.binary("Second Image",
            help="This field holds the second image used as image for the product, limited to 1024x1024px."),
    }
product_template()
