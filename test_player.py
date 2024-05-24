import unittest
from unittest.mock import Mock
from player import Player 
from sys import platform

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_initialization(self):
        self.assertEqual(self.player.y_position, 561)
        self.assertEqual(self.player.x_position, 100)
        self.assertEqual(self.player.image_rotation, 'right')
        self.assertFalse(self.player.jumping)


    def test_load_image(self):
        py = Mock()
        py.transform.scale = Mock(return_value="scaled_image")
        py.transform.flip = Mock(return_value="flipped_image")

        
        image = self.player.load_image("janosik0.png")
        expected_path = "images/janosik0.png" if platform != 'win32' else "images\\janosik0.png"
        self.assertEqual(self.player.image_source + "janosik0.png", expected_path)
        
    def test_turn_right(self):
        self.player.animation_timer = 1
        self.player.current_run = 0
        self.player.image_rotation = 'left'
        self.player.jumping = False
        self.player.load_image = Mock(return_value="mock_image")
        old_loc = self.player.rect.x
        self.player.turn_right()
        self.assertEqual(self.player.animation_timer, 2) 
        self.assertEqual(self.player.current_run, 1)
        self.assertEqual(self.player.image_rotation, 'right') 
        self.player.load_image.assert_called_once_with('janosik1.png', True)
        self.assertEqual(self.player.rect.x, old_loc + 8)
        self.player.turn_right() 
        self.assertEqual(self.player.animation_timer, 3) 
        self.assertEqual(self.player.current_run, 1)
        self.assertEqual(self.player.image_rotation, 'right') 
        self.assertEqual(self.player.rect.x, old_loc + 16)
        self.player.load_image.assert_called_once_with('janosik1.png', True)
        

    def test_turn_left(self):
        self.player.animation_timer = 1
        self.player.current_run = 0
        self.player.image_rotation = 'right'
        self.player.jumping = False
        self.player.load_image = Mock(return_value="mock_image")
        self.player.move = Mock()
        self.player.turn_left()
        self.assertEqual(self.player.animation_timer, 2) 
        self.assertEqual(self.player.current_run, 1)
        self.assertEqual(self.player.image_rotation, 'left') 
        self.player.load_image.assert_called_once_with('janosik1.png', True)
        


if __name__ == '__main__':
    unittest.main()
