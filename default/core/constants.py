DEFAULT_SUPERUSER = {
    "firstname": "admin",
    "lastname": "admin",
    "email": "admin@mail.com",
    "password": "@Dm1n!2E4567",
}

USERS_ICON_CLASS = "fas fa-users"


MENU_DATA = {
    "dashboard": {
        "menu": "Dashboard",
        "submenu": "",
        "icon": "fas fa-tachometer-alt",
        "url": "register_login:home",
        "subgroup": None,
    },
    "payroll": {
        "menu": "HR",
        "submenu": "Payroll",
        "icon": "fas fa-money-check-alt",
        "url": "register_login:payroll",
        "subgroup": None,
    },
    "timekeeping": {
        "menu": "HR",
        "submenu": "Timekeeping",
        "icon": "fas fa-clock",
        "url": "register_login:timekeeping",
        "subgroup": None,
    },
    "employees": {
        "menu": "HR",
        "submenu": "Employees",
        "icon": USERS_ICON_CLASS,
        "url": "register_login:employees",
        "subgroup": None,
    },
    "inventory": {
        "menu": "Warehouse",
        "submenu": "Inventory",
        "icon": "fas fa-boxes",
        "url": "warehouse:inventory",
        "subgroup": None,
    },
    "orders": {
        "menu": "Warehouse",
        "submenu": "Orders",
        "icon": "fas fa-shopping-cart",
        "url": "warehouse:orders",
        "subgroup": None,
    },
    "suppliers": {
        "menu": "Warehouse",
        "submenu": "Suppliers",
        "icon": "fas fa-truck",
        "url": "warehouse:suppliers",
        "subgroup": None,
    },
    "sales": {
        "menu": "Reports",
        "submenu": "Sales",
        "icon": "fas fa-chart-line",
        "url": "sales:sales",
        "subgroup": None,
    },
    "purchases": {
        "menu": "Reports",
        "submenu": "Purchases",
        "icon": "fas fa-chart-line",
        "url": "sales:purchases",
        "subgroup": None,
    },
    "customers": {
        "menu": "Reports",
        "submenu": "Customers",
        "icon": USERS_ICON_CLASS,
        "url": "sales:customers",
        "subgroup": None,
    },
    "vendors": {
        "menu": "Reports",
        "submenu": "Vendors",
        "icon": USERS_ICON_CLASS,
        "url": "sales:vendors",
        "subgroup": None,
    },
}