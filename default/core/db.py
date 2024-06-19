from register_login.models import CustomUser, Menu, CustomGroup
from warehouse.models import Shed, Rack, Item
from .constants import (
    HR_NAME,
    ADMIN_NAME,
    WAREHOUSE_NAME,
    REPORTS_NAME,
    SALES_NAME,
    PURCHASES_NAME,
    USERS_ICON_CLASS,
)


def create_objects_from_dict(object, data: dict) -> list:
    created_objects = []
    for key, values in data.items():
        obj = object.objects.create(**values)
        created_objects.append(obj)
    return created_objects


def fetch_exiting_objects(object, filter):
    try:
        object.objects.get(filter)
    except object.DoesNotExist:
        print(f"Object {object} with filter {filter} does not exist")
        return None


def create_warehouse_tables() -> dict:
    SHED_DATA = {
        "shed1": {"shed": "SHED001", "capacity": 1000},
        "shed2": {"shed": "SHED002", "capacity": 2000},
        "shed3": {"shed": "SHED003", "capacity": 3000},
    }
    created_sheds = create_objects_from_dict(Shed, SHED_DATA)
    if len(created_sheds) == 0:
        raise RuntimeError("Failed to create Sheds")

    RACK_DATA = {
        "rack1": {
            "code": "RACK001",
            "capacity": 100,
            "in_shed": fetch_exiting_objects(Shed, "shed='SHED001'"),
        },
        "rack2": {
            "code": "RACK002",
            "capacity": 200,
            "in_shed": fetch_exiting_objects(Shed, "shed='SHED001'"),
        },
        "rack3": {
            "code": "RACK003",
            "capacity": 300,
            "in_shed": fetch_exiting_objects(Shed, "shed='SHED002'"),
        },
        "rack4": {
            "code": "RACK004",
            "capacity": 400,
            "in_shed": fetch_exiting_objects(Shed, "shed='SHED002'"),
        },
        "rack5": {
            "code": "RACK005",
            "capacity": 500,
            "in_shed": fetch_exiting_objects(Shed, "shed='SHED003'"),
        },
        "rack6": {
            "code": "RACK006",
            "capacity": 600,
            "in_shed": fetch_exiting_objects(Shed, "shed='SHED003'"),
        },
    }
    created_racks = create_objects_from_dict(Rack, RACK_DATA)
    if len(created_racks) == 0:
        raise RuntimeError("Failed to create Racks")

    ITEM_DATA = {
        "item1": {
            "code": "ITEM001",
            "name": "Product A",
            "description": "Sample description for Product A",
            "quantity": 100,
            "in_rack": fetch_exiting_objects(Rack, "code='RACK001'"),
        },
        "item2": {
            "code": "ITEM002",
            "name": "Product B",
            "description": "Sample description for Product B",
            "quantity": 200,
            "in_rack": fetch_exiting_objects(Rack, "code='RACK002'"),
        },
        "item3": {
            "code": "ITEM003",
            "name": "Product C",
            "description": "Sample description for Product C",
            "quantity": 300,
            "in_rack": fetch_exiting_objects(Rack, "code='RACK003'"),
        },
        "item4": {
            "code": "ITEM004",
            "name": "Product D",
            "description": "Sample description for Product D",
            "quantity": 400,
            "in_rack": fetch_exiting_objects(Rack, "code='RACK004'"),
        },
        "item5": {
            "code": "ITEM005",
            "name": "Product E",
            "description": "Sample description for Product E",
            "quantity": 500,
            "in_rack": fetch_exiting_objects(Rack, "code='RACK005'"),
        },
        "item6": {
            "code": "ITEM006",
            "name": "Product F",
            "description": "Sample description for Product F",
            "quantity": 600,
            "in_rack": fetch_exiting_objects(Rack, "code='RACK006'"),
        },
        "item7": {
            "code": "ITEM007",
            "name": "Product G",
            "description": "Sample description for Product G",
            "quantity": 700,
            "in_rack": fetch_exiting_objects(Rack, "code='RACK001'"),
        },
        "item8": {
            "code": "ITEM008",
            "name": "Product H",
            "description": "Sample description for Product H",
            "quantity": 800,
            "in_rack": fetch_exiting_objects(Rack, "code='RACK002'"),
        },
        "item9": {
            "code": "ITEM009",
            "name": "Product I",
            "description": "Sample description for Product I",
            "quantity": 900,
            "in_rack": fetch_exiting_objects(Rack, "code='RACK003'"),
        },
        "item10": {
            "code": "ITEM010",
            "name": "Product J",
            "description": "Sample description for Product J",
            "quantity": 1000,
            "in_rack": fetch_exiting_objects(Rack, "code='RACK004'"),
        },
    }
    created_items = create_objects_from_dict(Item, ITEM_DATA)
    if len(created_items) == 0:
        raise RuntimeError("Failed to create Items")

    return {"sheds": created_sheds, "racks": created_racks, "items": created_items}


