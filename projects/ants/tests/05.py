test = {
  'name': 'Problem 5',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'By accessing the place instance attribute, which is a Place object',
          'choices': [
            'By accessing the place instance attribute, which is a Place object',
            r"""
            By accessing the place instance attribute, which is the name of
            some Place object
            """,
            'By calling the Place constructor, passing in the FireAnt instance',
            'By calling the FireAnt constructor'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'How can you obtain the current place of a FireAnt?'
        },
        {
          'answer': 'By accessing the bees instance attribute, which is a list of Bee objects',
          'choices': [
            r"""
            By accessing the bees instance attribute, which is a list of Bee
            objects
            """,
            r"""
            By accessing the bees instance attribute, which is a dictionary of
            Bee objects
            """,
            'By calling the add_insect method on the place instance',
            'By calling the Bee constructor, passing in the place instance'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'How can you obtain all of the Bees currently in a given place?'
        },
        {
          'answer': 'Yes, but you should iterate over a copy of the list to avoid skipping elements',
          'choices': [
            r"""
            Yes, but you should iterate over a copy of the list to avoid skipping
            elements
            """,
            'Yes, you can mutate a list while iterating over it with no problems',
            r"""
            No, Python doesn't allow list mutation on a list that is being
            iterated through
            """
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Can you iterate over a list while mutating it?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing FireAnt parameters
          >>> fire = FireAnt()
          >>> FireAnt.food_cost
          5
          >>> fire.armor
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing fire does damage to all Bees in its Place
          >>> place = colony.places['tunnel_0_4']
          >>> fire = FireAnt()
          >>> place.add_insect(fire)        # Add a FireAnt with 1 armor
          >>> place.add_insect(Bee(3))      # Add a Bee with 3 armor
          >>> place.add_insect(Bee(5))      # Add a Bee with 5 armor
          >>> len(place.bees)               # How many bees are there?
          2
          >>> place.bees[0].action(colony)  # The first Bee attacks FireAnt
          >>> len(place.bees)               # How many bees are left?
          1
          >>> place.bees[0].armor           # What is the armor of the remaining Bee?
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> place = colony.places['tunnel_0_4']
          >>> ant = FireAnt(1)           # Create a FireAnt with 1 armor
          >>> place.add_insect(ant)      # Add a FireAnt to place
          >>> ant.place is place
          True
          >>> place.remove_insect(ant)   # Remove FireAnt from place
          >>> ant.place is place         # Is the ant's place still that place?
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing fire damage
          >>> place = colony.places['tunnel_0_4']
          >>> bee = Bee(5)
          >>> place.add_insect(bee)
          >>> place.add_insect(FireAnt())
          >>> bee.action(colony) # attack the FireAnt
          >>> bee.armor
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing fire does damage to all Bees in its Place
          >>> place = colony.places['tunnel_0_4']
          >>> place.add_insect(FireAnt())
          >>> for i in range(100):          # Add 100 Bees with 3 armor
          ...     place.add_insect(Bee(3))
          >>> place.bees[0].action(colony)  # The first Bee attacks FireAnt
          >>> len(place.bees)               # How many bees are left?
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing fire damage is instance attribute
          >>> place = colony.places['tunnel_0_4']
          >>> bee = Bee(900)
          >>> buffAnt = FireAnt()
          >>> buffAnt.damage = 500   # Feel the burn!
          >>> place.add_insect(bee)
          >>> place.add_insect(buffAnt)
          >>> bee.action(colony) # attack the FireAnt
          >>> bee.armor  # is damage an instance attribute?
          400
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # General FireAnt Test
          >>> place = colony.places['tunnel_0_4']
          >>> bee = Bee(10)
          >>> ant = FireAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> bee.action(colony)    # Attack the FireAnt
          >>> bee.armor
          7
          >>> ant.armor
          0
          >>> place.ant is None     # The FireAnt should not occupy the place anymore
          True
          >>> bee.action(colony)
          >>> bee.armor             # Bee should not get damaged again
          7
          >>> bee.place.name        # Bee should not have been blocked
          'tunnel_0_3'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # General FireAnt Test
          >>> place = colony.places['tunnel_0_4']
          >>> bee = Bee(10)
          >>> ant = FireAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> ant.reduce_armor(0.1) # Poke the FireAnt
          >>> bee.armor             # Bee should not get damaged
          10
          >>> ant.armor
          0.9
          >>> place.ant is ant      # The FireAnt should still be at place
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
