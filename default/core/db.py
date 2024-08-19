from register_login.models import CustomUser, Menu, CustomGroup
from warehouse.models import Shed, Rack, Item
from .constants import (
    MENU_DATA,
)

def create_objects_from_dict(object, data: dict) -> dict:
    created_objects = {}
    for key, values in data.items():
        obj = object.objects.create(**values)
        created_objects[key] = obj
    return created_objects


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
            "in_shed": fetch_existing_objects(Shed, shed='SHED001'),
        },
        "rack2": {
            "code": "RACK002",
            "capacity": 200,
            "in_shed": fetch_existing_objects(Shed, shed='SHED001'),
        },
        "rack3": {
            "code": "RACK003",
            "capacity": 300,
            "in_shed": fetch_existing_objects(Shed, shed='SHED002'),
        },
        "rack4": {
            "code": "RACK004",
            "capacity": 400,
            "in_shed": fetch_existing_objects(Shed, shed='SHED002'),
        },
        "rack5": {
            "code": "RACK005",
            "capacity": 500,
            "in_shed": fetch_existing_objects(Shed, shed='SHED003'),
        },
        "rack6": {
            "code": "RACK006",
            "capacity": 600,
            "in_shed": fetch_existing_objects(Shed, shed='SHED003'),
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
            # "in_rack": fetch_existing_objects(Rack, code='RACK001'),
        },
        "item2": {
            "code": "ITEM002",
            "name": "Product B",
            "description": "Sample description for Product B",
            "quantity": 200,
            # "in_rack": fetch_existing_objects(Rack, code='RACK002'),
        },
        "item3": {
            "code": "ITEM003",
            "name": "Product C",
            "description": "Sample description for Product C",
            "quantity": 300,
            # "in_rack": fetch_existing_objects(Rack, code='RACK003'),
        },
    }
    for item in ITEM_DATA.values():
        item['in_rack'] = Rack.objects.get_or_create(
            code=item['code'],
            name=item['name'],
            description=item['description'],
            quantity=item['quantity'],
        )

def create_menu_data(manager: CustomUser) -> dict:
    categories = {
        'Default': ['dashboard'],
        'HR': ['payroll', 'timekeeping', 'employees'],
        'Warehouse': ['inventory', 'orders', 'suppliers'],
        'Sales': ['sales', 'purchases', 'customers', 'vendors'],
    }

    for group_name, menu_data in MENU_DATA.items():
        if group_name in categories['Default']:
            menu_data['group'], _ = CustomGroup.objects.get_or_create(name='Default', manager=manager)
        elif group_name in categories['HR']:
            menu_data['group'], _ = CustomGroup.objects.get_or_create(name='HR', manager=manager)
        elif group_name in categories['Warehouse']:
            menu_data['group'], _ = CustomGroup.objects.get_or_create(name='Warehouse', manager=manager)
        else:
            menu_data['group'], _ = CustomGroup.objects.get_or_create(name='Default', manager=manager) 
        
        menu_obj, created = Menu.objects.get_or_create(**menu_data)
        assert menu_obj in Menu.objects.all()