def create_menu_data() -> dict:
    CUSTOMGROUP_DATA = {
        "default": {
            "name": "Default",
            "manager": fetch_exiting_objects(CustomUser, ADMIN_NAME),
        },
        "hr": {
            "name": "HR",
            "manager": fetch_exiting_objects(CustomUser, ADMIN_NAME),
        },
        "warehouse": {
            "name": "Warehouse",
            "manager": fetch_exiting_objects(CustomUser, ADMIN_NAME),
        },
        "reports": {
            "name": "Reports",
            "manager": fetch_exiting_objects(CustomUser, ADMIN_NAME),
        },
        "sales": {
            "name": "Sales",
            "manager": fetch_exiting_objects(CustomUser, ADMIN_NAME),
        },
        "purchases": {
            "name": "Purchases",
            "manager": fetch_exiting_objects(CustomUser, ADMIN_NAME),
        },
    }
    created_customgroups = create_objects_from_dict(CustomGroup, CUSTOMGROUP_DATA)
    if len(created_customgroups) == 0:
        raise RuntimeError("Failed to create CustomGroups")

    MENU_DATA = {
        "dash": {
            "menu": "Dashboard",
            "submenu": "",
            "icon": "fas fa-tachometer-alt",
            "url": "register_login:home",
            "group": fetch_exiting_objects(CustomGroup, "name='Default'"),
            "subgroup": None,
        },
        "payroll": {
            "menu": "HR",
            "submenu": "Payroll",
            "icon": "fas fa-money-check-alt",
            "url": "register_login:payroll",
            "group": fetch_exiting_objects(CustomGroup, HR_NAME),
            "subgroup": None,
        },
        "timekeeping": {
            "menu": "HR",
            "submenu": "Timekeeping",
            "icon": "fas fa-clock",
            "url": "register_login:timekeeping",
            "group": fetch_exiting_objects(CustomGroup, HR_NAME),
            "subgroup": None,
        },
        "employees": {
            "menu": "HR",
            "submenu": "Employees",
            "icon": USERS_ICON_CLASS,
            "url": "register_login:employees",
            "group": fetch_exiting_objects(CustomGroup, HR_NAME),
            "subgroup": None,
        },
        "inventory": {
            "menu": "Warehouse",
            "submenu": "Inventory",
            "icon": "fas fa-boxes",
            "url": "warehouse:inventory",
            "group": fetch_exiting_objects(CustomGroup, WAREHOUSE_NAME),
            "subgroup": None,
        },
        "orders": {
            "menu": "Warehouse",
            "submenu": "Orders",
            "icon": "fas fa-shopping-cart",
            "url": "warehouse:orders",
            "group": fetch_exiting_objects(CustomGroup, WAREHOUSE_NAME),
            "subgroup": None,
        },
        "suppliers": {
            "menu": "Warehouse",
            "submenu": "Suppliers",
            "icon": "fas fa-truck",
            "url": "warehouse:suppliers",
            "group": fetch_exiting_objects(CustomGroup, WAREHOUSE_NAME),
            "subgroup": None,
        },
        "sales": {
            "menu": "Reports",
            "submenu": "Sales",
            "icon": "fas fa-chart-line",
            "url": "reports:sales",
            "group": fetch_exiting_objects(CustomGroup, REPORTS_NAME),
            "subgroup": None,
        },
        "purchases": {
            "menu": "Reports",
            "submenu": "Purchases",
            "icon": "fas fa-chart-line",
            "url": "reports:purchases",
            "group": fetch_exiting_objects(CustomGroup, REPORTS_NAME),
            "subgroup": None,
        },
        "customers": {
            "menu": "Reports",
            "submenu": "Customers",
            "icon": USERS_ICON_CLASS,
            "url": "reports:customers",
            "group": fetch_exiting_objects(CustomGroup, SALES_NAME),
            "subgroup": None,
        },
        "vendors": {
            "menu": "Reports",
            "submenu": "Vendors",
            "icon": USERS_ICON_CLASS,
            "url": "reports:vendors",
            "group": fetch_exiting_objects(CustomGroup, PURCHASES_NAME),
            "subgroup": None,
        },
    }
    created_menus = create_objects_from_dict(Menu, MENU_DATA)
    if len(created_menus) == 0:
        raise RuntimeError("Failed to create Menus")

    # USER_DATA = {
    # }
    # created_users = create_objects_from_dict(CustomUser, USER_DATA)
    # if len(created_users) == 0:
    #     raise RuntimeError('Failed to create Users')

    return {"customgroups": created_customgroups, "menus": created_menus}
