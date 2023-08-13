#!/usr/bin/python3
"""unittet classes
"""

from datetime import datetime
import inspect
from models import place
from models.base_model import BaseModel
import pep8
import unittest
Place = place.Place


class TestPlaceDocs(unittest.TestCase):
    """Tests class"""
    @classmethod
    def setUpClass(cls):
        """tests"""
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Test conforms"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        """Test PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_module_docstring(self):
        """Test docstring"""
        self.assertIsNot(place.__doc__, None,
                         "place.py needs a docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py needs a docstring")

    def test_place_class_docstring(self):
        """Test"""
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")

    def test_place_func_docstrings(self):
        """Test methods"""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPlace(unittest.TestCase):
    """Test class"""
    def test_is_subclass(self):
        """Test BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id_attr(self):
        """Test string"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """Test Place"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_name_attr(self):
        """Test string"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_description_attr(self):
        """Test Place string"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_rooms_attr(self):
        """Test attr"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test Place attr"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test max_guest"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test price_by_night"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test Placelatitude"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)

    def test_latitude_attr(self):
        """Test Place float"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids_attr(self):
        """Test list"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """test attrs"""
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in p.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test dict"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))
