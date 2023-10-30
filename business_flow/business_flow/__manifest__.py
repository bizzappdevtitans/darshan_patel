{
    "name": "Business Flow",
    "version": "15.0.0.0.1",
    "category": "Business Flow",
    "summary": "Pass Value From Sale Order To Purchase, Delivery and Invoice Order, Manufacture order",
    "author": "Bizzappdev",
    "website": "http://www.Bizzappdev.com",
    "description": """
     Bizzappdev
    """,
    "depends": ["sale_management", "account", "sale_project", "project",
                "purchase_stock", "stock", "purchase", "stock", "mrp"],
    "data": [
        "views/sales_order_view.xml",
        "views/account_move_view.xml",
        "views/project_project_view.xml",
        "views/project_task_view.xml",
        "views/purchase_order_view.xml",
        "views/stock_picking_view.xml",
        "views/manufacture_order_view.xml",
    ],
    "license": "LGPL-3",
}
