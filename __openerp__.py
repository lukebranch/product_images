{
    'name': 'Product Images',
    'description': 'This module is in answer to this forum post: https://www.odoo.com/forum/help-1/question/image-widget-is-lost-in-product-form-view-how-to-regain-it-70050',
    'category': 'Website',
    'version': '1.0',
    'author': 'Luke Branch',
    'depends': ['product','sale'],
    'data': [
        'views/product_images.xml',
    ],
    'application': True,
}
