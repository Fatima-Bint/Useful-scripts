import hashlib


"""
A simple script that generates hash using the hashlib library.
For demonstration purposes (1st cut), the following fields were used.

Fields
------
1. internal_id
2. basic_final_color
3. basic_final_clarity
4. sheryl_cut
5. culet_size

What is happening?
------------------
Basically a Stone model is modelled (simulated) as a native python class with the 
fields above.
The Stone model has methods that generates basic id and triple ids

Methods
-------
1. generate_basic_id()
2. generate_triple_id()


Usage:
1. Generate basic id
    - stone_instance.generate_basic_id()
2. Generate triple id
    - stone_instance.generate_triple_id()
"""


if __name__ == "__main__":
    class Stone:
        def __init__(self, internal_id, basic_final_color, basic_final_clarity, sheryl_cut, culet_size):
            """
            Initialize a stone with the following instance attributes
            :param internal_id:
            :param basic_final_color:
            :param basic_final_clarity:
            :param sheryl_cut:
            :param culet_size:
            """
            self.internal_id = internal_id
            self.basic_final_color = basic_final_color
            self.basic_final_clarity = basic_final_clarity
            self.sheryl_cut = sheryl_cut
            self.culet_size = culet_size

        def __generate_id(self, char_length=4):
            """
            Generate a hash given a django model instance (or any object) and a number of characters
            :param char_length:
            :return:
            """
            payload = f"{self.internal_id},{self.basic_final_color},{self.basic_final_clarity}," \
                      f"{self.sheryl_cut},{self.culet_size}".encode('utf-8')
            hashed = hashlib.blake2b(digest_size=char_length)
            hashed.update(payload)
            return hashed.hexdigest()

        def generate_basic_id(self):
            return f"{self.__generate_id()}-B"

        def generate_triple_id(self):
            return self.__generate_id()

    # Instantiate a stone and generate hash
    stone_1 = Stone("123456789", "G", "VVS2", "EX", "VS")

    import pdb; pdb.set_trace()