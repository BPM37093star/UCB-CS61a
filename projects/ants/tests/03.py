test = {
  'name': 'Problem 3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'The ThrowerAnt finds the nearest place in front of its own place that has Bees and throws at a random Bee in that place',
          'choices': [
            r"""
            The ThrowerAnt finds the nearest place in front of its own place
            that has Bees and throws at a random Bee in that place
            """,
            r"""
            The ThrowerAnt finds the nearest place behind its own place
            that has Bees and throws at a random Bee in that place
            """,
            r"""
            The ThrowerAnt finds the nearest place in either direction that has
            Bees and throws at a random Bee in that place
            """,
            'The ThrowerAnt throws at a random Bee in its own Place'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What Bee should a ThrowerAnt throw at?'
        },
        {
          'answer': "The place's entrance instance attribute",
          'choices': [
            "The place's entrance instance attribute",
            "The place's exit instance attribute",
            'Increment the place by 1',
            'Decrement the place by 1'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'How do you get the Place object in front of another Place object?'
        },
        {
          'answer': 'The Hive',
          'choices': [
            'The Hive',
            'None',
            'An empty Place'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What is the entrance of the first Place in a tunnel?'
        },
        {
          'answer': 'None',
          'choices': [
            'None',
            'A random Bee in the Hive',
            'The closest Bee behind the ThrowerAnt'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What should nearest_bee return if there is no Bee in front of the ThrowerAnt in the tunnel?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing nearest_bee
          >>> thrower = ThrowerAnt()
          >>> near_bee = Bee(2) # A Bee with 2 armor
          >>> far_bee = Bee(3)  # A Bee with 3 armor
          >>> ant_place = colony.places['tunnel_0_0']
          >>> near_place = colony.places['tunnel_0_3']
          >>> far_place = colony.places['tunnel_0_6']
          >>> ant_place.add_insect(thrower)
          >>> near_place.add_insect(near_bee)
          >>> far_place.add_insect(far_bee)
          >>> nearest_bee = thrower.nearest_bee(colony.hive)
          >>> nearest_bee.armor
          2
          >>> thrower.action(colony)    # Attack! ThrowerAnts do 1 damage
          >>> near_bee.armor
          1
          >>> far_bee.armor
          3
          >>> thrower.place is ant_place    # Don't change self.place!
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing nearest_bee
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> place = colony.places['tunnel_0_0']
          >>> near_bee = Bee(2)
          >>> far_bee = Bee(2)
          >>> colony.places["tunnel_0_3"].add_insect(near_bee)
          >>> colony.places["tunnel_0_6"].add_insect(far_bee)
          >>> hive = colony.hive
          >>> thrower.nearest_bee(hive) is far_bee
          False
          >>> thrower.nearest_bee(hive) is near_bee
          True
          >>> thrower.action(colony)    # Attack!
          >>> near_bee.armor            # Should do 1 damage
          1
          >>> thrower.place is place    # Don't change self.place!
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing Nearest bee not in the hive
          >>> thrower = ThrowerAnt()
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> hive = colony.hive
          >>> bee = Bee(2)
          >>> hive.add_insect(bee)      # Adding a bee to the hive
          >>> thrower.nearest_bee(hive) is bee
          False
          >>> thrower.action(colony)    # Attempt to attack
          >>> bee.armor                 # Bee armor should not change
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees on its own square
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> near_bee = Bee(2)
          >>> colony.places["tunnel_0_0"].add_insect(near_bee)
          >>> thrower.nearest_bee(colony.hive) is near_bee
          True
          >>> thrower.action(colony)   # Attack!
          >>> near_bee.armor           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees at end of tunnel
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> near_bee = Bee(2)
          >>> colony.places["tunnel_0_8"].add_insect(near_bee)
          >>> thrower.nearest_bee(colony.hive) is near_bee
          True
          >>> thrower.action(colony)   # Attack!
          >>> near_bee.armor           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees 4 places away
          >>> thrower = ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(thrower)
          >>> near_bee = Bee(2)
          >>> colony.places["tunnel_0_4"].add_insect(near_bee)
          >>> thrower.nearest_bee(colony.hive) is near_bee
          True
          >>> thrower.action(colony)   # Attack!
          >>> near_bee.armor           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing ThrowerAnt chooses a random target
          >>> thrower = ThrowerAnt()
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> bee1 = Bee(1001)
          >>> bee2 = Bee(1001)
          >>> colony.places["tunnel_0_3"].add_insect(bee1)
          >>> colony.places["tunnel_0_3"].add_insect(bee2)
          >>> # Throw 1000 times. The first bee should take ~1000*1/2 = ~500 damage,
          >>> # and have ~501 remaining.
          >>> for _ in range(1000):
          ...     thrower.action(colony)
          >>> # Test if damage to bee1 is within 6 standard deviations (~95 damage)
          >>> # If bees are chosen uniformly, this is true 99.9999998% of the time.
          >>> def dmg_within_tolerance():
          ...     return abs(bee1.armor-501) < 95
          >>> dmg_within_tolerance()
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
