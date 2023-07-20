import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-vertical-rental",
    description="Meta package for oca-vertical-rental Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-rental_base',
        'odoo13-addon-rental_offday',
        'odoo13-addon-rental_pricelist',
        'odoo13-addon-rental_pricelist_interval',
        'odoo13-addon-rental_product_pack',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
