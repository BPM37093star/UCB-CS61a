test = {
  'name': 'Problem OPTIONAL',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> laser = LaserAnt()
          >>> ant = HarvesterAnt(2)
          >>> bee1 = Bee(2)
          >>> bee2 = Bee(2)
          >>> bee3 = Bee(2)
          >>> bee4 = Bee(2)
          >>> colony.places["tunnel_0_0"].add_insect(laser)
          >>> colony.places["tunnel_0_0"].add_insect(bee4)
          >>> colony.places["tunnel_0_3"].add_insect(bee1)
          >>> colony.places["tunnel_0_3"].add_insect(bee2)
          >>> colony.places["tunnel_0_4"].add_insect(ant)
          >>> colony.places["tunnel_0_5"].add_insect(bee3)
          >>> laser.action(colony)
          >>> round(bee4.armor, 2)
          0.0
          >>> round(bee1.armor, 2)
          0.65
          >>> round(bee2.armor, 2)
          0.7
          >>> round(ant.armor, 2)
          0.95
          >>> round(bee3.armor, 2)
          1.2
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
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
