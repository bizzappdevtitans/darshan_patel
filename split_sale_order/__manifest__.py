{
    "name": "Split Sale Order",
    "version": "15.0.0.0.1",
    "category": "Sales Order",
    "summary": "split sale order based on category",
    "author": "BizzAppDev",
    "website": "https://bizzappdev.com",
    "depends": ["sale_management"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/sale_order_split_quotation_views.xml",
        "views/sale_order_view.xml",
    ],
    "license": "Other proprietary",
}
