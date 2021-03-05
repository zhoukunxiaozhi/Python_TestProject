import unittest

class demo1(unittest.TestCase):
     @classmethod
     def setUpClass(cls) -> None:
          print("setup class")

     @classmethod
     def tearDownClass(cls) -> None:
          print("teardown class")

     def setUp(self) -> None:
          print("setup")

     def tearDown(self) -> None:
          print("teardown")

     @unittest.skip
     def test_case001(self):
          print("test_case001")
          self.assertEqual(2,2,"不同！不同！")

     def test_case002(self):
          print("test_case002")
          self.assertIn("t","this")

     @unittest.skipIf(1+1==2,"跳过此用例")
     def test_case003(self):
          print("test_case003")
          self.assertNotIn("c","this")

class demo2(unittest.TestCase):
     @classmethod
     def setUpClass(cls) -> None:
          print("setup class")

     @classmethod
     def tearDownClass(cls) -> None:
          print("teardown class")

     def setUp(self) -> None:
          print("setup")

     def tearDown(self) -> None:
          print("teardown")

     @unittest.skip
     def test_case004(self):
          print("test_case004")
          self.assertEqual(2,2,"不同！不同！")

     def test_case005(self):
          print("test_case005")
          self.assertIn("t","this")

     @unittest.skipIf(1+1==2,"跳过此用例")
     def test_case006(self):
          print("test_case006")
          self.assertNotIn("c","this")

class demo3(unittest.TestCase):
     @classmethod
     def setUpClass(cls) -> None:
          print("setup class")

     @classmethod
     def tearDownClass(cls) -> None:
          print("teardown class")

     def setUp(self) -> None:
          print("setup")

     def tearDown(self) -> None:
          print("teardown")

     def test_case007(self):
          print("test_case007")
          self.assertEqual(2,2,"不同！不同！")

     def test_case008(self):
          print("test_case008")
          self.assertIn("t","this")

     def test_case009(self):
          print("test_case009")
          self.assertNotIn("c","this")

if __name__=='__main__':
     # unittest.main()

     # suit = unittest.TestSuite()
     # suit.addTest(demo1("test_case002"))
     # suit.addTest(demo2("test_case005"))
     # unittest.TextTestRunner().run(suit)

     # suit1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
     # suit3 = unittest.TestLoader().loadTestsFromTestCase(demo3)
     # suitall = unittest.TestSuite([suit1,suit3])
     # unittest.TextTestRunner().run(suitall)

     discover = unittest.defaultTestLoader.discover("./","test_file9.py")
     unittest.TextTestRunner().run(discover)

